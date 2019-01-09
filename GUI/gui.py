'''
Created by Jianyuan Su
Date: Jan 4, 2019
'''

from tkinter import *

from GUI import start_page, main_page
from framework import *
from output import *


class GUIMain(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Inverse Bach")
        self.geometry('800x600')

        # set container frame
        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # file variables
        self.ly_file = ''
        self.audio_file = ''

        self.frames = {}

        # store all available pages as frames
        for f in (start_page.StartPage, main_page.MainPage):

            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(start_page.StartPage)

    def show_frame(self, cont):
        # display the frame <cont>
        frame = self.frames[cont]
        frame.tkraise()

    def generate(self, key, transkey):
        # generate music files
        f = self.frames[start_page.StartPage]
        ly_dir = f.ly_sframe.get_dir()
        score_dir = f.score_sframe.get_dir()
        audio_dir = f.audio_sframe.get_dir()
        ly_file = self.ly_file
        audio_file = self.audio_file

        m = menuet.Menuet(key, transkey)
        m.generate()  # generate menuet

        c = converter.Converter(m)  # init converter

        # audio output
        midi = c.convert_to_audio()
        a = audio_generator.AudioOut(f'{audio_dir}/{audio_file}')
        a.add_midi(midi)
        a.write_and_close()

        # score output
        score = c.convert_to_score()
        g = ly_generator.LyOut()
        g.create(f'{ly_dir}/{ly_file}')
        g.add(score)
        g.write_and_close()
        g.build(score_dir)

        # process finish!
        print("Generating process successful, enjoy your music!")
