"""Exception for game"""


class GameOver(Exception):
    """Game Over exception. Stops the game and writes score in file"""
    score = 0
    name = ''

    def write_score(self):
        """Method sorts all scores and leave only 10 and if user score in top 10, his result is recorded"""
        with open('scores.txt', 'r') as scores_file:
            results = scores_file.readlines()
        results.append(f'{self.name} : {self.score}')
        results = list(map(lambda line: line.strip().split(' : '), results))
        results = sorted(results, key=lambda line: int(line[1]), reverse=True)[:10]
        results = list(map(lambda line: ' : '.join(line) + '\n', results))
        with open('scores.txt', 'w') as scores_file:
            scores_file.writelines(results)


class EnemyDown(Exception):
    """Enemy down exception. Indicates that enemy defeated"""
