from BasePlotter import BasePlotter
from MeasurementStatistics import MeasurementStatistics
from CSVWriter import CSVWriter
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class DiagramPlotter(BasePlotter):

    def __init__(self, outputDir):
        BasePlotter.__init__(self, outputDir)
    
    def initPlotting(self, filePatterns, measurementResult):
        BasePlotter.initPlotting(self, filePatterns, measurementResult)

    def plot(self):
        for i, filename in enumerate(self.filePatterns):
            measurementEntryList = self.measurementResult[i]
            for entry in measurementEntryList:
                freq = entry.frequency
                data = entry.data
                x = np.arange(0, len(data), 1)

                fig, ax = plt.subplots()
                ax.plot(x, data)
                ax.set_title(filename + ' @ ' + str(freq) + ' Hz')
                ax.set_xlabel('samples')
                ax.set_ylabel('dB')
                ax.grid()

                fig.savefig(self.outputDir + filename + '_' + str(int(freq)))
                  
    def terminate(self):
        BasePlotter.terminate(self)