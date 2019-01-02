
from framework import *
from output import *


def main():
    m = menuet.Menuet()
    m.generate()

    c = converter.Converter(m)

    # audio output test
    '''
    sample = c.convert_to_wav(framerate=8000)
    a = audio_generator.AudioOut(2, path="sample_audio/audio.wav", framerate=8000)
    a.add_sample(sample)
    a.write_and_close()
    '''
    # score output test
    
    score = c.convert_to_score()
    g = ly_generator.LyOut()
    g.create("sample_ly/score.ly")
    g.add(score)
    g.write_and_close()
    g.build("sample_score")


if __name__ == '__main__':
    main()
