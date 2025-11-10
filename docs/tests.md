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

If `pytest` is listed in your `pyproject.toml` as a test dependency, you can install it with:

```
pip install -e .[tests]
```

This installs your package in editable mode (`-e`) along with the test dependencies.

For the `dev-tutorial` package, `pytest` is already included in the `tests` optional dependencies:

```toml {.no-copy}
[project.optional-dependencies]
tests = [
  "pytest",
  "pytest-regressions"
]
```

### Running pytest

To run all tests in your project with added verbosity (`-v`):

```
pytest -v
```

Pytest automatically discovers test files (files starting with `test_` or ending with `_test.py`) and runs all functions starting with `test_`.

```console {.no-copy}
========================================================= test session starts =========================================================
platform darwin -- Python 3.9.6, pytest-8.4.2, pluggy-1.6.0 -- /Users/mbercx/tmp/workshop/.my_env/bin/python3
cachedir: .pytest_cache
rootdir: /Users/mbercx/tmp/workshop/dev-tutorial
configfile: pyproject.toml
plugins: datadir-1.8.0, regressions-2.8.3
collected 2 items

tests/test_functions.py::test_add PASSED                                                                                        [ 50%]
tests/test_functions.py::test_fixture PASSED                                                                                    [100%]

========================================================== 2 passed in 0.01s ==========================================================
```

Hopefully all the tests passed!
If a test fails, `pytest` shows detailed information about what went wrong.

### Writing a simple test

Tests go in the `tests/` directory.
Here's a simple example testing the `add` function from `tests/test_functions.py`:

```python
# tests/test_functions.py
from dev_tutorial.functions import add

def test_add():
    """Test the `add` function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
```

The key elements:

- **Function name starts with `test_`**: This tells pytest it's a test.
- **`assert` statements**: Check that conditions are true. If an assertion fails, the test fails.
- **Multiple assertions**: You can have multiple checks in one test.
- **Docstring**: Optional but recommended to describe what the test does.

### Using fixtures

Fixtures are reusable pieces of code that set up test conditions.
They're defined in `conftest.py` and can be used across multiple test files.

Here's the example from `dev-tutorial`:

```python
# tests/conftest.py
import pytest

@pytest.fixture
def list_of_integers():
    return [0, 1, 2, 3, 4]
```

```python
# tests/test_functions.py
from dev_tutorial.functions import sum_and_multiply

def test_fixture(list_of_integers):
    """Test the `sum_and_multiply` function using the `list_of_integers` fixture."""
    assert sum_and_multiply(list_of_integers, 2) == 20
```

Fixtures are useful for setting up test data or any code you want to reuse across tests.
To use a fixture, simply add it as a parameter to your test function.
`pytest` automatically calls the fixture and passes the result to your test.

In this example, `list_of_integers` returns `[0, 1, 2, 3, 4]`, which sums to 10.
Multiplying by 2 gives 20, which is what the test verifies.

### Writing an integration test with pytest-regressions

The `pytest-regressions` package provides fixtures for automatically comparing test outputs against stored reference data.
This is especially useful for testing complex outputs like dictionaries, dataframes, or files.

The `data_regression` fixture is particularly powerful for more complex data.
Here's an example from `tests/test_functions.py`:

```python
# tests/test_functions.py
def test_data_regression(list_of_integers, data_regression):
    result = multiply(list_of_integers, 2)
    data_regression.check(result)
```

In the template package, the test is still commented.
Remove the comment symbols (`#`) and run your tests again.
The first time you run this test, it will fail with:

```python {.no-copy}
>       data_regression.check(result)
E       Failed: File not found in data directory, created:
E       - /Users/mbercx/tmp/workshop/dev-tutorial/tests/test_functions/test_data_regression.yml
```

The `data_regression` fixture creates a file at `tests/test_functions/test_data_regression.yml` containing the reference output.
On subsequent runs, it compares the current output against this reference.

For the example above, the reference file would contain:

```yaml
- 0
- 2
- 4
- 6
- 8
```

If the output changes:

- The test **fails** and shows you the difference
- Run `pytest --force-regen` to update the reference files if the changes are intentional
- You can review the changes to verify they're correct

If you have some time, give it a try!
Change the factor in the test from 2 to 3, and see what happens.

!!! tip "Tips for writing good tests"

    - **Test edge cases**: Don't just test the happy path.
      What happens with empty inputs? Very large numbers? Invalid data?
    - **Keep tests independent**: Each test should work on its own, not depend on other tests running first.
    - **Use descriptive names**: `test_add_handles_negative_numbers` is better than `test_add_2`.

---

Your tests are keeping your code reliable! Now let's make your code look professional and catch potential bugs before they happen with automated formatting and linting.
**Next up: [Formatting/linting your code with Ruff](formatting.md)**
