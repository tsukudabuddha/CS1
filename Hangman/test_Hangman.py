import Hangman
import pytest


def test_is_word_guessed():
    x = isWordGuessed('cat', ['c', 'a', 't'])
    assert x == True
    x = isWordGuessed('cat', [])
    assert x == False
