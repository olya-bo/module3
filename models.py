import random

from exceptions import EnemyDown, GameOver
from settings import PLAYERS_LIVES, START_PLAYERS_SCORE


class Enemy(object):
    def __init__(self, level):
        self.level = level
        self.lives = self.level

    @staticmethod
    def select_attack():
        return random.randint(1, 3)

    def decrease_lives(self):
        self.lives -= 1
        if self.lives <= 0:
            raise EnemyDown


class Player(object):
    def __init__(self, name):
        self.name = name
        self.lives = PLAYERS_LIVES
        self.score = START_PLAYERS_SCORE

    @staticmethod
    def fight(attack, defence):
        if (attack == 1 and defence == 2) or (attack == 2 and defence == 3) or (attack == 3 and defence == 1):
            return 1
        elif attack == defence:
            return 0
        else:
            return -1

    def decrease_lives(self):
        self.lives -= 1
        if self.lives <= 0:
            exception = GameOver("Game Over!")
            exception.score = self.score
            raise exception

    def attack(self, enemy_obj):
        print("1 - wizard\n2 - knight\n3 - badman")
        attack = int(input("Choose your attack: "))
        defence = enemy_obj.select_attack()
        result = self.fight(attack, defence)
        if result == 0:
            print("It's a draw!")
        elif result == 1:
            print('You attacked successfully!')
            enemy_obj.decrease_lives()
        else:
            print('You missed!')

    def defence(self, enemy_obj):
        print("1 - wizard\n2 - knight\n3 - badman")
        defence = int(input("Choose defence: "))
        attack = enemy_obj.select_attack()
        result = self.fight(attack, defence)
        if result == 0:
            print("It's a draw!")
        elif result == 1:
            print('Enemy attacked successfully!')
            self.decrease_lives()
        else:
            print('Enemy missed!')
