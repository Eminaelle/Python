import pytest
from analysis import calculate_mode

@pytest.mark.parametrize("input_list,expected_result", [
    ([4, 2, 5, 4, 3, 4], [4]),
    ([1.2, 3.4, 1.2, 2.4, 1.2], [1.2]),
    ([1, 2, 3, 1, 2, 4, 5], [1, 2]),
    ([1, 1, 2, 2, 3, 3, 4], [1, 2, 3]),
    ([6, 7, 8, 9], None),
    ([1, 1, 2, 2, 3, 3], None),
    ([], None),
    (["a", "b", "a", "c", "b", "a"], ["a"])
])

def test_calculate_mode(input_list, expected_result):
    assert calculate_mode(input_list) == expected_result
