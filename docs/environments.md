# Python environments

## What

A Python virtual environment is an isolated workspace that contains a specific Python interpreter (binary) along with its own set of installed packages and dependencies.
Each environment is isolated, meaning packages installed in one environment don't affect others.

## Why

The main reason to use virtual environments is to avoid _dependency conflicts_: different projects often require different versions of the same package.

!!!example "Real-world scenario"

    Imagine you're maintaining two projects: Project A requires `numpy==1.19.0` and Project B needs `numpy==1.24.0`.
    Without environments, you'd have to constantly uninstall and reinstall numpy when switching between projects.
    With environments, each project has its own isolated numpy version, and switching is seamless.

Typically, you want to avoid installing _anything_ within your "global"/"system" environment.
Cleaning this up is much more involved than simply deleting a virtual environment and starting over.

## How

### Creating environments

There many tools out there for creating and managing environments in Python (arguably _too_ many).
For this workshop, we'll use the `venv` module, which is part of the standard library.
The main reason is that it's instructive: it's easier to understand how environments work, and many other tools are built on top of `venv`.

A very useful command in figuring out the Python interpreter/instance/binary you are working with is `which`:

=== "macOS/Linux"

    ```
    which python3
    ```

=== "Windows"

    ```
    where python3
    ```

This will point to the first Python binary in your `PATH`.
If you are not working in a virtual environment, this will typically be your system Python instance.
For example, in my case the command returns

```console {.no-copy}
/usr/bin/python3
```

Let's create a new virtual environment!
If you are still in your `test-repo` directory, navigate up one level to get back to your `softdev-workshop` directory:

```
cd ..
pwd
```

```console {.no-copy}
/path/to/your/softdev-workshop
```

The `venv` module can be run as a script using the `-m` option.
To create a virtual environment in the `.my_env` directory, run:

```
python3 -m venv .my_env
```

!!!info

    Running the `venv` module with `-m`, it behaves much like any command line tool.
    To see its usage, run:

    ```
    python3 -m venv --help
    ```

Time to _activate_ the virtual environment!

=== "`bash`/`zsh`"

    ```
    source .my_env/bin/activate
    ```

=== "`fish`"

    ```
    source .my_env/bin/activate.fish
    ```

=== "Windows"

    TODO

Typically, your prompt will be adapted, adding `(.my_env)` somewhere to indicate you are working "inside the `.my_env` environment".
To verify this, let's see what Python instance we're working with:

=== "macOS/Linux"

    ```
    which python3
    ```

=== "Windows"

    ```
    where python3
    ```

This should now return a path inside the `bin` subdirectory of the virtual environment directory:

```console {.no-copy}
/path/to/your/softdev-workshop/.my_env/bin/python3
```

### Installing packages

We've created and activated our virtual environment, but how do we install packages in it?
For this workshop, we'll use [`pip`](https://pip.pypa.io/en/stable/), which is installed by default in every virtual environment created with `venv`.
Let's first make sure we are working with the `pip` binary from our virtual environment:

=== "macOS/Linux"

    ```
    which pip
    ```

=== "Windows"

    ```
    where pip
    ```

Which should once again return a path within your environment directory:

```console {.no-copy}
/path/to/your/dir/.my_env/bin/pip
```

!!!warning "Important"

    If the command above does **not** return the `pip` binary corresponding to your environment, you will not be installing packages in it when using `pip install`!
    Make sure you have activated your environment as per the instructions above.

Let's install our first package!

```
pip install cowsay
```

If all goes well, you should see that v6.1 of the package is successfully installed: 

```console {.no-copy}
Collecting cowsay
  Downloading cowsay-6.1-py3-none-any.whl (25 kB)
Installing collected packages: cowsay
Successfully installed cowsay-6.1
```

??? warning "Wait, I'm getting a WARNING!"

    You likely will get a warning regarding your `pip` version being outdated:

    ```
    WARNING: You are using pip version 21.2.4; however, version 25.3 is available.
    You should consider upgrading via the '/path/to/your/dir/.my_env/bin/python3 -m pip install --upgrade pip' command.
    ```

    For the material in this workshop, you need at least `pip>=21.3`.
    If the reported `pip` version is older, follow the instructions to upgrade it.

Let's have the cow spit some facts:

```
cowsay -t "Python is awesome!"
```

As you can see, the `cowsay` package ships a cute little command-line interface (CLI) with its installation.
Try finding the location of this command again.

Finally, let's look at the `list` of packages we have installed in our virtual environment:

```
pip list
```

```console {.no-copy}
Package    Version
---------- -------
cowsay     6.1
pip        25.3
setuptools 58.0.4
```

As mentioned, `pip` is automatically installed in every virtual environment created with `venv`, whereas `cowsay` we installed afterwards with `pip`.
Finally, `setuptools` is a package that helps you build and distribute Python packages, but we don't need to go into that here.

!!!tip "A PEP a day keeps the doctor away"

    Can't get enough of virtual environments?
    Read the original Python Enhancement Proposal (PEP) that introduced them into the standard library: [PEP 405](https://peps.python.org/pep-0405/).

---

With your environment set up and ready to install packages, it's time to learn how to structure your own Python code as a package.
**Next up: [Packages](packages.md)**
