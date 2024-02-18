import pytest
from sort_heapsort import sort_heapsort

@pytest.mark.parametrize("input_list, expected_result, expected_exception, expected_message", [
    ([], [], None, None),  
    ([5], [5], None, None),  
    ([3, 2, 1], [1, 2, 3], None, None), 
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], None, None), 
    ([1.1, 3.3, 2.2, 5.5, 4.4], [1.1, 2.2, 3.3, 4.4, 5.5], None, None),
    ([4, 6, 2, 8, 1, 9], [1, 2, 4, 6, 8, 9], None, None),  
    ([-1, -3, -2, -4, -5], [-5, -4, -3, -2, -1], None, None),
    ([1, 3, 3, 2], [1, 2, 3, 3], None, None), 
    ([1, "two", 3], None, TypeError, "All elements must be the same type"),
    (["banana", "apple", "orange", "mango"], ["apple", "banana", "mango", "orange"], None, None ),
    (["Banana", "apple", "Orange", "mango"], ["Banana", "Orange", "apple", "mango"], None, None),
    (["a", "abc", "ab"],["a", "ab", "abc"], None, None),
    (["10", "2", "30", "22"], ["10", "2", "22", "30"], None, None),
    (["_", "a", "#", "!"], ["!", "#", "_", "a"], None, None)
])

def test_sort_heapsort(input_list, expected_result, expected_exception, expected_message):
    if expected_exception:
        with pytest.raises(expected_exception) as excinfo:
            sort_heapsort(input_list)
        assert str(excinfo.value) == expected_message
    else:
        sort_heapsort(input_list)
        assert input_list == expected_result