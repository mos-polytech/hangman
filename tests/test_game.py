def test_add_round():
    from hangman.game import Game
    from hangman.round import Round
    from hangman.players import HumanPlayer

    test_game = Game()
    test_round = Round('python')
    test_player_one = HumanPlayer()
    test_player_two = HumanPlayer()

    test_game.add_round(test_round, test_player_one, test_player_two)
    assert test_game.won_rounds[test_player_one.id] == 1


def test_get_winner():
    from hangman.game import Game
    from hangman.round import Round
    from hangman.players import HumanPlayer

    test_game = Game()
    test_round = Round('python')
    test_player_one = HumanPlayer()
    test_player_two = HumanPlayer()

    test_game.add_round(test_round, test_player_one, test_player_two)
    test_game.add_round(test_round, test_player_one, test_player_two)

    assert str(test_game.get_winner()) == str(test_player_one.id)


def test_get_winner_opponent():
    from hangman.game import Game
    from hangman.round import Round
    from hangman.players import HumanPlayer

    test_game = Game()
    test_round = Round('zxc')

    test_round.try_letter('q')
    test_round.try_letter('w')
    test_round.try_letter('e')
    test_round.try_letter('r')
    test_round.try_letter('t')
    test_round.try_letter('y')

    test_player_one = HumanPlayer()
    test_player_two = HumanPlayer()

    test_game.add_round(test_round, test_player_one, test_player_two)
    test_game.add_round(test_round, test_player_one, test_player_two)

    assert str(test_game.get_winner()) == str(test_player_two.id)


def test_get_winner_none():
    from hangman.game import Game
    test_game = Game()

    assert test_game.get_winner() is None
