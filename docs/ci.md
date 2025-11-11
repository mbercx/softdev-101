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
    Let's be real: ain't nobody got time for that!

## How

GitHub Actions is a CI/CD (Continuous Integration/Continuous Deployment) platform built into GitHub.
It lets you define workflows that run automatically in response to events like pushing code, opening pull requests, or adding a release tag.

A GitHub actions workflow is defined in a YAML file, stored in the `.github/workflows` directory.

### Example: Deploying documentation

Let's have a look at `deploy-mkdocs.yaml`:

```yaml {.no-copy}
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

**Breaking it down:**

- `name`: A descriptive name for the workflow that appears in the GitHub Actions UI.
- `on`: Defines when the workflow runs - here, on every push to the `main` branch.
- `permissions`: Grants write access to repository contents (needed to push to the `gh-pages` branch).
- `jobs`: Contains one or more jobs to run.
  Here we have a single `deploy` job.
- `runs-on`: Specifies the operating system for the job (ubuntu-latest).
- `steps`: A list of sequential actions to perform:
  - `actions/checkout@v4`: Checks out your repository code.
  - `actions/setup-python@v5`: Installs Python (version 3.x means latest 3.x release).
  - `run`: Executes shell commands - first installing dependencies, then deploying docs.

This workflow automatically rebuilds and deploys your documentation site every time you push to main!

### Viewing workflow runs

Once you push code to GitHub, you can view workflow runs in the **Actions** tab of your repository.
Each workflow run shows:

- Whether it passed or failed.
- The output of each step.
- How long each step took.

If a workflow fails, you can click into it to see which step failed and read the error messages to debug the issue.

!!! tip "Check your actions!"

    Learning how to write GitHub actions can be a tutorial in itself.
    For now, go to your repository on GitHub, and click on the Actions tab.
    Explore the various actions that ran, and see what you can understand.
