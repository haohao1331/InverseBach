from note import *
import random


class Measure:

    def __init__(self, location, chord,trans_measure):
        self.location = location
        self.beat = 3
        self.chord_progression = chord  # only one chord per bar
        self.top_notes = NoteList(self.beat)
        self.bot_notes = NoteList(self.beat)
        self.trans_measure=trans_measure        # True or False

    def add_chord_note(self):
        if self.location%10==4:
            note=Note(self.chord_progression+0,3,True)     # need to improve
            self.top_notes.add_chord_note(note)
        else:
            note1 = Note(self.chord_progression + random.choice([0, 2, 4]), 1, True)
            note2 = Note(self.chord_progression + random.choice([0, 2, 4]), 1, True)
            note3 = Note(self.chord_progression + random.choice([0, 2, 4]), 1, True)
            self.top_notes.add_chord_note(note1)
            self.top_notes.add_chord_note(note2)
            self.top_notes.add_chord_note(note3)
            # corresponds to the three chord notes of a bar
        return True

    def get(self):
        pass

    def get_chord_progression(self):
        return self.chord_progression

    def get_top_notes(self):
        return self.top_notes

    def get_bot_notes(self):
        return self.bot_notes

    def is_trans_measure(self):
        return self.trans_measure


class NoteList:

    def __init__(self, beat):
        self.beat = beat
        self.length = 0
        self.notes = []
        self.index = 0

    def add_chord_note(self, note):
        self.length += note.length()
        self.notes.append(note)
        return True

    def beat(self):
        return self.beat

    def length(self):
        return self.length

    def get_notes(self):
        return self.notes

    def print_notes(self):
        notes=[]
        for i in range(0,len(self.notes),1):
            notes = notes + [self.notes[i].frequency()]
        return notes

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

    def print_notes_name(self):
        notes=[]
        for i in range(0,len(self.notes),1):
            notes=notes+[self.notes[i].name()]
        return notes
