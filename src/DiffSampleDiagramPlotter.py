from BasePlotter import BasePlotter
from MeasurementStatistics import MeasurementStatistics
from CSVWriter import CSVWriter
import os
import numpy as np
import matplotlib.pyplot as plt

class DiffSampleDiagramPlotter(BasePlotter):

    def __init__(self, outputDir):
        BasePlotter.__init__(self, outputDir)
    
    def initPlotting(self, filePatterns, measurementResult):
        BasePlotter.initPlotting(self, filePatterns, measurementResult)
        if len(filePatterns) != 2:
            raise Exception('DiffSampleDiagramPlotter needs exactly two file pattern')

    def plot(self):
        measurementEntryList1 = self.measurementResult[0]
        measurementEntryList2 = self.measurementResult[1]

        for measurementEntry1 in measurementEntryList1:
            measurementEntry2 = list(filter(lambda x:x.frequency == measurementEntry1.frequency, measurementEntryList2))

            if len(measurementEntry2) == 1:
                measurementEntry2 = measurementEntry2[0]
                data1 = measurementEntry1.data
                data2 = measurementEntry2.data
                x1 = np.arange(0, len(data1), 1)
                x2 = np.arange(0, len(data2))
                y1 = data1
                y2 = data2
                y3 = []
                freq = measurementEntry1.frequency
                minX = min(len(x1), len(x2))
                for i in range(0, minX):
                    y3.append(abs(y1[i] - y2[i]))
                x3 = np.arange(0, len(y3))
                yLabel = 'dBm'
                fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=False)
                
                #TODO linewidth / dot
                ax1.scatter(x1, y1)
                ax1.set_title(self.filePatterns[0])
                ax1.set_ylabel(yLabel)

                ax2.scatter(x2, y2)
                ax2.set_title(self.filePatterns[1])
                ax2.set_ylabel(yLabel)

                ax3.scatter(x3, y3)
                ax3.set_title(self.filePatterns[0] + ' - ' + self.filePatterns[1])
                ax3.set_xlabel('samples')
                ax3.set_ylabel(yLabel)

                fig.subplots_adjust(hspace=1)        
                fig.savefig(self.outputDir + "DIFF_SAMPLE_" + self.filePatterns[0] + '-' + self.filePatterns[1] + '-' +  str(int(freq)))
                #TODO free resources
         
    def terminate(self):
        BasePlotter.terminate(self)