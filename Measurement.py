import top_block
import sys
from PyQt4 import Qt
from gnuradio import gr


class Measurement():

    def __init__(self):
        from distutils.version import StrictVersion
        if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
            style = gr.prefs().get_string('qtgui', 'style', 'raster')
            Qt.QApplication.setGraphicsSystem(style)
        self.qapp = Qt.QApplication(sys.argv)
        self.tb = top_block.top_block()
        #self.tb.start()
        #self.tb.show()

    def getSize(self):
        return len(self.tb.vector)

    def startMeasurement(self, index, time, debug=False):
        print("measuring {}").format(self.getFrequency(index))
        from distutils.version import StrictVersion
        if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
            style = gr.prefs().get_string('qtgui', 'style', 'raster')
            Qt.QApplication.setGraphicsSystem(style)
        self.tb.set_indice(index)
        #Qt.QTimer.singleShot(time * 1000, self.endMeasurement)
        self.tb.start()
        self.tb.show()
        if debug:
            self.printInfo()
        #self.qapp.exec_()

        Qt.QThread.sleep(time)
        self.tb.stop()
        self.tb.wait()

    def getFrequency(self, index):
        return self.tb.get_vector()[index]

    def printInfo(self):
        blk = self.tb
        print('\n')
        print('--------------------------------')
        print('indice: {}').format(blk.indice)
        print('--------------------------------')
        print('frequency: {}').format(blk.vector[blk.indice])
        print('bw: {}').format(blk.bw)
        print('ajuste: {}').format(blk.ajuste)
        print('samp_rate: {}').format(blk.samp_rate)
        print('--------------------------------')
        print('\n')

    def endMeasurement(self):
        print('timer fired')
        self.tb.stop()
        self.tb.wait()
        self.qapp.quit()