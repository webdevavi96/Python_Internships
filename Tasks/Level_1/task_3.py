# This is day 3 of my Python Developer Internship. In today's task, I have to create a function to validate emails with '@' and a domain name eg; gmail.com, yahoo.com, hotmail.com.

_validMail = ("@gmail.com", "@yahoo.com", "@hotmail.com")


def validate_emial(email: str) -> bool:
    _isValid = False

    # Checking if user haven't provided email, will return False.
    if not email:
        return _isValid

    # Converting email to lower case.
    _email = email.lower()

    # Validating email address.
    if _email.endswith(_validMail):
        _isValid = True

    # Returning True or False.
    return _isValid


# Taking user input
user_input = str(input("Enter email address to validate: "))

if validate_emial(user_input):
    print(f"{user_input} is a Valid email.")

else:
    print(f"{user_input} is an Invalid email.")
    print(f"Valid emails must contain one of these: {_validMail}")


# print(validate_emial("example.com"))
# print(validate_emial("example@gmail.com"))
# print(validate_emial("example@hotmail.com"))
# print(validate_emial("example@yahoo.com"))
