class CsvReader:
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=1):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.data = []
        self.head = None

    def __enter__(self):
        try:
            self.file = open(self.filename, 'r')
        except FileNotFoundError:
            return None

        lines = list(filter(len, self.file.read().split('\n')))
        records = [[field.strip() for field in line.split(self.sep)] for line in lines]

        for record in records:
            record = list(filter(len, record))
            if len(record) != len(records[0]):
                return None

        if self.header:
            self.head = records[0]
            self.data = records[1:]
        else:
            self.data = records

        return self

    def __exit__(self, __type, __value, __traceback):
        self.file.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Returns:
        nested list (list(list, list, ...)) representing the data.
        """
        return self.data[self.skip_top: len(self.data) - self.skip_bottom]

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        return self.head


if __name__ == "__main__":
    with CsvReader('good.csv', header=True) as file:
        if file is None:
            print("File is corrupted")
        else:
            data = file.getdata()
            header = file.getheader()
            print(data)
            print(header)
