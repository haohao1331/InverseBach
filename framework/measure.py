'''
created by Xinghao Li,Jan 4,2019
'''

from framework.note import *
import random


class Measure:      # the variable for every single measure

    def __init__(self, location, chord, trans_measure):
        self.location = location        # location of the measure, a two digit decimal number with the tenth digit
                                        # signifying line number and single digit representing the bar number of the line
        self.beat = 3                   # there are 3 beats in a bar for a menuet
        self.chord_progression = chord  # our current assumption is only one chord per bar
        self.top_notes = NoteList(self.beat)    # The right hand melody, new data structure
        self.bot_notes = NoteList(self.beat)    # The left hand harmony
        self.trans_measure=trans_measure        # True or False
        self.motive=int(100)                    # the motive, used in gen passing

    def get(self):
        pass

    def get_chord_progression(self):
        return self.chord_progression

    def get_top_notes(self):
        return self.top_notes

    def get_bot_notes(self):
        return self.bot_notes

    def get_location(self):
        return self.location

    def is_trans_measure(self):
        return self.trans_measure

    def get_motive(self):
        return self.motive

    def set_motive(self,motive):
        self.motive=motive
        return True


class NoteList:

    def __init__(self, beat):
        self.beat = beat    # three beats per measure
        self.length = 0     # currently how many beats are occupied
        self.notes = []     # the list that takes in the notes
        self.index = 0

    def add_chord_note(self, note):     # adding a chord note to the notelist
        self.length += note.length()
        self.notes.append(note)
        return True

    def insert_note(self,note,position):    # inserting a note in a note list, position is the position that the
                                            # inserted note will occupy after the incert
        if position==0:
            self.notes=[note]+self.notes
            return True
        elif position>len(self.notes):
            return False
        else:
            self.notes=self.notes[0:position]+[note]+self.notes[position:len(self.notes)]
            return True

    def beat(self):
        return self.beat

    def length(self):
        return self.length

    def get_notes(self):
        return self.notes

    def print_notes(self):      # just for debugging
        notes=[]
        for i in range(0,len(self.notes),1):
            notes = notes + [self.notes[i].frequency()]
        print(notes)
        return True

    def __len__(self):
        return len(self.notes)

    def __next__(self):
        if self.index >= len(self.notes):
            raise StopIteration
        ret = self.notes[self.index]
        self.index += 1
        return ret

    def __iter__(self):
        return self

    def __getitem__(self, item):
        return self.notes[item]

    def print_notes_name(self):     # for debugging as well
        notes=[]
        for i in range(0,len(self.notes),1):
            notes=notes+[self.notes[i].name()]
        return notes
