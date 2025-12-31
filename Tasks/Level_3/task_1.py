# This is day 8 of my internship.

"""
Task: File Manipulation
Write a Python program that reads a text
file and counts the occurrences of each
word in the file. Display the results in
alphabetical order along with their
respective counts.
"""

filename = "file.txt"

print("----------------------------------")


def file_manipulation(file):
    if file == "" or not file:
        return

    words_count = {}

    try:
        with open(file, "r", encoding="utf-8") as f:
            for ws in f:
                ws = ws.lower().strip()

                words = ws.split()

                for w in words:
                    w = w.strip(".,!?;:\"'()[]{}")

                    if w:
                        words_count[w] = words_count.get(w, 0) + 1

    except FileNotFoundError as e:
        print("File not found: ", str(e))

    except Exception as e:
        print("Exception occured while reading the file: ", str(e))

    for count in sorted(words_count):
        print(f"{count}: {words_count[count]}")
        


file_manipulation(filename)