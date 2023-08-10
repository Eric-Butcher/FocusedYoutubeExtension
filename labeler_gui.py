import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.label import Label
import os
import time
import shutil

"""
Requires:
    Kivy - Installation: python -m pip install "kivy[full]" kivy_examples
"""

class LabelingApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=50, spacing=10)
        # Window.maximize()

        self.image = Image(source='./unlabeled_data/Extracting Lidocaine from Anal Lubricant by NileRed.jpg')
        self.image.allow_stretch = True
        self.image.pos_hint = {'center_x': .5, 'center_y': .5}
        self.image.size_hint = (2, 2)
        self.image.padding_top = 10

        self.image_title = Label(text='')
        self.image_title.pos_hint = {'center_x': .5, 'center_y': .5}
        self.image_title.size_hint = (1, 0.5)
        self.image_title.halign = 'center'
        self.image_title.valign = 'middle'
        self.image_title.font_size = 60

        self.category_box = BoxLayout(orientation='horizontal', spacing=100)
        self.category_box.size_hint = (1, 0.2)
        self.category_box.pos_hint = {'center_x': .5, 'center_y': .5}

        self.category_1 = Label(text='Press Z to categorize as \nEducational')
        self.category_1.pos_hint = {'center_y': .5, 'left': 1}
        self.category_1.halign = 'center'
        self.category_1.valign = 'middle'
        self.category_1.font_size = 40

        self.category_2 = Label(text='Press M to categorize as \nEntertainment')
        self.category_2.pos_hint = {'center_y': .5, 'right': 1}
        self.category_2.halign = 'center'
        self.category_2.valign = 'middle'
        self.category_2.font_size = 40

        self.category_box.add_widget(self.category_1)
        self.category_box.add_widget(self.category_2)
        
        self.layout.add_widget(self.image)
        self.layout.add_widget(self.image_title)
        self.layout.add_widget(self.category_box)


        Window.bind(on_key_down=self.key_action)

        self.valid_path_list = self.get_valid_paths()
        self.index = 0

        return self.layout

    def key_action(self, *args):
        keycode = args[1]
        if keycode == 122:  # 'z' key
            shutil.copy(f"./unlabeled_data/{self.valid_path_list[self.index]}", './labeled_data/Educational')
            self.update_image()
        elif keycode == 109:  # 'm' key
            shutil.copy(f"./unlabeled_data/{self.valid_path_list[self.index]}", './labeled_data/Entertainment')
            self.update_image()

    def update_image(self):
        self.index += 1
        if self.index >= len(self.valid_path_list):
            self.image_title.text = "Congrats Eric! You've labeled all the images!"
            time.sleep(600)
        
        file_name = self.valid_path_list[self.index]
        self.image.source = f"./unlabeled_data/{file_name}"
        self.image_title.text = file_name[:-4]

    def get_valid_paths(self):
        all_paths = os.listdir('./unlabeled_data')
        labeled_paths = os.listdir('./labeled_data/Educational') + os.listdir('./labeled_data/Entertainment')
        valid_paths = [item for item in all_paths if item not in labeled_paths]
        print(f"Total number of images: {len(all_paths)}")
        print(f"Number of images labeled: {len(labeled_paths)}")
        print(f"Number of images to label: {len(valid_paths)}")
        self.image_title.text = f"Number of images labeled: {len(labeled_paths)}\nNumber of images to label: {len(valid_paths)}"
        return valid_paths


if __name__ == '__main__':
    LabelingApp().run()