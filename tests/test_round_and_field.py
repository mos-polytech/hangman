def test_word_is_unsolved_on_start():
    from hangman.round import Round

    test_round = Round('python')

    assert test_round.is_word_solved() is False


def test_word_is_solved():
    from hangman.round import Round

    test_round = Round('python')
    test_round.word_status = [True for _ in test_round.word]

    assert test_round.is_word_solved() is True


def test_game_over():
    from hangman.round import Round
    from hangman.field import HangmanField

    test_round = Round('python')
    max_tries = len(HangmanField().states)
    test_round.tries = max_tries

    assert test_round.is_lost() is True


def test_draw():
    from hangman.field import HangmanField

    for i in range(1, len(HangmanField().states)):
        last_len = len(HangmanField().states[i-1])
        assert last_len < len(HangmanField().states[i])


def test_draw_field(capsys):
    from hangman.round import Round
    from hangman.field import HangmanField

    test_round = Round('python')

    for i in HangmanField().states:
        test_round.draw_field()
        out, _ = capsys.readouterr()
        assert out == i or out == '\n'
        test_round.tries += 1


def test_try_letter_right():
    from hangman.round import Round
    test_round = Round('python')

    test_round.try_letter('t')
    assert test_round.word_status[2] is True


def test_try_letter_tryed(capsys):
    from hangman.round import Round
    test_round = Round('python')

    test_round.try_letter('h')
    test_round.try_letter('h')
    out, _ = capsys.readouterr()
    assert out == 'Already tried\n'


def test_try_letter_wrong():
    from hangman.round import Round
    test_round = Round('python')
    wrong_tries = test_round.wrong_tries

    test_round.try_letter('f')

    assert test_round.wrong_tries - wrong_tries == 1


def test_mask_letter():
    from hangman.round import Round
    test_round = Round('python')

    test_round.try_letter('p')
    test_round.try_letter('n')

    assert test_round.mask_word() == 'p _ _ _ _ n'


def test_is_finished_right():
    from hangman.round import Round
    test_round = Round('python')

    test_round.try_letter('p')
    test_round.try_letter('y')
    test_round.try_letter('t')
    test_round.try_letter('h')
    test_round.try_letter('o')
    test_round.try_letter('n')

    assert test_round.is_finished() is True


def test_is_finished_wrong():
    from hangman.round import Round
    test_round = Round('python')

    assert test_round.is_finished() is False


def test_draw_result_wrong(capsys):
    from hangman.round import Round
    test_round = Round('python')

    test_round.draw_result()
    out, _ = capsys.readouterr()
    assert out == '\n----------\nWord is not solved, point goes to your opponent.\n'


def test_draw_result_right(capsys):
    from hangman.round import Round
    test_round = Round('python')

    test_round.try_letter('p')
    test_round.try_letter('y')
    test_round.try_letter('t')
    test_round.try_letter('h')
    test_round.try_letter('o')
    test_round.try_letter('n')

    test_round.draw_result()
    out, _ = capsys.readouterr()
    assert out == '\n----------\nWord is solved, a point goes to you!\n'
