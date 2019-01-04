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
        self.key = key
        self.transkey = key_list[index + transkey_index]
        self.A = {'a': 0, 'bes': 1, 'b': 2, 'c': 3, 'des': 4, 'd': 5, 'ees': 6, 'e': 7, 'f': 8, 'ges': 9, 'g': 10,
                  'aes': 11}
        self.B = ['a', 'bes', 'b', 'c', 'des', 'd', 'ees', 'e', 'f', 'ges', 'g', 'aes'] * 2 + ['a']
        self.key_index=self.A[self.key]
        self.transkey_index=self.A[self.transkey]
        self.key_notes=self.generate_key_notes()
        self.transkey_notes=self.generate_transkey_notes()
        self.content = []

    def chord1(self):
        m1 = Measure(11, 1,False)
        m2 = Measure(12, random.choice([2, 4, 6]),False)
        m3 = Measure(13, 1,False)
        m4 = Measure(14, 5,False)
        self.content=self.content + [m1, m2, m3, m4]
        return True

    def chord2(self):
        # choosing which key to transpose to will happen in the init function
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

    def chord3(self):
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

    def chord4(self):
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
            # print("note ", f1, "added in measure", i + 1)
        return True

    def set_chord1(self):
        for i in range(0, len(self.content), 4):
            # print(i+1)
            # print(self.content[i].is_trans_measure(),self.content[i].get_chord_progression())
            available=self.get_chord_notes(self.content[i].is_trans_measure(),self.content[i].get_chord_progression())
            # print(available)
            f1=self.content[i].get_top_notes().get_notes()[0].frequency()
            # print(self.closest(f1,available,2))
            f2=random.choice(self.closest(f1,available,2))
            f3=random.choice(self.closest(f2,available,2))
            self.content[i].get_top_notes().add_chord_note(Note(f2, 1, True))
            self.content[i].get_top_notes().add_chord_note(Note(f3, 1, True))
            # print("note ", f2, "added in measure", i + 1)
            # print("note ", f3, "added in measure", i + 1)
        return True

    def set_chord2(self):
        for i in range(1,len(self.content),4):
            # print(i+1)
            f0 = self.content[i - 1].get_top_notes().get_notes()[2].frequency()
            available=self.get_chord_notes(self.content[i].is_trans_measure(),self.content[i].get_chord_progression())
            # print(available)
            f1 = random.choice(self.closest(f0, available, 2))
            f2 = random.choice(self.closest(f1, available, 2))
            f3 = random.choice(self.closest(f2, available, 2))
            self.content[i].get_top_notes().add_chord_note(Note(f1, 1, True))
            self.content[i].get_top_notes().add_chord_note(Note(f2, 1, True))
            self.content[i].get_top_notes().add_chord_note(Note(f3, 1, True))
            # print("note ", f1, "added in measure", i + 1)
            # print("note ", f2, "added in measure", i + 1)
            # print("note ", f3, "added in measure", i + 1)
        return True

    def set_chord3(self):
        for i in range(2, len(self.content), 4):
            # print(i + 1)
            f0 = self.content[i - 1].get_top_notes().get_notes()[2].frequency()
            available = self.get_chord_notes(self.content[i].is_trans_measure(),
                                             self.content[i].get_chord_progression())
            # print(available)
            f1 = random.choice(self.closest(f0, available, 2))
            f2 = random.choice(self.closest(f1, available, 2))
            # print(self.content[i].get_location())
            if self.content[i].get_location()==33:
                # print(available)
                fifth=self.chord_to_note(self.content[i].is_trans_measure(),5)
                # print(fifth)
                no5=[]
                for g in range(0,len(available),1):
                    if available[g] not in fifth:
                        no5=no5+[available[g]]

                f3 = random.choice(self.closest(f2, no5, 2))
                # print(f3)
            else:
                f3 = random.choice(self.closest(f2, available, 2))
            self.content[i].get_top_notes().add_chord_note(Note(f1, 1, True))
            self.content[i].get_top_notes().add_chord_note(Note(f2, 1, True))
            self.content[i].get_top_notes().add_chord_note(Note(f3, 1, True))
            # print("bar: ",i+1,"  length: ",len(self.content[i].get_top_notes().get_notes()))
            # print("note ", f1, "added in measure", i + 1)
            # print("note ", f2, "added in measure", i + 1)
            # print("note ", f3, "added in measure", i + 1)
        return True

    def set_chord4(self):
        for i in range(3,len(self.content),4):
            # print("in set chord4: ",i + 1)
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
            # print(f0,available)
            self.content[i].get_top_notes().add_chord_note(Note(f1, 3, True))
            # print("note ", f1, "added in measure", i + 1)

        return True

    def gen_passing(self):
        notes=[]
        motives = [[], [2], [1], [0], [1,2],[0,2], [0,1], [0,1,2], [1.5, 0.5, 1],
                   [1, 1.5, 0.5], [2, 1], [1, 2]]
        for i in range(0,len(self.content),1):
            notes=notes+[[]]
            for g in range(0, len(self.content[i].get_top_notes().get_notes()), 1):
                notes[i]=notes[i]+[self.content[i].get_top_notes().get_notes()[g].frequency()]
        # print(notes, len(notes))
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
                # print(i+1, self.content[i].get_motive())
                self.content[i].get_top_notes().get_notes()[0].set_length(2)
                # setting the chord note to length 2
                f1 = self.content[i].get_top_notes().get_notes()[0].frequency()
                f2 = self.closest(f1,self.chord_to_note(self.content[i].is_trans_measure(),self.note_to_chord(self.content[i].is_trans_measure(),f1)+1),1)
                self.content[i].get_top_notes().insert_note(Note(f2,1,False),0)
            elif self.content[i].get_motive() == 12:  # doing noting
                # print(i+1, self.content[i].get_motive())
                pass
            elif self.content[i].get_motive() == 8:
                # print(i+1, self.content[i].get_motive())
                self.content[i].get_top_notes().get_notes()[0].set_length(1.5)
                self.content[i].get_top_notes().get_notes()[1].set_length(0.5)
            elif self.content[i].get_motive() == 9:
                # print(i+1, self.content[i].get_motive())
                self.content[i].get_top_notes().get_notes()[1].set_length(1.5)
                self.content[i].get_top_notes().get_notes()[2].set_length(0.5)
            elif self.content[i].get_motive() == 10:
                # print(i+1, self.content[i].get_motive())
                pass
            elif self.content[i].get_motive() == 0:
                # print(i+1, self.content[i].get_motive())
                pass
            else:                                       # adding simple passing notes
                # print(len(notes[i]))
                step2 = [0, 0, 0]
                # print(i+1, motives[int(self.content[i].get_motive())])
                for g in motives[int(self.content[i].get_motive())]:
                    # print(step2)
                    # print(motives[int(self.content[i].get_motive())])
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

    def gen_cadence_harmony(self):
        pivot=18
        for i in range(3,len(self.content),4):
            # print("bar:",i+1)
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
        print("cadence harmony complete")
        return True

    def gen_first_measure_harmony(self):
        pivot=15
        for i in range(0,len(self.content),4):
            # print("bar:", i + 1)
            top_chord_notes=[]
            for g in range(0,len(self.content[i].get_top_notes().get_notes()),1):
                if self.content[i].get_top_notes().get_notes()[g].is_chord_note():
                    top_chord_notes=top_chord_notes+[self.content[i].get_top_notes().get_notes()[g].frequency()]
            # print("top chord notes:",top_chord_notes)
            f1=self.closest(pivot,self.chord_to_note(self.content[i].is_trans_measure(),self.content[i].get_chord_progression()),1)
            # print("top chord notes[1]:", self.note_to_chord(self.content[i].is_trans_measure(),top_chord_notes[1]))
            if self.note_to_chord(self.content[i].is_trans_measure(),top_chord_notes[1])==5 or self.note_to_chord(self.content[i].is_trans_measure(),top_chord_notes[1])==1:
                # print(self.chord_to_note(self.content[i].is_trans_measure(),3))
                f2=self.closest(f1,self.chord_to_note(self.content[i].is_trans_measure(),3),1)
            elif self.note_to_chord(self.content[i].is_trans_measure(),top_chord_notes[1])==3:
                one=self.closest(f1,self.chord_to_note(self.content[i].is_trans_measure(),1),1)
                five=self.closest(f1,self.chord_to_note(self.content[i].is_trans_measure(),5),1)
                f2=random.choice([one,five])
            else:
                print("error in first measure harmony bar",i+1)
            # print("top chord notes[2]:", self.note_to_chord(self.content[i].is_trans_measure(), top_chord_notes[2]))
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
        print("gen_first_measure_harmony complete")
        return True

    def gen_harmony(self):
        pivot = 15
        for i in range(0, len(self.content), 1):
            print("bar:", i + 1)
            if self.content[i].get_location()%10 in [2,3]:
                print("chord progression of bar",self.content[i].get_chord_progression())
                top_chord_notes = []
                for g in range(0, len(self.content[i].get_top_notes().get_notes()), 1):
                    if self.content[i].get_top_notes().get_notes()[g].is_chord_note():
                        top_chord_notes = top_chord_notes + [self.content[i].get_top_notes().get_notes()[g].frequency()]
                # print(top_chord_notes)
                print("top chord notes[0]=", self.note_to_chord(self.content[i].is_trans_measure(), top_chord_notes[0]))
                if abs(self.note_to_chord(self.content[i].is_trans_measure(),top_chord_notes[0]) - self.content[i].get_chord_progression()) in [0,4,3]:
                    f1 = self.closest(pivot, self.chord_to_note(self.content[i].is_trans_measure(), self.content[i].get_chord_progression()+2), 1)
                elif abs(self.note_to_chord(self.content[i].is_trans_measure(), top_chord_notes[0]) - self.content[i].get_chord_progression()) in [2,5]:
                    one = self.closest(pivot, self.chord_to_note(self.content[i].is_trans_measure(), self.content[i].get_chord_progression()), 1)
                    five = self.closest(pivot, self.chord_to_note(self.content[i].is_trans_measure(), self.content[i].get_chord_progression()+4), 1)
                    f1 = random.choice([one, five])
                else:
                    print("error in gen harmony bar:",i+1)

                print("top chord notes[1]=",
                          self.note_to_chord(self.content[i].is_trans_measure(), top_chord_notes[1]))
                if abs(self.note_to_chord(self.content[i].is_trans_measure(),top_chord_notes[1]) - self.content[i].get_chord_progression()) in [0,4,3]:
                    f2 = self.closest(pivot, self.chord_to_note(self.content[i].is_trans_measure(), self.content[i].get_chord_progression()+2), 1)
                elif abs(self.note_to_chord(self.content[i].is_trans_measure(), top_chord_notes[1]) - self.content[i].get_chord_progression()) in [2,5]:
                    one = self.closest(f1, self.chord_to_note(self.content[i].is_trans_measure(), self.content[i].get_chord_progression()), 1)
                    five = self.closest(f1, self.chord_to_note(self.content[i].is_trans_measure(), self.content[i].get_chord_progression()+4), 1)
                    f2 = random.choice([one, five])
                else:
                    print("error in gen harmony bar:",i+1)

                print("top chord notes[2]=",
                          self.note_to_chord(self.content[i].is_trans_measure(), top_chord_notes[2]))
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
        print("gen harmony complete")
        return True

    def decorate_harmony(self):
        for i in range(0,len(self.content)-1,1):
            if self.content[i].get_location() not in [14,24,34,44]:
                f1 = self.content[i].get_bot_notes().get_notes()[0].frequency()
                f2 = self.content[i].get_bot_notes().get_notes()[1].frequency()
                f3 = self.content[i].get_bot_notes().get_notes()[2].frequency()
                f4 = self.content[i+1].get_bot_notes().get_notes()[0].frequency()
                f=[f1,f2,f3,f4]
                step2=[0,0,0]
                for g in range(0,len(f)-1,1):
                    if abs(f[g]-f[g+1]) in [3,4]:gi
                        step2[g]=1
                        fp=self.get_passing_note(self.content[i].is_trans_measure(),f[g],f[g+1],self.content[i].get_chord_progression())
                        self.content[i].get_bot_notes().get_notes()[g].set_length(0.5)
                        self.content[i].get_bot_notes().insert_note(Note(fp, 0.5, False),1+g+sum(step2[0:g]))
        return True

    def to_printable_format(self):
        # print("to printable format")
        for i in range(0, len(self.content), 1):      # iteration for one measure
            for g in range(0, len(self.content[i].get_top_notes().get_notes()), 1):       # iteration for the top notes
                if self.content[i].get_top_notes().get_notes()[g].frequency()>=15:
                    name = self.B[self.content[i].get_top_notes().get_notes()[g].frequency()-12]+ '\'\''
                    self.content[i].get_top_notes().get_notes()[g].set_name(name)
                    # print("top ",self.content[i].get_top_notes().get_notes()[g].frequency(),name)
                elif self.content[i].get_top_notes().get_notes()[g].frequency()>=3:
                    name = self.B[self.content[i].get_top_notes().get_notes()[g].frequency()] + '\''
                    self.content[i].get_top_notes().get_notes()[g].set_name(name)
                    # print("top ",self.content[i].get_top_notes().get_notes()[g].frequency(), name)
                else:
                    name = self.B[self.content[i].get_top_notes().get_notes()[g].frequency()]
                    self.content[i].get_top_notes().get_notes()[g].set_name(name)
        for i in range(0, len(self.content), 1):      # iteration for one measure
            for g in range(0, len(self.content[i].get_bot_notes().get_notes()), 1):     # iteration for bot notes
                # print("bar: " ,i+1)
                if self.content[i].get_bot_notes().get_notes()[g].frequency()>=15:
                    name = self.B[self.content[i].get_bot_notes().get_notes()[g].frequency()-12]
                    self.content[i].get_bot_notes().get_notes()[g].set_name(name)
                    # print("top ",self.content[i].get_top_notes().get_notes()[g].frequency(),name)
                elif self.content[i].get_bot_notes().get_notes()[g].frequency()>=3:
                    name = self.B[self.content[i].get_bot_notes().get_notes()[g].frequency()] +','
                    self.content[i].get_bot_notes().get_notes()[g].set_name(name)
                    # print("top ",self.content[i].get_top_notes().get_notes()[g].frequency(), name)
                else:
                    name = self.B[self.content[i].get_bot_notes().get_notes()[g].frequency()] +',,'
                    self.content[i].get_bot_notes().get_notes()[g].set_name(name)
        '''
        A={'c':130.8127827,'des':138.5913155,'d':146.832384,'ees':155.5634919,'e':164.8137785,'f':174.6141157,
           'ges':184.9972114,'g':195.997718,'aes':207.6523488,'a':220,'bes':233.0818808,'b':246.9416506}

        for i in range(0,len(self.content),1):          # converting into real frequency
            for g in range(0,len(self.content[i].get_top_notes().get_notes()),1):
                if self.content[i].get_top_notes()[g].name()[0]!=',':       # top notes with c'
                    accum=0
                    for h in range(len(self.content[i].get_top_notes()[g].name())-1,-1,-1):
                        if self.content[i].get_top_notes()[g].name()[h]!='\'':
                            break
                        accum=accum+1
                    frequency = A[self.content[i].get_top_notes()[g].name()[0:len(self.content[i].get_top_notes()[g].name())-accum]]*2**accum
                    self.content[i].get_top_notes()[g].set_frequency(frequency)
                elif self.content[i].get_top_notes()[g].name()[0]==',':     # top notes with ,c
                    accum = 0
                    for h in range(0, len(self.content[i].get_top_notes()[g].name()), 1):
                        if self.content[i].get_top_notes()[g].name()[h] != ',':
                            break
                        accum = accum + 1
                    frequency = A[self.content[i].get_top_notes()[g].name()[0:accum]] /(2 ** (len(self.content[i].get_top_notes()[g].name()) - accum))
                    self.content[i].get_top_notes()[g].set_frequency(frequency)
            for g in range(0, len(self.content[i].get_bot_notes().get_notes()), 1):
                if self.content[i].get_bot_notes()[g].name()[0]!=',':       # bot notes with c'
                    accum = 0
                    for h in range(len(self.content[i].get_bot_notes()[g].name()) - 1, -1, -1):
                        if self.content[i].get_bot_notes()[g].name()[h] != '\'':
                            break
                        accum = accum + 1
                    frequency = A[self.content[i].get_bot_notes()[g].name()[0:len(self.content[i].get_bot_notes()[g].name()) - accum]] * 2 ** accum
                    self.content[i].get_bot_notes()[g].set_frequency(frequency)
                elif self.content[i].get_bot_notes()[g].name()[0]==',':     # bot notes with ,c
                    accum = 0
                    for h in range(0, len(self.content[i].get_bot_notes()[g].name()), 1):
                        if self.content[i].get_bot_notes()[g].name()[h] != ',':
                            break
                        accum = accum + 1
                    frequency = A[self.content[i].get_bot_notes()[g].name()[accum:len(self.content[i].get_bot_notes()[g].name())]] / (
                                2 ** (len(self.content[i].get_bot_notes()[g].name()) - accum))
                    self.content[i].get_bot_notes()[g].set_frequency(frequency)
        '''
        return True

    def generate(self):
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
        self.get()
        return True

    def get(self):
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

    def generate_key_notes(self):
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
        # print("key_notes: ", storekey)
        return storekey

    def generate_transkey_notes(self):
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
        # print("transkey_notes ", storetranskey)
        return storetranskey

    def chord_to_note(self,is_transkey,chord_note):   # is_transkey is True/False, chord_note is the note position 1-7
        convert = [11, 0, 2, 4, 5, 7, 9, 11]
        if not is_transkey:
            s = self.key_index
        else:
            s = self.transkey_index
        note = (s + convert[(chord_note % 7)]) % 12
        # print(note)
        notes = []
        for i in range(0, 25, 1):
            if i % 12==note:
                notes = notes + [int(i)]
        # print(notes)
        return notes

    def note_to_chord(self,is_transkey,note):
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
            # print(chord)
            return chord

    def get_chord_notes(self,is_transkey,chord_progression):    # is_transkey is True/False, chord_progression is 1-7
        chord_notes=self.chord_to_note(is_transkey,chord_progression)+self.chord_to_note(is_transkey,chord_progression+2)+self.chord_to_note(is_transkey, chord_progression + 4)
        chord_notes.sort()
        # print(chord_notes)
        return chord_notes

    def closest(self,pivot,list,option):    # have a pivot note, and a list of notes to choose from, option is how many return values
        L=list
        L.sort()
        # print(L)
        if option==2:
            # print(L[0])
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
                    '''
                    if L[i]==pivot:
                        if abs(L[i-1]-pivot)<abs(L[i+1]-pivot):
                            return L[i-1]
                        else:
                            return L[i+1]
                    '''
                    if L[i]<=pivot<=L[i+1]:
                        if abs(L[i]-pivot)<abs(L[i+1]-pivot):
                            return L[i]
                        else:
                            return L[i+1]
        print("pivot: ",pivot)
        print("list: ",list)
        print("option: ",option)
        return False

    def get_passing_note(self,is_transkey,note1,note2,chord_progression):    # note1,note2 in A-frequency,chord_progression is 1-7,option
        passing=-1
        if note1 == note2:
            passing=self.closest(note1,(self.chord_to_note(is_transkey,(self.note_to_chord(is_transkey, note1) + random.choice([1, -1])))),1)
        elif abs(note1-note2)== 1 or abs(note1 - note2) == 2:
            x=self.closest(note1,self.get_chord_notes(is_transkey,chord_progression),2)
            # print("x: ",x)
            # print(self.chord_to_note(is_transkey,self.note_to_chord(is_transkey,note1)))
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
