from framework import *
from math import sin, pi


class Converter:

    def __init__(self, raw):
        self.raw = raw

    def convert_to_score(self):

        length_map = {1: '4', 2: '2', 3: '2.', 0.5: '8', 1.5: '4.'}

        res = ""
        res += "\\new PianoStaff \n<< "
        res += "\\new Staff { "

        men = self.raw.get_content()

        res += "\\time 3/4 \\clef \"treble\" \\key " + self.raw.get_key() + " \\major "

        length = 0
        for row in range(4):

            for column in range(4):
                msr = men[row*4+column]

                for n in msr.get_top_notes():
                    res += n.name()
                    if length != n.length():
                        length = n.length()
                        res += length_map[length]
                    res += ' '

            if row != 3:
                res += '\\break '

        res += '}\n'

        res += "\\new Staff { \\clef \"bass\" "

        length = 0
        for row in range(4):

            for column in range(4):
                msr = men[row * 4 + column]

                for n in msr.get_bot_notes():
                    res += n.name()
                    if length != n.length():
                        length = n.length()
                        res += length_map[length]
                    res += ' '

            if row != 3:
                res += '\\break '

        res += '} >>'

        return res

    def convert_to_wav(self, sampwidth=2, speed=0.75, framerate=44100):
        sample = []
        men = self.raw.get_content()

        for i in range(16):
            msr = men[i]
            tnotes = msr.get_top_notes()
            bnotes = msr.get_bot_notes()
            segments = []
            llen = 0
            tlen = 0
            ti = 0
            blen = 0
            bi = 0

            while tlen < 3 and blen < 3:
                # ntlen = tlen
                # if ti < tmax-1:
                ntlen = tlen + tnotes[ti+1].length()
                # nblen = blen
                # if bi < bmax-1:
                nblen = blen + bnotes[bi+1].length()

                if ntlen < nblen:
                    segments.append((ntlen - llen, (tnotes[ti].frequency(), bnotes[bi].frequency())))
                    ti += 1
                    llen = ntlen
                    tlen = ntlen
                elif ntlen > nblen:
                    segments.append((nblen - llen, (tnotes[ti].frequency(), bnotes[bi].frequency())))
                    bi += 1
                    llen = nblen
                    blen = nblen
                else:
                    segments.append((nblen - llen, (tnotes[ti].frequency(), bnotes[bi].frequency())))
                    ti += 1
                    bi += 1
                    llen = nblen
                    tlen = ntlen
                    blen = nblen

            for seg in segments:
                length = seg[0]
                tfreq = seg[1][0]
                bfreq = seg[1][1]

                tN = int(framerate * speed / tfreq)
                bN = int(framerate * speed / bfreq)
                tNPer = int(speed * length * framerate / tN)
                bNPer = int(speed * length * framerate / bN)
                tY = tN * [0.0]
                bY = bN * [0.0]

                for x in range(tN):
                    tY[x] = Converter._fourier_term_one(sampwidth, x, tN)

                for x in range(bN):
                    bY[x] = Converter._fourier_term_one(sampwidth, x, bN)

                tY = tNPer * tY
                bY = bNPer * bY

                for j in range(min(len(tY), len(bY))):
                    sample.append(tY[j]+bY[j])

        return sample

    @staticmethod
    def _fourier_term_one(sampwidth, x, N):
        return 4 / pi * sin(sampwidth * pi * x / N)
