def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Returns:
    An iterable.
    None if the iterable can not be used by the function.
    """
    if callable(function_to_apply):
        if hasattr(iterable, '__iter__'):
            for elm in iterable:
                if function_to_apply is None or function_to_apply(elm):
                    yield elm
        else:
            raise TypeError("'{}' object is not iterable".format(type(iterable).__name__))
    else:
        raise TypeError("'{}' object is not callable".format(type(function_to_apply).__name__))
