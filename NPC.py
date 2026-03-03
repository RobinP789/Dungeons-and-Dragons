from random import randint
import random

age = ['young', 'middle age', 'elderly']
location = ['an isolated area', 'a town', 'a city']
gender = ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'nonbinary individual', 'nonbinary individual']
marriage = ['married', 'not married']
kids = ['one child', 'two children', 'three children', 'four children', 'five children', 'six or more children']
vibe = ['girly pop', 'scholarly', 'vexing', 'n intense', 'relaxed', 'n artistic', 'type A', 'pious', 'sychophant', 'jock', 'goth', 'n inquisitive', 'generous']
quirk = ['narcolepsy', 'RBF', 'many piercings', 'a large scar', 'monochomatic clothing']

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
