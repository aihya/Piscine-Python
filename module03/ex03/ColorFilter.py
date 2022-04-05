import numpy
import matplotlib.image as mplim
import matplotlib.pyplot as plt
import copy


class ColorFilter:

    def __init__(self):
        pass

    @staticmethod
    def invert(array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        """
        if isinstance(array, numpy.ndarray):
            for pixel_row in array:
                for pixel in pixel_row:
                    pixel[:3] = 1 - pixel[:3]
            return array

    @staticmethod
    def to_blue(array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        """
        if isinstance(array, numpy.ndarray):
            blue = numpy.zeros(array.shape)
            for r, pixel_row in enumerate(array):
                for c, pixel in enumerate(pixel_row):
                    blue[r][c][2:] = pixel[2:]
            return blue


    @staticmethod
    def to_green(array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        """
        if isinstance(array, numpy.ndarray):
            green = copy.deepcopy(array)
            for r, pixel_row in enumerate(array):
                for c, pixel in enumerate(pixel_row):
                    green[r][c][0], green[r][c][2] = 0, 0
            return green


    @staticmethod
    def to_red(array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        """
        if isinstance(array, numpy.ndarray):
            red = array - ColorFilter.to_green(array) - ColorFilter.to_blue(array)
            for r, pixel_row in enumerate(array):
                for c, pixel in enumerate(pixel_row):
                    red[r][c][3] = pixel[3]
            return red

    @staticmethod
    def to_celluloid(array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        """
        shades = 5
        thresh = numpy.linspace(0, 1, num=shades)

        def cel_shade(__channel):
            target = __channel
            for th in thresh:
                if __channel < th:
                    target = th
                    break
            return target

        if isinstance(array, numpy.ndarray):
            for r, pixel_row in enumerate(array):
                for c, pixel in enumerate(pixel_row):
                    array[r][c][0] = cel_shade(array[r][c][0])  # Red channel
                    array[r][c][1] = cel_shade(array[r][c][1])  # Green channel
                    array[r][c][2] = cel_shade(array[r][c][2])  # Blue channel
            return array

    @staticmethod
    def to_grayscale(array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = ’mean’/’m’: performs the mean of RBG channels.
        For filter = ’weight’/’w’: performs a weighted mean of RBG channels.
        Args:
        array: numpy.ndarray corresponding to the image.
        filter: string with accepted values in [’m’,’mean’,’w’,’weight’]
        weights: [kwargs] list of 3 floats where the sum equals to 1,
        corresponding to the weights of each RBG channels.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        """
        if isinstance(array, numpy.ndarray):

            if filter in ('m', 'mean'):  # Mean filter
                for pixel_row in array:
                    for pixel in pixel_row:
                        pixel[:3] = pixel[:3].sum() / 3
                return array

            if filter in ('w', 'weight'):  # Weighted mean filter
                if len(kwargs.keys()):
                    try:
                        weights = kwargs['weights']
                        if isinstance(weights, list) and len(weights) == 3:
                            assert isinstance(weights[0], float), None
                            assert isinstance(weights[1], float), None
                            assert isinstance(weights[2], float), None
                            if weights[0] + weights[1] + weights[2] == 1.0:
                                for pixel_row in array:
                                    for pixel in pixel_row:
                                        pixel[:3] = (pixel[:3] * weights).sum()
                                return array
                    except KeyError:
                        return None
                    except AssertionError:
                        return None