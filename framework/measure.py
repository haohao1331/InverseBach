from note import *
import random


class Measure:

    def __init__(self, location, chord):
        self.location = location
        self.beat = 3
        self.chord_progression = chord  # only one chord per bar
        self.top_notes = NoteList(self.beat)
        self.bot_notes = NoteList(self.beat)

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
        return True

    def get(self):
        pass

    def get_chord_progression(self):
        return self.chord_progression

    def get_top_notes(self):
        return self.top_notes

    def get_bot_notes(self):
        return self.bot_notes


class NoteList:

    def __init__(self, beat):
        self.beat = beat
        self.length = 0
        self.notes = []

    def add_chord_note(self, note):
        self.length += note.length()
        self.notes.append(note)
        return True

    def print_notes(self):
        notes=[]
        for i in range(0,len(self.notes),1):
            notes = notes + [self.notes[i].frequency()]
        return notes
