from decimal import DivisionByZero
import sys

def isnum(string):
    if len(string) and string[0] in "+-":
        if string[1:].isnumeric():
            return True
        return False
    if len(string) and string.isnumeric():
        return True
    return False

if __name__ == "__main__":
    try:
        assert len(sys.argv[1:]) <= 2, "too many arguments\n"
        assert len(sys.argv[1:]) == 2, "not enough arguments\n"
        assert isnum(sys.argv[1]) and isnum(sys.argv[2]), "only numbers\n"

        a, b = int(sys.argv[1]), int(sys.argv[2])
        print("Sum:        {}".format(a + b))
        print("Difference: {}".format(a - b))
        print("Product:    {}".format(a * b))
        print("Quotient:   {}".format(a / b))
        print("Remainder:  {}".format(a % b))

    except AssertionError as e:
        print("InputError: {}".format(e))
        print("Usage: python3 operations.py <number1> <number2>")
        print("Example:\n\tpython3 operations.py 10 3")
    except ZeroDivisionError:
        print("Quotient:   ERROR (div by zero)")
        print("Remainder:  ERROR (modulo by zero)")
