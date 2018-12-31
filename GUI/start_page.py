from tkinter import *
from tkinter import filedialog, messagebox
from GUI import main_page


class StartPage(Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.master = master
        self.controller = controller
        controller.title("InverseBach")

        self.save = IntVar()
        self.save.set(0)
        self.ly_file = StringVar()
        self.ly_file.set("<replace me>")
        self.audio_file = StringVar()
        self.audio_file.set("<replace me>")

        self.ly_sframe = SelectionFrame(self, text="Select .ly score file generating location")
        self.ly_sframe.pack()
        self.ly_file_label = Label(self, text="Enter name of .ly score file")
        self.ly_file_label.pack()
        self.ly_file_entry = Entry(self, textvariable=self.ly_file)
        self.ly_file_entry.pack()

        self.score_sframe = SelectionFrame(self, text="Select music score file generating location")
        self.score_sframe.pack()

        self.audio_sframe = SelectionFrame(self, text="Select audio file generating location")
        self.audio_sframe.pack()
        self.audio_file_label = Label(self, text="Enter name of .wav audio file")
        self.audio_file_label.pack()
        self.audio_file_entry = Entry(self, textvariable=self.audio_file)
        self.audio_file_entry.pack()

        self.load_settings()

        self.save_check = Checkbutton(self, text="save directory settings", variable=self.save,
                                      onvalue=1, offvalue=0)
        self.save_check.pack()
        self.next_button = Button(self, text="Next", command=self.next_item)
        self.next_button.pack()

        self.master.bind('n', self.next_item)
        self.master.bind('q', quit)

    def next_item(self):
        error_entries = self.get_error_entries()
        if len(error_entries) > 0:
            err_m = "The contents in these entries are invalid\n"
            entry_name = {self.ly_file_entry: ".ly music score file name",
                          self.audio_file_entry: ".wav audio score file name",
                          self.ly_sframe.entry: ".ly music score directory",
                          self.score_sframe.entry: ".pdf music score directory",
                          self.audio_sframe.entry: ".wav audio file directory"
                          }

            for entry in error_entries:
                entry.configure(bg='red')
                entry.delete(0, 'end')
                err_m += entry_name[entry] + '\n'

            messagebox.showerror("Error", err_m)
            return

        self.controller.ly_file = self.ly_file.get() + '.ly'
        self.controller.audio_file = self.audio_file.get() + '.wav'

        self.ly_file_entry.config(bg='white')
        self.audio_file_entry.config(bg='white')

        self.save_settings()
        self.controller.show_frame(main_page.MainPage)

    def load_settings(self):
        try:
            fi = open('settings/start.setting', 'r')
            self.ly_sframe.set_dir(fi.readline()[0:-1])
            self.score_sframe.set_dir(fi.readline()[0:-1])
            self.audio_sframe.set_dir(fi.readline()[0:-1])
            self.ly_file.set(fi.readline()[0:-1])
            self.audio_file.set(fi.readline()[0:-1])
        except FileNotFoundError:
            return

    def save_settings(self):
        if self.save.get() == 1:
            fo = open('settings/start.setting', 'w')
            s = f'{self.ly_sframe.get_dir()}\n{self.score_sframe.get_dir()}\n{self.audio_sframe.get_dir()}\n' \
                f'{self.ly_file.get()}\n{self.audio_file.get()}\n'
            fo.write(s)

    def get_error_entries(self):
        ret = []
        if self.ly_sframe.get_dir() == '':
            ret.append(self.ly_sframe.entry)
        if self.score_sframe.get_dir() == '':
            ret.append(self.score_sframe.entry)
        if self.audio_sframe.get_dir() == '':
            ret.append(self.audio_sframe.entry)

        if not self.entry_check(self.ly_file.get()):
            ret.append(self.ly_file_entry)
        if not self.entry_check(self.audio_file.get()):
            ret.append(self.audio_file_entry)

        return ret

    @staticmethod
    def entry_check(var):
        if len(var) == 0 or re.search(r'[^A-Za-z0-9_\-\\]', var):
            return False
        return True

    def reset_bgcolor(self, entry):
        if entry.cget('bg') == 'red':
            entry.configure(bg='white')


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
        self.entry = Entry(self.frame, textvariable=self.dir, state='disabled')
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
