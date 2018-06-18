from BinaryReader import BinaryReader
import os

class BasePlotter():

    def __init__(self, outputDir):
        self.binaryReader = BinaryReader()
        self.outputDir = outputDir

    def initPlotting(self, filePatterns, measurementResult):
        self.filePatterns = filePatterns
        self.measurementResult = measurementResult
    
    def plot(self):
        pass
    
    def terminate(self):
        pass