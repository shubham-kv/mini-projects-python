
# Calculator CLI

A small command-line calculator that performs basic arithmetic (+, - , *, /,
etc).

## Features

1. Takes command-line input in the form `<x> <operation> <y>` and prints
   result.
2. Interactive REPL with repl history.

## Installation

```bash
pip install git+https://github.com/shubham-kv/mini-projects-python.git#egg=calc_cli\&subdirectory=02_calc_cli
```

## Usage

```bash
% calc 1 + 2 
3.0

% calc 3 - 1
2.0

% calc 4 \* 6
24.0

% calc 4 \/ 6
0.6666666666666666

% calc 17 % 3
2.0

% calc 17 \/\/ 3
5.0
```

Escape `*` & `/` characters with a leading `\` so that it doesn't get
picked by your shell.

Running `calc` without any arguments enters into repl mode:

```bash
$ calc
Calculator REPL mode. Type 'quit' or CTRL+D to quit.
>>> 1 + 2
3.0
>>> 3 - 1
2.0
>>> 4 * 6
24.0
>>> 4 / 6
0.6666666666666666
>>> 17 % 3  # Modulo
2.0
>>> 17 // 3 # Floor division
5.0
```

## LICENSE

MIT
