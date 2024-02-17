import pytest
from analyse import calculate_average


@pytest.mark.parametrize("input_list,expected_result, expected_exception, expected_message", [
    ([10, 20, 30, 40], 25.0, None, None),
    ([1.5, 2.5, 3.5, 4.5, 5.5], pytest.approx(3.5), None, None),
    ([1, 2, 3, 4, 0], 2.0, None, None),
    ([100, 200], 150.0, None, None),
    ([-10, -20, 30, 40], 10.0, None, None),
    ([-1, -2, -3, -4, -5], -3.0, None, None),
    ([-10.1, -20.2, 30.3, 40.4], pytest.approx(10.1), None, None),
    ([100, -200], -50.0, None, None),
    (["not", "numbers"], None, TypeError, "Non-numeric value found"),
    ([], None,ValueError, "The data are empty") 
])

def test_calculate_average(input_list, expected_result, expected_exception, expected_message):
    if expected_exception:
        with pytest.raises(expected_exception) as excinfo:
            calculate_average(input_list)
        assert str(excinfo.value) == expected_message
    else:
        assert calculate_average(input_list) == expected_result
