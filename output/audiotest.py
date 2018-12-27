import numpy
from scipy.io.wavfile import write
import wave
from math import sin, pi


def wavWrite(y, fs, nbits, audioFile):
    """ Write samples to WAV file
    Args:
        samples: (ndarray / 2D ndarray) (floating point) sample vector
                    mono: DIM: nSamples
                    stereo: DIM: nSamples x nChannels

        fs: 	(int) Sample rate in Hz
        nBits: 	(int) Number of bits
        fnWAV: 	(string) WAV file name to write
    """
    if nbits == 8:
        intsamples = (y+1.0) * AudioIO.normFact['int' + str(nbits)]
        fX = np.int8(intsamples)
    elif nbits == 16:
        intsamples = y * AudioIO.normFact['int' + str(nbits)]
        fX = np.int16(intsamples)
    elif nbits > 16:
        fX = y

    write(audioFile, fs, fX)


N = 168
x = range(N)
y = N * [0]

for i in x:
    y1 = 4 / pi * sin(2 * pi * i / N)
    y2 = 4 / (3 * pi) * sin(6 * pi * i / N)
    y3 = 4 / (5 * pi) * sin(10 * pi * i / N)
    y[i] = y1 + y2 + y3
y = 1313 * y
x = range(3*N)

fout = wave.open("test.wav", 'w')
fout.setnchannels(1)
fout.setsampwidth(2)
fout.setframerate(44100)
fout.setcomptype('NONE', 'Not Compressed')
BinStr = b''
for i in range(len(y)):
    BinStr += wave.struct.pack('h', round(y[i]*20000))
fout.writeframesraw(BinStr)
fout.close()
