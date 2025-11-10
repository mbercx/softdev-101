# Publishing

## What

Publishing a Python package means making it available for others to install via `pip install`.
The primary distribution platform is the Python Package Index (PyPI), the official repository where over 500,000 packages are hosted.
When you run `pip install numpy` or `pip install pytest`, you're installing packages from PyPI.

## Why

Publishing your code serves several important purposes:

**Ease of installation**: Instead of cloning repositories and installing from source, users can simply `pip install your-package`.
This dramatically lowers the barrier to entry for using your code.

**Dependency management**: When your package is on PyPI, other packages can list it as a dependency in their `pyproject.toml`.
This creates a network of packages that work together seamlessly.

**Versioning and stability**: PyPI hosts multiple versions of your package, allowing users to pin to specific versions they know work (`your-package==1.2.3`) while you continue developing new features.

**Discoverability**: PyPI makes your package searchable and discoverable by the broader Python community, increasing its potential impact and user base.

**Professional credibility**: A well-maintained package on PyPI signals that your code is ready for production use and demonstrates your commitment to software engineering best practices.

!!!example "Real-world scenario"

    You've developed a useful data analysis tool for your research group.
    Currently, colleagues need to:

    1. Clone your GitHub repository
    2. Navigate to the directory
    3. Create a virtual environment
    4. Run `pip install -e .`
    5. Remember to pull updates regularly

    After publishing to PyPI, they simply run `pip install your-tool` and get started immediately.
    Updates are just `pip install --upgrade your-tool` away.

## How

Publishing involves:

- Building your package into distribution formats (typically a wheel `.whl` and source distribution `.tar.gz`).
- Uploading these distributions to PyPI.
- Making your package discoverable and installable by anyone in the Python community.

In the days of old, you may have executed these steps manually.

