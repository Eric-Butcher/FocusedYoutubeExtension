"""
A web scrapping script to get the titles and thumbnails of videos from youtube homepage using selenium and safari webdrivers and save them.
Save thumbnails in a folder and titles as the name of the thumbnail image.
"""
import time
import os
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pathvalidate import sanitize_filename

"""
Channels already scraped:
    - khanacademy
    - veritasium
    - TEDEd
    - crashcourse
    - kurzgesagt
    - Wendoverproductions
    - AsapSCIENCE
    - CGPGrey
    - Fireship
    - Vsauce
    - NatGeo
    - Vox
    - NBCNews
    - FoxNews
"""

# Change this to the channel name you want to scrape
CHANNEL_NAME = "FoxNews"


driver = webdriver.Safari()
driver.get(f'https://www.youtube.com/@{CHANNEL_NAME}/videos')
driver.set_window_position(0, 0)
driver.set_window_size(1920, 1080)
time.sleep(2)

list_of_existing_files = os.listdir("./unlabeled_data")

def find_and_save():
    # Find the thumbnails
    video_boxes = driver.find_elements(By.CLASS_NAME, "style-scope ytd-rich-item-renderer")
    count = 0
    saved_count = 0

    for box in video_boxes:
        thumbnail = box.find_element(By.TAG_NAME, "img")
        thumbnail_url = thumbnail.get_attribute("src")

        title = box.find_element(By.ID, "video-title")
        title_text = title.text

        creator_text = CHANNEL_NAME

        if thumbnail_url and title_text and creator_text: # If all three are found
            count += 1
            title_and_creator_filename = sanitize_filename(fr'{title_text} by {creator_text}') + ".jpg"
            if title_and_creator_filename not in list_of_existing_files:
                saved_count += 1
                urllib.request.urlretrieve(thumbnail_url, fr"./unlabeled_data/{title_and_creator_filename}")
    
    print()
    print(f"Found {count} thumbnails")
    print(f"Saved {saved_count} thumbnails")
    print(f"Total Files: {len(os.listdir('./unlabeled_data'))}")

if __name__ == "__main__":
    SCROLL_PAUSE_TIME = 0.5
    reached_page_end = False
    last_no_of_video_boxes = 0
    NUMBERS_OF_SCROLLS_WITHOUT_CHANGE_BEFORE_BREAK = 20
    number_of_scroll_without_change = 0

    while not reached_page_end:
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, window.scrollY + 300)")

        # Check if page end is reached
        new_no_of_video_boxex = len(driver.find_elements(By.CLASS_NAME, "style-scope ytd-rich-item-renderer"))
        print(f"New: {new_no_of_video_boxex}, Last: {last_no_of_video_boxes}, No Change: {number_of_scroll_without_change}")

        if (new_no_of_video_boxex <= last_no_of_video_boxes) and (number_of_scroll_without_change > NUMBERS_OF_SCROLLS_WITHOUT_CHANGE_BEFORE_BREAK):
            reached_page_end = True
        elif new_no_of_video_boxex >= 200:
            reached_page_end = True
        elif (new_no_of_video_boxex <= last_no_of_video_boxes):
            number_of_scroll_without_change += 1
        else:
            last_no_of_video_boxes = new_no_of_video_boxex
            number_of_scroll_without_change = 0

    find_and_save()

time.sleep(2)
driver.quit()