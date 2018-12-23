from measure.py import Measure
import random

class Menuet:

    def __init__(self, key=-1, transkey=0):
        self.key = key
        self.transkey = transkey
        self.content = []
        self.set_chord_note()

    def set_chord_note(self):
        self.content += self.chord1()
        self.content += self.chord2()
        self.content += self.chord3()
        self.content += self.chord4()

    def chord1(self):
        choices = [2, 4, 5, 6]
        m1 = Measure(11, 1)
        m2 = Measure(12, random.choice(choices))
        m3 = Measure(13, 1)
        m4 = Measure(14, 5)
        return [m1, m2, m3, m4]

    def chord2(self):
        pass

    def chord3(self):
        pass

    def chord4(self):
        c1 = self.content[0:4]
        a = c1[3]
        c1[3] = c1[2]
        c1[2] = a

    def to_printable_format(self):
        pass