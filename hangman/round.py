from hangman.field import HangmanField


class Round(object):
    empty_mark = '_'

    def __init__(self, word):
        self.word = word
        self._field = HangmanField()

        self.max_wrong_tries = len(self._field.states)
        self.tries = 0
        self.wrong_tries = 0
        self.tried_letters = set()
        self.word_status = [False for _ in self.word]

    def is_word_solved(self):
        return all(status is True for status in self.word_status)

    def is_lost(self):
        return self.tries >= self.max_wrong_tries

    def is_finished(self):
        if self.is_word_solved():
            return True

        return self.is_lost()

    def try_letter(self, letter):
        if letter in self.tried_letters:
            print('Already tried')
            return

        if letter in self.word:
            for index, l in enumerate(self.word):
                if l == letter:
                    self.word_status[index] = True
        else:
            self.wrong_tries += 1

        self.tries += 1
        self.tried_letters.add(letter)

    def mask_word(self):
        result = []
        for index, letter in enumerate(self.word):
            if self.word_status[index]:
                result.append(letter)
            else:
                result.append(self.empty_mark)

        return ' '.join(result)

    def draw_field(self):
        self._field.draw(self.wrong_tries)

    def draw_result(self):
        print()
        print('-' * 10)
        print()

        if self.is_word_solved():
            print('Word is solved, a point goes to you!')
        else:
            print('Word is not solved, point goes to your opponent.')
