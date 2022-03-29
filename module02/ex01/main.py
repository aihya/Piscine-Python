def what_are_the_vars(*args, **kwargs):
    """Add new attributes to an instance of the class ObjectC.
    Args:
        *args: Set of arguments without names.
        **kwargs: dictionary of key: value pairs.
    Returns:
        Instance of class ObjectC if all attributes are set.
        Otherwise, return None if an attribute already exist.
    """
    objc = ObjectC()

    # Set 'args' first: Suffix the index of the corresponding arg with 'var_'.
    for i, arg in enumerate(args):
        setattr(objc, 'var_{}'.format(i), arg)

    # Set 'kwargs' second: If 'key' already exist, return None. Otherwise add it to the set of attributes.
    for key in kwargs.keys():
        if getattr(objc, key, None) is not None:
            return None
        setattr(objc, key, kwargs[key])

    return objc


class ObjectC(object):
    def __init__(self):
        pass


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    doom_printer(obj)

