def test_add_round():
    from hangman.game import Game
    from hangman.round import Round
    from hangman.players import HumanPlayer

    test_game = Game()
    test_round = Round('python')
    test_player_one = HumanPlayer()
    test_player_two = HumanPlayer()

    test_game.add_round(test_round,test_player_one,test_player_two)
    assert test_game.won_rounds[test_player_one.id] == 1
