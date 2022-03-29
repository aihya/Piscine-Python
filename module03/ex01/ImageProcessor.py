import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class ImageProcessor:

    @staticmethod
    def load(cls, path):
        array = None
        if type(path) == str and path.endswith('.png'):
            try:
                array = mpimg.imread(path)
            except Exception as E:
                print("Exception: {}: {}".format(type(E).__name__, E))
        return array

    @staticmethod
    def display(cls, array):
        plot = plt.imshow(array)
        plt.show()

