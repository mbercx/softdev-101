from dev_tutorial.functions import add


def test_add():
    """Test the `add` function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_fixture(readability_counts):
    assert readability_counts is True
