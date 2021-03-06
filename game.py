"""Main game file"""
from exceptions import GameOver, EnemyDown
from models import Enemy, Player
from settings import OPTIONS, START, SHOW_SCORES, EXIT, HELP


def play():
    """Main game function. Runs game"""
    name = input('Enter your name: ')
    while True:
        option = input('Enter start if you are not a loser: ')
        if option == START:
            player = Player(name)
            level = 1
            enemy = Enemy(level)
            while True:
                try:
                    player.attack(enemy)
                    player.defence(enemy)
                except EnemyDown:
                    level += 1
                    enemy = Enemy(level)
                    player.score += 5
        elif option == SHOW_SCORES:
            with open('scores.txt', 'r') as score:
                print(score.read())
        elif option == EXIT:
            raise KeyboardInterrupt
        elif option == HELP:
            print('Option list:')
            print("\n".join(OPTIONS))
        else:
            print('You mist. Type "help" if you need help')


if __name__ == '__main__':
    try:
        play()
    except GameOver as exception:
        print(exception)
        print(f"You loose! Your score is {exception.score}.")
        exception.write_score()
    except KeyboardInterrupt:
        pass
    finally:
        print('Good bye bitch!')
