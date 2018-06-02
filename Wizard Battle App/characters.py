import random


class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, creature):
        print('The wizard {} attacks {}!'.format(self.name, creature.name))

        my_roll = random.randint(1, 12) * self.level
        creature_roll = random.randint(1, 12) * creature.level

        print('You roll {}...'.format(my_roll))
        print('{} rolls {}...'.format(creature, creature_roll))

        if my_roll >= creature_roll:
            print('The wizard has handily triumphed over {}!!!'.format(creature.name))
            return True
        else:
            print('The wizard has been defeated!!!')
            return False

class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return "{} (lvl. {})".format(self.name, self.level)
