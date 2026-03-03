from random import randint

class Die6():
    """Represent a die, which can be rolled."""

    def __init__(self, sides=6):
        """Initialize the die."""
        self.sides = sides

    def roll_die(self):
        """Return a number between 1 and the number of sides."""
        return randint(1, self.sides)
        
class Die4():
    def __init__(self, sides=4):
        self.sides = sides
    def roll_die(self):
        return randint(1, self.sides)
        
class Die8():
    def __init__(self, sides=8):
        self.sides = sides
    def roll_die(self):
        return randint(1, self.sides)
        
class Die10():
    def __init__(self, sides=10):
        self.sides = sides
    def roll_die(self):
        return randint(1, self.sides)

class Die12():
    def __init__(self, sides=12):
        self.sides = sides
    def roll_die(self):
        return randint(1, self.sides)

class Die20():
    def __init__(self, sides=20):
        self.sides = sides
    def roll_die(self):
        return randint(1, self.sides)

class Die100():
    def __init__(self, sides=100):
        self.sides = sides
    def roll_die(self):
        return randint(1, self.sides)
        
# Make a 6-sided die, and show the results of 10 rolls.
d4 = Die4()
d6 = Die6()
d8 = Die8()
d10 = Die10()
d12 = Die12()
d20 = Die20()
d100 = Die100()

results = []
for roll_num in range(1):
    result4 = d4.roll_die()
    result6 = d6.roll_die()
    result8 = d8.roll_die()
    result10 = d10.roll_die()
    result12 = d12.roll_die()
    result20 = d20.roll_die()
    result100 = d100.roll_die()
    results.append(result100)
    results.append(result20)
    results.append(result12)
    results.append(result10)
    results.append(result8)
    results.append(result6)
    results.append(result4)
   

print(results)  
print("d100 d20 d12 d10 d8 d6 d4")
