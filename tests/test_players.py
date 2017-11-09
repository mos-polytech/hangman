def test_class_exists():
    from hangman.players import ComputerPlayer
    assert isinstance(ComputerPlayer, type)


def test_computer_word_is_string():
    from hangman.players import ComputerPlayer
    comp = ComputerPlayer()
    assert isinstance(comp.quess_new_word(), str)
