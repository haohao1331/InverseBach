from note.py import Note


class Measure:

    def __init__(self, type, chord):
        self.type = type
        self.beat = 3
        self.chord_progression = chord
        self.top_notes = NoteList()
        self.bot_notes = NoteList()

    def add_note(self, note):
        self.notes.append(note)


class NoteList:

    def __init__(self, beat):
        self.beat = beat
        self.length = 0
        self.notes = []

    def add_chord_note(self, note):
        self.length += note.length()
        self.notes.append(note)
