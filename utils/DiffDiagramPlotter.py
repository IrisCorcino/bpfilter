from BasePlotter import BasePlotter
from MeasurementStatistics import MeasurementStatistics
from CSVWriter import CSVWriter
import os
import numpy as np
import matplotlib.pyplot as plt

class DiffDiagramPlotter(BasePlotter):

    def __init__(self, outputDir):
        BasePlotter.__init__(self, outputDir)
    
    def initPlotting(self, filePatterns, measurementResult):
        BasePlotter.initPlotting(self, filePatterns, measurementResult)
        if len(filePatterns) != 2:
            raise Exception('DiffDiagramPlotter needs exactly two file pattern')

    def plot(self):
        measurementEntryList1 = self.measurementResult[0]
        measurementEntryList2 = self.measurementResult[1]
        x = []
        y1 = []
        y2 = []
        y3 = []
        for measurementEntry1 in measurementEntryList1:
            measurementEntry2 = list(filter(lambda x:x.index == measurementEntry1.index, measurementEntryList2))

            if len(measurementEntry2) == 1:
                measurementEntry2 = measurementEntry2[0]
                x.append(measurementEntry1.frequency)
                mean1 = MeasurementStatistics.getMean(measurementEntry1.data)
                mean2 = MeasurementStatistics.getMean(measurementEntry2.data)
                y1.append(mean1)
                y2.append(mean2)
                y3.append(mean1 - mean2)
        yLabel = 'dB'
        fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)
        
        ax1.scatter(x, y1)
        ax1.set_title(self.filePatterns[0])
        ax1.set_ylabel(yLabel)

        ax2.scatter(x, y2)
        ax2.set_title(self.filePatterns[1])
        ax2.set_ylabel(yLabel)

        ax3.scatter(x, y3)
        ax3.set_title(self.filePatterns[0] + ' - ' + self.filePatterns[1])
        ax3.set_xlabel('frequency [Hz]')
        ax3.set_ylabel(yLabel)

        fig.subplots_adjust(hspace=1)        
        fig.savefig(self.outputDir + "DIFF_" + self.filePatterns[0] + '-' + self.filePatterns[1])
         
    def terminate(self):
        BasePlotter.terminate(self)