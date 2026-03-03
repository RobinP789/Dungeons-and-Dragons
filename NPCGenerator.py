from random import randint
import random

age = ['young', 'middle age', 'elderly']
location = ['an isolated area', 'a town', 'a city']
gender = ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'nonbinary individual', 'nonbinary individual']
marriage = ['married', 'not married']
kids = ['one child', 'two children', 'three children', 'four children', 'five children', 'six or more children']

rage = random.choice(age)
rloc = random.choice(location)
rgen = random.choice(gender)
rmar = random.choice(marriage)
rkid = random.choice(kids)

print(rage, rgen)
print("from", rloc)
print("who is", rmar)

if rmar == 'married':
        print("and has", rkid)

