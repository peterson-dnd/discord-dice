import pytest
import parser
import dice.utils

def test_parse():
    rolls = "1d8 + 4d6 + 5"
    result = dice.utils.parse(rolls)

    assert result == ["1d8", "+", "4d6", "+", "5"]
