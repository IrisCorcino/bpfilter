import numpy as np

class BinaryReader:

    def __init__(self, littleEndian = True):
        self.format = '<f4' if littleEndian else '>f4'

    def readToFloat(self, filename, skip):
        data = np.fromfile(filename, self.format)
        data = data[skip:]
        return list(data)
