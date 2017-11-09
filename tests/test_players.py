import inspect


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

    assert test_human._validate_word(None) is False
    # В программе можно сделать пусто слово
    # assert test_human._validate_word('') is False
    assert test_human._validate_word('русскоеслово') is False
    assert test_human._validate_word('python') is True


def test_human_should_cnahge_turn():
    from hangman.players import HumanPlayer
    test_human = HumanPlayer()

    assert test_human.should_change_turns() is True


# так не и не поняла а как же input закинуть
# поэтому честно списала
def test_selected():
    from hangman.players import HumanPlayer
    result = HumanPlayer()
    results = inspect.getsource(result.select_other_player)
    assert 'input(' in results
    assert 'except KeyError:' in results


def test_quest_new_word():
    from hangman.players import HumanPlayer
    result = HumanPlayer()
    results = inspect.getsource(result.quess_new_word())
    assert 'word = None' in results
