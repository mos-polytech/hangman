from collections import Counter
import inspect


def test_is_word_solved():
    from hangman.round import Round
    solved = Round(word='')
    assert solved.empty_mark == '_'
    assert solved.is_word_solved() is True
    solveds = Round(word='cat')
    assert solveds.is_word_solved() is False


def test_is_lost():
    from hangman.round import Round
    solveds = Round(word='')
    solveds.tries = 0
    solveds.max_wrong_tries = 6
    assert solveds.is_lost() is False
    solveds.tries = 7
    assert solveds.is_lost() is True


def test_is_finished():
    from hangman.round import Round
    solveds = Round(word='')
    assert solveds.is_finished() is True
    solved = Round(word='cat')
    assert solved.is_finished() is False


def test_try_letter():
    from hangman.round import Round
    solved = Round(word='asd')
    solved.tries = 1
    solved.try_letter(letter='a')
    assert solved.tries is 1
    solved.try_letter(letter='b')
    assert solved.tries is 2


def test_mask_word():
    from hangman.round import Round
    solved = Round(word='aaaddd')
    c = Counter(solved.mask_word())
    assert c['_'] == len(solved.word)
    assert '_' in solved.mask_word()


def test_draw_result():
    from hangman.round import Round
    solved = Round(word='')
    if solved.is_word_solved():
        result = inspect.getsource(solved.draw_result)
        assert "print('Word is solved,')" in result
        assert "print('Word is not solved,')"in result
