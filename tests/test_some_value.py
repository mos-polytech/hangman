from hangman.round import Round


def test_creation():
    round_ = Round('test')
    assert round_.is_word_solved() is False
    assert round_.is_lost() is False
