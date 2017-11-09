def test_quess_new_word():
    from hangman.players import ComputerPlayer
    test_comp = ComputerPlayer

    assert len(test_comp.quess_new_word()) > 0
