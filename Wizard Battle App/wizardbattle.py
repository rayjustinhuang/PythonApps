import random
import time

from characters import Wizard, Creature


def main():
    game_header()
    game_loop()


def game_header():
    print('------------------------------')
    print('     WIZARD TEXT GAME APP')
    print('------------------------------')


def game_loop():

    creatures = [
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000),
    ]

    # print(creatures)

    hero = Wizard('Gandalf', 75)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from a dark and foggy forest...'
              .format(active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [a]ttack, [r]un away, or [l]ook around? ')
        if cmd == 'a':
            # print('attack')
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('The wizard retreats to recover...')
                time.sleep(5)
                print('The wizard returns revitalized')
        elif cmd == 'r':
            # print('run away')
            print('The wizard has become unsure of himself and flees...')
        elif cmd == 'l':
            # print('look around')
            print('The wizard {} takes a look around and sees...'.format(hero.name))
            for c in creatures:
                print(' * A {} of level {}'.format(c.name, c.level))
        else:
            print('exiting game...')
            break

        if not creatures:
            print("You've defeated all the creatures!!! You win!")
            break

        print()


if __name__ == '__main__':
    main()
