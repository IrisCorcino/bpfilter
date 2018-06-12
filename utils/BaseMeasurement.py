import sys
from PyQt4 import Qt
from gnuradio import gr

class BaseMeasurement():

    def __init__(self):
        from distutils.version import StrictVersion
        if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
            style = gr.prefs().get_string('qtgui', 'style', 'raster')
            Qt.QApplication.setGraphicsSystem(style)
        self.qapp = Qt.QApplication(sys.argv)

    def setTopBlock(self, top_block):
        self.tb = top_block

    def getSize(self):
        return len(self.tb.vector)

    def startMeasurement(self, index, time):
        print("measuring {}").format(self.getFrequency(index))
        self.tb.set_indice(index)
        Qt.QThread.sleep(1)
        self.tb.start()
        self.tb.show()

        Qt.QThread.sleep(time)
        self.tb.stop()
        self.tb.wait()

    def getFrequency(self, index):
        return self.tb.get_vector()[index]

    def getSources(self):
        pass

    def getPattern(self, filename):
        return filename.partition('_')[0]

    def getOutputLocation(self):
        #TODO dynamic
        return "/home/iris/Desktop/medidas/"
