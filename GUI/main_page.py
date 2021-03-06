'''
Created by Jianyuan Su
Date: Jan 4, 2019
'''

from tkinter import *
from GUI import start_page


class MainPage(Frame):
    def __init__(self, master, controller):
        super().__init__(master)

        # variables
        self.dance = StringVar()
        self.dance.set("Menuet")
        self.key = StringVar()
        self.key.set("random")
        self.transkey = IntVar()

        # dance type selection
        self.dance_label = Label(self, text="Select dance type")
        self.dance_label.grid(row=0, column=0)
        self.dance_option = OptionMenu(self, self.dance, "Menuet")
        self.dance_option.grid(row=0, column=1)

        # key selection
        self.key_option = OptionMenu(self, self.key, 'random', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'aes', 'bes', 'des', 'ees', 'ges')
        self.key_option.grid(row=1, column=0)
        self.transkey_scale = Scale(self, variable=self.transkey, from_=-1, to=1, label='transpose key', orient='horizontal')
        self.transkey_scale.grid(row=2, column=0)

        # trans key selection
        self.back_button = Button(self, text="Back", command=lambda: controller.show_frame(start_page.StartPage))
        self.back_button.grid(row=3, column=0)
        self.gen_button = Button(self, text="Generate", command=lambda: controller.generate(self.key.get(), self.transkey.get()))
        self.gen_button.grid(row=3, column=1)
