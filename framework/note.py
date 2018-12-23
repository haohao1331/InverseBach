class Note:

    def __init__(self, frequency, length, chord_note):
        self._chord_note = chord_note
        self._frequency = frequency
        self._length = length

    def set_frequency(self, frequency):
        self._frequency = frequency

    def set_length(self, length):
        self._length = length

    def frequency(self):
        return self._frequency

    def length(self):
        return self._length

    def is_chord_note(self):
        return self._chord_note
