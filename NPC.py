from random import randint
import random

age = ['young', 'young', 'young', 'middle age', 'middle age', 'elderly']
location = ['an isolated area', 'a town', 'a city']
gender = ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'nonbinary individual', 'nonbinary individual']
marriage = ['married', 'married', 'not married', 'not married', 'not married']
kids = ['no children', 'no children', 'no children', 'one child', 'one child', 'two children', 'two children', 'two children', 'three or more children']
vibe = ['girly pop', 'scholarly', 'horny', 'vexing', 'n intense', 'relaxed', 'n artistic', 'type A', 'pious', 'sychophant', 'jock', 'goth', 'n inquisitive', 'generous']
quirk = ['narcolepsy', 'RBF', 'many piercings', 'a large scar', 'monochomatic clothing', 'a colourful scarf', 'a missing finger', 'tattoos', 'an elaborate hairstyle', 'heterochromia', 'a weird pet', 'a pet cat', 'a pet dog', 'a pet bird', 'a pet reptile', 'a gambling addiction', 'a drinking problem', 'the mouth of a sailor', 'a large mole', 'a pock-marked face', 'glasses', 'glasses', 'glasses', 'a lazy eye', 'disheveled hair', 'a visible birthmark', 'a shellfish allergy', 'a nut allergy', 'a bee allergy', 'lactose intolerance', 'bad breath', 'exessive body hair', 'a limp', 'a loud laugh', 'a hyena-like laugh', 'a burn scar', 'a weird trinket', 'an eye twitch', 'a persistant itch', 'a lisp', 'missing teeth', 'a smoking addiction', 'a fake beard/fake breasts', 'an instrument strapped to their back', 'vitilagio', 'a twin', 'chronic pain', 'a missing limb', 'perfect pitch', 'a unique hair colour', 'a lot of make-up', 'illegible handwriting', 'arachnophobia', 'a forgotten past', 'a troubled past', 'a storied past', 'a mission to find something', 'a mission to find someone', 'a bountry on their head', 'a large debt', 'a fanclub', 'a collection of bones', 'a collection of dolls', 'a collection of trinkets', 'a collection of foreign weapons', 'a collection of rare books', 'a collection of Saints Tokens', 'a collection of pornographic books', 'a passion for theatre', 'a passion for music', 'a passion for painting', 'a passion for tinkering', 'a passion for gardening']

rage = random.choice(age)
rloc = random.choice(location)
rgen = random.choice(gender)
rmar = random.choice(marriage)
rkid = random.choice(kids)
rvib = random.choice(vibe)
rqui = random.choice(quirk)

print(rage, rgen)
print("with", rqui, "and a", rvib, "vibe")
print("from", rloc)
print("who is", rmar)

if rmar == 'married':
        print("and has", rkid)



