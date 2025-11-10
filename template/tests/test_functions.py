from dev_tutorial.functions import add, sum_and_multiply, multiply


def test_add():
    """Test the `add` function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_fixture(list_of_integers):
    """Test the `sum_and_multiply` function using the `list_of_integers` fixture."""
    assert sum_and_multiply(list_of_integers, 2) == 20


# def test_data_regression(list_of_integers, data_regression):
#     """Test the `multiply` function via data regression."""
#     result = multiply(list_of_integers, 2)
#     data_regression.check(result)
