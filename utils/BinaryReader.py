import numpy as np

class BinaryReader:

    def __init__(self):
        self.data = []

    def readToFloat(self, filename, littleEndian = True):
        format = '<f4' if littleEndian else '>f4'
        self.data = np.fromfile(filename, format)
        self.data = self.data[32768:]

    def getSize(self):
        return len(self.data)

    def getData(self):
        return self.data

    def getMin(self):
        return min(self.data)

    def getMax(self):
        return max(self.data)

    def getMean(self):
        return np.mean(self.data)

    def getStd(self):
        return np.std(self.data)