from framework import *


class Converter:

    def __init__(self, raw):
        self.raw = raw
        self.res = ""

    def convert_menuet(self):

        self.res += "\\time 3/4\n\\key " + self.raw.get_key() + " \\major\n"
        self.res += "<<\n"

        for row in range(4):
            self.res += "\\new Staff {"
            self.res += "\\clef \"treble\" "
            for column in range(4):
                measure = self.raw.get_content()[row*4+column]
                length = 0
                for note in measure.get_top_notes():
                    self.res += note.name()
                    if length != note.length():
                        length = note.length()
                        self.res += length
                    self.res += ' '

                self.res += '| '
            self.res += '}\n'

            self.res += "\\new Staff {"
            self.res += "\\clef \"bass\" "
            for column in range(4):
                measure = self.raw.get_content()[row * 4 + column]
                length = 0
                for note in measure.get_bot_notes():
                    self.res += note.name()
                    if length != note.length():
                        length = note.length()
                        self.res += length
                    self.res += ' '

                self.res += '| '
            self.res += '}\n'
            self.res += '>>\n'




