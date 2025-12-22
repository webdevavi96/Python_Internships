# This is the task - 1 of my Cognifyz Internship. In this task I have to Create a function to take string as input and return the reversed String.


def reverse_string(text: str) -> str:
    reversed_string = ""
    if text:
        reversed_string = text[::-1]
    return reversed_string


text1 = "Hello"
text2 = ""

print(f"text1 is: {reverse_string(text1)}")
print(f"text2 is: {reverse_string(text2)}")
print(f"text2 is: {reverse_string("Revres")}")
