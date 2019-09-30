#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: September 2019
# This program calculates the area of a determined (length) regular octagon.


import math


def main():
    # main function

    # Input
    length = int(input("Enter the length of the regular octagon (cm): "))

    # process
    area = (2 * (1 + (math.sqrt(2))) * length * length)

    # output
    print("The area for this octagon is: {0}cm^2".format(area))


if __name__ == "__main__":
    main()
