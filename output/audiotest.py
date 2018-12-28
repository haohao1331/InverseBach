
import wave
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
            self.bin_str += wave.struct.pack('h', round(s*20000))

    def write(self):
        self.file.writeframesraw(self.bin_str)

    def close(self):
        self.file.close()

    def write_and_close(self):
        self.write()
        self.close()


frequency = 261.626
framerate = 44100
N = framerate / frequency
x = range(N)
y = N * [0]

for i in x:
    y1 = 4 / pi * sin(2 * pi * i / N)
    y2 = 4 / (3 * pi) * sin(6 * pi * i / N)
    y3 = 4 / (5 * pi) * sin(10 * pi * i / N)
    y[i] = y1 + y2 + y3
y = 1313 * y
x = range(3*N)

out = AudioOut("test.wav", sampwidth=2)
out.add_sample(y)
out.write_and_close()
