"""Modules for game"""
import random

from exceptions import EnemyDown, GameOver
from settings import PLAYERS_LIVES, START_PLAYERS_SCORE


def validator(massage=''):
    """Validator function"""
    while True:
        print(
            "1 - wizard",
            "2 - knight",
            "3 - badman",
            '*'*50,
            "If you want to end the game and exit press 'exit'",
            '*'*50,
            sep="\n"
        )
        option = input(massage)
        if option in ('1', '2', '3'):
            return int(option)
        if option == 'exit':
            raise KeyboardInterrupt
        print('try again stooped man')


class Enemy:
    """Enemy class"""
    def __init__(self, level):
        self.level = level
        self.lives = self.level

    @staticmethod
    def select_attack():
        """Method returns random int from 1 to 3"""
        return random.randint(1, 3)

    def decrease_lives(self):
        """Method decreases enemy lives counter. Raises EnemyDown exception if lives is 0"""
        self.lives -= 1
        if self.lives <= 0:
            print(f"{'🖤' * self.level}\nCongratulations you kill enemies!")
            raise EnemyDown

    def print_heart(self):
        """Pretty print for Enemy live level"""
        return f"Enemy - {self.level}:\n{'💙' * self.lives}{'💔' * (self.level - self.lives)}"


class Player:
    """Player class"""
    def __init__(self, name):
        self.name = name
        self.lives = PLAYERS_LIVES
        self.score = START_PLAYERS_SCORE

    @staticmethod
    def fight(attack, defence):
        """Method returns -1, 0 or 1 based on game rules"""
        if any(
            [attack == 1 and defence == 2,
             attack == 2 and defence == 3,
             attack == 3 and defence == 1]
        ):
            return 1
        if attack == defence:
            return 0
        return -1

    def decrease_lives(self):
        """Method decreases Player lives counter. Raises GameOver exception if lives is 0"""
        self.lives -= 1
        if self.lives <= 0:
            print(self.print_heart())
            exception = GameOver("Game Over!")
            exception.score = self.score
            exception.name = self.name
            raise exception

    def attack(self, enemy_obj):
        """Method for attack game phase"""
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
        """Method for defence game phase"""
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
        """Pretty print for Player live level"""
        return f"{self.name} (score - {self.score}):\n"\
               "{'💙' * self.lives}{'💔' * (PLAYERS_LIVES - self.lives)}"
