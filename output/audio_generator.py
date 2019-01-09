'''
Created by Jianyuan Su
Date: Jan 4, 2019
'''

import wave
import struct
from math import sin, pi


class AudioOut:

    def __init__(self, path=""):
        self.path = path  # path to file
        self.file = None  # file object
        self.midi = None  # midi object
        if path != "":  # if path exists, create file object
            self.create(path)

    def create(self, path):
        self.path = path
        self.file = open(path, 'wb')

    def add_midi(self, midi):
        self.midi = midi

    def write(self):
        self.midi.writeFile(self.file)

    def close(self):
        self.file.close()

    def write_and_close(self):
        self.write()
        self.close()
