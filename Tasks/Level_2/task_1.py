# This is day 5 of my Internship.

"""
Task:
Create a basic calculator using Python
"""

def calculator(num1: int, num2: int, op: str) -> int:
    _result = 0

    switch = {
        "+": lambda num1, num2: num1 + num2,
        "*": lambda num1, num2: num1 * num2,
        "/": lambda num1, num2: num1 / num2,
        "%": lambda num1, num2: (num1 / num2) * 100,
        "-": lambda num1, num2: (num1 - num2),
    }

    operation = switch.get(op)

    if operation is None:
        return 0

    _result = operation(num1, num2)
    return _result


calculat = True

while calculat:
    num1 = int(input("Enter first number to calculate: "))
    num2 = int(input("Enter second number to calculate: "))
    op = str(input("Chhose oprater (+, -, *, /, %): "))

    if num1 < num2:
        num1, num2 = num2, num1

    result = calculator(num1, num2, op)

    print(round(result, 2))

    comm = str(input("Enter c to exit, Enter to Contineu: "))

    if comm == "c":
        calculat = False
