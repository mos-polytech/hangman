import pytest

def test_word_is_unsolved():
    from hangman.round import Round

    test_round = Round('python')

    assert test_round.is_word_solved() == False

def test_game_over():
    from  hangman.round import Round

    test_round = Round('python')
    test_round.tries = 5
    
    assert test_round.is_lost() == True
