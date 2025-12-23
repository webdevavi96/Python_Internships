# This is day 2 of my Python internship. In today's task, I have to create a function to convert temprature from one unit to another.


"""
Task 2: Temprature Converter: Create a Python program that converts
temperatures between Celsius and
Fahrenheit. Prompt the user to enter a
temperature value and the unit of
measurement, and then display the
converted temperature.
"""

import math

units = {1: "Celsius", 2: "Fahrenheit", 3: "Kelvin"}

print(units)

unit_from = int(input("convert From: "))
unit_to = int(input("Convert To: "))
temperature = float(input("Enter Temperature: "))
new_temperature = 0


def convert_temprature(unit_from, unit_to, temperature):

    if unit_from not in units or unit_to not in units:
        raise ValueError("Invalid unit selection")

    from_unit = units[unit_from]
    to_unit = units[unit_to]

    if from_unit == to_unit:
        return temperature

    conversions = {
        ("Celsius", "Fahrenheit"): lambda t: (t * 9 / 5) + 32,
        ("Celsius", "Kelvin"): lambda t: t + 273.15,
        ("Fahrenheit", "Celsius"): lambda t: (t - 32) * 5 / 9,
        ("Fahrenheit", "Kelvin"): lambda t: (t - 32) * 5 / 9 + 273.15,
        ("Kelvin", "Celsius"): lambda t: t - 273.15,
        ("Kelvin", "Fahrenheit"): lambda t: (t - 273.15) * 9 / 5 + 32,
    }

    # Implemented Error handeling for better user experience.

    try:
        return conversions[(from_unit, to_unit)](temperature)

    except KeyError:
        raise ValueError("Conversion is not possible on these values.")

    except KeyboardInterrupt:
        raise ValueError("Existed successfully.")

    except Exception as e:
        print(str(e))


try:
    result = round(convert_temprature(unit_from, unit_to, temperature), 2)  # type: ignore
    print(f"Converted temperature is: {result}{units[unit_to][0]}")

except Exception as e:
    print(str(e))
