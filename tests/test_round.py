def test_round():
    from hangman.round import Round

    test_round = Round('python')
    
    assert test_round.is_word_solved() == False
