def madlib():
    place = input('Place...')
    place2 = input('Place...')
    family = input('Family member or friend...')
    verb = input('Verb...')
    obj = input('Object...')
    adj = input('Adjective...')
    adj2 = input('Adjective...')
    adj3 = input('Adjective...')
    noun = input('Noun...')
    timeOfDay = input('Time Of Day...')
    skill = input('Skill or ability...')
    badguy = input('Villain or person at fault...')
    action = input('Action...')
    action2 = input('Action...')

    madlib = f"I {verb} the {obj} in the middle of {place}, so I made a {adj} {noun}. I did this every {timeOfDay} that year.  I forgot that they mail home a report at the end of year, and my {family} got it before I could intercept with my {skill}. {family} was {adj2} at the {badguy} for this {action}. The {place2} also {action2} that year and had already {adj3} their records, so they had to take my {family} proof I’ve never told them the truth."

    print('Title: School Mad Lib >>', madlib)


if __name__ == '__main__':
    madlib()
