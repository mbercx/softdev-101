# Documentation

## What

Documentation is written material that explains what your code does, how to use it, and why design decisions were made.

## Why

Documentation serves multiple audiences and purposes:

**For yourself**: You'll be surprised how quickly you forget how your own code works.
Documentation serves as a reference when you return to a project after weeks or months.

**For users**: Clear documentation helps people understand how to install and use your code without having to read the implementation.
Good examples and tutorials lower the barrier to entry.

**For developers**: Documentation explains the "why" behind design decisions, making it easier for others (and future you) to understand the codebase and contribute effectively.

**For discoverability**: Well-documented projects are more likely to be found, used, and contributed to.
A good README can be the difference between a project being adopted or ignored.

!!!example "Real-world scenario"

    You've written a useful Python package six months ago.
    A colleague wants to use it, but there's no documentation.
    They ask you "How do I install this? What does function X do? Why did you structure it this way?"
    You realize you can't remember the answers without digging through the code yourself.

    With documentation, your colleague can find answers independently, and you can focus on new work instead of repeatedly explaining the same concepts.

## How

For this workshop, we'll focus on creating user-facing documentation using [MkDocs](https://www.mkdocs.org/), a static site generator that creates beautiful documentation from Markdown files.

### Setting up MkDocs

MkDocs is already set up in the `dev_tutorial` package.
Let's look at the key components:

The `mkdocs.yml` configuration file:

```yaml
site_name: Basics of software development

theme:
  name: material
  features:
    - navigation.expand
    - content.code.copy

markdown_extensions:
  - admonition
  - pymdownx.superfences
  - pymdownx.tabbed:
      alternate_style: true
```

Key elements:

- `site_name`: The title of your documentation site.
- `theme`: We use [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/), a popular, clean theme.
- `features`: Enable specific functionality (expandable navigation, code copy buttons).
- `markdown_extensions`: Add support for admonitions, code blocks, tabs, etc.

### Building the documentation

To build the documentation, we need to run `mkdocs`, and also have the `mkdocs-material` theme installed.
These are both Python packages, so you could install them manually via `pip`.
However, the convention is to list all required "devops" (development operations) packages as extras or "optional dependencies": 

```
[project.optional-dependencies]
docs = [
  "mkdocs",
  "mkdocs-material"
]
```

For the documentation packages, you have to install the `docs` extra:

```
pip install -e dev_tutorial[docs]
```

Notice the `[docs]` at the end: this tells `pip` to also install the optional dependencies specified under `docs`.
The output is a little bigger this time!
We only installed `mkdocs` and `mkdocs-material`, but they have their own dependencies.

Now we can use the `mkdocs` command to build the documentation:

```
mkdocs build
```

```console {.no-copy}
INFO    -  Cleaning site directory
INFO    -  Building documentation to directory: /path/to/your/dir/dev_tutorial/site
INFO    -  Documentation built in 0.22 seconds
```

As the second `INFO` message indicates, the website is built in the `site` directory.
Open it and have a look:

```
open site/index.html
```

You should recognise it, it's the documentation you're reading now!

Building the documentation and reloading the page every time is rather tedious.
Fortunately, you can also "serve" the documentation:

```
mkdocs serve
```

this will run a server that automatically detects file changes when you save them, and updates the build.

### Writing documentation

Documentation files go in the `docs/` directory as Markdown (`.md`) files.
The page you're reading right now is `docs/documentation.md`!

MkDocs uses standard Markdown syntax. For example, to create a link:

```markdown
[link text](https://example.com)
```

this will render: [link text](https://example.com).

MkDocs Material also supports **admonitions** via the `admonition` extension.
These are highlighted boxes that make important information stand out:

```markdown
!!!warning "Important"
    This is a note that stands out from the main text.
    You can include code, lists, and other Markdown inside!
```

this will render:

!!!warning "Important"
    This is a note that stands out from the main text.
    You can include code, lists, and other Markdown inside!

If you're not familiar with Markdown, try this [10 minute tutorial](https://commonmark.org/help/tutorial/).
For the Material for MkDocs theme and all its possible extensions, we refer to [their documentation](https://squidfunk.github.io/mkdocs-material/).

!!! tip "Give it a try!"

    Serve the documentation with `mkdocs serve`, open this page, make some changes and save the file.
    Can you see the page being updated?

You're probably wondering how to deploy the documentation to a website, as I've done for this repository.

### Deploying to GitHub Pages

GitHub Pages is a free hosting service for static websites, perfect for documentation.
MkDocs makes deploying to GitHub Pages incredibly simple.

First, make sure your documentation builds successfully:

```
mkdocs build
```

Then deploy with a single command:

```
mkdocs gh-deploy
```

This command:

1. Builds your documentation to the `site/` directory
2. Creates (or updates) a `gh-pages` branch in your repository
3. Pushes the built site to that branch
4. GitHub automatically serves the content from the `gh-pages` branch

Your documentation will be available at:

```
https://<username>.github.io/dev_tutorial/
```

For example, this documentation is hosted at: [https://mbercx.github.io/softdev-101/](https://mbercx.github.io/softdev-101/)

!!!note "First time setup"

    The first time you deploy, you may need to enable GitHub Pages in your repository settings:

    1. Go to your repository on GitHub
    2. Click **Settings** → **Pages**
    3. Under "Source", select the `gh-pages` branch
    4. Click **Save**

    After a few minutes, your documentation will be live!

!!!warning "Be careful with `gh-deploy`"

    The `gh-deploy` command force-pushes to the `gh-pages` branch, overwriting its history.
    This is usually fine since the `gh-pages` branch only contains built documentation, not source code.
    However, make sure you're in the right repository before deploying!
