'''
created by Xinghao Li,Jan 4,2019
'''


class Note:

    def __init__(self, frequency, length, chord_note):
        self._chord_note = chord_note   # True/False, indicating if this note is a chord note or not
        self._frequency = frequency     # the frequency of the note, initially is from 0-24,later converted in to Hz
        self._length = length           # the number of beats that a note occupies
        self._name = ""                 # the name of the note

    def set_frequency(self, frequency):
        self._frequency = frequency

    def set_length(self, length):
        self._length = length

    def set_name(self, name):
        self._name = name

    def frequency(self):
        return self._frequency

    def length(self):
        return self._length

    def name(self):
        return self._name

    def is_chord_note(self):
        return self._chord_note
