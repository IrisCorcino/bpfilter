import sys
from os import listdir
from PyQt4 import Qt
from gnuradio import gr

class Measurement():
    
    def __init__(self, topBlock):
        from distutils.version import StrictVersion
        if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
            style = gr.prefs().get_string('qtgui', 'style', 'raster')
            Qt.QApplication.setGraphicsSystem(style)
        self.qapp = Qt.QApplication(sys.argv)
        self.tb = topBlock()
        self.outputLocation = self.tb.get_OutputDir()

    def getSize(self):
        return len(self.tb.vector)

    def startMeasurement(self, index, time):
        self.tb.set_indice(index)
        
        self.tb.start()
        self.tb.show()
        Qt.QThread.sleep(time)
        self.tb.stop()
        self.tb.wait()

    def setOutputLocation(self, outputLocation):
        self.tb.set_OutputDir(outputLocation)
        self.outputLocation = outputLocation
    
    def getOutputLocation(self):
        return self.outputLocation
