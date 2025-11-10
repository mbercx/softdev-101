# ⚙️ Setup

## Before the workshop

To get up and running quickly, please make sure you have the following ready for the workshop:

1. Bring a laptop!
2. A working Python binary for your OS, version 3.9 or above.
   You can find a guide for various operating systems [here](https://realpython.com/installing-python/#macos-how-to-check-or-get-python).
3. A [GitHub](https://github.com/) account.
4. Have [`git`](https://git-scm.com/) installed on your system.
5. A code editor.
   My preferred option is [VSCode](https://code.visualstudio.com/).

### GitHub authentication

For some parts of the workshop, you'll need to be able to authenticate to GitHub from the terminal.
If you don't know how to do this, the easiest is to use a _token_:

1. Go to GitHub → Click on your profile avatar (top right) → Settings → Developer settings (bottom) → Personal access tokens → Tokens (classic).
2. Click "Generate new token" → "Generate new token (classic)".
3. Give it a description in the "Note" (e.g., "Software development workshop").
4. Select scopes: check **both** "repo" and "workflow".
5. Click "Generate token" at the bottom and copy the token.

Whenever you need to authenticate to GitHub (e.g. when you `push` to your remote), you can use this token as your password.

!!!warning

    Be sure to copy and save the token somewhere **safe**!

!!!info "Operating System"

    You can use your preferred operating system, but I have no experience with Windows.
    If you are using Windows, it may be a good idea to install [WSL](https://learn.microsoft.com/en-us/windows/wsl/install).
    I'll try to also show the Powershell equivalent of each command, but these don't always exist, and I may forget some here and there.
