from framework.measure import *
import random

class Menuet:

    def __init__(self, key=-1, transkey=0):
        keys = ['f', 'c', 'g', 'd', 'a', 'e', 'b', 'ges', 'des', 'aes', 'ees', 'bes', 'f','c']
        index = random.randint(1, 12)
        self.key = key
        self.transkey = transkey
        if self.key==-1:
            self.key=keys[index]
            if self.transkey == 0:
                transkey_index=random.choice([1, -1])
                self.transkey = keys[transkey_index + index]
            else:
                transkey_index = transkey
                self.transkey = keys[index + transkey_index]
        else:
            self.key=keys[key]
            self.transkey = transkey    #the key that we are transposing to, int value of [-2,-1,+1,+2], cannot be zero
            if self.transkey == 0:
                transkey_index = random.choice([1, -1])
                self.transkey = keys[transkey_index + key]
            else:
                transkey_index = transkey
                self.transkey = keys[key + transkey_index]
        self.transkey_index = transkey_index
        self.content = []


    def chord1(self):
        choices = [2, 4, 5, 6]
        m1 = Measure(11, 1,False)
        m2 = Measure(12, random.choice(choices),False)
        m3 = Measure(13, 1,False)
        m4 = Measure(14, 5,False)
        self.content=self.content + [m1,m2,m3,m4]
        return True

    def chord2(self):
        # choosing which key to transpose to will happen in the init function
        if self.transkey_index == 1:
            choices = [5, 6]   # the available transition chordes for the line
            transchord = random.choice(choices)
            m1 = Measure(21, 1, False)
            m2 = Measure(22, transchord, False)
            m3 = Measure(23, 5, True)     # based on transkey
            m4 = Measure(24, 1, True)     # based on transkey
            self.content = self.content + [m1, m2, m3, m4]
            return True
        elif self.transkey_index == -1:
            choices = [2, 4]   # the available transition chordes for the line
            transchord = random.choice(choices)
            m1 = Measure(21, 1, False)
            m2 = Measure(22, transchord, False)
            m3 = Measure(23, 5, True)  # based on transkey
            m4 = Measure(24, 1, True)  # based on transkey
            self.content = self.content + [m1, m2, m3, m4]
            return True
        # we can also do cases where transkey=2,-2

    def chord3(self):
        sequence=random.choice([False])     # need to include True case
        if sequence and (self.transkey == 1):
            m1 = Measure(31, 1,True)     # based on transkey
            m2 = Measure(32, 6,True)     # based on transkey
            m3 = Measure(33, 1,False)
            m4 = Measure(34, 1,False)
            # this is the cadence, melody consist only two chord notes, actual chord progression is 1-5
            self.content = self.content + [m1, m2, m3, m4]    # this returns only one possibility, many more available
            return True
        else:           # case where sequence is False and transkey is -1
            m1 = Measure(31, 1,True)     # based on transkey
            m2 = Measure(32, 2,True)     # based on transkey
            m3 = Measure(33, 1,False)
            m4 = Measure(34, 1,False)     # this is the cadence
            self.content = self.content + [m1, m2, m3, m4]    # this returns only one possibility, many more available
            return True

    def chord4(self):
        m1 = Measure(41, self.content[0].get_chord_progression(),False)
        m2 = Measure(42, self.content[1].get_chord_progression(),False)
        m3 = Measure(43, self.content[3].get_chord_progression(),False)
        m4 = Measure(44, self.content[2].get_chord_progression(),False)
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
        self.to_printable_format()
        return True

    def to_printable_format(self):
        names = ['c','des','d','ees','e','f','ges','g','aes','a','bes','b']*2
        key_index=-1
        transkey_index=-1
        for i in range(0,len(names),1):
            if self.key==names[i]:
                key_index=i
                break
        for i in range(0,len(names),1):
            if self.transkey==names[i]:
                transkey_index=i
                break
        # if key_index==-1 or transkey_index==-1:
            # print("False in matching key list")
        key_notes=[]
        transkey_notes=[]
        for i in [0, 2, 4, 5, 7, 9, 11]:       # for major scales only
            key_notes=key_notes+[names[key_index+i]]
            transkey_notes=transkey_notes+[names[transkey_index+i]]
        # print("key_notes: ",key_notes)
        # print("transkey_notes ",transkey_notes)
        key_notes=key_notes*2
        transkey_notes=transkey_notes*2
        for i in range(0, len(self.content), 1):      # iteration for one measure
            for g in range(0, len(self.content[i].get_top_notes().get_notes()), 1):       # iteration for the top notes
                if self.content[i].is_trans_measure():
                    if self.content[i].get_top_notes().get_notes()[g].frequency()>=8:
                        name = transkey_notes[self.content[i].get_top_notes().get_notes()[g].frequency()-8] + '\''
                        self.content[i].get_top_notes().get_notes()[g].set_name(name)
                        # print(self.content[i].get_top_notes().get_notes()[g].frequency(),name)
                    else:
                        name = transkey_notes[self.content[i].get_top_notes().get_notes()[g].frequency()-1] + '\''
                        self.content[i].get_top_notes().get_notes()[g].set_name(name)
                        # print(self.content[i].get_top_notes().get_notes()[g].frequency(), name)
                else:
                    if self.content[i].get_top_notes().get_notes()[g].frequency()>=8:
                        name = key_notes[self.content[i].get_top_notes().get_notes()[g].frequency()-8]+'\''
                        self.content[i].get_top_notes().get_notes()[g].set_name(name)
                        # print(self.content[i].get_top_notes().get_notes()[g].frequency(), name)
                    else:
                        name = key_notes[self.content[i].get_top_notes().get_notes()[g].frequency()-1]+'\''
                        self.content[i].get_top_notes().get_notes()[g].set_name(name)
                        # print(self.content[i].get_top_notes().get_notes()[g].frequency(), name)

    def get(self):
        # print("key is" ,self.key)
        # print("transkey is",self.transkey)
        measure_chord_progressions=[]
        for i in range(0,len(self.content), 1):
            measure_chord_progressions=measure_chord_progressions+[(self.content[i]).get_chord_progression()]
        # print("the chord progression is ", measure_chord_progressions)
        return True

    def get_notes(self):
        for i in range(0,len(self.content),1):
            print(self.content[i].get_top_notes().print_notes())
        return True

    def get_content(self):
        return self.content

    '''
    def get_notes_name(self):
        for i in range(0,len(self.content),1):
            print(self.content[i].get_top_notes().print_notes_name())
        return True
    '''

    def get_key(self):
        return self.key

    def get_transkey(self):
        return self.transkey
