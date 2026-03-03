from random import randint
import random

age = ['young', 'young', 'young', 'middle age', 'middle age', 'elderly']
location = ['an isolated area', 'a town', 'a city']
gender = ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'nonbinary individual', 'nonbinary individual']
marriage = ['married', 'married', 'not married', 'not married', 'not married']
kids = ['no children', 'no children', 'no children', 'one child', 'one child', 'two children', 'two children', 'two children', 'three or more children']
vibe = ['girly pop', 'scholarly', 'horny', 'vexing', 'n intense', 'relaxed', 'n artistic', 'type A', 'pious', 'sychophant', 'jock', 'goth', 'n inquisitive', 'generous']
quirk = ['narcolepsy', 'RBF', 'many piercings', 'a large scar', 'monochomatic clothing', 'a colourful scarf', 'a missing finger', 'tattoos', 'an elaborate hairstyle', 'heterochromia', 'a pet cat', 'a pet dog', 'a pet bird', 'a pet reptile', 'a gambling addiction', 'a drinking problem', 'the mouth of a sailor', 'a large mole', 'a pock-marked face', 'glasses', 'glasses', 'glasses', 'a lazy eye', 'disheveled hair', 'a visible birthmark', 'a shellfish allergy', 'a nut allergy', 'a bee allergy', 'lactose intolerance', 'bad breath', 'exessive body hair', 'a limp', 'a loud laugh', 'a hyena-like laugh']

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

