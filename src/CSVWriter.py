import csv

class CSVWriter():

    def open(self, fileName):
        self.file = open(fileName, 'wb')
        self.writer = csv.writer(self.file)

    def writeRow(self, row):
        self.writer.writerow(row)

    def close(self):
        self.file.close()
