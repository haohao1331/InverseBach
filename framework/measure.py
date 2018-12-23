from note.py import Note
import random

class Measure:

    def __init__(self, type, chord):
        self.type = type
        self.beat = 3
        self.chord_progression = chord  # only one chord per bar
        self.top_notes = NoteList(self.beat)
        self.bot_notes = NoteList(self.beat)


    def add_chord_note(self):
        if self.type%10==4:
            note=Note(self.chord_progression+0,3,True)     #need to improve
            self.top_notes.add_chord_note(note)
        else:
            note1 =Note(self.chord_progression+random.choice([0,2,4]),1,True)
            note2 = Note(self.chord_progression + random.choice([0, 2, 4]), 1, True)
            note3 = Note(self.chord_progression + random.choice([0, 2, 4]), 1, True)
            self.top_notes.add_chord_note(note1)
            self.top_notes.add_chord_note(note2)
            self.top_notes.add_chord_note(note3)
class NoteList:

    def __init__(self, beat):
        self.beat = beat
        self.length = 0
        self.notes = []

    def add_chord_note(self, note):
        self.length += note.length()
        self.notes.append(note)
