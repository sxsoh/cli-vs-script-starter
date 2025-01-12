# CLI vs Script - Specification Lab

[![build](../../actions/workflows/build.yml/badge.svg)](../../actions/)
![Platforms: Linux, MacOS, Windows](https://img.shields.io/badge/Platform-Linux%20%7C%20MacOS%20%7C%20Windows-blue.svg)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-blue.svg)](https://github.com/psf/black)
[![Commits: Conventional](https://img.shields.io/badge/Commits-Conventional-blue.svg)](https://www.conventionalcommits.org/en/v1.0.0/)
[![Discord](https://img.shields.io/discord/872320492936257537?logo=discord)](https://discord.gg/kjah8MFYbR)

## Introduction

This assignment is about understanding different ways to use Python to
implement and/or run numerical functions.

## Learning Objectives

By completing this assignment, you will:

1. Use git and GitHub to manage source code file changes
2. Use Poetry to run a Command Line Interface implemented in Python
3. Use Python to run a Python script (.py)
4. Use Google Colaboratory to run a Python Notebook (.ipynb)
5. Write in Markdown
6. Meet all gatorgrade specifications

## Quick Links

- Due date: Check Discord or the
  [Assignment Schedule](https://allegheny-college-cmpsc-101-spring-2025.github.io/site/assignments.html)
- Policy on
  [Tokens](https://allegheny-college-cmpsc-101-spring-2025.github.io/site#tokens)
- [#data-structures Discord channel](https://discord.com/channels/877320365825749002/1326565523042992159)
- [Starter repo](https://github.com/allegheny-college-cmpsc-101-spring-2025/cli-vs-script-starter)

## Policy Reminders

Students are reminded to uphold the Honor Code. Cloning this assignment
repository is a commitment to the latter.

For this assignment, you may use class materials, the textbook, notes,
and the internet, including AI, for reference and learning. AI may **not** be
used to generate answers that you submit. All code and writing that are turned
in **must be your own work and your own words**. Copying or otherwise
representing ChatGTP or other AI outputs as your own work or your own words is
not permitted.

Please ask questions freely in Lab, on the #data-structures Discord channel,
TL office hours, instructor office hours, or by opening a GitHub Issue with
@emgraber tagged at least 24 hours before the deadline.

Modifications to the gatorgrade.yml file are not permitted without explicit
instruction.

## Project Details

### Goals

The Python programming language can be used in a variety of ways. Sometimes a
Python Interpreter is used to run python scripts, which are files ending with
`.py`. Sometimes a Python Kernel in a browser is used to run a Python Notebook,
which are files ending with `.ipynb`. Sometimes tools like Poetry can be used to
run command line interfaces (CLIs) that are implemented in the Python
programming language. Despite the differences between these methods, all of them
are capable of running the same numerical functions.

This repository is set up to let you explore how the same numerical functions can
be run in different ways using different methods.

### Running Instructions

As mentioned above, there are several ways to use Python. Read more below!

#### Poetry

If you have cloned this lab, in the cli directory, you will notice poetry's
best friend, the `pyproject.toml`. This cli directory contains the python source
code for a CLI with poetry as the virtual environment manager.

To activate the environment and install all needed packages, type `poetry install`.
In order to use or run anything that is part of a `poetry` environment, the words
`poetry run` must appear first. Thus to run the CLI, the command is `poetry run cli`...
where `cli` is the CLI. CLIs usually need options, and in our case the option is
`option` (to help you remember that term) and the value can be either
`even_odd_checks` or `floating_point_operations`.

A full call to the CLI would look like this: `poetry run cli --option even_odd_checks`

#### Scripts

In the `script` directory, there is a python file `main.py`. Please explore the
file and note the similarities and differences between `main.py` in `script` and
`main.py` in `cli`.

`main.py` in the script directory contains all the logic to run the same
numerical computations as the CLI, but the method for running the code is
different. Instead of calling a CLI using the Poetry virtual environment, you
will use a Python Interpreter without Poetry at all by typing `python main.py`
from within the script directory.

Follow any prompts by answering `even_odd_checks` or `floating_point_operations`
after `python main.py`.

#### Notebooks

Python notebooks are a bit like editable python scripts that run in a browser
using a python kernel (similar to an interpreter). The python kernel has a
memory that is built-up and updated over time, as the kernel runs.

Python notebooks are used for working with smaller bits of code that may need
to be edited a lot, or tested in small pieces. Notebook is divided into cells,
which contain either Markdown (for labeling and nice looking text), or python
source code. A python kernel runs in the background and awaits python commands
that are dynamically run by the programmer in a cell-by-cell manner.

Whenever a cell with source code is run within a notebook, the symbols
(variables, function names, etc) that are defined or updated within that cell
are **retained** in the kernels memory. If multiple cells use the same symbols,
the kernel will simply read off the previously stored values assigned to the
symbols without warning. It is therefore up to the programmer to keep track of
what cells have already been run, what symbols may already be in memory, and in
what order to run the cells.

Since CMPSC101 course notes are often presented in Google Colaboratory (python
notebooks), you should open the `main.ipynb` notebook located in the `notebook`
directory in Google Colab. In order to do this, you must upload the notebook
into your own Google Drive. After it is uploaded, double clicking on the file
name `main.ipynb` should open it up in Colab.

Run the cells one at a time, and follow any prompts by answering
`even_odd_checks` or `floating_point_operations`.

### Expected Output for CLI, script, and notebook

The code for the command line interface is already implemented. From the cli
directory, running the command `poetry run cli --option even_odd_checks` should
produce the following output.

```shell
~ ~ ~ ~ ~ ~ ~ ~ ~
✨ The value of the cli option is even_odd_checks

✨ I will now being running even_odd_checks
The number of 0 is even!
The number of 10 is even!
The number of 11 is odd!
The number of -10 is even!
The number of -11 is odd!
~ ~ ~ ~ ~ ~ ~ ~ ~
```

The code for the script is already implemented. From the script directory,
running the command `python main.py` and inputting the option `even_odd_checks`
when prompted should result in the following output.

```shell
Please indicate if I should run even_odd_checks or floating_point_operations: even_odd_checks
~ ~ ~ ~ ~ ~ ~ ~ ~
✨ The value of the input is even_odd_checks

✨ I will now being running even_odd_checks
The number of 0 is even!
The number of 10 is even!
The number of 11 is odd!
The number of -10 is even!
The number of -11 is odd!
~ ~ ~ ~ ~ ~ ~ ~ ~
```

The code for the python notebook is already implemented. From the notebook
directory, upload `main.ipynb` into Google Colab. Running the cells
consecutively will produce the following output:

```shell
Please indicate if I should run even_odd_checks or floating_point_operations: even_odd_checks
```

```shell
~ ~ ~ ~ ~ ~ ~ ~ ~
✨ The value of the input is even_odd_checks

✨ I will now being running even_odd_checks
```

```shell
The number of 0 is even!
The number of 10 is even!
The number of 11 is odd!
The number of -10 is even!
The number of -11 is odd!
```

```shell
~ ~ ~ ~ ~ ~ ~ ~ ~
```

### Gatorgrade

The command `gatorgrade --config config/gatorgrade.yml` will check your work. If
your work meets the baseline requirements and adheres to the best practices that
proactive programmers adopt you will see that all the checks pass when you run
`gatorgrade`. The grade for this lab is the gatorgrade score reported in GitHub
Actions. Note, modifications to the gatorgrade.yml file are not permitted without
explicit instruction.

### TODOs

- Explore all the files on your own
- confirm that the output you see matches the expected output using `even_odd_checks`
- make sure you can understand what happens when you use
  `floating_point_operations` in the CLI, the script, and the notebook instead
  of `even_odd_checks`.
- Answer all the questions in the writing reflection.
- Run gatorgrade to check that all the linters and formatters pass.
- Perform any linting that may be needed by using the helper tasks described
  below, and your error-reading skills.
- Submit your work, and check the GitHub actions!

Note: Please ensure that you know how to submit work to GitHub using git in
the terminal.

- Open a terminal
- `cd` to the project directory on your computer
- type `git status` to see a list of files you have updated
- type `git add .` to "stage" your files
- type `git commit -m "professional message about changes made"`
- type `git push origin main`
- type your ssh passphrase if requested

### Helper Tasks

Helper tasks are run in the terminal with the poetry environment activated.
The format of the commands are always `poetry run task xyz`...where `xyz`
is the helper task name.

If you study the source code in the `pyproject.toml` file you will see that it
includes the following section that specifies different executable "helper
task" names like `ruff`, `fix`, `ruffdetails`, etc.

```toml
[tool.taskipy.tasks]
```

If you are in the `cli` directory that contains the
`pyproject.toml` file, the helper tasks
make it easy to run commands like `poetry run task ruff` to automatically run
the ruff linter designed to check the Python source code in your program
to confirm that your source code adheres to industry standards for formatting.
You can also use the command `poetry run task fix` to automatically reformat the
source code. `poetry run task ruffdetails` will print out detailed linting errors
that point to exactly what ruff views as a linting error. Make sure to examine
the `pyproject.toml` file for other convenient tasks that you can use to both
check and improve your project!

If your program has
all of the anticipated functionality, you can run the command `poetry run task
test` and see that the test suite produces output like the following.

```shell
collected 4 items

tests/test_cli.py ....
```
