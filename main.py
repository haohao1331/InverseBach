
from framework import *
from output import *


def main():
    m = menuet.Menuet(key=1, transkey=1)
    m.generate()

    c = converter.Converter(m)
    c.convert_to_wav()
    # score = c.convert_to_score()

    '''
    g = ly_generator.Generator()
    g.create("score.ly")
    g.add(score)
    g.write_and_close()
    g.build()
    '''


if __name__ == '__main__':
    main()
