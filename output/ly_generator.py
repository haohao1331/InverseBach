from subprocess import call


class Generator:

    def __init__(self):
        self.path = ""
        self.file = None
        self.content = ""

    def create(self, path):
        self.path = path
        self.file = open(path, 'w')
        self.content += "\\version \"2.18.2\"{}"  # TODO generalize version

    def add(self, score):
        self.content = self.content[0:len(self.content)-1] + score + '}'

    def write(self):
        self.file.write(self.content)

    def build(self):
        call(["lilypond", self.path])



