from random import randint


def generator(text, sep=" ", option=None):
    try:
        assert type(text) == str, "ERROR"
        assert type(sep) == str and len(sep), "ERROR"
        assert option in [None, "shuffle", "ordered", "unique"], "ERROR"

        array = text.split(sep)

        if option is None:
            for elm in array:
                yield elm

        elif option == "shuffle":
            for i, _ in enumerate(array):
                ri = randint(i, len(array) - 1)
                array[i], array[ri] = array[ri], array[i]
                yield array[i]

        elif option == "ordered":
            for elm in sorted(array):
                yield elm

        elif option == "unique":
            words = set()
            for elm in array:
                if elm not in words:
                    words.add(elm)
                    yield elm

    except AssertionError as E:
        print(E)
