from BinaryReader import BinaryReader

class MeasurementEntry():
    SKIP_SAMPLES = 32768
    binaryReader = BinaryReader()

    def __init__(self, index, frequency, data):
        self.index = index
        self.frequency = frequency
        self.data = data

    @staticmethod
    def createEntry(inputDirectory, filename):
        f = filename.replace('.bin','')
        splittedF = f.split('_')
        index = int(splittedF[1])
        frequency = float(splittedF[2])
        data = MeasurementEntry.binaryReader.readToFloat(inputDirectory + filename, MeasurementEntry.SKIP_SAMPLES)
        return MeasurementEntry(index, frequency, data)