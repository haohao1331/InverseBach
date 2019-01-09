'''
created by Xinghao Li,Jan 4,2019
'''

from framework.measure import *
import random


class Menuet:

    def __init__(self, key='random', transkey=0):
        keys = {'c':1, 'g':2, 'd':3, 'a':4, 'e':5, 'b':6, 'ges':7, 'des':8, 'aes':9, 'ees':10, 'bes':11, 'f':12}
        key_list = ['f','c', 'g', 'd', 'a', 'e', 'b', 'ges', 'des', 'aes', 'ees', 'bes', 'f','c']
        if key=='random':
            index=random.randint(1,12)
        else:
            index=keys[key]
        if transkey==0:
            transkey_index=random.choice([1,-1])
        else:
            transkey_index=transkey
        self.key = key_list[index]      # the key of the menuet
        self.transkey = key_list[index + transkey_index]    # the transpose key of the menuet
        self.A = {'a': 0, 'bes': 1, 'b': 2, 'c': 3, 'des': 4, 'd': 5, 'ees': 6, 'e': 7, 'f': 8, 'ges': 9, 'g': 10,
                  'aes': 11}    # will be later refferenced as A-frequency
        self.B = ['a', 'bes', 'b', 'c', 'des', 'd', 'ees', 'e', 'f', 'ges', 'g', 'aes'] * 2 + ['a']
        # A and B are for converting between numbers and the name of the key
        self.key_index=self.A[self.key]     # the A-frequency of the key
        self.transkey_index=self.A[self.transkey]   # the A-frequency of the transkey
        self.key_notes=self.generate_key_notes()    # list of key notes in A-freq
        self.transkey_notes=self.generate_transkey_notes()  # list of transkey notes in A-freq
        self.content = []

    def chord1(self):   # generating the chord progression for line 1
        m1 = Measure(11, 1,False)
        m2 = Measure(12, random.choice([2, 4, 6]),False)    # these are the chords that transition the keys
        m3 = Measure(13, 1,False)
        m4 = Measure(14, 5,False)
        self.content=self.content + [m1, m2, m3, m4]
        return True

    def chord2(self):       # generating the chord progression for line 2
        if self.key_index-self.transkey_index== 5 or self.transkey_index-self.key_index==7: # case where transkey +1
            transchord = random.choice([5, 6])  # the available transition chordes for the line
            m1 = Measure(21, 1, False)
            m2 = Measure(22, transchord, False)
            m3 = Measure(23, 5, True)  # based on transkey
            m4 = Measure(24, 1, True)  # based on transkey
            self.content = self.content + [m1, m2, m3, m4]
        elif self.key_index-self.transkey_index== 7 or self.transkey_index-self.key_index==5:
            transchord = random.choice([2, 4])      # the available transition chordes for the line
            m1 = Measure(21, 1, False)
            m2 = Measure(22, transchord, False)
            m3 = Measure(23, 5, True)  # based on transkey
            m4 = Measure(24, 1, True)  # based on transkey
            self.content = self.content + [m1, m2, m3, m4]
        # we can also do cases where transkey=2,-2
        else:
            print("error: second line chord not added")
        return True

    def chord3(self):       # generating the chord progression for line 3
        sequence = random.choice([False])  # need to include True case
        if sequence and (self.transkey == 1):
            m1 = Measure(31, 1, True)  # based on transkey
            m2 = Measure(32, 6, True)  # based on transkey
            m3 = Measure(33, 1, False)
            m4 = Measure(34, 1, False)
            # this is the cadence, melody consist only two chord notes, actual chord progression is 1-5
            self.content = self.content + [m1, m2, m3, m4]  # this returns only one possibility, many more available
        else:  # case where sequence is False and transkey is -1
            m1 = Measure(31, 1, True)  # based on transkey
            m2 = Measure(32, 2, True)  # based on transkey
            m3 = Measure(33, 1, False)
            m4 = Measure(34, 1, False)  # this is the cadence
            self.content = self.content + [m1, m2, m3, m4]  # this returns only one possibility, many more available
        return True

    def chord4(self):       # generating the chord progression for line 4, the last line will be same as the
                            # first line but with an authentic cadence
        m1 = Measure(41, self.content[0].get_chord_progression(), False)
        m2 = Measure(42, self.content[1].get_chord_progression(), False)
        m3 = Measure(43, self.content[3].get_chord_progression(), False)
        m4 = Measure(44, self.content[2].get_chord_progression(), False)
        self.content = self.content + [m1, m2, m3, m4]
        return True

    def set_first_note(self):       # first note of the first measures of each line
        starting_note=13
        for i in range(0,len(self.content),4):
            available=self.chord_to_note(self.content[i].is_trans_measure(),1)
            f1=self.closest(starting_note,available,1)      # this allows f1 to be the same as the pivot
            self.content[i].get_top_notes().add_chord_note(Note(f1, 1, True))
        return True

    def set_chord1(self):       # set chord note for the first bars of each line
        for i in range(0, len(self.content), 4):
            available=self.get_chord_notes(self.content[i].is_trans_measure(),self.content[i].get_chord_progression())
            f1=self.content[i].get_top_notes().get_notes()[0].frequency()
            f2=random.choice(self.closest(f1,available,2))
            f3=random.choice(self.closest(f2,available,2))
            self.content[i].get_top_notes().add_chord_note(Note(f2, 1, True))
            self.content[i].get_top_notes().add_chord_note(Note(f3, 1, True))
        return True

    def set_chord2(self):       # set chord note for the second bars of each line
        for i in range(1,len(self.content),4):
            f0 = self.content[i - 1].get_top_notes().get_notes()[2].frequency()
            available=self.get_chord_notes(self.content[i].is_trans_measure(),self.content[i].get_chord_progression())
            f1 = random.choice(self.closest(f0, available, 2))
            f2 = random.choice(self.closest(f1, available, 2))
            f3 = random.choice(self.closest(f2, available, 2))
            self.content[i].get_top_notes().add_chord_note(Note(f1, 1, True))
            self.content[i].get_top_notes().add_chord_note(Note(f2, 1, True))
            self.content[i].get_top_notes().add_chord_note(Note(f3, 1, True))
        return True

    def set_chord3(self):       # set chord note for the third bars of each line
        for i in range(2, len(self.content), 4):
            f0 = self.content[i - 1].get_top_notes().get_notes()[2].frequency()
            available = self.get_chord_notes(self.content[i].is_trans_measure(),
                                             self.content[i].get_chord_progression())
            f1 = random.choice(self.closest(f0, available, 2))
            f2 = random.choice(self.closest(f1, available, 2))
            if self.content[i].get_location()==33:
                fifth=self.chord_to_note(self.content[i].is_trans_measure(),5)
                no5=[]
                for g in range(0,len(available),1):
                    if available[g] not in fifth:
                        no5=no5+[available[g]]

                f3 = random.choice(self.closest(f2, no5, 2))
            else:
                f3 = random.choice(self.closest(f2, available, 2))
            self.content[i].get_top_notes().add_chord_note(Note(f1, 1, True))
            self.content[i].get_top_notes().add_chord_note(Note(f2, 1, True))
            self.content[i].get_top_notes().add_chord_note(Note(f3, 1, True))
        return True

    def set_chord4(self):           # set chord note for the fourth bars of each line
        for i in range(3,len(self.content),4):
            f0 = self.content[i - 1].get_top_notes().get_notes()[2].frequency()
            if i==3:
                if self.note_to_chord(self.content[i].is_trans_measure(),f0)==1:
                    available=self.chord_to_note(self.content[i].is_trans_measure(),random.choice([2,7]))
                elif self.note_to_chord(self.content[i].is_trans_measure(),f0)==3:
                    available = self.chord_to_note(self.content[i].is_trans_measure(), 2)
                elif self.note_to_chord(self.content[i].is_trans_measure(),f0)==5:
                    available = self.chord_to_note(self.content[i].is_trans_measure(), 5)
                else:
                    print("false in set_chord4 line 1")
            elif i==7:
                if self.note_to_chord(self.content[i].is_trans_measure(),f0)==2:
                    available = self.chord_to_note(self.content[i].is_trans_measure(), 1)
                elif self.note_to_chord(self.content[i].is_trans_measure(),f0)==7:
                    available = self.chord_to_note(self.content[i].is_trans_measure(), 1)
                elif self.note_to_chord(self.content[i].is_trans_measure(),f0)==5:
                    available = self.chord_to_note(self.content[i].is_trans_measure(), 3)
                else:
                    print("false in set_chord4 line 2")
            elif i==11:
                if self.note_to_chord(self.content[i].is_trans_measure(),f0)==1:
                    available=self.chord_to_note(self.content[i].is_trans_measure(), 7)
                elif self.note_to_chord(self.content[i].is_trans_measure(),f0)==3:
                    available = self.chord_to_note(self.content[i].is_trans_measure(), 2)
                else:
                    print("false in set_chord4 line 3")
            elif i==15:
                if self.note_to_chord(self.content[i].is_trans_measure(),f0)==2:
                    available=self.chord_to_note(self.content[i].is_trans_measure(), 1)
                elif self.note_to_chord(self.content[i].is_trans_measure(),f0)==7:
                    available = self.chord_to_note(self.content[i].is_trans_measure(), 1)
                elif self.note_to_chord(self.content[i].is_trans_measure(),f0)==5:
                    available = self.chord_to_note(self.content[i].is_trans_measure(), 3)
                else:
                    print("false in set_chord4 line 4")
            else:
                print("false in set_chord4")
            f1 = self.closest(f0, available, 1)
            self.content[i].get_top_notes().add_chord_note(Note(f1, 3, True))

        return True

    def gen_passing(self):      # generates the passing note of each bar
        notes=[]
        motives = [[], [2], [1], [0], [1,2],[0,2], [0,1], [0,1,2], [1.5, 0.5, 1],   # the motives determines the rhythm of each bar
                   [1, 1.5, 0.5], [2, 1], [1, 2]]
        for i in range(0,len(self.content),1):
            notes=notes+[[]]
            for g in range(0, len(self.content[i].get_top_notes().get_notes()), 1):
                notes[i]=notes[i]+[self.content[i].get_top_notes().get_notes()[g].frequency()]
        self.content[0].set_motive(random.randint(1, 9))
        self.content[1].set_motive(random.randint(0, 9))
        self.content[2].set_motive(random.randint(0, 9))
        self.content[3].set_motive(12)
        self.content[4].set_motive(self.content[0].get_motive())
        self.content[5].set_motive(self.content[1].get_motive())
        self.content[6].set_motive(self.content[2].get_motive())
        self.content[7].set_motive(12)
        self.content[8].set_motive(random.randint(0, 9))
        self.content[9].set_motive(random.randint(0, 9))
        self.content[10].set_motive(random.randint(0, 9))
        self.content[11].set_motive(11)
        self.content[12].set_motive(self.content[0].get_motive())
        self.content[13].set_motive(self.content[1].get_motive())
        self.content[14].set_motive(self.content[2].get_motive())
        self.content[15].set_motive(12)
        for i in range(0,len(self.content),1):
            if self.content[i].get_motive() == 11:    # adding the cadence at the end of line 3
                self.content[i].get_top_notes().get_notes()[0].set_length(2)
                # setting the chord note to length 2
                f1 = self.content[i].get_top_notes().get_notes()[0].frequency()
                f2 = self.closest(f1,self.chord_to_note(self.content[i].is_trans_measure(),self.note_to_chord(self.content[i].is_trans_measure(),f1)+1),1)
                self.content[i].get_top_notes().insert_note(Note(f2,1,False),0)
            elif self.content[i].get_motive() == 12:  # doing noting
                pass
            elif self.content[i].get_motive() == 8:
                self.content[i].get_top_notes().get_notes()[0].set_length(1.5)
                self.content[i].get_top_notes().get_notes()[1].set_length(0.5)
            elif self.content[i].get_motive() == 9:
                self.content[i].get_top_notes().get_notes()[1].set_length(1.5)
                self.content[i].get_top_notes().get_notes()[2].set_length(0.5)
            elif self.content[i].get_motive() == 10:
                pass
            elif self.content[i].get_motive() == 0:
                pass
            else:                                       # adding simple passing notes
                step2 = [0, 0, 0]
                for g in motives[int(self.content[i].get_motive())]:
                    if g==2:
                        step2[2]=1
                        self.content[i].get_top_notes().get_notes()[2 + step2[0]+step2[1]].set_length(0.5)
                        fp=self.get_passing_note(self.content[i].is_trans_measure(),notes[i][2],notes[i+1][0],self.content[i].get_chord_progression())
                        self.content[i].get_top_notes().insert_note((Note(fp, 0.5, False)), 3 + step2[0]+step2[1])
                    if g==1:
                        step2[1] = 1
                        self.content[i].get_top_notes().get_notes()[1+step2[0]].set_length(0.5)
                        fp = self.get_passing_note(self.content[i].is_trans_measure(), notes[i][1], notes[i][2], self.content[i].get_chord_progression())
                        self.content[i].get_top_notes().insert_note((Note(fp, 0.5, False)), 2+step2[0])
                    if g==0:
                        step2[0] = 1
                        self.content[i].get_top_notes().get_notes()[0].set_length(0.5)
                        fp = self.get_passing_note(self.content[i].is_trans_measure(), notes[i][0], notes[i][1], self.content[i].get_chord_progression())
                        self.content[i].get_top_notes().insert_note((Note(fp, 0.5, False)), 1)
        return True

    def gen_cadence_harmony(self):      # generating the left hand for each cadence part, fourth bar of each line
        pivot=18
        for i in range(3,len(self.content),4):
            if self.content[i].get_location()//10==3:
                f1 = self.closest(pivot,self.chord_to_note(self.content[i].is_trans_measure(),5),1)
                self.content[i].get_bot_notes().add_chord_note(Note(f1, 3, True))
            elif self.content[i].get_location()%10==4:
                phrase_ending=random.randint(1,3)
                if phrase_ending==1:    # [1,1,1]
                    f1=self.closest(pivot,self.chord_to_note(self.content[i].is_trans_measure(),self.content[i].get_chord_progression()),1)
                    if f1<=5:
                        f1=f1+12
                    f2=f1-5
                    f3=f1-12
                    self.content[i].get_bot_notes().add_chord_note(Note(f1, 1, True))
                    self.content[i].get_bot_notes().add_chord_note(Note(f2, 1, True))
                    self.content[i].get_bot_notes().add_chord_note(Note(f3, 1, True))
                elif phrase_ending==2:
                    f1 = self.closest(pivot, self.chord_to_note(self.content[i].is_trans_measure(),
                                                                self.content[i].get_chord_progression()), 1)
                    if f1 <= 5:
                        f1 = f1 + 12
                    f2 = f1 - 5
                    f3 = f1 - 8
                    f4= f1-12
                    self.content[i].get_bot_notes().add_chord_note(Note(f1, 1, True))
                    self.content[i].get_bot_notes().add_chord_note(Note(f2, 0.5, True))
                    self.content[i].get_bot_notes().add_chord_note(Note(f3, 0.5, True))
                    self.content[i].get_bot_notes().add_chord_note(Note(f4, 1, True))
                elif phrase_ending == 3:
                    f1 = self.closest(pivot, self.chord_to_note(self.content[i].is_trans_measure(),
                                                                self.content[i].get_chord_progression()), 1)
                    if f1 <= 5:
                        f1 = f1 + 12
                    f2 = f1 - 5
                    f3 = f1 - 8
                    f4 = f1 - 12
                    self.content[i].get_bot_notes().add_chord_note(Note(f1, 0.5, True))
                    self.content[i].get_bot_notes().add_chord_note(Note(f2, 0.5, True))
                    self.content[i].get_bot_notes().add_chord_note(Note(f3, 0.5, True))
                    self.content[i].get_bot_notes().add_chord_note(Note(f2, 0.5, True))
                    self.content[i].get_bot_notes().add_chord_note(Note(f4, 1, True))
                else:
                    print("error in setting phrase ending")
        return True

    def gen_first_measure_harmony(self):        # setting the left hand for the first measure
        pivot=15
        for i in range(0,len(self.content),4):
            top_chord_notes=[]
            for g in range(0,len(self.content[i].get_top_notes().get_notes()),1):
                if self.content[i].get_top_notes().get_notes()[g].is_chord_note():
                    top_chord_notes=top_chord_notes+[self.content[i].get_top_notes().get_notes()[g].frequency()]
            f1=self.closest(pivot,self.chord_to_note(self.content[i].is_trans_measure(),self.content[i].get_chord_progression()),1)
            if self.note_to_chord(self.content[i].is_trans_measure(),top_chord_notes[1])==5 or self.note_to_chord(self.content[i].is_trans_measure(),top_chord_notes[1])==1:
                f2=self.closest(f1,self.chord_to_note(self.content[i].is_trans_measure(),3),1)
            elif self.note_to_chord(self.content[i].is_trans_measure(),top_chord_notes[1])==3:
                one=self.closest(f1,self.chord_to_note(self.content[i].is_trans_measure(),1),1)
                five=self.closest(f1,self.chord_to_note(self.content[i].is_trans_measure(),5),1)
                f2=random.choice([one,five])
            else:
                print("error in first measure harmony bar",i+1)
            if self.note_to_chord(self.content[i].is_trans_measure(),top_chord_notes[2])==5 or self.note_to_chord(self.content[i].is_trans_measure(),top_chord_notes[2])==1:
                f3=self.closest(f2,self.chord_to_note(self.content[i].is_trans_measure(),3),1)
            elif self.note_to_chord(self.content[i].is_trans_measure(),top_chord_notes[2])==3:
                one=self.closest(f2,self.chord_to_note(self.content[i].is_trans_measure(),1),1)
                five=self.closest(f2,self.chord_to_note(self.content[i].is_trans_measure(),5),1)
                f3=random.choice([one,five])
            else:
                print("error in first measure harmony bar", i + 1)
            self.content[i].get_bot_notes().add_chord_note(Note(f1, 1, True))
            self.content[i].get_bot_notes().add_chord_note(Note(f2, 1, True))
            self.content[i].get_bot_notes().add_chord_note(Note(f3, 1, True))
        return True

    def gen_harmony(self):      # generates the rest of the harmony
        pivot = 15
        for i in range(0, len(self.content), 1):
            if self.content[i].get_location()%10 in [2,3]:
                top_chord_notes = []
                for g in range(0, len(self.content[i].get_top_notes().get_notes()), 1):
                    if self.content[i].get_top_notes().get_notes()[g].is_chord_note():
                        top_chord_notes = top_chord_notes + [self.content[i].get_top_notes().get_notes()[g].frequency()]
                if abs(self.note_to_chord(self.content[i].is_trans_measure(),top_chord_notes[0]) - self.content[i].get_chord_progression()) in [0,4,3]:
                    f1 = self.closest(pivot, self.chord_to_note(self.content[i].is_trans_measure(), self.content[i].get_chord_progression()+2), 1)
                elif abs(self.note_to_chord(self.content[i].is_trans_measure(), top_chord_notes[0]) - self.content[i].get_chord_progression()) in [2,5]:
                    one = self.closest(pivot, self.chord_to_note(self.content[i].is_trans_measure(), self.content[i].get_chord_progression()), 1)
                    five = self.closest(pivot, self.chord_to_note(self.content[i].is_trans_measure(), self.content[i].get_chord_progression()+4), 1)
                    f1 = random.choice([one, five])
                else:
                    print("error in gen harmony bar:",i+1)
                if abs(self.note_to_chord(self.content[i].is_trans_measure(),top_chord_notes[1]) - self.content[i].get_chord_progression()) in [0,4,3]:
                    f2 = self.closest(pivot, self.chord_to_note(self.content[i].is_trans_measure(), self.content[i].get_chord_progression()+2), 1)
                elif abs(self.note_to_chord(self.content[i].is_trans_measure(), top_chord_notes[1]) - self.content[i].get_chord_progression()) in [2,5]:
                    one = self.closest(f1, self.chord_to_note(self.content[i].is_trans_measure(), self.content[i].get_chord_progression()), 1)
                    five = self.closest(f1, self.chord_to_note(self.content[i].is_trans_measure(), self.content[i].get_chord_progression()+4), 1)
                    f2 = random.choice([one, five])
                else:
                    print("error in gen harmony bar:",i+1)
                if abs(self.note_to_chord(self.content[i].is_trans_measure(),top_chord_notes[2]) - self.content[i].get_chord_progression()) in [0,4,3]:
                    f3 = self.closest(pivot, self.chord_to_note(self.content[i].is_trans_measure(), self.content[i].get_chord_progression()+2), 1)
                elif abs(self.note_to_chord(self.content[i].is_trans_measure(), top_chord_notes[2]) - self.content[i].get_chord_progression()) in [2,5]:
                    one = self.closest(f2, self.chord_to_note(self.content[i].is_trans_measure(), self.content[i].get_chord_progression()), 1)
                    five = self.closest(f2, self.chord_to_note(self.content[i].is_trans_measure(), self.content[i].get_chord_progression()+4), 1)
                    f3 = random.choice([one, five])
                else:
                    print("error in gen harmony bar:",i+1)
                self.content[i].get_bot_notes().add_chord_note(Note(f1, 1, True))
                self.content[i].get_bot_notes().add_chord_note(Note(f2, 1, True))
                self.content[i].get_bot_notes().add_chord_note(Note(f3, 1, True))
        return True

    def decorate_harmony(self):     # adding some passing notes to the harmony
        for i in range(0,len(self.content)-1,1):
            if self.content[i].get_location() not in [14,24,34,44]:
                f1 = self.content[i].get_bot_notes().get_notes()[0].frequency()
                f2 = self.content[i].get_bot_notes().get_notes()[1].frequency()
                f3 = self.content[i].get_bot_notes().get_notes()[2].frequency()
                f4 = self.content[i+1].get_bot_notes().get_notes()[0].frequency()
                f=[f1,f2,f3,f4]
                step2=[0,0,0]
                for g in range(0,len(f)-1,1):
                    if abs(f[g]-f[g+1]) in [3,4]:
                        step2[g]=1
                        fp=self.get_passing_note(self.content[i].is_trans_measure(),f[g],f[g+1],self.content[i].get_chord_progression())
                        self.content[i].get_bot_notes().get_notes()[g+sum(step2[0:g])].set_length(0.5)
                        self.content[i].get_bot_notes().insert_note(Note(fp, 0.5, False),1+g+sum(step2[0:g]))
        return True

    def to_printable_format(self):      # converts everything into new format such that it is able to create WAV file for
                                        # the audio and pdf for the music score
        for i in range(0, len(self.content), 1):      # iteration for one measure
            for g in range(0, len(self.content[i].get_top_notes().get_notes()), 1):       # iteration for the top notes
                if self.content[i].get_top_notes().get_notes()[g].frequency()>=15:
                    name = self.B[self.content[i].get_top_notes().get_notes()[g].frequency()-12]+ '\'\''
                    self.content[i].get_top_notes().get_notes()[g].set_name(name)
                elif self.content[i].get_top_notes().get_notes()[g].frequency()>=3:
                    name = self.B[self.content[i].get_top_notes().get_notes()[g].frequency()] + '\''
                    self.content[i].get_top_notes().get_notes()[g].set_name(name)
                else:
                    name = self.B[self.content[i].get_top_notes().get_notes()[g].frequency()]
                    self.content[i].get_top_notes().get_notes()[g].set_name(name)
        for i in range(0, len(self.content), 1):      # iteration for one measure
            for g in range(0, len(self.content[i].get_bot_notes().get_notes()), 1):     # iteration for bot notes
                if self.content[i].get_bot_notes().get_notes()[g].frequency()>=15:
                    name = self.B[self.content[i].get_bot_notes().get_notes()[g].frequency()-12]
                    self.content[i].get_bot_notes().get_notes()[g].set_name(name)
                elif self.content[i].get_bot_notes().get_notes()[g].frequency()>=3:
                    name = self.B[self.content[i].get_bot_notes().get_notes()[g].frequency()] +','
                    self.content[i].get_bot_notes().get_notes()[g].set_name(name)
                else:
                    name = self.B[self.content[i].get_bot_notes().get_notes()[g].frequency()] +',,'
                    self.content[i].get_bot_notes().get_notes()[g].set_name(name)

        A={'c':48,'des':49,'d':50,'ees':51,'e':52,'f':53,'ges':54,'g':55,'aes':56,'a':57,'bes':58,'b':59}

        for i in range(0,len(self.content),1):          # converting into piano keys for audio
            for g in range(0,len(self.content[i].get_top_notes().get_notes()),1):
                if self.content[i].get_top_notes()[g].name()[len(self.content[i].get_top_notes()[g].name())-1]=='\'':       # top notes with c'
                    accum=0
                    for h in range(len(self.content[i].get_top_notes()[g].name())-1,-1,-1):
                        if self.content[i].get_top_notes()[g].name()[h]!='\'':
                            break
                        accum=accum+1
                    frequency = A[self.content[i].get_top_notes()[g].name()[0:len(self.content[i].get_top_notes()[g].name())-accum]]+12*accum
                    self.content[i].get_top_notes()[g].set_frequency(frequency)
                elif self.content[i].get_top_notes()[g].name()[len(self.content[i].get_top_notes()[g].name())-1]==',':       # top notes with c,
                    accum=0
                    for h in range(len(self.content[i].get_top_notes()[g].name())-1,-1,-1):
                        if self.content[i].get_top_notes()[g].name()[h]!=',':
                            break
                        accum=accum+1
                    frequency = A[self.content[i].get_top_notes()[g].name()[0:len(self.content[i].get_top_notes()[g].name())-accum]]-(12**accum)
                    self.content[i].get_top_notes()[g].set_frequency(frequency)
                else:
                    frequency = A[self.content[i].get_top_notes()[g].name()]
                    self.content[i].get_top_notes()[g].set_frequency(frequency)
            for g in range(0, len(self.content[i].get_bot_notes().get_notes()), 1):
                if self.content[i].get_bot_notes()[g].name()[len(self.content[i].get_bot_notes()[g].name())-1]=='\'':       # bot notes with c'
                    accum=0
                    for h in range(len(self.content[i].get_bot_notes()[g].name())-1,-1,-1):
                        if self.content[i].get_bot_notes()[g].name()[h]!='\'':
                            break
                        accum=accum+1
                    frequency = A[self.content[i].get_bot_notes()[g].name()[0:len(self.content[i].get_bot_notes()[g].name())-accum]]+12*accum
                    self.content[i].get_bot_notes()[g].set_frequency(frequency)
                elif self.content[i].get_bot_notes()[g].name()[len(self.content[i].get_bot_notes()[g].name())-1]==',':       # bot notes with c,
                    accum=0
                    for h in range(len(self.content[i].get_bot_notes()[g].name())-1,-1,-1):
                        if self.content[i].get_bot_notes()[g].name()[h]!=',':
                            break
                        accum=accum+1
                    frequency = A[self.content[i].get_bot_notes()[g].name()[0:len(self.content[i].get_bot_notes()[g].name())-accum]]-(12*accum)
                    self.content[i].get_bot_notes()[g].set_frequency(frequency)
                else:
                    frequency = A[self.content[i].get_bot_notes()[g].name()]
                    self.content[i].get_bot_notes()[g].set_frequency(frequency)
        return True

    def generate(self):     # generating the menuet
        self.chord1()
        self.chord2()
        self.chord3()
        self.chord4()
        print("Done chord progression generation")
        self.set_first_note()
        self.set_chord1()
        self.set_chord2()
        self.set_chord3()
        self.set_chord4()
        print("Done chord notes generation")
        self.gen_passing()
        print("Done passing note generation")
        self.gen_cadence_harmony()
        self.gen_first_measure_harmony()
        self.gen_harmony()
        self.decorate_harmony()
        print("Done harmony generation")
        self.to_printable_format()
        print("Done generation")
        # self.get_notes_name()
        return True

    def get(self):      # for debugging
        print("key is" ,self.key)
        print("transkey is",self.transkey)
        print("key_notes:      ", self.key_notes)
        print("transkey_notes: ", self.transkey_notes)
        print("key_index: ",self.key_index)
        print("transkey_index: ",self.transkey_index)
        measure_chord_progressions=[]
        for i in range(0,len(self.content), 1):
            measure_chord_progressions=measure_chord_progressions+[(self.content[i]).get_chord_progression()]
        print("the chord progression is ", measure_chord_progressions)
        return True

    def get_notes(self):
        print("Top notes are: ")
        for i in range(0, len(self.content), 1):
            self.content[i].get_top_notes().print_notes()
        print("Bot notes are: ")
        for i in range(0, len(self.content), 1):
            self.content[i].get_bot_notes().print_notes()
            pass
        return True

    def get_content(self):
        return self.content

    def get_notes_name(self):
        for i in range(0,len(self.content),1):
            print(self.content[i].get_top_notes().print_notes_name())
        return True

    def get_key(self):
        return self.key

    def get_transkey(self):
        return self.transkey

    def generate_key_notes(self):       # generates all the notes that belong to key, in A freq
        for i in range(0, len(self.B), 1):
            if self.key == self.B[i]:
                self.key_index = i
                break
        if self.key_index==-1:
            print("False in matching key list")
        key_notes = []
        for i in [0, 2, 4, 5, 7, 9, 11]:  # for major scales only
            key_notes = key_notes + [self.key_index + i]
        a=[]
        b=[]
        for i in range(0,len(key_notes),1):
            a=a+[key_notes[i]-12]
            b=b+[key_notes[i]+12]
        key_notes=a+key_notes+b
        storekey=[]
        for i in range(0,len(key_notes),1):
            if 0<=key_notes[i]<=24:
                storekey=storekey+[key_notes[i]]
        return storekey

    def generate_transkey_notes(self):      # generates all the notes that belong to transkey, in A freq
        for i in range(0, len(self.B), 1):
            if self.transkey == self.B[i]:
                self.transkey_index = i
                break
        if self.transkey_index==-1:
            print("False in matching key list")
        transkey_notes = []
        for i in [0, 2, 4, 5, 7, 9, 11]:  # for major scales only
            transkey_notes = transkey_notes + [self.transkey_index + i]
        c=[]
        d=[]
        for i in range(0,len(transkey_notes),1):
            c=c+[transkey_notes[i]-12]
            d=d+[transkey_notes[i]+12]
        transkey_notes=c+transkey_notes+d
        storetranskey=[]
        for i in range(0,len(transkey_notes),1):
            if 0<=transkey_notes[i]<=24:
                storetranskey=storetranskey+[transkey_notes[i]]
        return storetranskey

    def chord_to_note(self,is_transkey,chord_note):   # is_transkey is True/False, chord_note is the note position 1-7
                                            # returns the corresponding list of notes when given the chord progression
        convert = [11, 0, 2, 4, 5, 7, 9, 11]
        if not is_transkey:
            s = self.key_index
        else:
            s = self.transkey_index
        note = (s + convert[(chord_note % 7)]) % 12
        notes = []
        for i in range(0, 25, 1):
            if i % 12==note:
                notes = notes + [int(i)]
        return notes

    def note_to_chord(self,is_transkey,note):   # is_transkey is True/False, note is the note position in A-freq
                                    # returns the corresponding chord that this note belongs to
        chord=-10
        start_position=-10
        if not is_transkey:
            a=self.key_notes
            s=self.key_index
        else:
            a=self.transkey_notes
            s=self.transkey_index
        for i in range(0,len(a),1):
            if a[i]==s:
                start_position=i
                break
        if start_position==-10:
            print("error in finding starting position")
            return False
        for i in range(0,7,1):
            if note%12==a[start_position+i]%12:
                chord=i+1
                break
        if chord==-10:
            print("cannot find the corresponding chord")
            return False
        else:
            return chord

    def get_chord_notes(self,is_transkey,chord_progression):    # is_transkey is True/False, chord_progression is 1-7
                                                # returns the list of chord_notes that belongs to this chord_progression
        chord_notes=self.chord_to_note(is_transkey,chord_progression)+self.chord_to_note(is_transkey,chord_progression+2)+self.chord_to_note(is_transkey, chord_progression + 4)
        chord_notes.sort()
        return chord_notes

    def closest(self,pivot,list,option):    # have a pivot note, and a list of notes to choose from, option is how many return values
                    # in option 1, returns the single note that is closest to the pivot note, in A-freq
                    # in option 2, returns a list of 2 notes that is closest but different to the pivot note, in A-freq
        L=list
        L.sort()
        if option==2:
            for i in range(0,len(L),1):
                if L[i]==pivot:
                    if i==0:
                        return [L[i+1],L[i+1]]
                    if i==len(L)-1:
                        return [L[len(L)-2],L[len(L)-2]]
                    else:
                        return [L[i-1],L[i+1]]
            if pivot<L[0]:
                return [L[0],L[1]]
            elif pivot>L[len(L)-1]:
                return [L[len(L)-1],L[len(L)-2]]
            else:
                for i in range(0,len(L)-1,1):
                    if L[i]<=pivot<=L[i+1]:
                        return [L[i],L[i+1]]
        elif option==1:
            if pivot<=L[0]:
                return L[0]
            elif pivot>=L[len(L)-1]:
                return L[len(L)-1]
            else:
                for i in range(0,len(L)-1,1):
                    if L[i]<=pivot<=L[i+1]:
                        if abs(L[i]-pivot)<abs(L[i+1]-pivot):
                            return L[i]
                        else:
                            return L[i+1]
        return False

    def get_passing_note(self,is_transkey,note1,note2,chord_progression):    # note1,note2 in A-frequency,chord_progression is 1-7
                                    # is_transkey is True/False
                                    # returns the suited passing not that fits in between the input two notes, in A-freq
        passing=-1
        if note1 == note2:
            passing=self.closest(note1,(self.chord_to_note(is_transkey,(self.note_to_chord(is_transkey, note1) + random.choice([1, -1])))),1)
        elif abs(note1-note2)== 1 or abs(note1 - note2) == 2:
            x=self.closest(note1,self.get_chord_notes(is_transkey,chord_progression),2)
            diff=[abs(x[0]-note2),abs(x[1]-note2)]
            if diff[0]>diff[1]:
                passing=x[1]
            else:
                passing=x[0]
        elif abs(note1 - note2) == 3:
            passing = min(note1, note2) + 1
            if passing not in self.key_notes:
                passing = min(note1, note2) + 2
        elif abs(note1-note2)==4:
            passing = (note1+note2)//2
        elif abs(note1-note2)==5:
            passing = note2
        elif abs(note1-note2)==6:
            x = self.closest(note1, self.chord_to_note(is_transkey, self.note_to_chord(is_transkey, note1)), 2)
            diff = [abs(x[0] - note2), abs(x[1] - note2)]
            if diff[0] > diff[1]:
                passing = x[1]
            else:
                passing = x[0]
        elif abs(note1-note2)==7:
            passing=(note1+note2)//2
        elif abs(note1-note2)==8:
            passing = min(note1, note2) + 3
            if passing not in self.key_notes:
                passing = min(note1, note2) + 5
        elif abs(note1-note2)==9:
            passing = min(note1, note2) + 4
            if passing not in self.key_notes:
                passing = min(note1, note2) + 5
        elif abs(note1 - note2) == 10:
            passing=note2
        elif abs(note1 - note2) == 11:
            passing=note2
        elif abs(note1 - note2) == 12:
            passing=min(note1,note2)+7
        else:
            passing=note2
        if passing==-1:
            print("error in get_passing_note")
        return passing
