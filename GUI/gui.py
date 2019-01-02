from tkinter import *

from GUI import start_page, main_page
from framework import *
from output import *


class GUIMain(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Inverse Bach")
        self.geometry('800x600')

        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.ly_file = ''
        self.audio_file = ''

        self.frames = {}
        for f in (start_page.StartPage, main_page.MainPage):

            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(start_page.StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def generate(self, key, transkey):
        f = self.frames[start_page.StartPage]
        ly_dir = f.ly_sframe.get_dir()
        score_dir = f.score_sframe.get_dir()
        audio_dir = f.audio_sframe.get_dir()
        ly_file = self.ly_file
        audio_file = self.audio_file

        m = menuet.Menuet(key, transkey)
        m.generate()

        c = converter.Converter(m)

        # audio output
        if f.no_audio.get() == 0:
            sample = c.convert_to_wav(framerate=8000)
            a = audio_generator.AudioOut(2, path=f'{audio_dir}/{audio_file}', framerate=8000)
            a.add_sample(sample)
            a.write_and_close()

        # score output

        score = c.convert_to_score()
        g = ly_generator.LyOut()
        g.create(f'{ly_dir}/{ly_file}')
        g.add(score)
        g.write_and_close()
        g.build(score_dir)

        print("Generating process successful, enjoy your music!")

    # def file_check(self, ly, score, audio):
