# Tests

## What

Tests are code that verifies your source code works as expected.
They automatically check that functions produce correct outputs for given inputs, handle edge cases properly, and behave correctly when things go wrong.

Common types of tests include:

- **Unit tests**: Test individual functions or methods in isolation.
- **Integration tests**: Test how different parts of your code work together.
- **Regression tests**: Ensure bugs that were fixed don't come back.

## Why

Testing serves several critical purposes:

**Carefree development**: With good tests, you can confidently change your code knowing that if you break something, the tests will catch it.

**Catch bugs early**: Tests help you find problems before your code reaches users (or before your paper is published).
It's much cheaper to fix a bug during development than after deployment.

**Prevent regressions**: Once you fix a bug, write a test for it.
This ensures the same bug doesn't sneak back in during future changes.

!!!example "Real-world scenario"

    You've written a Python script to analyze experimental data for your research.
    It works correctly but takes 30 minutes to run, so you want to make it faster.

    You manage to make it run in 3 minutes - great! But how do you know it still produces the same results?

    Without tests, you'd need to manually compare outputs, check figures visually, and hope you didn't introduce subtle bugs during optimization.
    With tests that verify your code produces correct results for known inputs, you can confidently run your test suite and know within seconds whether your optimizations broke anything.

## How

