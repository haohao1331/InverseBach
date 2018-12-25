class Note:

    def __init__(self, frequency, length, chord_note):
        self._chord_note = chord_note
        self._frequency = frequency
        self._length = length
        self._name = ""

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
