import pytest

def test_start_game_input():
    from hangman.main import start_game
    with pytest.raises(OSError):
        start_game()
