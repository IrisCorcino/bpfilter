import collections
import sys
import os.path
from FileModificationChecker import FileModificationChecker

class MeasurementStarter():
    
    def __init__(measurement):
        if len(sys.argv) != 4:
            raise Exception('incorrect number of arguments')
        self.measurement = measurement
        self.measurement.setOutputLocation(sys.argv[1])
        self.measuringTime = sys.argv[2]
        self.fileModificationChecker = FileModificationChecker(self.outputDir)

    def start(self):
        outputDir = self.measurement.getOutputLocation()
        for index in xrange(0, measurement.getSize()-1):
            measurement.startMeasurement(index,self.measuringTime)
        self.fileModificationChecker.printModifiedFiles()