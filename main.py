#!/usr/bin/python3

if __name__ == "__main__":
    n = int(input("Please enter a positive number: "))
    for i in range(n):
        for j in range(i):
            print("=" * j)

    print("WELL DONE!")
