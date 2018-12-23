from measure.py import Measure
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
        return [m1, m2, m3, m4]

    def chord2(self):
        choices=[-1,1]  #can be extended to 2 sharps or flats
        if self.transkey==0:
            self.transkey=random.choice(choices)
        if self.transkey==1:
            choices=[5,6]   #the available transition chordes for the line
            transchord=random.choice(choices)
            m1 = Measure(21, 1)
            m2 = Measure(22, transchord)
            m3 = Measure(23, 5)     #based on transkey
            m4 = Measure(24, 1)     #based on transkey
            return [m1, m2, m3, m4]
        elif self.transkey==-1:
            choices=[2,4]   #the available transition chordes for the line
            transchord = random.choice(choices)
            m1 = Measure(21, 1)
            m2 = Measure(22, transchord)
            m3 = Measure(23, 5)  # based on transkey
            m4 = Measure(24, 1)  # based on transkey
            return [m1, m2, m3, m4]
        #we can also do cases where transkey=2,-2

    def chord3(self):
        sequence=random.choice([False])     #need to include True case
        if (sequence) and (self.transkey==1):
            m1 = Measure(31, 1)     # based on transkey
            m2 = Measure(32, 6)     # based on transkey
            m3 = Measure(33, 1)
            m4 = Measure(34, 1)     #this is the cadence, melody consist only two chord notes, actual chord progression is 1-5
            return [m1,m2,m3,m4]    #this returns only one possibility, many more available
        else:           # case where sequence is False and transkey is -1
            m1 = Measure(31, 1)     # based on transkey
            m2 = Measure(32, 2)     # based on transkey
            m3 = Measure(33, 1)
            m4 = Measure(34, 1)     #this is the cadence
            return [m1,m2,m3,m4]    #this returns only one possibility, many more available

    def chord4(self):
        c1 = self.content[0:4]
        a = c1[3]
        c1[3] = c1[2]
        c1[2] = a
        return c1

    def set_chord_note(self):
        self.content += self.chord1()
        self.content += self.chord2()
        self.content += self.chord3()
        self.content += self.chord4()
        for i in range(0,len(self.content),1):
            (self.content)[i].add_chord_note
        return True

    def gen_passing(self):
        pass

    def to_printable_format(self):
        pass

    def get(self):
        print("key is" ,self.key)
        print("transkey is",self.transkey)
        print(self.content)
        return True
