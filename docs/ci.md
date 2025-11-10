# Continuous Integration

## What

Continuous Integration (CI) is the practice of automatically building, testing, and validating your code every time you make changes.
Instead of manually running tests or checks before merging code, CI systems do this automatically.

## Why

In a sense, a good software developer is _lazy_.
They dislike manual work, and want to automate as much as possible.
CI allows you to stop doing all the checks/steps for every code change manually.
The added benefit is that this is _much_ less error prone: e.g. your documentation will never be out of date because you forgot to deploy it.

!!!example "Real-world scenario"

    You're maintaining a Python package, and someone wants to make a change to your code.
    Without CI, you'll have to test their changes locally: did they install/run the `pre-commit`?
    Are the tests passing for the Python versions you support?
    Ain't nobody got time for that!

## How

GitHub Actions is a CI/CD (Continuous Integration/Continuous Deployment) platform built into GitHub.
It lets you define workflows that run automatically in response to events like pushing code, opening pull requests, or adding a release tag.

A GitHub actions workflow is defined in a YAML file, stored in the `.github/workflows` directory.
Let's have a look at `deploy-mkdocs.yaml`:

```yaml {.no-copy}
# deploy-mkdocs.yaml
name: Deploy MkDocs site to Github pages
on:
  push:
    branches:
      - main

permissions:
  contents: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: 3.x

      - run: pip install mkdocs mkdocs-material
      - run: mkdocs gh-deploy --force

```