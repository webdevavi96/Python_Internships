# This is day 4 of my Internship.
# Task 4:
"""
I have to create a function to generate fbonacci series based on input.
"""


n = int(input("Enter the number to generate fabonacci form: "))


def fabonacci_seq(n):
    if n == 0 or n == 1:
        return n

    if n == 2:
        return 1

    _curr = 0
    _next = 1
    _sum = 0
    _series = [0,1]

    for _ in range(1, n):
        _sum = _curr + _next
        _series.append(_sum)

        _curr = _next
        _next = _sum

    return _series


print(fabonacci_seq(n))
