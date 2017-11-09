import pytest

def test_start_game():
    from hangman.main import start_game
    with pytest.raises(OSError):
        start_game()
