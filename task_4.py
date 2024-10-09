class ScoreLimitExceededError(Exception):
    def __str__(self):
        return 'Вы не можете добавить более 1000 очков за раз.'


class GameScore:
    def __init__(self):
        self.score = 0

    def add_score(self, added_score):
        if added_score >= 1000:
            raise ScoreLimitExceededError
        self.score += added_score

    def subtract_score(self, delta):
        if self.score - delta < 0:
            raise ValueError('Очки не могут быть меньше нуля')
        self.score -= delta

    def __str__(self):
        return f'Score: {self.score}'


if __name__ == '__main__':
    g1 = GameScore()
    g1.add_score(500)
    print(g1)
    g1.subtract_score(300)
    print(g1)
    g1.add_score(12000)
