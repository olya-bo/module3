class GameOver(Exception):
    score = 0

    def write_score(self):
        with open('scores.txt', 'a') as f:
            f.write(str(self.score) + "\n")


class EnemyDown(Exception):
    pass
