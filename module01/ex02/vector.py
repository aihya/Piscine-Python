class Vector:

    TUPLE_SIZE_ERR = "Vector entry tuple {} needs 2 elements, found {}."
    TUPLE_NON_INT_RANGE_ERR = "Vector entry tuple {} contains non-integer boundry."
    ROW_VECTOR_NON_FLT_ERR = "Row vectors must contain floats only, found ({}) {}."
    COLUMN_VECTOR_NON_FLOAT_ERR = "Column vectors must contain lists of float only, found ({}) {}."
    COLUMN_VECTOR_SHAPE_ERR = "Column vectors are of shape Nx1, found ({})."
    DIFFERENT_SHAPE_ERR = "Cannot {} vectors of different shapes."
    DIFFERENT_TYPES_ERR = "Cannot {} Vector to {}."
    INVALID_VECTOR_VALUE_ERR = "Vector values must be float or lists of float, found ({}) {}."
    INVALID_VECTOR_ENTRY_ERR = "Invalid entry, found ({}) {}."
    ZERO_DIVISION_ERR = "Cannot divide Vector by Zero."
    INVALID_DIVIDOR_ERR = "Division by int or float only, found {}."
    INVALID_MULTIPLIER_ERR = "Multiplication with int or float only, found {}."


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
            assert len(entry) == 2, Vector.TUPLE_SIZE_ERR.format(entry, len(entry))
            assert type(entry[0]) == int and type(entry[1]) == int, Vector.TUPLE_NON_INT_RANGE_ERR.format(entry)
            self.values = Vector.init_range(entry[0], entry[1])
            self.shape = [len(self.values), 1]

        # Check the coherence of entry.
        elif type(entry) == list:
            if type(entry[0]) == float:
                for e in entry:
                    if type(e) != float:
                        raise ValueError(Vector.ROW_VECTOR_NON_FLT_ERR.format(e, type(e)))
                self.shape = [1, len(self.values)]
            elif type(entry[0]) == list:
                for e in entry:
                    if type(e) != list or type(e[0]) != float:
                        raise ValueError(Vector.COLUMN_VECTOR_NON_FLOAT_ERR.format(e, type(e)))
                    if len(e) != 1:
                        raise ValueError(Vector.COLUMN_VECTOR_SHAPE_ERR.format(e))
                self.shape = [len(self.values), 1]
            else:
                raise ValueError(Vector.INVALID_VECTOR_VALUE_ERR.format(entry[0], type(entry[0])))
        else:
            raise TypeError(Vector.INVALID_VECTOR_ENTRY_ERR.format(entry, type(entry)))

    def is_column(self):
        return True if type(self.shape[0]) == list else False

    def is_row(self):
        return True if type(self.shape[0]) == float else False

    def same_shape_as(self, other):
        return (self.is_row() and other.is_row()) or (self.is_column() and other.is_column())

    def __add__(self, other):
        try:
            if type(other) in [int, float]:  # If other is integer or float
                if type(self.values[0]) == float:
                    return Vector([e + other for e in self.values])
                return Vector([[e[0] + other] for e in self.values])
            elif isinstance(other, Vector):  # Else, if other is a Vector
                if self.shape == other.shape:
                    if self.shape == [1, 1] and not self.same_shape_as(other):
                        raise TypeError(Vector.DIFFERENT_SHAPE_ERR.format("add"))
                    return Vector([a + b if self.is_row() else [a[0] + b[0]] for a, b in zip(self.values, other.values)])
            raise TypeError(Vector.DIFFERENT_TYPES_ERR.format("add", type(other)))
        except TypeError as E:
            print("{}: {}".format(type(E.__class__), E))

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        try:
            if type(other) in [int, float]:  # If other is integer or float
                if type(self.values[0]) == float:
                    return Vector([e - other for e in self.values])
                return Vector([[e[0] - other] for e in self.values])
            elif isinstance(other, Vector):  # Else, if other is a Vector
                if self.shape == other.shape:
                    if self.shape == [1, 1] and not self.same_shape_as(other):
                        raise TypeError(Vector.DIFFERENT_SHAPE_ERR.format("subtract"))
                    return Vector([a - b if self.is_row() else [a[0]-b[0]] for a, b in zip(self.values, other.values)])
            raise TypeError(Vector.DIFFERENT_TYPES_ERR.format("subtract", type(other)))
        except TypeError as E:
            print("{}: {}".format(type(E.__class__), E))

    def __rsub__(self, other):
        return self - other

    def __truediv__(self, other):
        try:
            assert type(other) in [int, float], Vector.INVALID_DIVIDOR_ERR.format(type(other))
            return Vector([e / other if self.is_row() else [e[0] / other] for e in self.values])
        except ZeroDivisionError:
            print(Vector.ZERO_DIVISION_ERR)
        except AssertionError as E:
            print("{}: {}".format(type(E.__class__), E))

    def __rtruediv__(self, other):
        try:
            assert type(other) in [int, float], Vector.INVALID_DIVIDOR_ERR.format(type(other))
            return Vector([other / e if self.is_row() else [other / e[0]] for e in self.values])
        except ZeroDivisionError:
            print(Vector.ZERO_DIVISION_ERR)
        except AssertionError as E:
            print("{}: {}".format(type(E.__class__), E))

    def __mul__(self, other):
        try:
            assert type(other) in [int, float], Vector.INVALID_MULTIPLIER_ERR.format(type(other))
            return [e * other if self.is_row() else [e * other] for e in self.values]
        except AssertionError as E:
            print("{}: {}".format(type(E.__class__), E))

    def __rmul__(self, other):
        return self * other

    def __str__(self):
        txt = ""
        if self.is_row():
            txt += ', '.join([str(e) for e in self.values])
        else:
            txt += '\n'.join([str(e[0]) for e in self.values])
        txt += "\nShape: {}x{}".format(self.shape[0], self.shape[1])
        return txt

    def __repr__(self):
        return "Vector({})".format(self.values)

    def dot(self, other):
        pass

    def T(self):
        return Vector([[e] if self.is_row() else e[0] for e in self.values])
