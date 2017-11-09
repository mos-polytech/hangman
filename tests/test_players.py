def test_comp_quess_new_word():
    from hangman.players import ComputerPlayer
    test_comp = ComputerPlayer()

    assert len(test_comp.quess_new_word()) > 0


def test_comp_should_change_turns():
    from hangman.players import ComputerPlayer
    test_comp = ComputerPlayer()

    assert test_comp.should_change_turns() is False


def test_human_validate_word():
    from hangman.players import HumanPlayer
    test_human = HumanPlayer()

    assert test_human._validate_word('') is False
    assert test_human._validate_word('русскоеслово') is False
    assert test_human._validate_word('python') is True
