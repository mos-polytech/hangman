def test_add_round():
    from hangman.game import Game
    test_game = Game()

    test_game.add_round(1,1,2)
    assert test_game.won_rounds[1] == 1
