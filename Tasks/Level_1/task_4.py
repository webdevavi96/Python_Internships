# This is day 4 of my Internship.


"""
Task 4:

I have to cereat a function to check whether the string is Palindrom or not.
"""


def is_palindrom(user_input: str) -> bool:
    _user_input = user_input.lower()
    _reversed = _user_input[::-1]
    _is_palindrom = False

    if _reversed == user_input:
        _is_palindrom = True
        return _is_palindrom

    return _is_palindrom


user_input = str(input("Enter a string to check whether it's palindrom or not: "))
result = is_palindrom(user_input)

if result:
    print(f"{user_input} is a palindrom string")

else:
    print(f"{user_input} is not a palindrom string.")
