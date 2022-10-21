def madlib():
    adj1 = input('Adjective...')
    adj2 = input('Adjective...')
    adj3 = input('Adjective...')
    adj4 = input('Adjective...')
    adj5 = input('Adjective...')
    adj6 = input('Adjective...')
    pastVerb = input('Past tense verb...')

    animalS = input('Small animal...')
    animalL = input('Large animal...')
    firstName = input('First name...')
    firstNames = input('First name\'s...')
    girlName = input('Girl\'s name...')
    pluralNoun = input('Plural noun...')
    pluralNoun1 = input('Plural noun...')
    pluralNoun2 = input('Plural noun...')
    pluralNoun3 = input('Plural noun...')
    pluralNoun4 = input('Plural noun...')
    numWorlds = input('number 1-50...')
    num = input('number...')
    num2 = input('number...')

    madlib = f"I, the {adj1} and {adj2} {firstName} has {pastVerb} {firstName}'s {adj3} sister and plans to steal her {adj4} {pluralNoun}! What are a {animalL} and backpacking {animalS} to do? Before you can help {girlName}, you'll have to collect the {adj5} {pluralNoun1} and {adj6} {pluralNoun2} that open up the {numWorlds} worlds connected to a {firstNames} lair. There are {num} {pluralNoun3} and {num2} {pluralNoun4} in the game, along with hundreds of other goodies for you to find."

    print('Title: Video Game Mad Lib >>', madlib)


if __name__ == '__main__':
    madlib()
