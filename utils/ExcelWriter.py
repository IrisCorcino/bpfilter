import csv

class ExcelWriter():

    def open(self, fileName):
        self.file = open(fileName, 'wb')
        self.writer = csv.writer(self.file)

    def writeRow(self, data):
        self.writer.writerow(data)

    def close(self):
        self.file.close()