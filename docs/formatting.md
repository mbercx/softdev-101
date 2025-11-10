# Formatting

## What

Code formatting refers to the consistent styling of your code - how it looks visually.
This includes indentation, spacing, line length, quote styles, and other stylistic choices that don't affect how the code runs but impact how it reads.

A code formatter automatically reformats your code to follow a consistent style.
Popular Python formatters include:

- **black**: An opinionated formatter that enforces a strict style with minimal configuration.
- **ruff**: A fast formatter that can also perform linting (checking for code quality issues).

## Why

Consistent formatting serves several important purposes:

**Focus on logic, not style**: With automatic formatting, you don't waste time or mental energy deciding where to put spaces, how to break lines, or arguing about style preferences during code reviews.

**Improved readability**: Consistent code is easier to read and understand.
When all code follows the same patterns, you can focus on what the code does rather than getting distracted by inconsistent styling.

**Better collaboration**: When everyone's code looks the same, it's easier to work together.
Code reviews focus on functionality rather than style preferences, and git diffs show real changes instead of whitespace adjustments.

!!!example "Real-world scenario"

    You're collaborating with two colleagues on a data analysis project.
    One person uses tabs for indentation, another uses 2 spaces, and you use 4 spaces.
    One person puts spaces around operators (`x = 1 + 2`), another doesn't (`x=1+2`).

    Every time you work on the same file, version control shows dozens of "changes" that are just formatting differences.
    Code reviews become debates about style instead of correctness.

    With a formatter like `black` or `ruff`, everyone runs the formatter before committing.
    All code looks identical regardless of who wrote it, git diffs only show meaningful changes, and you can focus on solving problems instead of arguing about spaces.

## How

We'll use `ruff` as our formatter.
It's fast, modern, and can handle both formatting (using `black` under the hood) and linting.
Let's install `ruff` in our environment:

```
pip install ruff
```

Let's see `ruff` in action!
First, create a poorly formatted Python file to demonstrate the formatter.

Copy this messy code into a new file `src/dev_tutorial/messy.py`:

```python
def calculate_statistics(data,include_median=True):
    """Calculate statistics for a list of numbers."""
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

You should see output like:

```console {.no-copy}
1 file reformatted
```

Open `src/dev_tutorial/messy.py` again and check how the code has changed.
`ruff` has automatically fixed all the formatting issues.
