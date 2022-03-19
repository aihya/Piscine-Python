class Vector:

    @classmethod
    def init_range(cls, start, end):
        return [[float(i)] for i in range(start, end)]

    def __init__(self, entry):
        self.values = entry
        self.shape = [0, 0]

        # Initialize self.values with init_range class method.
        if isinstance(entry, int):
            self.values = Vector.init_range(0, entry)
            self.shape = [len(self.values), 1]

        elif isinstance(entry, tuple):
            assert len(entry) == 2, "Vector entry tuple {} needs 2 elements, found {}.".format(entry, len(tuple))
            assert type(entry[0]) == int and type(entry[1]) == int, "Vector entry tuple {} contains non-integer range.".format(entry)
            self.values = Vector.init_range(entry[0], entry[1])
            self.shape = [len(self.values), 1]

        # Check the coherence of entry.
        elif type(entry) == list:
            if type(entry[0]) == float:
                for e in entry:
                    if type(e) != float:
                        raise ValueError("Row vectors must contain floats only, found {}".format(type(e)))
                self.shape = [1, len(self.values)]
            elif type(entry[0]) == list:
                for e in entry:
                    if type(e[0]) != float:
                        raise ValueError("Column vectors must contain floats only, found ({} -> {}).".format(e, type(e[0])))
                    if len(e) != 1:
                        raise ValueError("Column vectors are of shape Nx1, found ({} -> Nx{}).".format(e, len(e)))
                self.shape = [len(self.values), 1]

    def __add__(self, other):
        if type(other) == int:
            self.values = [e + other for e in self.values]
        elif type(other) == Vector:
            if self.shape == other.shape:
                if self.shape[0] == 1:
                    return [self.values[i] + other.values[i] for i in range(self.shape[1])]
                return [self.values[i][0] + other.values[i][0] for i in range(self.shape[0])]
            raise TypeError("Cannot add vectors of different shapes ({} and {})".format())

    def __radd(self, other):
        pass

    def __sub__(self, other):
        pass

    def __rsub__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __rtruediv__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __rmul__(self, other):
        pass

    def __str__(self, other):
        pass

    def __repr__(self, other):
        pass

    def dot(self, other):
        pass

    def T(self, other):
        pass
