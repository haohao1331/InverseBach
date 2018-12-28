
from framework import *
from output import *


def main():
    m = menuet.Menuet(key=1, transkey=1)
    m.generate()

    c = converter.Converter(m)
    sample = c.convert_to_wav()
    # score = c.convert_to_score()

    a = audio_generator.AudioOut(2, path="test.wav")
    a.add_sample(sample)
    a.write_and_close()

    '''
    score output test
    g = ly_generator.LyOut()
    g.create("score.ly")
    g.add(score)
    g.write_and_close()
    g.build()
    '''


if __name__ == '__main__':
    main()
