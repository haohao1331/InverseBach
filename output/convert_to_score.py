from framework import *


class Converter:

    def __init__(self, raw):
        self.raw = raw

    def convert_menuet(self):

        length_map = {1: '4', 2: '2', 3: '2.', 0.5: '8', 1.5: '4.'}

        res = ""
        res += "\\new PianoStaff \n<< "
        res += "\\new Staff { "

        men = self.raw.get_content()

        res += "\\time 3/4 \\clef \"treble\" \\key " + self.raw.get_key() + " \\major "

        length = 0
        for row in range(4):

            for column in range(4):
                msr = men[row*4+column]

                for n in msr.get_top_notes():
                    res += n.name()
                    if length != n.length():
                        length = n.length()
                        res += length_map[length]
                    res += ' '

            if row != 3:
                res += '\\break '

        res += '}\n'

        res += "\\new Staff { \\clef \"bass\" "

        length = 0
        for row in range(4):

            for column in range(4):
                msr = men[row * 4 + column]

                for n in msr.get_top_notes():
                    res += n.name()
                    if length != n.length():
                        length = n.length()
                        res += length_map[length]
                    res += ' '

            if row != 3:
                res += '\\break '

        res += '} >>'

        return res
