class GameOver(Exception):
    score = 0
    name = ''

    def write_score(self):
        with open('scores.txt', 'r') as f:
            results = f.readlines()
        results.append(f'{self.name} : {self.score}')
        results = list(map(lambda line: line.strip().split(' : '), results))
        # results.append([self.name, str(self.score)])
        results = sorted(results, key=lambda line: int(line[1]), reverse=True)[:10]
        results = list(map(lambda line: ' : '.join(line) + '\n', results))
        with open('scores.txt', 'w') as f:
            f.writelines(results)


class EnemyDown(Exception):
    pass
