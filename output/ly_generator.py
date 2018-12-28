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
        self.content += "\\version \"2.18.2\"{}"  # TODO generalize version

    def add(self, score):
        self.content = self.content[0:len(self.content)-1] + score + '}'

    def write(self):
        self.file.write(self.content)

    def close(self):
        self.file.close()

    def write_and_close(self):
        self.write()
        self.close()

    def build(self):
        call(["lilypond", self.path])



