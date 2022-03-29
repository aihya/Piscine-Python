def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Returns:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """

    if callable(function_to_apply):
        if hasattr(iterable, '__iter__'):
            if len(iterable) == 0:
                raise TypeError("empty iterable.")
            it = iter(iterable)
            value = next(it)
            for v in it:
                value = function_to_apply(value, v)
            return value
        else:
            raise TypeError("'{}' object is not iterable".format(type(iterable).__name__))
    else:
        raise TypeError("'{}' object is not callable".format(type(function_to_apply).__name__))
