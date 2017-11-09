def test_class_exists():
    from hangman.field import HangmanField
    assert isinstance(HangmanField, type)


def test_hangman_field():
    from hangman.field import HangmanField
    field = HangmanField()
    assert isinstance(field.states, list)
