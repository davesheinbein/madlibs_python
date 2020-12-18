from madlibs_stories import madlibs, zoo
import random

if __name__ == "__main__":
    m = random.choice([madlibs, zoo])
    m.madlib()
