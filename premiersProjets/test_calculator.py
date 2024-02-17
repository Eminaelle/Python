from calculator import square

#test avec la commande pytest

def test_positive():
    test_dict = {2 : 4, 3 : 9}
    for i in test_dict:
        assert square(i) == test_dict[i]

def test_negative():
    test_dict = {-2 : 4, -3 : 9}
    for i in test_dict:
        assert square(i) == test_dict[i]

def test_zero():
    assert square(0) == 0

