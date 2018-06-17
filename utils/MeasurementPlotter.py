import sys
import os
from CSVPlotter import CSVPlotter
from DiagramPlotter import DiagramPlotter
from DiffDiagramPlotter import DiffDiagramPlotter
from MeasurementEntry import MeasurementEntry
from FileModificationChecker import FileModificationChecker

PLOTTER_CSV = 0
PLOTTER_DIAGRAM = 1
PLOTTER_DIFF_DIAGRAM = 2

class MeasurementPlotter():

    def __init__(self, plotterID, outputDir, inputDir, filePatterns):
        if plotterID == PLOTTER_CSV:
            self.plotter = CSVPlotter(outputDir)
        elif plotterID == PLOTTER_DIAGRAM:
            self.plotter = DiagramPlotter(outputDir)
        elif plotterID == PLOTTER_DIFF_DIAGRAM:
            self.plotter = DiffDiagramPlotter(outputDir)
        else:
            raise Exception('plotter with id ', plotterID, ' does not exist')
        self.outputDir = outputDir
        self.inputDir = inputDir
        self.filePatterns = filePatterns
        self.fileModificationChecker = FileModificationChecker(self.outputDir)

    def start(self):
        measurementResult = []
        for i,filePattern in enumerate(self.filePatterns):
            files = self.getFilesWithPattern(filePattern)
            print "INPUT FILES2 = ", files
            measurementEntryList = []
            for filename in files:
                measurementEntryList.append(MeasurementEntry.createEntry(self.inputDir, filename))
                sorted(measurementResult, key=lambda entry: entry.index)
            measurementResult.append(measurementEntryList)
        self.plotter.initPlotting(self.filePatterns, measurementResult)
        self.plotter.plot()
        self.plotter.terminate()
        self.fileModificationChecker.printModifiedFiles()
    
    def getFilesWithPattern(self, filePattern):
        files = os.listdir(self.inputDir)
        inputFiles = list(filter(lambda x: x.split('_')[0] == filePattern, files))
        print "INPUT FILES = ", inputFiles
        return inputFiles

if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise Exception('incorrect number of arguments')
    filePatterns = []
    for i in range(4, len(sys.argv)):
        filePatterns.append(sys.argv[i])
    plotter = MeasurementPlotter(int(sys.argv[1]), sys.argv[2], sys.argv[3], filePatterns)
    plotter.start()