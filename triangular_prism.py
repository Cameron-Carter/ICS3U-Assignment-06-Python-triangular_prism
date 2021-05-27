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

    # Function call
    prism_volume = calculate_volume(base_input, height_input, length_input)

    # Process and output
    if prism_volume == -1:
        print("Invalid dimensions.")
    else:
        print("The volume of the prism is {} cm³.".format(prism_volume))
    print("\nDone.")


if __name__ == "__main__":
    main()
