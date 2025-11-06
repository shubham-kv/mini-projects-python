import os
import atexit

try:
    import readline
except ImportError:
    import pyreadline3 as readline  # Windows fallback

from calc.output import print_result


def setup_history():
    history_file = os.path.expanduser("~/.calc_repl_history")

    if os.path.exists(history_file):
        readline.read_history_file(history_file)

    atexit.register(readline.write_history_file, history_file)


def repl():
    setup_history()
    print("Calculator REPL mode. Type 'quit' or CTRL+D to quit.")

    while True:
        try:
            cmd = input(">>> ").strip()
        except (KeyboardInterrupt, EOFError):
            print()
            break

        if cmd in ["q", "quit"]:
            print()
            break

        expr = [word for word in cmd.split(" ") if word]

        if len(expr) < 3:
            continue

        try:
            x, y = float(expr[0]), float(expr[2])
        except ValueError:
            continue

        print_result(x, expr[1], y)
