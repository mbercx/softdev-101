# Packages

## What

A Python package is a collection of modules (Python files) organized in a directory structure that can be imported and distributed.
At its simplest, a package is just a directory containing Python files and a special `__init__.py` file that marks it as a package.

The basic structure looks like this:

```
mypackage/
├── __init__.py
├── module1.py
└── module2.py
```

## Why

Packages serve several important purposes:

**Organization**: As your code grows beyond a single file, packages help you organize related functionality into logical groups.
Instead of one massive `utils.py` file, you might have `mypackage/strings.py`, `mypackage/numbers.py`, etc.

**Reusability**: Proper package structure makes it easy to reuse your code across different projects.
Once packaged, you can install your code with `pip install mypackage` just like any other library.

**Distribution**: A well-structured package can be shared with others via PyPI (Python Package Index), GitHub, or private repositories.
This is how all the packages you `pip install` are organized.

!!!example "Real-world scenario"

    You've written some useful data processing functions for one project.
    Later, you need the same functions in a different project.
    Without proper packaging, you'd copy-paste the files and manually track dependencies.
    With a package, you simply `pip install` it in the new project and import what you need.

# How

In principle, you can adopt any package structure you'd like.
However, adhering to a standard package structure makes it easier for others to understand and contribute to your code.
Everyone knows where to find the source code, tests, and documentation.
Have a look at the structure of the `softdev-101` package:

```
tree softdev-101/
```

```console {.no-copy}
softdev-101/
├── docs
│   ├── ci.md
│   ├── ...
│   └── version_control.md
├── LICENSE
├── mkdocs.yml
├── pyproject.toml
├── README.md
├── src
│   └── softdev_101
│       ├── __about__.py
│       └── __init__.py
└── tests
    ├── conftest.py
    └── test_example.py
```

??? warning "The `tree` command doesn't exist!"

    You may not have `tree` installed on your system.
    As you can see, it's a neat way to see the contents of a directory, but it's not necessary for the tutorial.
    Feel free to install it if you like it though!

Let's go over the various directories and files:

- `docs`: these contain the documentation files, which you are reading right now!
  The `mkdocs.yml` file is the configuration for the documentation, you'll read all about that in [the corresponding topic](documentation.md).
- `LICENSE`: it's standard practise to ship your code with a license, that tells others how they can use your code.
  A very common (and permissive) option is the MIT license.
- `pyproject.toml`: The modern standard for Python package configuration.
  Contains package metadata (name, version, dependencies), build system settings, and tool configurations.
- `README.md`: The front page of your package - the first thing people see on GitHub or PyPI.
- `src/`: Contains your actual source code. Using a `src/` directory is best practice because it keeps the project root clean and prevents import issues during testing.
- `src/softdev_101/`: The actual Python package. Note the underscore instead of hyphen - package names must be valid Python identifiers.
- `tests/`: Your test files, kept separate from source code. We'll cover this in [the tests topic](tests.md).
