#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on May 2021
# This program calculates the volume of a triangular prism

import string


def calculate_volume(base, height, length):
    # Gets volume

    # Process and output
    volume = (base * height) / 2 * length

    return volume


def main():
    # This function calls calculate_volume

    # Input
    base_input = str(input("Enter base of a triangular prism (cm): "))
    height_input = str(input("Enter height (cm): "))
    length_input = str(input("Enter length (cm): "))

    # Process and output
    try:
        base_as_float = float(base_input)
        height_as_float = float(height_input)
        length_as_float = float(length_input)
        prism_volume = calculate_volume(
            base_as_float, height_as_float, length_as_float
        )
        if prism_volume > 0:
            print("The volume of the prism is {} cm³.".format(prism_volume))
    except Exception:
        print("Invalid dimensions")
    print("\nDone.")


if __name__ == "__main__":
    main()
