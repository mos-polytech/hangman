import string
import uuid
import random


class ComputerPlayer(object):
    changes_turns = False

    def __init__(self):
        self.id = uuid.uuid4()

    def quess_new_word(self):
        words = [
            'python',
            'cat',
            'pizza',
        ]

        return random.choice(words)

    def should_change_turns(self):
        return self.changes_turns


class HumanPlayer(ComputerPlayer):
    changes_turns = True

    def _validate_word(self, word):
        if word is None:
            return False

        for letter in word:
            if letter.lower() not in string.ascii_lowercase:
                return False

        return True

    def select_other_player(self):
        player_type = {
            'human': HumanPlayer,
            'ai': ComputerPlayer,
        }

        while True:
            try:
                selected = input('ai or human: ')
                return player_type[selected]
            except KeyError:
                pass

    def quess_new_word(self):
        word = None

        while not self._validate_word(word):
            word = input('Input your English word: ')

        return word
