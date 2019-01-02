from subprocess import call


class LyOut:

    def __init__(self, path=""):
        self.path = path
        self.file = None
        self.content = ""
        if path != "":
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
        call(["lilypond", "--output="+dir, self.path])



