#!/usr/bin/env python3

# Created by: Dahrio Francois
# Created on: May 2022
# This program calculates fahrenheit from celsius


def celsius_to_fahrenheit():
    # This function calculates calculates fahrenheit from celsius
    try:
        # input
        celsius = int(input("Enter temperature in °C: "))

        # process
        fahrenheit = celsius * 9 / 5 + 32

        # output
        print("")
        print("Temperature is {} °F.".format(fahrenheit))
        print("")
        print("Done")
    except Exception:
        print("\nThis was not an integer, please enter an integer")


def main():
    # This calls other functions

    # call functions
    celsius_to_fahrenheit()


if __name__ == "__main__":
    main()
