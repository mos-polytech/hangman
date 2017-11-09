from collections import defaultdict


class Game(object):
    def __init__(self):
        self.rounds = []
        self.won_rounds = defaultdict(int)

    def add_round(self, played_round, player, opponent):
        self.rounds.append(played_round)

        if played_round.is_lost():
            winner = opponent
        else:
            winner = player

        self.won_rounds[winner.id] += 1

    def get_winner(self):
        for player_id, wins in self.won_rounds.items():
            if wins >= 2:
                return player_id

        return None
