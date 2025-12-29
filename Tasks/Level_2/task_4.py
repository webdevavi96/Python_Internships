# This is day 7 of my InternshipTask: Password Strength Checker

"""
Task:
Create a Python function that evaluates
the strength of a password entered by the
user.

Implement checks for factors such as
length, presence of uppercase and
lowercase letters, digits, and special
characters."""


password = str(input("Enter password to check is that a valid password or not: "))
valid_pass = {
    "special": ["@", "!", "#", "%", "&"],
    "caps": [
        "A",
        "S",
        "D",
        "F",
        "G",
        "H",
        "J",
        "K",
        "L",
        "Z",
        "X",
        "C",
        "V",
        "B",
        "N",
        "M",
        "Q",
        "W",
        "E",
        "R",
        "T",
        "Y",
        "U",
        "I",
        "O",
        "P",
    ],
    "smcaps": [
        "a",
        "d",
        "s",
        "f",
        "g",
        "h",
        "j",
        "k",
        "l",
        "z",
        "x",
        "c",
        "v",
        "b",
        "n",
        "m",
        "q",
        "w",
        "e",
        "r",
        "t",
        "y",
        "u",
        "i",
        "o",
        "p",
    ],
    "nums": ["1", "2", "3", " 4", "5", "6", "7", "8", "9", "0"],
}


def is_valid_pass(password: str) -> bool:
    _valid = False

    for sp in range(len(valid_pass["special"])):
        for cp in range(len(valid_pass["caps"])):
            for sm in range(len(valid_pass["smcaps"])):
                for nm in range(len(valid_pass["nums"])):
                    if (
                        password.__contains__(valid_pass["special"][sp])
                        and password.__contains__(valid_pass["smcaps"][sm])
                        and password.__contains__(valid_pass["caps"][cp])
                        and password.__contains__(valid_pass["nums"][nm])
                    ):
                        _valid = True
                    else:
                        break

    return _valid


if is_valid_pass(password):
    print("You have a strong password.")

else:
    print(
        f"Your password isn't strong! A valid password must contains atleast one of these: {valid_pass['special']}, {valid_pass['caps'], valid_pass['smcaps']} and {valid_pass['nums']}"
    )
