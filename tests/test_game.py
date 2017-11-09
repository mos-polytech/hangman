def test_class_exists():
    from hangman.game import Game
    assert isinstance(Game, type)
