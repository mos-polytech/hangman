import pytest


def test_main_commands():
    from hangman.cli import main

    with pytest.raises(Exception):
        main()
