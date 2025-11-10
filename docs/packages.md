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

## How

### Workshop repository

For the rest of this workshop, you'll need to have a `git`-tracked Python package to work on.
[Create a new **empty** repository on GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository#creating-a-new-repository-from-the-web-ui) called `dev-tutorial` and `clone` it to your local directory:

```
git clone https://github.com/<YOUR_USERNAME>/dev-tutorial.git
```

??? question "Can I also work with my own code?"

    Of course!
    But you may have a bit more work: the instructions in the next pages won't perfectly fit your package.
    If you get stuck, consider starting from a fresh repository and using the template discussed below.

To get the workshop package template, we'll use a tool called `copier`.
First install it in your virtual environment:

```
pip install copier
```

Then copy the workshop template into your fresh repository.

```
copier copy -f https://github.com/mbercx/softdev-101 dev-tutorial/
```

To make sure Python is aware of the changes we make as we work on our package, let's install the package from its local directory in "editable" mode (`-e`):

```
pip install -e dev-tutorial/
```

Listing the packages installed in our environment again with `pip list`:

```console {.no-copy}
❯ pip list
Package                Version Editable project location
---------------------- ------- ---------------------------------------
annotated-types        0.7.0
colorama               0.4.6
copier                 9.10.3
cowsay                 6.1
dev-tutorial           0.0.1   /Users/mbercx/tmp/workshop/dev-tutorial
...
```

You can see a new column: `Editable project location`.

### Structure

In principle, you can adopt any package structure you'd like.
However, adhering to a standard package structure makes it easier for others to understand and contribute to your code.
Everyone knows where to find the source code, tests, and documentation.
Have a look at the structure of the `dev-tutorial` package:

```
tree dev-tutorial
```

```console {.no-copy}
dev-tutorial
├── docs
│   ├── developer.md
│   └── index.md
├── LICENSE
├── mkdocs.yml
├── pyproject.toml
├── README.md
├── src
│   └── dev_tutorial
│       ├── __about__.py
│       └── __init__.py
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
- `src/dev_tutorial/`: The actual Python package. Note the underscore instead of hyphen - package names must be valid Python identifiers.
- `tests/`: Your test files, kept separate from source code. We'll cover this in [the tests topic](tests.md).

### Pushing the template files to GitHub

Let's push the local changes in our `dev-tutorial` package to GitHub.
First, enter the package directory:

```
cd dev-tutorial
```

Stage _all_ the new files with:

```
git add .
```

And `commit` them:

```
git commit -m 'Initial commit'
```

You'll see the full list of files that have been added in this commit.
Time to `push` your local changes to GitHub:

```
git push origin
```

`origin` is the default name of the remote repository you cloned from.
To see all the remotes you have configured, use:

```
git remote -v
```
