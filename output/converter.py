from framework import *
from math import sin, pi


class Converter:

    def __init__(self, raw):
        self.raw = raw

    def convert_to_score(self):

        length_map = {1: '4', 2: '2', 3: '2.', 0.5: '8', 1.5: '4.', 0.25: '16', 0.75: '8.'}
        key = self.raw.get_key().upper()
        if len(key) > 1:
            key = key[0] + '\u266d'

        res = ""
        res += "date = #(strftime \"%d-%m-%Y\" (localtime (current-time)))\n\\header{\n" \
               "title = \"Menuet in " + key + " Major\"\n" \
               "composer = \"I. S. baCh\"}\n"
        res += "\\version \"2.18.2\"{"
        res += "\\new PianoStaff \n<< "
        res += "\\new Staff { "

        men = self.raw.get_content()

        res += "\\time 3/4 \\clef \"treble\" \\key " + self.raw.get_key() + " \\major \\tempo \"Moderato\""

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

        res += "\\new Staff { \\clef \"bass\" \\key " + self.raw.get_key() + " \\major "

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

        res += '} >>}'

        res += "\\markup{\\date}"

        return res

    def convert_to_wav(self, sampwidth=2, speed=0.75, framerate=44100):
        sample = []
        men = self.raw.get_content()

        for i in range(16):
            msr = men[i]
            segments = self._segmentize(msr)

            # ok up to this point
            for seg in segments:
                length = seg[0]
                tfreq = seg[1][0]
                bfreq = seg[1][1]

                tN = round(framerate / tfreq)
                bN = round(framerate / bfreq)
                tNPer = round(speed * length * framerate / tN)
                bNPer = round(speed * length * framerate / bN)
                tY = tN * [0.0]
                bY = bN * [0.0]

                for x in range(tN):
                    tY[x] = self._fourier_term_one(sampwidth, x, tN)

                for x in range(bN):
                    bY[x] = self._fourier_term_one(sampwidth, x, bN)

                tY = tNPer * tY
                bY = bNPer * bY

                for j in range(min(len(tY), len(bY))):
                    sample.append(tY[j]+bY[j])

        return sample

    @staticmethod
    def _segmentize(msr):
        tnotes = msr.get_top_notes()
        bnotes = msr.get_bot_notes()
        segments = []
        llen = 0
        tlen = 0
        ti = 0
        blen = 0
        bi = 0

        while tlen < 3 and blen < 3:
            ntlen = tlen + tnotes[ti].length()
            nblen = blen + bnotes[bi].length()

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

        # print(segments)
        return segments

    @staticmethod
    def _fourier_term_one(sampwidth, x, N):
        return 4 / pi * sin(sampwidth * pi * x / N)
