from midiutil import MIDIFile

degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = 60   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

mfile = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
mfile.addTempo(0, time, tempo)


for i, pitch in enumerate(degrees):
    mfile.addNote(track, channel, pitch, time + i, duration, volume)

with open("major-scale.mid", "wb") as output_file:
    mfile.writeFile(output_file)
