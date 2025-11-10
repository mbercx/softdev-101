# Version control

## What

A version control system (VCS) is a tool that tracks changes to a file or set of files over time so that you can recall specific versions later.
There are many VCS out there, but the leading one is `git`.
Unless you need to learn a specific VCS because your collaborators use it, I would stick with `git`.

## Why

Version control serves several critical purposes:

**History and recovery**: Track every change made to your code, who made it, and when.
If something breaks, you can identify exactly what changed and revert to a working version.

**Collaboration**: Multiple people can work on the same codebase simultaneously without overwriting each other's changes.
Git helps merge contributions and resolve conflicts.

**Code review**: Changes can be reviewed before being merged into the main code, improving quality and knowledge sharing across the team.

!!!example "Real-world scenario"

    Imagine you have a piece of working code, but want to make some changes.
    It's late, you're out of coffee, and after working for half an hour you realise that you've made several mistakes, and **the code is completely broken**.
    However, you've already saved your file with your changes, and you don't have a backup.

    - How would you know what you have changed to the code?
    - How would you go back to the version that worked?

    Running 'undo' repeatedly might work if you catch it immediately, but what if you closed the editor or worked across multiple files?
    You could spend hours reconstructing the code.
    With `git`, you can see exactly what changed with `git diff` and revert to the working version with a single command.

!!!note "Glossary"

    We'll be using a lot of lingo in this workshop that you might not be familiar with.
    If you find yourself wondering what e.g. a version control system (VCS) is again, [have a look at the glossary](glossary.md).

## How

Git is a massive beast, and learning how to use it properly is beyond the scope of this introduction.
I would _highly_ recommend that you simply sit down at some point and read [the first three chapters of the Git book](https://git-scm.com/book/en/v2).
Here, we'll simply show some basic `git` commands to get you up and running, and go through the rest of the workshop material.

Start by creating an empty directory:

```
mdkir test
cd test
```

To start tracking any changes made to files in this directory, run

```
git init
```

Great!
Let's check our status:

```
git status
```

```console {.no-copy}
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

We can see three pieces of information:

1. We're working on the `main` _branch_.
   Branches are a very important concept in `git`, and they get [a whole chapter in the Git book](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell).
   We'll come back to why we use them later.
2. There are no _commits_ yet.
   Commits are a snapshot of your codebase, but we haven't added any code yet!
3. There is nothing _to_ commit.
   Again: we haven't added any code yet, so that makes sense.

So let's add some code!

```
echo 'print("Hello world!")' > module.py
```

Let's check our status again with `git status`.
We can see something has changed:

```console {.no-copy}
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        module.py
```

The `module.py` file is now in the list of "untracked" files.
By default, `git` will not track your changes; you need to tell it to do so!
The message in brackets hints as to how:

```
git add module.py
```

It seems like nothing has happened, but running `git status` again:

```console {.no-copy}
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   module.py
```

We can see that the `module.py` file is now a "new file" which is "to be committed".
Time to do our first commit:

```
git commit -m 'Initial commit'
```

```console {.no-copy}
[main (root-commit) 333f360] Initial commit
 1 file changed, 1 insertion(+)
 create mode 100644 module.py
```

We have made our first commit on the `main` branch, i.e. the "root commit".
Some more details:

- `333f360` is the short form of the commit SHA (Secure Hash Algorithm).
  It can be used to reference to commits with various `git` commands.
- Using the `-m, --message` option, we have specified a commit _message_ (`Initial commit`).
  A commit message can be used to explain the changes, and good commit messages are an essential component of good development practises.
- We've changed 1 file, where we added 1 line (insertion).
- Since it's a new file, `git` "created" it with mode `100644` (`100`: regular file; `644` = UNIX file permissions).

What if we change the contents of the file?
Let's add another line of code:

```
echo 'print("How are you?")' >> module.py
```

Running `git status` again:

```console {.no-copy}
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   module.py

no changes added to commit (use "git add" and/or "git commit -a")
```

We can now see that `git` noticed that we _modified_ the `module.py` file.
To see the changes we can use `git diff`:

```
git diff
```
```console {.no-copy}
diff --git a/module.py b/module.py
index f1a1813..dd87b53 100644
--- a/module.py
+++ b/module.py
@@ -1 +1,2 @@
 print("Hello world!")
+print("How are you?")
```

Let's stage (`add`) and commit our changes:

``` 
git add module.py
git commit -m 'Add question'
```
```console {.no-copy}
[main 49451af] Add question
 1 file changed, 1 insertion(+)
```

!!!tip Committing all tracked changes

    You may be wondering why you have to `git add` a file before committing its changes.
    In many cases, you might not want to commit _all_ the changes you've made in the repository.
    However, you can use the `-a, --all` option to do this, e.g.:

    ```
    git commit -a -m 'Add question'
    ```

Finally, let's have a look at the Git log:

```
git log
```

```console {.no-copy}
commit 49451af53c90be75918eb86c41491ec452bf4dfa (HEAD -> main)
Author: Marnik Bercx <mbercx@gmail.com>
Date:   Fri Nov 7 15:34:31 2025 +1000

    Add question

commit 333f36023da1dbce96cdcb19b48ad52adca4c58a
Author: Marnik Bercx <mbercx@gmail.com>
Date:   Fri Nov 7 15:17:41 2025 +1000

    Initial commit
```

!!!info "`git`/GitHub workshop at UQ"

    At UQ, Ben Roberts also runs a workshop on using `git` and GitHub which goes into much more detail than this tutorial.
    If you're curious, [have a look at the workshop material](https://github.com/benroberts999/git-workshop).

---

Now that you understand version control basics, let's move on to managing Python dependencies and isolated workspaces.
**Next up: [Python environments](environments.md)**
