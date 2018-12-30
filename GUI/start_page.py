from tkinter import *
from tkinter import filedialog
from GUI import main_page


class StartPage(Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.master = master
        self.controller = controller
        controller.title("InverseBach")

        self.save = IntVar()
        self.save.set(0)

        self.ly_sframe = SelectionFrame(self, text="Select .ly score file generating location")
        self.ly_sframe.pack()
        self.score_sframe = SelectionFrame(self, text="Select music score file generating location")
        self.score_sframe.pack()
        self.audio_sframe = SelectionFrame(self, text="Select audio file generating location")
        self.audio_sframe.pack()

        self.load_settings()

        self.save_check = Checkbutton(self, text="save directory settings", variable=self.save,
                                      onvalue=1, offvalue=0)
        self.save_check.pack()
        self.next_button = Button(self, text="Next", command=self.next_item)
        self.next_button.pack()

        self.master.bind('n', self.next_item)
        self.master.bind('q', quit)

    def next_item(self):
        self.save_settings()
        self.controller.show_frame(main_page.MainPage)

    def load_settings(self):
        try:
            fi = open('settings/dir.setting', 'r')
            self.ly_sframe.set_dir(fi.readline()[0:-1])
            self.score_sframe.set_dir(fi.readline()[0:-1])
            self.audio_sframe.set_dir(fi.readline()[0:-1])
        except FileNotFoundError:
            return

    def save_settings(self):
        if self.save.get() == 1:
            fo = open('settings/dir.setting', 'w')
            s = f'{self.ly_sframe.get_dir()}\n{self.score_sframe.get_dir()}\n{self.audio_sframe.get_dir()}\n'
            fo.write(s)


class SelectionFrame(Frame):
    def __init__(self, master, text="", *args, **kwargs):
        self.master = master
        super().__init__(master, *args, **kwargs)
        self.create_widgets(text)

    def create_widgets(self, text):
        self.dir = StringVar()
        self.label = Label(self, text=text)
        self.label.pack()
        self.frame = Frame(self)
        self.frame.pack()
        self.entry = Entry(self.frame, textvariable=self.dir)
        self.entry.grid(row=0, column=0)
        self.button = Button(self.frame, text="Select Directory",
                             command=self.select_directory)
        self.button.grid(row=0, column=1)

    def select_directory(self):
        name = filedialog.askdirectory()
        self.entry.insert(0, name)
        self.dir.set(name)

    def set_dir(self, d):
        self.dir.set(d)

    def get_dir(self):
        return self.dir.get()
