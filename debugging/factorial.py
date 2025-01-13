#!/usr/bin/python3
import sys

MAX_N = 1000  # Limite supérieure pour éviter les calculs trop longs

def factorial(n, show_steps=False):
    """
    Calculate the factorial of a number with optional step-by-step display.
    
    Args:
        n (int): The number to calculate factorial for
        show_steps (bool): Whether to show calculation steps
    
    Returns:
        int: The factorial of n
    
    Raises:
        ValueError: If n is negative or greater than MAX_N
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n > MAX_N:
        raise ValueError(f"Number too large. Maximum allowed is {MAX_N}")
    
    result = 1
    if show_steps:
        print(f"Calculating {n}!")
        if n == 0:
            print("0! is defined as 1")
        else:
            print(f"Starting with {result}")
    
    while n > 1:
        result *= n
        if show_steps:
            print(f"× {n} = {result}")
        n -= 1
    
    return result

def print_usage():
    """Print program usage information."""
    print("Usage: ./factorial.py <number> [-s|--steps]")
    print("Options:")
    print("  -s, --steps    Show calculation steps")
    print("Example:")
    print("  ./factorial.py 5 --steps")

if __name__ == "__main__":
    try:
        # Vérifier le nombre minimum d'arguments
        if len(sys.argv) < 2:
            print_usage()
            sys.exit(1)

        # Vérifier si l'option --steps est présente
        show_steps = "-s" in sys.argv or "--steps" in sys.argv
        
        # Obtenir le nombre (premier argument qui n'est pas une option)
        n = None
        for arg in sys.argv[1:]:
            if not arg.startswith("-"):
                try:
                    n = int(arg)
                    break
                except ValueError:
                    print(f"Error: '{arg}' is not a valid integer")
                    sys.exit(1)
        
        if n is None:
            print("Error: No number provided")
            print_usage()
            sys.exit(1)

        # Calculer et afficher le résultat
        result = factorial(n, show_steps)
        if show_steps:
            print(f"\nFinal result {n}! = {result}")
        else:
            print(result)

    except ValueError as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nCalculation interrupted by user")
        sys.exit(1)