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

### Building your package

Before you can publish your package, you need to build it into distribution formats that `pip` can install.
The two standard formats are:

- **Wheel (`.whl`)**: A pre-built binary distribution that installs quickly
- **Source distribution (`.tar.gz`)**: The raw source code that gets built during installation

To create these distributions, you need a **build backend**.
The workshop template uses [Hatchling](https://hatch.pypa.io/), a modern, standards-compliant build system.
You can see this configured in your `pyproject.toml`:

```toml {.no-copy}
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

This tells Python's build tools to use Hatchling when building your package.

To build your package, use the `build` module (part of the Python Packaging Authority's standard tooling):

```bash
pip install build
python -m build
```

```console {.no-copy}
* Creating isolated environment: venv+pip...
* Installing packages in isolated environment:
  - hatchling
* Getting build dependencies for sdist...
* Building sdist...
* Building wheel from sdist...
* Creating isolated environment: venv+pip...
* Installing packages in isolated environment:
  - hatchling
* Getting build dependencies for wheel...
* Building wheel...
Successfully built dev-tutorial-<YOUR_USERNAME>-0.0.1.tar.gz and dev_tutorial_<YOUR_USERNAME>-0.0.1-py3-none-any.whl
```

This creates a `dist/` directory containing both distribution formats:

=== "Linux/macOS"

    ```bash
    ls dist/
    ```

=== "Windows"

    ```powershell
    dir dist\
    ```

Expected output:

```console {.no-copy}
dev-tutorial-<YOUR_USERNAME>-0.0.1.tar.gz
dev_tutorial_<YOUR_USERNAME>-0.0.1-py3-none-any.whl
```

### Versioning

Notice that the built distributions include a version number (`0.0.1`).
This comes from the `__version__` variable in `src/dev_tutorial_<YOUR_USERNAME>/__about__.py`:

```python {.no-copy}
__version__ = "0.0.1"
```

Version numbers help users understand what changes between releases.
The standard approach is [Semantic Versioning (SemVer)](https://semver.org/), which uses the format `MAJOR.MINOR.PATCH`:

- **MAJOR**: Increment when you make backwards-incompatible API changes (e.g., `1.0.0` → `2.0.0`)
- **MINOR**: Increment when you add functionality in a backward-compatible manner (e.g., `1.0.0` → `1.1.0`)
- **PATCH**: Increment when you make backward-compatible bug fixes (e.g., `1.0.0` → `1.0.1`)

For example:
- `0.0.1` → `0.0.2`: Fixed a bug
- `0.0.2` → `0.1.0`: Added a new feature
- `0.1.0` → `1.0.0`: First stable release or breaking changes

!!!info "Version 0.x.x"

    Versions starting with `0.` (like `0.1.0`) indicate the package is still in early development.
    Users should expect breaking changes between minor versions.
    Once your API is stable, release version `1.0.0`.

### Creating API tokens

Before you can upload to PyPI or Test PyPI, you need to create an **API token** for authentication.
PyPI no longer accepts username/password authentication - tokens are required.

For Test PyPI:

1. Create an account at [https://test.pypi.org/](https://test.pypi.org/)
2. Go to Account Settings → API tokens
3. Click "Add API token"
4. Give it a name (e.g., "dev-tutorial upload")
5. Copy the token immediately - it's only shown once!

The token will look like `pypi-...` (a long string of characters).

!!!warning "Save your token!"

    API tokens are only displayed once when created.
    Store it somewhere safe - you'll need it for uploads.
    If you lose it, you'll have to create a new one.

### Uploading to Test PyPI

Before publishing to the real PyPI, it's smart to test with **Test PyPI** - a separate instance where you can experiment without consequences.

Install `twine`, the tool for uploading packages:

```bash
pip install twine
```

Upload your distributions to Test PyPI:

```bash
twine upload --repository testpypi dist/*
```

When prompted:
- **Username**: Enter `__token__` (exactly as written, with double underscores)
- **Password**: Paste your API token (including the `pypi-` prefix)

Once uploaded, your package will be available at:

```
https://test.pypi.org/project/dev-tutorial-<YOUR_USERNAME>/
```

To install from Test PyPI and verify it works:

```bash
pip install --index-url https://test.pypi.org/simple/ dev-tutorial-<YOUR_USERNAME>
```

!!! info "The real PyPI"

    Test PyPI is a separate service from the real PyPI.
    Packages uploaded there are periodically deleted, and dependencies from the real PyPI might not be available.
    It's purely for testing the upload process!
    Publishing to the real PyPI is very similar, but I would only do it with _your_ proper package when it's ready.

### Automating with GitHub Actions

Manually building and uploading packages works, but it's error-prone and tedious.
A better approach is to automate the entire publishing process with GitHub Actions.
The workshop template includes a workflow file `.github/workflows/cd.yml` that automatically publishes to Test PyPI when you push a version tag.

!!! question "If you are feeling lost"

    I know this all seems like a lot. It is!
    The main goal here is to expose you to this approach of doing things, you can take your time in understanding all the aspects.

### Setting up trusted publishing

Instead of storing API tokens as secrets, the workflow uses **trusted publishing** - a modern, more secure authentication method.
With trusted publishing, PyPI trusts GitHub Actions to publish on your behalf without needing to manage tokens.

To set this up on Test PyPI:

1. Go to [https://test.pypi.org/](https://test.pypi.org/) and log in
2. Click **Your projects** (but you won't have a project yet - that's okay!)
3. Go to **Publishing** in the left sidebar
4. Scroll to **Add a new pending publisher**
5. Fill in the form:
   - **PyPI Project Name**: `dev-tutorial-<YOUR_USERNAME>` (your package name)
   - **Owner**: Your GitHub username
   - **Repository name**: `dev-tutorial-<YOUR_USERNAME>`
   - **Workflow name**: `cd.yml`
6. Click **Add**

!!!info "How trusted publishing works"

    When your GitHub Actions workflow runs, GitHub issues a short-lived identity token that proves the workflow is running from your specific repository.
    Test PyPI verifies this token and allows the upload - no long-lived secrets needed!
    This is more secure because there are no tokens to leak or rotate.

### Automated publishing workflow

With trusted publishing and automated workflows, releasing a new version is as simple as:

1. Update the version in `__about__.py` following SemVer (e.g., `0.0.1` → `0.1.0`)
2. Commit the bump in version number:

    ```
    # Update version, commit, tag, and push
    git commit -am 'Bump version to 0.1.0'
    ```

3. Create and push a Git tag:

    ```
    git tag v0.1.0
    git push origin main v0.1.0
    ```

→ **GitHub Actions automatically builds and publishes to Test PyPI!**

Watch the workflow run in the **Actions** tab of your repository.
If something goes wrong, check the workflow logs for error messages.

Once published, verify your package has a new version at `https://test.pypi.org/project/dev-tutorial-<YOUR_USERNAME>/`.

!!! info "This is the end..."

    For now, this is the end of this basics of software development workshop.
    More material might be coming soon!
