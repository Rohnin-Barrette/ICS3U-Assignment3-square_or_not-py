#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: Sept 2021
# This is a program that calculates the area and perimiter of a
# rectangle with user input. and tells user if it's a square or not


def main():
    # This is a program that calculates the area and perimiter of a rectangle.

    # input
    length = int(input("Enter Length of the rectangle (mm): "))
    width = int(input("Enter width of the rectangle (mm): "))

    # process & output
    if length <= 0 or width <= 0:
        print("Invalid input!!!")
    else:
        area = length * width
        perimeter = 2 * (length + width)
        print("")
        print("Area is {0} mm².".format(area))
        print("Perimeter is {0} mm.".format(perimeter))
    if length == width:
        print("It is a square.")
    else:
        print("It is a rectangle.")


if __name__ == "__main__":
    main()
