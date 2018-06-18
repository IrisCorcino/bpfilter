from BasePlotter import BasePlotter
from MeasurementStatistics import MeasurementStatistics
from CSVWriter import CSVWriter
import os

class CSVPlotter(BasePlotter):
    TITLES = ['Index', 'Frequency', 'sample count', 'Min', 'Max', 'Mean', 'Std']
    FIRST_AND_LAST = 20

    def __init__(self, outputDir):
        BasePlotter.__init__(self, outputDir)
    
    def initPlotting(self, filePatterns, measurementResult):
        BasePlotter.initPlotting(self, filePatterns, measurementResult)
        self._createWriters()
        self._writeHeader()

    def plot(self):
        for i, writer in enumerate(self.writers):
            measurementEntryList = self.measurementResult[i]
            for measurementEntry in measurementEntryList:
                self._writeMeasurementEntry(writer, measurementEntry)
    
    def terminate(self):
        self._closeWriters()

    def _createWriters(self):
        self.writers = []
        for filePattern in self.filePatterns:
            writer = CSVWriter()
            writer.open(self.outputDir + filePattern + '.csv')
            self.writers.append(writer)

    def _writeHeader(self):
        for writer in self.writers:
            writer.writeRow(self.TITLES)

    def _writeMeasurementEntry(self, writer, measurementEntry):
        index = measurementEntry.index
        freq = measurementEntry.frequency
        data = measurementEntry.data
        size = MeasurementStatistics.getSize(data)
        minV = MeasurementStatistics.getMin(data)
        maxV = MeasurementStatistics.getMax(data)
        mean = MeasurementStatistics.getMean(data)
        std = MeasurementStatistics.getStd(data)
        firstAndLast20 = MeasurementStatistics.getFirstAndLast(data, 20)
        d = [index, freq, size, minV, maxV, mean, std]
        d.extend(firstAndLast20)
        writer.writeRow(d)

    def _closeWriters(self):
        for writer in self.writers:
            writer.close()