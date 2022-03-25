class CsvReader:
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.data = []

    def __enter__(self):
        self.file = open(self.filename, 'r')
        for record in self.file.read().split('\n'):
            fields = record.split(self.sep)
            if self.data and len(fields) != len(self.data[0]):
                return None
            print(fields)
            self.data.append(fields)
        return self

    def __exit__(self, __type, __value, __traceback):
        self.file.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Returns:
        nested list (list(list, list, ...)) representing the data.
        """
        return self.data[self.skip_top + (1 if self.header else 0):self.skip_bottom]

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        return self.header


if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        data = file.getdata()
        header = file.getheader()
        print(data)
        print(header)