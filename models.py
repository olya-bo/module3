import random

from exceptions import EnemyDown, GameOver
from settings import PLAYERS_LIVES, START_PLAYERS_SCORE


def validator(massage=''):
    while True:
        print(f"1 - wizard\n2 - knight\n3 - badman\n{'*'*50}\nIf you want to end the game and exit press 'exit'\n{'*'*50}")
        option = input(massage)
        if option in ('1', '2', '3'):
            return int(option)
        elif option == 'exit':
            raise KeyboardInterrupt
        print('try again stooped man')


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
            print(f"{'🖤' * self.level}\nCongratulations you kill enemies!")
            raise EnemyDown

    def print_heart(self):
        return f"Enemy - {self.level}:\n{'💙' * self.lives}{'💔' * (self.level - self.lives)}"


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
            print(self.print_heart())
            exception = GameOver("Game Over!")
            exception.score = self.score
            exception.name = self.name
            raise exception

    def attack(self, enemy_obj):
        print(self.print_heart())
        print(enemy_obj.print_heart())
        attack = validator("Choose your attack: ")
        defence = enemy_obj.select_attack()
        result = self.fight(attack, defence)
        if result == 0:
            print("It's a draw!")
        elif result == 1:
            print('You attacked successfully!')
            enemy_obj.decrease_lives()
            self.score += 1
        else:
            print('You missed!')

    def defence(self, enemy_obj):
        print(self.print_heart())
        print(enemy_obj.print_heart())
        defence = validator("Choose defence: ")
        attack = enemy_obj.select_attack()
        result = self.fight(attack, defence)
        if result == 0:
            print("It's a draw!")
        elif result == 1:
            print('Enemy attacked successfully!')
            self.decrease_lives()
        else:
            print('Enemy missed!')

    def print_heart(self):
        return f"{self.name} (score - {self.score}):\n{'💙' * self.lives}{'💔' * (PLAYERS_LIVES - self.lives)}"
