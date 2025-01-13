#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # On réduit n à chaque itération pour éviter une boucle infinie
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <number>")
        sys.exit(1)

    try:
        input_number = int(sys.argv[1])
        if input_number < 0:
            print("Error: Factorial is not defined for negative numbers.")
        else:
            f = factorial(input_number)
            print(f)
    except ValueError:
        print("Error: Please provide a valid integer.")