from framework import *


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

    def convert_to_wav(self, speed=0.75, framerate=44100):
        bin = b''
        men = self.raw.get_content()

        for i in range(16):
            msr = men[i]
            tnotes = msr.get_top_notes()
            bnotes = msr.get_bot_notes()
            segments = []
            tlen = 0
            tmax = len(tnotes)
            ti = 0
            blen = 0
            bmax = len(bnotes)
            bi = 0

            while tlen < 3 and blen < 3:
                ntlen = tlen
                if ti < tmax-1:
                    ntlen += tnotes[ti+1].length()
                nblen = blen
                if bi < bmax-1:
                    nblen += bnotes[bi+1].length()

                if ntlen < nblen:
                    segments.append((ntlen-tlen, (tnotes[ti].frequency(), bnotes[bi].frequency())))
                    ti += 1
                elif ntlen > nblen:
                    segments.append((nblen - blen, (tnotes[ti].frequency(), bnotes[bi].frequency())))
                    bi += 1
                else:
                    segments.append((nblen - blen, (tnotes[ti].frequency(), bnotes[bi].frequency())))
                    ti += 1
                    bi += 1

            print(segments)
