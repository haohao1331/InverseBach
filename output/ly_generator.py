'''
Created by Jianyuan Su
Date: Jan 4, 2019
'''

from subprocess import call


class LyOut:

    def __init__(self, path=""):
        self.path = path  # path to file
        self.file = None  # file object
        self.content = ""  # file content
        if path != "":  # if path exists, create file object
            self.create(path)

    def create(self, path):
        self.path = path
        self.file = open(path, 'w')

    def add(self, score):
        self.content += score

    def write(self):
        self.file.write(self.content)

    def close(self):
        self.file.close()

    def write_and_close(self):
        self.write()
        self.close()

    def build(self, dir):
        call(["lilypond", "--output="+dir, self.path])  # call shell command



