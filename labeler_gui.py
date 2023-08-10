import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.label import Label
import os
import time
import csv
import shutil

"""
Requires:
    Kivy - Installation: python -m pip install "kivy[full]" kivy_examples
"""

UNLABELED_CSV_PATH = './mapped.csv'
LABELED_CSV_PATH = './labeled_mapped.csv'
MAPPED_UNLABELED_DATA_DIR = './mapped_unlabeled_data'
BLACKLISTED_CSV_PATH = './blacklisted.csv'

class LabelingApp(App):
    # , unlabeled_csv_path, labeled_csv_path, blacklisted_csv_path, mapped_unlabeled_data_dir
    def __init__(self, unlabeled_csv_path, labeled_csv_path, blacklisted_csv_path, mapped_unlabeled_data_dir, **kwargs):
        super().__init__(**kwargs)
        self.unlabeled_csv_path = unlabeled_csv_path
        self.labeled_csv_path = labeled_csv_path
        self.blacklisted_csv_path = blacklisted_csv_path
        self.mapped_unlabeled_data_dir = mapped_unlabeled_data_dir
        
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=50, spacing=10)
        # Window.maximize()

        self.image = Image(source='')
        self.image.allow_stretch = True
        self.image.pos_hint = {'center_x': .5, 'center_y': .5}
        self.image.size_hint = (2, 2)
        self.image.padding_top = 10

        self.image_title = Label(text='')
        self.image_title.pos_hint = {'center_x': .5, 'center_y': .5}
        self.image_title.size_hint = (1, 0.5)
        self.image_title.halign = 'center'
        self.image_title.valign = 'middle'
        self.image_title.font_size = 50

        self.category_box = BoxLayout(orientation='horizontal', spacing=100)
        self.category_box.size_hint = (1, 0.2)
        self.category_box.pos_hint = {'center_x': .5, 'center_y': .5}

        self.category_1 = Label(text='Press Z to Categorize as \nEducational')
        self.category_1.pos_hint = {'center_y': .5, 'left': 1}
        self.category_1.halign = 'center'
        self.category_1.valign = 'middle'
        self.category_1.font_size = 30

        self.category_2 = Label(text='Press R to Discard Image')
        self.category_2.pos_hint = {'center_y': .5, 'center': 1}
        self.category_2.halign = 'center'
        self.category_2.valign = 'middle'
        self.category_2.font_size = 30

        self.category_3 = Label(text='Press M to Categorize as \nEntertainment')
        self.category_3.pos_hint = {'center_y': .5, 'right': 1}
        self.category_3.halign = 'center'
        self.category_3.valign = 'middle'
        self.category_3.font_size = 30

        self.category_box.add_widget(self.category_1)
        self.category_box.add_widget(self.category_2)
        self.category_box.add_widget(self.category_3)
        
        self.layout.add_widget(self.image)
        self.layout.add_widget(self.image_title)
        self.layout.add_widget(self.category_box)


        Window.bind(on_key_down=self.key_action)

        self.valid_titles, self.valid_titles_dict = self.get_valid_titles()
        self.valid_titles = list(self.valid_titles)

        self.index = -1
        self.update_image()

        return self.layout

    def key_action(self, *args):
        keycode = args[1]
        if keycode == 122:  # 'z' key
            self.label_image('Educational')
            self.update_image()
        elif keycode == 109:  # 'm' key
            self.label_image('Entertainment')
            self.update_image()
        elif keycode == 114: # 'r' key
            self.remove_image()
            self.update_image()

    def update_image(self):
        self.index += 1
        if self.index >= len(self.valid_titles):
            self.image_title.text = "Congrats Eric! You've labeled all the images!"
            time.sleep(600)
        
        updated_image_title = self.valid_titles[self.index]
        file_name = self.valid_titles_dict[updated_image_title]
        self.image.source = f"./{self.mapped_unlabeled_data_dir}/{file_name}"
        self.image_title.text = updated_image_title[:-4]

    def label_image(self, category):
        with open(self.labeled_csv_path, 'a') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([category, self.image_title.text, self.image.source])

    # get list of images already in the unlabeled csv file
    def get_titles_of_images_in_unlabeled_csv(self, csv_path):
        unlabeled_images = {}
        with open(csv_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader) # skip header
            for row in csv_reader:
                unlabeled_images[row[0]] = row[1]
        return unlabeled_images
    
    # get list of images already in the labeled csv file
    def get_titles_of_images_in_labeled_csv(self, csv_path):
        labeled_images = {}
        with open(csv_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader) # skip header
            for row in csv_reader:
                labeled_images[row[1]] = row[2]
        return labeled_images
    
    # get list of blacklisted images already in the blacklisted csv file
    def get_titles_of_images_in_blacklisted_csv(self, csv_path):
        blacklisted_images = {}
        with open(csv_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader) # skip header
            for row in csv_reader:
                blacklisted_images[row[0]] = row[1]
        return blacklisted_images
    
    def remove_image(self):
        with open(self.blacklisted_csv_path, 'a') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([self.image_title.text, self.image.source])

    def get_valid_titles(self):
        all_titles_dict = self.get_titles_of_images_in_unlabeled_csv(self.unlabeled_csv_path)
        labeled_titles_dict = self.get_titles_of_images_in_labeled_csv(self.labeled_csv_path)
        blacklisted_titles_dict = self.get_titles_of_images_in_blacklisted_csv(self.blacklisted_csv_path)

        # get list of titles that are not in the labeled csv file and the blacklisted csv file
        valid_titles = [item for item in all_titles_dict if ((item not in labeled_titles_dict) and (item not in blacklisted_titles_dict))] 
        valid_titles_dict = {k: all_titles_dict[k] for k in valid_titles}
        
        print(f"Total number of images: {len(all_titles_dict)}")
        print(f"Number of images labeled: {len(labeled_titles_dict) + len(blacklisted_titles_dict)}")
        print(f"Number of images to label: {len(valid_titles_dict)}")
        self.image_title.text = f"Number of images labeled: {len(labeled_titles_dict)}\nNumber of images to label: {len(valid_titles_dict)}"
        return valid_titles_dict.keys(), valid_titles_dict

if __name__ == '__main__':
    if (not os.path.exists(LABELED_CSV_PATH)) or (os.stat(LABELED_CSV_PATH).st_size == 0):
        with open(LABELED_CSV_PATH, 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["label", "title", "path"])
    if (not os.path.exists(BLACKLISTED_CSV_PATH)) or (os.stat(BLACKLISTED_CSV_PATH).st_size == 0):
        with open(BLACKLISTED_CSV_PATH, 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["title", "path"])

    LabelingApp(
        unlabeled_csv_path=UNLABELED_CSV_PATH,
        labeled_csv_path=LABELED_CSV_PATH,
        blacklisted_csv_path=BLACKLISTED_CSV_PATH,
        mapped_unlabeled_data_dir=MAPPED_UNLABELED_DATA_DIR
    ).run()