class TableWorksheet:  
    def __init__(self, worksheet):
        self.worksheet = worksheet

    def val(self, col, row):
        return self.worksheet[f"{col}{row}"].value

    def vals(self, cols, row):
        return tuple(self.val(col, row) for col in cols)

    def check(self, col, row):
        return not (self.val(col, row) or\
                    self.val(col, row + 1) or\
                    self.val(col, row + 2))

    def checks(self, cols, row):
        return any((self.check(col, row) for col in cols))

