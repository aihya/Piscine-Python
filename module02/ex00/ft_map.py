def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Returns:
    An iterable.
    None if the iterable can not be used by the function.
    """

    if not callable(function_to_apply):
        raise TypeError("'{}' object is not callable".format(type(function_to_apply).__name__))
    if not hasattr(iterable, '__iter__'):
        raise TypeError("'{}' object is not iterable".format(type(iterable).__name__))

    # return (function_to_apply(elm) for elm in iterable)
    for elm in iterable:
        yield function_to_apply(elm)


class Map:

    def __init__(self, function, iterable):
        self.index = 0
        self.iterable = iterable
        self.function = function

    def __iter__(self):
        return self

    def __next__(self):
        try:
            __next = self.iterable[self.index]
            self.index += 1
            return __next
        except IndexError:
            raise StopIteration
