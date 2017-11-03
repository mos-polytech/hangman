class HangmanField(object):
    states = [
        '',
        '+',
        '+' * 2,
        '+' * 3,
        'x' * 4,
        'X' * 5,
    ]

    def draw(self, wrong_tries: int) -> None:
        print(self.states[wrong_tries])
