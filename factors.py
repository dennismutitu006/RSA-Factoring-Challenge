#!/usr/bin/python3
import math
import sys

def factorize(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return i, number // i
    return None, None

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        for line in file:
            number = int(line.strip())
            factor1, factor2 = factorize(number)
            if factor1 is not None and factor2 is not None:
                print(f"{number}={factor1}*{factor2}")

if __name__ == "__main__":
    main()

