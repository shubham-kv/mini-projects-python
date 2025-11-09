import argparse
from calc.repl import repl
from calc.output import print_result


def build_arg_parser():
    parser = argparse.ArgumentParser(description="A simple CLI calculator")

    parser.add_argument("x", type=float, nargs="?", help="First number")
    parser.add_argument(
        "operator",
        nargs="?",
        choices=["+", "-", "*", "**", "/", "//", "%"],
        help="Operation to perform",
    )
    parser.add_argument("y", type=float, nargs="?", help="Second number")

    return parser


def main():
    parser = build_arg_parser()
    args = parser.parse_args()

    if all([args.x, args.operator, args.y]):
        print_result(args.x, args.operator, args.y)
        return

    repl()
