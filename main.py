
from framework import *
from output import *
import os


def main():
    menuet = Menuet()
    menuet.generate()

    c = Converter(menuet)
    


if __name__ == '__main__':
    main()



# test

'''
g = ly_generator.Generator()
g.create("score.ly")
g.add("c' e' g' e'")
g.write()
g.close()
g.build()
'''

# os.system("lilypond score.ly")

