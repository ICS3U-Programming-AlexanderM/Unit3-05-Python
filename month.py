#!/usr/bin/env python3

# Created by: Alexander Matheson
# Created on: Dec 12, 2021
# This program gets the user to enter a number.
# It then tells them the month that corresponds to that number.


# compare number to cases
def compare(user_number):
    cases = {
        1: lambda: print("The month corresponding to {} is January"
                         . format(user_number)),
        2: lambda: print("The month corresponding to {} is February"
                         . format(user_number)),
        3: lambda: print("The month corresponding to {} is March"
                         . format(user_number)),
        4: lambda: print("The month corresponding to {} is April"
                         . format(user_number)),
        5: lambda: print("The month corresponding to {} is May"
                         . format(user_number)),
        6: lambda: print("The month corresponding to {} is June"
                         . format(user_number)),
        7: lambda: print("The month corresponding to {} is July"
                         . format(user_number)),
        8: lambda: print("The month corresponding to {} is August"
                         . format(user_number)),
        9: lambda: print("The month corresponding to {} is September"
                         . format(user_number)),
        10: lambda: print("The month corresponding to {} is October"
                          . format(user_number)),
        11: lambda: print("The month corresponding to {} is November"
                          . format(user_number)),
        12: lambda: print("The month corresponding to {} is December"
                          . format(user_number)),
    }
    cases.get(user_number, lambda: print("{} does not correspond to a month"
              . format(user_number)))()


def main():
    # this function checks the user's number

    # get input
    user_number = int(input("Enter your number: "))
    print("")

    compare(user_number)


if __name__ == "__main__":
    main()
