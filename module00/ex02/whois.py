import sys

if __name__ == "__main__":
    if len(sys.argv[1:]) == 0:
        exit(0)
    try:
        arg = sys.argv[1]
        assert len(sys.argv[1:]) <= 1, "more than one argument is provided"
        assert (arg[0] in "+-" and arg[1:].isnumeric()) or arg.isnumeric(), "argument is not integer"

        if int(arg) == 0:
            print("I'm Zero")
        elif int(arg) % 2 == 0:
            print("I'm Even")
        else:
            print("I'm Odd")
    except AssertionError as e:
        print("{}: {}".format(type(e).__name__, e))
