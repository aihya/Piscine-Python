import numpy


class NumPyCreator:

    @staticmethod
    def from_list(lst):
        if type(lst) != list:
            return None
        array = numpy.array(lst)
        if array.dtype == object:
            return None
        return array

    @staticmethod
    def from_tuple(tpl):
        if type(tpl) != tuple:
            return None
        array = numpy.array(tpl)
        if array.dtype == object:
            return None
        return array

    @staticmethod
    def from_iterable(itr):
        if hasattr(itr, '__iter__'):
            return numpy.array(itr)
        return None

    @staticmethod
    def from_shape(shape, value=0):
        if type(shape) != tuple or type(value) not in [int, float]:
            return None
        for elm in shape:
            if type(elm) != int:
                return None
        array = numpy.zeros(shape)
        if value:
            array.fill(value)
        return array

    @staticmethod
    def random(shape):
        if type(shape) != tuple:
            return None
        for elm in shape:
            if type(elm) != int:
                return None
        return numpy.random.random(shape)

    @staticmethod
    def identity(n):
        if type(n) != int:
            return None
        return numpy.identity(n)
