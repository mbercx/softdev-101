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
* **clone**: Creating a local copy of a remote repository on your computer, including all its files, history, and branches.
* **staging area**: An intermediate space in git where you prepare changes before committing them. Also called the "index".
* **merge**: Combining changes from one branch into another, integrating the development histories of both branches.
* **pull request (PR)**: A request to merge changes from one branch into another, typically used for code review and collaboration on platforms like GitHub.
* **HEAD**: A pointer in git that refers to the current branch or commit you're working on.
* **module**: A Python file containing definitions and statements that can be imported and used in other Python programs.
* **import**: A Python statement that brings code from other modules or packages into your current program's namespace.
* **IDE (Integrated Development Environment)**: A software application that combines a code editor, debugger, and other development tools in one interface (e.g., VS Code, PyCharm).
* **debugging**: The process of finding and fixing errors (bugs) in code, often using tools that allow you to pause execution and inspect variables.
* **REPL (Read-Eval-Print Loop)**: An interactive programming environment that reads user input, evaluates it, prints the result, and loops back. Python's interactive shell is a REPL.
* **CI/CD (Continuous Integration/Continuous Deployment)**: Automated processes that build, test, and deploy code changes, ensuring that software is always in a releasable state.
* **refactoring**: Restructuring existing code to improve its readability, maintainability, or performance without changing its external behavior.
* **semantic versioning**: A versioning scheme using three numbers (MAJOR.MINOR.PATCH) to communicate the nature of changes in software releases (e.g., 1.2.3).
