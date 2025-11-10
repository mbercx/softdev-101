# Tests

## What

Tests are code that verifies your source code works as expected.
They automatically check that functions produce correct outputs for given inputs, handle edge cases properly, and behave correctly when things go wrong.

Common types of tests include:

- **Unit tests**: Test individual functions or methods in isolation.
- **Integration tests**: Test how different parts of your code work together.
- **Regression tests**: Ensure bugs that were fixed don't come back.

## Why

Testing serves several critical purposes:

**Carefree development**: With good tests, you can confidently change your code knowing that if you break something, the tests will catch it.

**Catch bugs early**: Tests help you find problems before your code reaches users (or before your paper is published).
It's much cheaper to fix a bug during development than after deployment.

**Prevent regressions**: Once you fix a bug, write a test for it.
This ensures the same bug doesn't sneak back in during future changes.

!!!example "Real-world scenario"

    You've written a Python script to analyze experimental data for your research.
    It works correctly but takes 30 minutes to run, so you want to make it faster.

    You manage to make it run in 3 minutes - great! But how do you know it still produces the same results?

    Without tests, you'd need to manually compare outputs, check figures visually, and hope you didn't introduce subtle bugs during optimization.
    With tests that verify your code produces correct results for known inputs, you can confidently run your test suite and know within seconds whether your optimizations broke anything.

## How

The most popular testing framework for Python is `pytest`.

### Installing pytest

If pytest is listed in your `pyproject.toml` as a test dependency, you can install it with:

```
pip install -e .[tests]
```

This installs your package in editable mode (`-e`) along with the test dependencies.

For the `dev_tutorial` package, pytest is already included in the `tests` optional dependencies:

```toml
[project.optional-dependencies]
tests = [
  "pytest"
]
```

### Running pytest

To run all tests in your project:

```
pytest
```

Pytest automatically discovers test files (files starting with `test_` or ending with `_test.py`) and runs all functions starting with `test_`.

```console {.no-copy}
======================== test session starts =========================
collected 1 item

tests/test_example.py .                                        [100%]

========================= 1 passed in 0.01s ==========================
```

The `.` indicates the test passed. If a test fails, pytest shows detailed information about what went wrong.

### Writing a simple test

Tests go in the `tests/` directory. Here's a simple example:

```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
```

The key elements:

- **Function name starts with `test_`**: This tells pytest it's a test
- **`assert` statements**: Check that conditions are true. If an assertion fails, the test fails
- **Multiple assertions**: You can have multiple checks in one test

### Using fixtures

Fixtures are reusable pieces of code that set up test conditions.
They're defined in `conftest.py` and can be used across multiple test files.

Here's the example from `dev_tutorial`:

```python
# tests/conftest.py
import pytest

@pytest.fixture
def readability_counts() -> bool:
    return True
```

```python
# tests/test_example.py
def test_example(readability_counts):
    assert readability_counts is True
```

Fixtures are useful for e.g. setting up test data or any code you want to reuse across tests. 
To use a fixture, simply add it as a parameter to your test function.
`pytest` automatically calls the fixture and passes the result to your test.

!!! tip "Tips for writing good tests"

    - **Test edge cases**: Don't just test the happy path.
      What happens with empty inputs? Very large numbers? Invalid data?
    - **Keep tests independent**: Each test should work on its own, not depend on other tests running first.
    - **Use descriptive names**: `test_add_handles_negative_numbers` is better than `test_add_2`.
