
from output import ly_generator
import os

# test

g = ly_generator.Generator()
g.create("score.ly")
g.add("c' e' g' e'")
g.write()
g.close()
g.build()


# os.system("lilypond score.ly")

