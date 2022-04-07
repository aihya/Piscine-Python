import matplotlib.pyplot as plt
import matplotlib.image as mplimg


class ImageProcessor:

    def __init__(self):
        pass

    @staticmethod
    def load(path):
        if type(path) == str and path.endswith('.png'):
            try:
                array = mplimg.imread(path)
                print("Loading image of dimensions {} x {}".format(array.shape[0], array.shape[1]))
                return array
            except Exception as E:
                print("Exception: {}: {}".format(type(E).__name__, E))

    @staticmethod
    def display(array):
        plt.imshow(array)
        plt.show()


def deco(func, *args, **kward):
    def wrapper():
        print("WEE")
        var = func(*args, **kwargs)
        return var
    return wrapper


@deco
def f(l):
    sum(l)

f()