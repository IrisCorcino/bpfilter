import collections
import sys
import os.path
from FileModificationChecker import FileModificationChecker

class MeasurementStarter():
    
    def __init__(self, measurement):
        if len(sys.argv) != 3:
            raise Exception('incorrect number of arguments')
        self.measurement = measurement
        self.measurement.setOutputLocation(sys.argv[1])
        self.measuringTime = int(sys.argv[2])
        self.outputDir = self.measurement.getOutputLocation()
        self.fileModificationChecker = FileModificationChecker(self.outputDir)

    def start(self):
        for index in xrange(0, self.measurement.getSize()-1):
            self.measurement.startMeasurement(index,self.measuringTime)
        self.fileModificationChecker.printModifiedFiles()