import csv
import os
import shutil

"""
    - get list of images in the directory
    - get list of images already in the csv file
    - find the images that are not in the csv file
    - add the images to the csv file with the image title and the path to the image file (which should be a number now)

    Structure of the csv file:
    label, title, path
"""

DIR_PATH = "./unlabeled_data"
MAPPED_DIR_PATH = "./mapped_unlabeled_data"
CSV_PATH = "./mapped.csv"

# get list of images in the directory
def get_titles_of_images__in_dir(dir_path):
    images = os.listdir(dir_path)
    return images

# get list of images already in the csv file
def get_titles_of_images_in_csv(csv_path):
    images = []
    with open(csv_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            images.append(row[1])
    return images

# find the images that are not in the csv file
def get_titles_of_images_not_in_csv(dir_path, csv_path):
    images_in_dir = get_titles_of_images__in_dir(dir_path)
    images_in_csv = get_titles_of_images_in_csv(csv_path)
    images_not_in_csv = []
    for image in images_in_dir:
        if image not in images_in_csv:
            images_not_in_csv.append(image)
    return images_not_in_csv

# get the number of the last image in the csv file
def no_of_last_image_in_csv(csv_path):
    with open(csv_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        last_row = None
        for row in csv_reader:
            last_row = row
        if last_row is None:
            return 0
        return int(last_row[2][:-4])
    
# if the csv file is empty, write the header
def write_header(csv_path):
    with open(csv_path, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["label", "title", "path"])


# add the images to the csv file with the image title and the path to the image file (which should be a number now)
def add_images_to_csv(dir_path, mapped_dir_path, csv_path):
    titles_of_images_not_in_csv = get_titles_of_images_not_in_csv(dir_path, csv_path)
    with open(csv_path, 'a') as csv_file:
        csv_writer = csv.writer(csv_file)
        image_number = no_of_last_image_in_csv(csv_path)
        count = 0
        for image_title in titles_of_images_not_in_csv:
            count += 1
            image_path =  image_number + count + ".jpg"
            csv_writer.writerow([0, image_title, image_path])
            shutil.copy(f"{dir_path}/{image_title}", f"{mapped_dir_path}/{image_path}")


if __name__ == "__main__":
    if not os.path.exists(MAPPED_DIR_PATH):
        os.makedirs(MAPPED_DIR_PATH)
    if (not os.path.exists(CSV_PATH)) or (os.stat(CSV_PATH).st_size == 0):
        write_header(CSV_PATH)
    add_images_to_csv(DIR_PATH, MAPPED_DIR_PATH, CSV_PATH)
