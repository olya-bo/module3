from exceptions import GameOver, EnemyDown
from models import Enemy, Player


def play():
    name = input('Enter your name: ')
    option = input('Enter start if you are not a loser')
    if option == 'start':
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


if __name__ == '__main__':
    try:
        play()
    except GameOver as e:
        print(e)
        e.write_score()
    except KeyboardInterrupt:
        pass
    finally:
        print('Good bye!')
