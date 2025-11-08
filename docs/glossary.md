# 📜 Glossary

!!! note
    This page mainly discusses "semantics": i.e. what do we mean when we say words?
    These definitions are my own, and are by no means perfect.
    But hopefully they help you understand the content of this material better!

* **version control system (VCS)**: a tool that records changes to a file or set of files over time so that you can recall specific versions later.
* **repository**: A directory tracked by `git` that stores all your project files along with the complete history of every change made to them.
* **commit**: A snapshot of your project at a specific point in time, recording what changes were made, who made them, and when. Each commit has a unique identifier and typically includes a message describing the changes.
* **branch**: An independent line of development in a git repository that allows you to work on features or fixes in isolation from the main codebase. Branches can be merged back together later.
* **remote**: A `git` repository hosted on a server (typically GitHub) that you can push changes to and pull changes from, enabling collaboration with others.
* **fork**: A personal copy of someone else's repository that you can modify independently and optionally contribute changes back to the original.
* **virtual environment**: An isolated Python workspace containing its own interpreter and packages, isolated from other environments and the system Python installation.
* **dependency**: A package or library that your code requires to function properly. Dependencies can have their own dependencies (transitive dependencies).
* **package**: A collection of Python modules that can be installed and imported. Packages are distributed through repositories like PyPI and installed using tools like `pip`.
* **pip**: `pip` installs packages! Python's package installer, used to install, upgrade, and manage packages from the Python Package Index (PyPI) and other sources.
* **standard library**: The collection of modules that come with Python by default and can be imported without additional installation (e.g., `os`, `sys`, `json`, `datetime`).
* **built-in**: A function, type, or feature that's available in Python without importing anything (e.g., `print()`, `len()`, `list`). These are always available.
