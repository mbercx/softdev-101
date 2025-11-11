# Formatting & Linting

## What

**Code formatting** refers to the consistent styling of your code - how it looks visually.
This includes indentation, spacing, line length, quote styles, and other stylistic choices that don't affect how the code runs but impact how it reads.

**Linting** checks your code for potential bugs, code smells, and programming errors.
It catches issues like unused variables, undefined names, or overly complex code before they cause problems.

## Why

**Formatting** helps you focus on logic rather than style:

- **Save time and energy**: No more deciding where to put spaces or how to break lines
- **Improved readability**: Consistent code is easier to read and understand
- **Better collaboration**: Everyone's code looks the same, so git diffs show real changes instead of whitespace adjustments

**Linting** catches bugs before they happen:

- **Early bug detection**: Find issues like unused variables or undefined names before running your code
- **Code quality**: Identify overly complex code, missing error handling, or potential performance issues
- **Learn best practices**: Linters teach you Python conventions and common pitfalls to avoid

!!!example "Real-world scenario"

    You're collaborating with two colleagues on a data analysis project.
    One person uses tabs for indentation, another uses 2 spaces, and you use 4 spaces.
    One person puts spaces around operators (`x = 1 + 2`), another doesn't (`x=1+2`).

    Every time you work on the same file, version control shows dozens of "changes" that are just formatting differences.
    Code reviews become debates about style instead of correctness.

    With a formatter like `black` or `ruff`, everyone runs the formatter before committing.
    All code looks identical regardless of who wrote it, git diffs only show meaningful changes, and you can focus on solving problems instead of arguing about spaces.

## How

We'll use `ruff` as our tool of choice.
It's fast, modern, and can handle both formatting (using `black` under the hood) and linting.
Let's install `ruff` in our environment:

```
pip install ruff
```

Let's see `ruff` in action!
Have a look at the file `src/dev_tutorial_<YOUR_USERNAME>/messy.py`:

```python {.no-copy}
# src/dev_tutorial_<YOUR_USERNAME>/messy.py
def calculate_statistics(data,include_median=True):
    """Calculate statistics for a list of numbers."""
    debug_mode=True
    if len(data)==0:
        return None

    mean=sum(data)/len(data)
    result={'mean':mean,'min':min(data),'max':max(data)}

    if include_median:
        sorted_data=sorted(data)
        n=len(sorted_data)
        median=sorted_data[n//2] if n%2!=0 else (sorted_data[n//2-1]+sorted_data[n//2])/2
        result['median']=median

    return result
```

This code has several formatting issues:

- Missing spaces after commas in function parameters
- Inconsistent spacing around operators (`==`, `=`, `/`, `%`, `//`)
- No spaces around dictionary keys and values

Now run the formatter:

```
ruff format
```

```console {.no-copy}
1 file reformatted,  5 files left unchanged
```

Open `src/dev_tutorial_<YOUR_USERNAME>/messy.py` again and check how the code has changed.
`ruff` has automatically fixed all the formatting issues:

```python
def calculate_statistics(data, include_median=True):
    """Calculate statistics for a list of numbers."""
    debug_mode = True
    if len(data) == 0:
        return None

    mean = sum(data) / len(data)
    result = {"mean": mean, "min": min(data), "max": max(data)}

    if include_median:
        sorted_data = sorted(data)
        n = len(sorted_data)
        median = (
            sorted_data[n // 2]
            if n % 2 != 0
            else (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        )
        result["median"] = median

    return result
```

Much better!
But we still haven't checked the code for quality issues.
Let's run the linter:

```
ruff check
```

```console {.no-copy}
F841 Local variable `debug_mode` is assigned to but never used
 --> src/dev_tutorial_<YOUR_USERNAME>/messy_code.py:3:5
  |
1 | def calculate_statistics(data, include_median=True):
2 |     """Calculate statistics for a list of numbers."""
3 |     debug_mode = True
  |     ^^^^^^^^^^
4 |     if len(data) == 0:
5 |         return None
  |
help: Remove assignment to unused variable `debug_mode`

Found 1 error.
No fixes available (1 hidden fix can be enabled with the `--unsafe-fixes` option).
```

The linter found an issue with our code!
To understand the problem, run:

```
ruff rule F841
```

Now fix the issue by removing the unused `debug_mode` variable
After making these changes manually, run both commands again to verify everything is clean:

```
ruff format && ruff check
```

```console {.no-copy}
6 files left unchanged
All checks passed!
```

### Automating with pre-commit

Instead of remembering to run `ruff format` and `ruff check` before every commit, you can use `pre-commit` to automatically run these checks.

`pre-commit` is a framework that manages git hooks - scripts that run automatically before you commit code.

First, install pre-commit:

```
pip install pre-commit
```

The project already has a `.pre-commit-config.yaml` file that configures which checks to run (have a look!).
To install the git hooks, run:

```
pre-commit install
```

Now, every time you try to commit code, `pre-commit` will automatically:

1. Run `ruff format` to format your code
2. Run `ruff check` to lint your code
3. If any issues are found, the commit will be blocked until you fix them

You can also run the checks manually without committing:

```
pre-commit run -a
```

This ensures your code is always formatted and linted before it enters version control!

!!! tip "Give it a try!"

    Try to make some changes to one of the modules, and run `git commit`.
    Both the linter and formatter should run automatically.

---

You've set up local tools to build & deploy documentation, run tests and check your code.
Wouldn't it be nice if all this ran automatically every time you push to GitHub?
That's where Continuous Integration comes in!
**Next up: [Continuous Integration (CI)](ci.md)**
