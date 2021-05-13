#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: May 2021
# This program adds up positive integers
#    with numbers inputted from the user

def main():
    # this function adds up positive numbers

    loop_counter = 0

    # input
    positive_string = input("Enter an positive integer: ")

    # process

    # output
    try:
        positive_integer = int(positive_string)

        if positive_integer < 0:
            print("Enter a positive number")
        else:
            sum = 0
            loop_counter = 0

            # https://www.javatpoint.com/python-sum-natural-numbers
            while loop_counter <= positive_integer:
                sum += loop_counter
                loop_counter += 1

            print("The sum of all positive number from 1 to {} is {}"
                  .format(positive_integer, sum))
    except Exception:
        print("{} is not an number".format(positive_string))
    finally:
        print("\nThanks for trying")


if __name__ == "__main__":
    main()
