from culc.main import _sum


def test_sum():
    assert _sum([1, 2, 3]) == 6, 'Should be 6'


def test_sum_tuple():
    assert _sum([1, 2, 2]) == 6, 'Should be 6'
