#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun Jun 10 20:28:47 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import osmosdr
import sip
import sys
import time
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.vector = vector = (88.1e6,89.1e6,89.7e6,90.1e6,90.5e6,90.9e6,91.3e6,92.1e6,92.5e6,92.9e6,93.7e6,94.1e6,94.7e6,95.3e6,95.7e6,96.1e6,96.5e6,96.9e6,97.3e6,97.7e6,98.1e6,98.5e6,98.9e6,99.3e6,100.1e6,100.9e6,101.3e6,101.5e6,101.7e6,102.1e6,102.5e6,103.3e6,104.1e6,104.3e6,104.7e6,105.1e6,105.7e6,106.3e6,106.9e6,107.3e6,107.9e6)
        self.indice = indice = 0
        self.ajuste = ajuste = 0
        self.samp_rate = samp_rate = 3e6
        self.rfgain = rfgain = 70
        self.freq_Passa_Faixa_REAL = freq_Passa_Faixa_REAL = vector[indice]+ (vector[indice +  1]- vector[indice]) + ajuste
        self.freq_Passa_Faixa = freq_Passa_Faixa = vector[indice+1]
        self.Update_Interval = Update_Interval = 0.1
        self.Quadrature = Quadrature = 50e4
        self.NUM = NUM = 0
        self.FreqChannel = FreqChannel = vector[indice]
        self.FileNameSND = FileNameSND = "SND_"+str(indice)+".bin"
        self.BandWidth = BandWidth = 100e3

        ##################################################
        # Blocks
        ##################################################
        self._rfgain_range = Range(0, 100, 1, 70, 10)
        self._rfgain_win = RangeWidget(self._rfgain_range, self.set_rfgain, 'Ganho', "slider", float)
        self.top_grid_layout.addWidget(self._rfgain_win, 0,0,1,2)
        self._indice_range = Range(0, 40, 1, 0, 2)
        self._indice_win = RangeWidget(self._indice_range, self.set_indice, "indice", "counter", int)
        self.top_grid_layout.addWidget(self._indice_win, 1,0,1,1)
        self._ajuste_range = Range(-600e3, 600e3, 100, 0, 10)
        self._ajuste_win = RangeWidget(self._ajuste_range, self.set_ajuste, "ajuste", "counter_slider", float)
        self.top_grid_layout.addWidget(self._ajuste_win, 0,6,1,2)
        self._BandWidth_range = Range(0, 100e3, 1, 100e3, 10)
        self._BandWidth_win = RangeWidget(self._BandWidth_range, self.set_BandWidth, 'Largura de Banda', "slider", float)
        self.top_grid_layout.addWidget(self._BandWidth_win, 0,3,1,2)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(vector[indice], 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(2, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(2, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(rfgain, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna('', 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)

        self.low_pass_filter_0_1 = filter.fir_filter_ccf(12, firdes.low_pass(
        	2, samp_rate, 100e3, 10e3, firdes.WIN_HAMMING, 6.76))
        self._freq_Passa_Faixa_REAL_tool_bar = Qt.QToolBar(self)

        if None:
          self._freq_Passa_Faixa_REAL_formatter = None
        else:
          self._freq_Passa_Faixa_REAL_formatter = lambda x: eng_notation.num_to_str(x)

        self._freq_Passa_Faixa_REAL_tool_bar.addWidget(Qt.QLabel('Freq (Chanel +1) + ajuste (PF)'+": "))
        self._freq_Passa_Faixa_REAL_label = Qt.QLabel(str(self._freq_Passa_Faixa_REAL_formatter(self.freq_Passa_Faixa_REAL)))
        self._freq_Passa_Faixa_REAL_tool_bar.addWidget(self._freq_Passa_Faixa_REAL_label)
        self.top_grid_layout.addWidget(self._freq_Passa_Faixa_REAL_tool_bar, 1,6,1,1)

        self._freq_Passa_Faixa_tool_bar = Qt.QToolBar(self)

        if None:
          self._freq_Passa_Faixa_formatter = None
        else:
          self._freq_Passa_Faixa_formatter = lambda x: eng_notation.num_to_str(x)

        self._freq_Passa_Faixa_tool_bar.addWidget(Qt.QLabel('Freq(channel + 1)'+": "))
        self._freq_Passa_Faixa_label = Qt.QLabel(str(self._freq_Passa_Faixa_formatter(self.freq_Passa_Faixa)))
        self._freq_Passa_Faixa_tool_bar.addWidget(self._freq_Passa_Faixa_label)
        self.top_grid_layout.addWidget(self._freq_Passa_Faixa_tool_bar, 1,4,1,1)

        self.blocks_rms_xx_1 = blocks.rms_cf(0.0001)
        self.blocks_rms_xx_0 = blocks.rms_cf(0.0001)
        self.blocks_nlog10_ff_0_1_0 = blocks.nlog10_ff(20, 1, 1)
        self.blocks_file_sink_1_0 = blocks.file_sink(gr.sizeof_float*1, "/home/iris/Desktop/SND/medida_SND/"+ FileNameSND, False)
        self.blocks_file_sink_1_0.set_unbuffered(False)
        self.blocks_divide_xx_0 = blocks.divide_ff(1)
        self.band_pass_filter = filter.fir_filter_ccf(12, firdes.band_pass(
        	2, samp_rate, (vector[indice+1] -vector[indice])-BandWidth+ ajuste, (vector[indice+1] -vector[indice])+BandWidth+ ajuste, 10e3, firdes.WIN_HAMMING, 6.76))
        self.POTENCIA_PASSA_BAIXA_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1
        )
        self.POTENCIA_PASSA_BAIXA_0.set_update_time(Update_Interval)
        self.POTENCIA_PASSA_BAIXA_0.set_title('SND (dB)')

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.POTENCIA_PASSA_BAIXA_0.set_min(i, -1)
            self.POTENCIA_PASSA_BAIXA_0.set_max(i, 1)
            self.POTENCIA_PASSA_BAIXA_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.POTENCIA_PASSA_BAIXA_0.set_label(i, "Data {0}".format(i))
            else:
                self.POTENCIA_PASSA_BAIXA_0.set_label(i, labels[i])
            self.POTENCIA_PASSA_BAIXA_0.set_unit(i, units[i])
            self.POTENCIA_PASSA_BAIXA_0.set_factor(i, factor[i])

        self.POTENCIA_PASSA_BAIXA_0.enable_autoscale(False)
        self._POTENCIA_PASSA_BAIXA_0_win = sip.wrapinstance(self.POTENCIA_PASSA_BAIXA_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._POTENCIA_PASSA_BAIXA_0_win, 3,6,1,1)
        self._NUM_range = Range(0, 40, 1, 0, 2)
        self._NUM_win = RangeWidget(self._NUM_range, self.set_NUM, "NUM", "counter", int)
        self.top_grid_layout.addWidget(self._NUM_win, 1,0,1,1)
        self._FreqChannel_tool_bar = Qt.QToolBar(self)

        if None:
          self._FreqChannel_formatter = None
        else:
          self._FreqChannel_formatter = lambda x: eng_notation.num_to_str(x)

        self._FreqChannel_tool_bar.addWidget(Qt.QLabel('Freq (Chanel)'+": "))
        self._FreqChannel_label = Qt.QLabel(str(self._FreqChannel_formatter(self.FreqChannel)))
        self._FreqChannel_tool_bar.addWidget(self._FreqChannel_label)
        self.top_grid_layout.addWidget(self._FreqChannel_tool_bar, 1,2,1,1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter, 0), (self.blocks_rms_xx_0, 0))
        self.connect((self.blocks_divide_xx_0, 0), (self.blocks_nlog10_ff_0_1_0, 0))
        self.connect((self.blocks_nlog10_ff_0_1_0, 0), (self.POTENCIA_PASSA_BAIXA_0, 0))
        self.connect((self.blocks_nlog10_ff_0_1_0, 0), (self.blocks_file_sink_1_0, 0))
        self.connect((self.blocks_rms_xx_0, 0), (self.blocks_divide_xx_0, 1))
        self.connect((self.blocks_rms_xx_1, 0), (self.blocks_divide_xx_0, 0))
        self.connect((self.low_pass_filter_0_1, 0), (self.blocks_rms_xx_1, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.band_pass_filter, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.low_pass_filter_0_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_vector(self):
        return self.vector

    def set_vector(self, vector):
        self.vector = vector
        self.rtlsdr_source_0.set_center_freq(self.vector[self.indice], 0)
        self.set_freq_Passa_Faixa_REAL(self._freq_Passa_Faixa_REAL_formatter(self.vector[self.indice]+ (self.vector[self.indice +  1]- self.vector[self.indice]) + self.ajuste))
        self.set_freq_Passa_Faixa(self._freq_Passa_Faixa_formatter(self.vector[self.indice+1]))
        self.band_pass_filter.set_taps(firdes.band_pass(2, self.samp_rate, (self.vector[self.indice+1] -self.vector[self.indice])-self.BandWidth+ self.ajuste, (self.vector[self.indice+1] -self.vector[self.indice])+self.BandWidth+ self.ajuste, 10e3, firdes.WIN_HAMMING, 6.76))
        self.set_FreqChannel(self._FreqChannel_formatter(self.vector[self.indice]))

    def get_indice(self):
        return self.indice

    def set_indice(self, indice):
        self.indice = indice
        self.set_FileNameSND("SND_"+str(self.indice)+".bin")
        self.rtlsdr_source_0.set_center_freq(self.vector[self.indice], 0)
        self.set_freq_Passa_Faixa_REAL(self._freq_Passa_Faixa_REAL_formatter(self.vector[self.indice]+ (self.vector[self.indice +  1]- self.vector[self.indice]) + self.ajuste))
        self.set_freq_Passa_Faixa(self._freq_Passa_Faixa_formatter(self.vector[self.indice+1]))
        self.band_pass_filter.set_taps(firdes.band_pass(2, self.samp_rate, (self.vector[self.indice+1] -self.vector[self.indice])-self.BandWidth+ self.ajuste, (self.vector[self.indice+1] -self.vector[self.indice])+self.BandWidth+ self.ajuste, 10e3, firdes.WIN_HAMMING, 6.76))
        self.set_FreqChannel(self._FreqChannel_formatter(self.vector[self.indice]))

    def get_ajuste(self):
        return self.ajuste

    def set_ajuste(self, ajuste):
        self.ajuste = ajuste
        self.set_freq_Passa_Faixa_REAL(self._freq_Passa_Faixa_REAL_formatter(self.vector[self.indice]+ (self.vector[self.indice +  1]- self.vector[self.indice]) + self.ajuste))
        self.band_pass_filter.set_taps(firdes.band_pass(2, self.samp_rate, (self.vector[self.indice+1] -self.vector[self.indice])-self.BandWidth+ self.ajuste, (self.vector[self.indice+1] -self.vector[self.indice])+self.BandWidth+ self.ajuste, 10e3, firdes.WIN_HAMMING, 6.76))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(2, self.samp_rate, 100e3, 10e3, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter.set_taps(firdes.band_pass(2, self.samp_rate, (self.vector[self.indice+1] -self.vector[self.indice])-self.BandWidth+ self.ajuste, (self.vector[self.indice+1] -self.vector[self.indice])+self.BandWidth+ self.ajuste, 10e3, firdes.WIN_HAMMING, 6.76))

    def get_rfgain(self):
        return self.rfgain

    def set_rfgain(self, rfgain):
        self.rfgain = rfgain
        self.rtlsdr_source_0.set_gain(self.rfgain, 0)

    def get_freq_Passa_Faixa_REAL(self):
        return self.freq_Passa_Faixa_REAL

    def set_freq_Passa_Faixa_REAL(self, freq_Passa_Faixa_REAL):
        self.freq_Passa_Faixa_REAL = freq_Passa_Faixa_REAL
        Qt.QMetaObject.invokeMethod(self._freq_Passa_Faixa_REAL_label, "setText", Qt.Q_ARG("QString", self.freq_Passa_Faixa_REAL))

    def get_freq_Passa_Faixa(self):
        return self.freq_Passa_Faixa

    def set_freq_Passa_Faixa(self, freq_Passa_Faixa):
        self.freq_Passa_Faixa = freq_Passa_Faixa
        Qt.QMetaObject.invokeMethod(self._freq_Passa_Faixa_label, "setText", Qt.Q_ARG("QString", self.freq_Passa_Faixa))

    def get_Update_Interval(self):
        return self.Update_Interval

    def set_Update_Interval(self, Update_Interval):
        self.Update_Interval = Update_Interval
        self.POTENCIA_PASSA_BAIXA_0.set_update_time(self.Update_Interval)

    def get_Quadrature(self):
        return self.Quadrature

    def set_Quadrature(self, Quadrature):
        self.Quadrature = Quadrature

    def get_NUM(self):
        return self.NUM

    def set_NUM(self, NUM):
        self.NUM = NUM

    def get_FreqChannel(self):
        return self.FreqChannel

    def set_FreqChannel(self, FreqChannel):
        self.FreqChannel = FreqChannel
        Qt.QMetaObject.invokeMethod(self._FreqChannel_label, "setText", Qt.Q_ARG("QString", self.FreqChannel))

    def get_FileNameSND(self):
        return self.FileNameSND

    def set_FileNameSND(self, FileNameSND):
        self.FileNameSND = FileNameSND
        self.blocks_file_sink_1_0.open("/home/iris/Desktop/SND/medida_SND/"+ self.FileNameSND)

    def get_BandWidth(self):
        return self.BandWidth

    def set_BandWidth(self, BandWidth):
        self.BandWidth = BandWidth
        self.band_pass_filter.set_taps(firdes.band_pass(2, self.samp_rate, (self.vector[self.indice+1] -self.vector[self.indice])-self.BandWidth+ self.ajuste, (self.vector[self.indice+1] -self.vector[self.indice])+self.BandWidth+ self.ajuste, 10e3, firdes.WIN_HAMMING, 6.76))


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
