import numpy


class ScrapBooker:

    def __init__(self):
        pass

    def crop(self, array, dim, position=(0, 0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width oof the image) from the coordinates given by position arguments.
        Args:
        array: numpy.ndarray
        dim: tuple of 2 integers.
        position: tuple of 2 integers.
        Returns:
        new_arr: the cropped numpy.ndarray.
        None otherwise (combinaison of parameters not incompatible).
        """
        if isinstance(array, numpy.ndarray) and isinstance(dim, tuple) == isinstance(position, tuple):
            try:
                assert len(dim) == len(position) == 2, None
                assert isinstance(dim[0], int) == isinstance(dim[1], int), None
                assert isinstance(position[0], int) == isinstance(position[1], int), None
                return array[position[0]:position[0] + dim[0], position[1]:position[1] + dim[1]]
            except AssertionError:
                return None

    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: vertical, 1: horizontal)
        Args:
        array: numpy.ndarray.
        n: non null positive integer lower than the number of row/column of the array
        (depending of axis value).
        axis: positive non null integer.
        Returns:
        new_arr: thined numpy.ndarray.
        None otherwise (combinaison of parameters not incompatible).
        """
        if isinstance(array, numpy.ndarray) and isinstance(n, int) == isinstance(axis, int):
            if n > 0 and (axis == 0 or axis == 1):
                axis = 0 if axis else 1
                if n < array.shape[axis]:
                    to_exclude = tuple(range(n-1, array.shape[axis], n))
                    return numpy.delete(array, to_exclude, axis)

    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        Returns:
        new_arr: juxtaposed numpy.ndarray.
        None otherwise (combinaison of parameters not incompatible).
        """
        if isinstance(array, numpy.ndarray) and isinstance(n, int) == isinstance(axis, int):
            if n > 0 and axis in (0, 1):
                return numpy.concatenate(tuple(numpy.copy(array) for i in range(n)), axis)

    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        array: numpy.ndarray.
        dim: tuple of 2 integers.
        Returns:
        new_arr: mosaic numpy.ndarray.
        None otherwise (combinaison of parameters not incompatible).
        """
        if isinstance(array, numpy.ndarray) and isinstance(dim, tuple):
            if len(dim) == 2 and isinstance(dim[0], int) == isinstance(dim[1], int):
                _mosaic = self.juxtapose(array, dim[0], 0)
                return self.juxtapose(_mosaic, dim[1], 1)
