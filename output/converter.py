'''
Created by Jianyuan Su
Date: Jan 4, 2019
'''

from midiutil import MIDIFile


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
                # print(msr.get_top_notes().print_notes_name())

                for i in range(len(msr.get_top_notes())):
                    n = msr.get_top_notes()[i]
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

                for i in range(len(msr.get_bot_notes())):
                    n = msr.get_bot_notes()[i]
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

    def convert_to_audio(self, tempo=60, volume=100):
        midi = MIDIFile(1)
        midi.addTempo(0, 0, tempo)
        men = self.raw.get_content()
        ttime = 0
        btime = 0
        for i in range(16):
            msr = men[i]
            for note in msr.get_top_notes():
                midi.addNote(0, 0, note.frequency(), ttime, note.length(), volume)
                ttime += note.length()
            for note in msr.get_bot_notes():
                midi.addNote(0, 0, note.frequency(), btime, note.length(), volume)
                btime += note.length()

        return midi
