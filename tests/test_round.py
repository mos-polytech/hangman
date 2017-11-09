def test_class_exists():
    from hangman.round import Round
    assert isinstance(Round, type)


def test_mask_word_is_str():
    from hangman.round import Round
    rounds = Round('banana')
    assert isinstance(rounds.mask_word(), str)


def test_mask_word():
    from hangman.round import Round
    rounds = Round('banana')
    assert rounds.mask_word() == '_ _ _ _ _ _'
