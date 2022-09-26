"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
        halfLength = len(numbers)/2
        if (halfLength % 2 == 0):
            print(numbers[(numbers//2 + numbers//2+1)/2])
        else:
            print(numbers[halfLength])
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
