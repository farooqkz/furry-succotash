#!/usr/bin/python3

if __name__ == "__main__":
    n = int(input("Please enter a positive number(some more text to make a long string and cause failure of linting: "))
    for i in range(n):
        for j in range(i):
            print("=" * j * h) # usage of an undefined variable "h"

    print("WELL DONE!")
