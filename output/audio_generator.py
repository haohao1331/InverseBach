
import wave
import struct
from math import sin, pi


class AudioOut:

    def __init__(self, sampwidth, framerate=44100, nchannels=1, path=""):
        self.path = path
        self.file = None
        self.bin_str = b''
        if path != "":
            self._setup(path, sampwidth, framerate, nchannels)

    def _setup(self, path, sampwidth, framerate, nchannels):
        self.file = wave.open(path, 'w')
        self.file.setnchannels(nchannels)
        self.file.setframerate(framerate)
        self.file.setsampwidth(sampwidth)
        self.file.setcomptype('NONE', 'Not Compressed')

    def add_sample(self, sample, clear=False):
        if clear:
            self.bin_str = b''

        for s in sample:
            s = round(s*10000)
            if -0x7fff-1 <= s <= 0x7fff:
                self.bin_str += struct.pack('h', s)

    def write(self):
        self.file.writeframesraw(self.bin_str)

    def close(self):
        self.file.close()

    def write_and_close(self):
        self.write()
        self.close()
