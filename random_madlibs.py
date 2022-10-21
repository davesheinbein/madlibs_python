from madlibs_stories import madlibs, zoo, arcade, jungle, school, videoGame
import random

if __name__ == "__main__":
    m = random.choice([madlibs, zoo, arcade, jungle, school, videoGame])
    m.madlib()
