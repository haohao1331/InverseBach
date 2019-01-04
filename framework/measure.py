from framework.note import *
import random


class Measure:

    def __init__(self, location, chord, trans_measure):
        self.location = location
        self.beat = 3
        self.chord_progression = chord  # only one chord per bar
        self.top_notes = NoteList(self.beat)
        self.bot_notes = NoteList(self.beat)
        self.trans_measure=trans_measure        # True or False
        self.motive=int(100)
    '''
    def add_chord_note(self, key):
        A = {'c': 3, 'des': 4, 'd': 5, 'ees': 6, 'e': 7, 'f': 8,'ges': 9, 'g': 10, 'aes': 11, 'a': 0, 'bes': 1, 'b': 2}
        # this is the mapping of the notes to the numbers, in order to solve the octaves problem
        names = ['c', 'des', 'd', 'ees', 'e', 'f', 'ges', 'g', 'aes', 'a', 'bes', 'b'] * 2
        key_index = -1
        for i in range(0, len(names), 1):
            if key == names[i]:
                key_index = i
                break
        if key_index==-1:
            print("False in matching key list")
        key_notes = []
        for i in [0, 2, 4, 5, 7, 9, 11]:  # for major scales only
            key_notes = key_notes + [names[key_index + i]]
        # print("key_notes: ", key_notes)
        key_notes = key_notes * 2
        chord_notes = [key_notes[self.chord_progression-1],key_notes[self.chord_progression+1],key_notes[self.chord_progression+3]]
        # print("chord notes of this measure: ",chord_notes)
        if self.location%10==4:
            note = Note(A[chord_notes[0]], 3, True)     # adding the root of the chord in top notes
            self.top_notes.add_chord_note(note)
        else:
            while True:
                f1=random.choice([0, 1, 2])
                f2=random.choice([0, 1, 2])
                f3=random.choice([0, 1, 2])
                if not(f1==f2==f3):
                    break

            note1 = Note(A[chord_notes[f1]], 1, True)
            note2 = Note(A[chord_notes[f2]], 1, True)
            note3 = Note(A[chord_notes[f3]], 1, True)
            self.top_notes.add_chord_note(note1)
            self.top_notes.add_chord_note(note2)
            self.top_notes.add_chord_note(note3)
            # corresponds to the three chord notes of a bar, this is with respect to the mapping of A
        return True
    '''
    '''
    
    def add_harmony(self,key):
        A = {'c': 3, 'des': 4, 'd': 5, 'ees': 6, 'e': 7, 'f': 8, 'ges': 9, 'g': 10, 'aes': 11, 'a': 0, 'bes': 1, 'b': 2}
        # this is the mapping of the notes to the numbers, in order to solve the octaves problem
        names = ['c', 'des', 'd', 'ees', 'e', 'f', 'ges', 'g', 'aes', 'a', 'bes', 'b'] * 2
        key_index = -1
        for i in range(0, len(names), 1):
            if key == names[i]:
                key_index = i
                break
        if key_index == -1:
            print("False in matching key list")
        key_notes = []
        for i in [0, 2, 4, 5, 7, 9, 11]:  # for major scales only
            key_notes = key_notes + [names[key_index + i]]
        # print("key_notes: ", key_notes)
        key_notes = key_notes * 2
        chord_notes = [key_notes[self.chord_progression - 1], key_notes[self.chord_progression + 1],
                       key_notes[self.chord_progression + 3]]
        # print("chord notes of this measure: ",chord_notes)
        note = Note(A[chord_notes[0]], 3, True)
        self.bot_notes.add_chord_note(note)
        return True
    '''

    def get(self):
        pass

    def get_chord_progression(self):
        return self.chord_progression

    def get_top_notes(self):
        return self.top_notes

    def get_bot_notes(self):
        return self.bot_notes

    def get_location(self):
        return self.location

    def is_trans_measure(self):
        return self.trans_measure

    def get_motive(self):
        return self.motive

    def set_motive(self,motive):
        self.motive=motive
        return True


class NoteList:

    def __init__(self, beat):
        self.beat = beat
        self.length = 0
        self.notes = []
        self.index = 0

    def add_chord_note(self, note):
        self.length += note.length()
        self.notes.append(note)
        return True

    def insert_note(self,note,position):
        if position==0:
            self.notes=[note]+self.notes
            return True
        elif position>len(self.notes):
            return False
        else:
            self.notes=self.notes[0:position]+[note]+self.notes[position:len(self.notes)]
            return True

    def beat(self):
        return self.beat

    def length(self):
        return self.length

    def get_notes(self):
        return self.notes

    def print_notes(self):
        notes=[]
        for i in range(0,len(self.notes),1):
            notes = notes + [self.notes[i].frequency()]
        print(notes)
        '''
        notes = []
        for i in range(0, len(self.notes), 1):
            notes = notes + [self.notes[i].name()]
        print(notes)
        '''
        return True

    def __len__(self):
        return len(self.notes)

    def __next__(self):
        if self.index >= len(self.notes):
            raise StopIteration
        ret = self.notes[self.index]
        self.index += 1
        return ret

    def __iter__(self):
        return self

    def __getitem__(self, item):
        return self.notes[item]

    def print_notes_name(self):
        notes=[]
        for i in range(0,len(self.notes),1):
            notes=notes+[self.notes[i].name()]
        return notes
