import collections
import sys
import os.path
from FileModificationChecker import FileModificationChecker

class MeasurementStarter():
    
    def __init__(self, measurement):
        if len(sys.argv) < 3 or len(sys.argv) > 5:
            raise Exception('incorrect number of arguments')
        self.measurement = measurement
        self.measurement.setOutputLocation(sys.argv[1])
        self.measuringTime = int(sys.argv[2])
        self.outputDir = self.measurement.getOutputLocation()
        self.fileModificationChecker = FileModificationChecker(self.outputDir)
        if len(sys.argv) == 3:
            self.startIndex = 0
            self.endIndex = self.measurement.getSize()
        elif len(sys.argv) == 4:
            self.startIndex = self._getStartIndexFromArgv()
            self.endIndex = self.startIndex + 1 
        else:
            self.startIndex = self._getStartIndexFromArgv()    
            self.endIndex = self._getEndIndexFromArgv()
            if self.startIndex >= self.endIndex:
                raise Exception('illegal indices')

    def _getStartIndexFromArgv(self):
        startIndex = int(sys.argv[3])
        if startIndex < 0 or startIndex > self.measurement.getSize():
            raise Exception('illegal start index')    
        return startIndex

    def _getEndIndexFromArgv(self):
        endIndex = int(sys.argv[4]) + 1
        if endIndex > self.measurement.getSize():
            raise Exception('illegal end index')
        return endIndex

    def start(self):
        for index in xrange(self.startIndex, self.endIndex):
            self.measurement.startMeasurement(index,self.measuringTime)
        self.fileModificationChecker.printModifiedFiles()