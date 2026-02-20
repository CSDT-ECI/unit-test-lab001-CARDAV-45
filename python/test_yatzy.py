from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/

def test_chance_mixedDice_returnsCorrectSum():
    result = Yatzy.chance(1, 2, 3, 4, 5)
    assert result == 15

def test_yatzy_allDiceSame_returns50():
    result = Yatzy.yatzy([1, 1, 1, 1, 1])
    assert result == 50


def test_ones_multipleOnes_returnsSumOfOnes():
    result = Yatzy.ones(1, 1, 1, 2, 3)
    assert result == 3


def test_twos_multipleTwos_returnsSumOfTwos():
    result = Yatzy.twos(2, 2, 3, 4, 5)
    assert result == 4