"""
The Prototype design pattern is a creational design pattern that allows you to create new objects 
by copying an existing object, known as the prototype. This pattern is particularly useful 
when the cost of creating an object is more expensive than copying it. 
It helps in reducing the overhead of creating objects by cloning an existing instance.
"""


import copy

# Define a prototype class for a monster
class MonsterPrototype:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def clone(self):
        return copy.deepcopy(self)

# Concrete monster prototypes
goblin_prototype = MonsterPrototype("Goblin", 30, 5)
orc_prototype = MonsterPrototype("Orc", 50, 10)
skeleton_prototype = MonsterPrototype("Skeleton", 20, 3)

# Create new monsters by cloning the prototypes
monster1 = goblin_prototype.clone()
monster2 = orc_prototype.clone()
monster3 = skeleton_prototype.clone()

# Modify the cloned monsters if needed
monster1.name = "Red Goblin"
monster2.health = 60

# Print the details of the created monsters
print(f"Monster 1: {monster1.name} (Health: {monster1.health}, Damage: {monster1.damage})")
print(f"Monster 2: {monster2.name} (Health: {monster2.health}, Damage: {monster2.damage})")
print(f"Monster 3: {monster3.name} (Health: {monster3.health}, Damage: {monster3.damage})")
