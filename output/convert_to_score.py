from framework import *


class Converter:

    def __init__(self, raw):
        self.raw = raw

    def convert(self):
        keys=['c','g','d','a','e','b','fis','des','aes','ees','bes','f']
        key=keys[self.raw.get_key()-1]
        transkey=keys[self.raw.get_transkey()+self.raw]

