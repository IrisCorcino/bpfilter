import sys
from PyQt4 import Qt
from gnuradio import gr

class BaseMeasurement():

    def __init__(self, topBlock):
        from distutils.version import StrictVersion
        if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
            style = gr.prefs().get_string('qtgui', 'style', 'raster')
            Qt.QApplication.setGraphicsSystem(style)
        self.qapp = Qt.QApplication(sys.argv)
        self.tb = topBlock

    def getSize(self):
        return len(self.tb.vector)

    def startMeasurement(self, index, time):
        print("measuring {}").format(self.getFrequency(index))
        self.tb.set_indice(index)
        self.tb.start()
        self.tb.show()

        Qt.QThread.sleep(time)
        self.tb.stop()
        self.tb.wait()

    def getFrequency(self, index):
        return self.tb.get_vector()[index]

    @abstractmethod
    def getFilters(self):
				pass

    def getPattern(self, filename):
        return filename.partition('_')[0]
