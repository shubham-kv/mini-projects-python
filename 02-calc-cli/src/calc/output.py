from calc.core import add, floor_division, subtract, multiply, divide, modulo, exponent

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "**": exponent,
    "/": divide,
    "//": floor_division,
    "%": modulo,
}


def print_result(x: float, op: str, y: float):
    if op not in operations:
        print(
            "Invalid operator: '%s' (Choose from '+', '-', '*', '**', '/', '//', '%%')!"
            % op
        )
        return

    result: float
    operation = operations[op]

    try:
        result = operation(x, y)
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except OverflowError:
        print("Result too large!")
    else:
        print(result)
