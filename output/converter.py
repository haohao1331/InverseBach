'''
Created by Jianyuan Su
Date: Jan 4, 2019
'''

from math import sin, pi


class Converter:

    def __init__(self, raw):
        self.raw = raw  # menuet object

    def convert_to_score(self):

        # define mapping from beat length to lilypond length
        length_map = {1: '4', 2: '2', 3: '2.', 0.5: '8', 1.5: '4.', 0.25: '16', 0.75: '8.'}
        key = self.raw.get_key().upper()  # key as part of score title
        if len(key) > 1:
            key = key[0] + '\u266d'  # if accidental exists, add flat symbol

        # initialize content
        res = ""

        # set date, title and composer
        res += "date = #(strftime \"%d-%m-%Y\" (localtime (current-time)))\n\\header{\n" \
               "title = \"Menuet in " + key + " Major\"\n" \
               "composer = \"I. S. baCh\"}\n"
        res += "\\version \"2.18.2\"{"

        # music sheet begin
        res += "\\new PianoStaff \n<< "
        res += "\\new Staff { "

        men = self.raw.get_content()  # grab menuet content

        # treble clef begin
        res += "\\time 3/4 \\clef \"treble\" \\key " + self.raw.get_key() + " \\major \\tempo \"Moderato\" \\repeat volta 2{"

        length = 0
        for row in range(4):

            for column in range(4):
                msr = men[row*4+column]  # grab measure

                for n in msr.get_top_notes():
                    res += n.name()  # add note name
                    if length != n.length():  # if encounters new length
                        length = n.length()
                        res += length_map[length]  # add note length
                    res += ' '
            if row == 1 or row == 3:
                res += "} "  # repeat end
            if row != 3:
                res += '\\break '  # change to next row
            if row == 1:
                res += "\\repeat volta 2{"  # repeat begin

        # treble clef end
        res += '}\n'

        # bass clef begin
        res += "\\new Staff { \\clef \"bass\" \\key " + self.raw.get_key() + " \\major "

        length = 0
        for row in range(4):

            # identical to treble clef
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

        # bass clef and whole music sheet end
        res += '} >>}'

        # add date
        res += "\\markup{\\date}"

        return res

    def convert_to_wav(self, sampwidth=2, speed=0.75, framerate=44100):
        sample = []  # init sample result for return
        men = self.raw.get_content()  # grab menuet

        for i in range(16):
            msr = men[i]  # grab measure
            # compute list of segments
            segments = self._segmentize(msr)

            for seg in segments:
                length = seg[0]  # length of segment
                tfreq = seg[1][0]  # top note in segment
                bfreq = seg[1][1]  # bottom note in segment

                tN = round(framerate / tfreq)  # number of samples in one top period
                bN = round(framerate / bfreq)  # number of samples in one bottom period
                tNPer = round(speed * length * framerate / tN)  # number of periods in treble clef
                bNPer = round(speed * length * framerate / bN)  # number of periods in bass clef
                tY = tN * [0.0]  # init result of treble clef
                bY = bN * [0.0]  # init result of bass clef

                for x in range(tN):
                    tY[x] = self._fourier_term_one(sampwidth, x, tN)  # set Y of every sample to the first term in Fourier series corresponding to X

                for x in range(bN):
                    bY[x] = self._fourier_term_one(sampwidth, x, bN)

                tY = tNPer * tY  # repeat tY for tNPer periods
                bY = bNPer * bY  # repeat bY for bNPer periods

                # append sample to return
                for j in range(min(len(tY), len(bY))):
                    sample.append(tY[j]+bY[j])

        return sample

    @staticmethod
    def _segmentize(msr):
        # break a measure into segments where no change in notes occur
        tnotes = msr.get_top_notes()  # NoteList of top notes
        bnotes = msr.get_bot_notes()  # NoteList of bottom notes
        segments = []  # resultant list of segments
        llen = 0  # last length
        tlen = 0  # current top length
        ti = 0  # top NoteList index
        blen = 0  # current bottom length
        bi = 0  # bottom NoteList index

        # while measure end is not reached
        while tlen < 3 and blen < 3:
            ntlen = tlen + tnotes[ti].length()  # set next top length to current top length plus next top note length
            nblen = blen + bnotes[bi].length()  # same idea as above

            if ntlen < nblen:  # if next top note length is less than bottom note length
                # add a segment, length as the minimum of differenece of next top note length and current total length, frequency as the combination of top and bottom note
                segments.append((ntlen - llen, (tnotes[ti].frequency(), bnotes[bi].frequency())))
                ti += 1  # increment top index
                llen = ntlen  # set last length to next top note length
                tlen = ntlen  # set top note length to next top note length
            elif ntlen > nblen:  # if next top note length is greater than bottom note length
                # segment covers current bottom length
                segments.append((nblen - llen, (tnotes[ti].frequency(), bnotes[bi].frequency())))
                bi += 1
                llen = nblen
                blen = nblen
            else:  # if next top and bottom lengths equal
                # segment covers both current top and bottom length, starting from last length
                segments.append((nblen - llen, (tnotes[ti].frequency(), bnotes[bi].frequency())))
                ti += 1
                bi += 1
                llen = nblen
                tlen = ntlen
                blen = nblen

        return segments

    @staticmethod
    def _fourier_term_one(sampwidth, x, N):
        # calculate the first term in Fourier series
        return 4 / pi * sin(sampwidth * pi * x / N)
