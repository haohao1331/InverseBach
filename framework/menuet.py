from measure import *
import random

class Menuet:

    def __init__(self, key=-1, transkey=0):
        self.key = key
        if self.key==-1:
            self.key=random.randint(1,12)
        self.transkey = transkey    #the key that we are transposing to, int value of [-2,-1,+1,+2], cannot be zero
        if self.transkey == 0:
            self.transkey=random.choice([1,-1])
        self.content = []

    def chord1(self):
        choices = [2, 4, 5, 6]
        m1 = Measure(11, 1)
        m2 = Measure(12, random.choice(choices))
        m3 = Measure(13, 1)
        m4 = Measure(14, 5)
        self.content=self.content + [m1,m2,m3,m4]
        return True

    def chord2(self):
        choices=[-1,1]  # can be extended to 2 sharps or flats
        if self.transkey == 0:
            self.transkey=random.choice(choices)
        if self.transkey==1:
            choices=[5,6]   # the available transition chordes for the line
            transchord=random.choice(choices)
            m1 = Measure(21, 1)
            m2 = Measure(22, transchord)
            m3 = Measure(23, 5)     # based on transkey
            m4 = Measure(24, 1)     # based on transkey
            self.content = self.content + [m1, m2, m3, m4]
            return True
        elif self.transkey==-1:
            choices=[2,4]   # the available transition chordes for the line
            transchord = random.choice(choices)
            m1 = Measure(21, 1)
            m2 = Measure(22, transchord)
            m3 = Measure(23, 5)  # based on transkey
            m4 = Measure(24, 1)  # based on transkey
            self.content = self.content + [m1, m2, m3, m4]
            return True
        # we can also do cases where transkey=2,-2

    def chord3(self):
        sequence=random.choice([False])     # need to include True case
        if (sequence) and (self.transkey==1):
            m1 = Measure(31, 1)     # based on transkey
            m2 = Measure(32, 6)     # based on transkey
            m3 = Measure(33, 1)
            m4 = Measure(34, 1)
            # this is the cadence, melody consist only two chord notes, actual chord progression is 1-5
            self.content = self.content + [m1, m2, m3, m4]    # this returns only one possibility, many more available
            return True
        else:           # case where sequence is False and transkey is -1
            m1 = Measure(31, 1)     # based on transkey
            m2 = Measure(32, 2)     # based on transkey
            m3 = Measure(33, 1)
            m4 = Measure(34, 1)     # this is the cadence
            self.content = self.content + [m1, m2, m3, m4]    # this returns only one possibility, many more available
            return True

    def chord4(self):
        m1 = Measure(41, self.content[0].get_chord_progression())
        m2 = Measure(42, self.content[1].get_chord_progression())
        m3 = Measure(43, self.content[3].get_chord_progression())
        m4 = Measure(44, self.content[2].get_chord_progression())
        self.content = self.content + [m1,m2,m3,m4]
        return True

    def set_chord_note(self):
        for i in range(0, len(self.content), 1):
            (self.content[i]).add_chord_note()
        return True

    def gen_passing(self):
        pass

    def gen_harmony(self):
        pass

    def generate(self):
        self.chord1()
        self.chord2()
        self.chord3()
        self.chord4()
        self.set_chord_note()
        self.gen_passing()
        self.gen_harmony()
        return True

    def to_printable_format(self):
        pass

    def get(self):
        print("key is" ,self.key)
        print("transkey is",self.transkey)
        measure_chord_progressions=[]
        for i in range(0,len(self.content), 1):
            measure_chord_progressions=measure_chord_progressions+[(self.content[i]).get_chord_progression()]
        print("the chord progression is ", measure_chord_progressions)
        return True

    def get_notes(self):
        for i in range(0,len(self.content),1):
            print(self.content[i].get_top_notes().print_notes())
        return True
