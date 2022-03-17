import sys

def isnumber(num):
    if len(num) > 0 and num[0] in '+-':
        if num[1:].isnumeric():
            return True
    elif len(num) > 0 and num.isnumeric():
        return True
    return False

def filterwords(words, n):
    alnums = ''.join([c for c in words if c.isalnum() or c == ' '])
    return [w for w in alnums.split() if len(w) > n]


if __name__ == "__main__":
    try:
        assert len(sys.argv[1:]) == 2, "ERROR"
        assert isnumber(sys.argv[2]), "ERROR"
        assert int(sys.argv[2]) >= 0, "ERROR"

        print(filterwords(sys.argv[1], int(sys.argv[2])))

    except AssertionError as e:
        print(e)
