"""Project-wide pytest fixtures & hooks.

Docs: https://docs.pytest.org/en/stable/how-to/fixtures.html#conftest-py-sharing-fixtures-across-multiple-files
"""

import pytest


@pytest.fixture
def list_of_integers():
    return [0, 1, 2, 3, 4]
