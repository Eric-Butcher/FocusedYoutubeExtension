"""
A web scrapping script to get the titles and thumbnails of videos from youtube homepage using selenium and safari webdrivers and save them.
Save thumbnails in a folder and titles as the name of the thumbnail image.
"""
import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pathvalidate import sanitize_filename


webdriver = webdriver.Safari()
webdriver.get('https://www.youtube.com/')
webdriver.set_window_position(0, 0)
webdriver.set_window_size(1920, 1080)
time.sleep(2)

def find_and_save():
    # Find the thumbnails
    video_boxes = webdriver.find_elements(By.CLASS_NAME, "style-scope ytd-rich-item-renderer")
    count = 0

    for box in video_boxes:
        thumbnail = box.find_element(By.TAG_NAME, "img")
        thumbnail_url = thumbnail.get_attribute("src")

        title = box.find_element(By.ID, "video-title")
        title_text = title.text

        creator_div = box.find_element(By.ID, "channel-name")
        try:
            creator_a_tag = creator_div.find_element(By.TAG_NAME, "a")
            creator_text = creator_a_tag.text
        except:
            creator_text = None

        if thumbnail_url and title_text and creator_text: # If both are not None
            count += 1
            title_and_creator = sanitize_filename(f'{title_text} by {creator_text}')
            urllib.request.urlretrieve(thumbnail_url, fr"./unlabeled_data/{title_and_creator}.jpg")
    
    print(f"Saved {count} thumbnails")

if __name__ == "__main__":
    SCROLL_PAUSE_TIME = 0.3

    for i in range(50):
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Scroll down to bottom
        webdriver.execute_script("window.scrollTo(0, window.scrollY + 600)")

    find_and_save()

time.sleep(2)
webdriver.quit()