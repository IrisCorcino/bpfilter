#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun Apr 22 21:50:15 2018
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
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import math
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
        self.indice = indice = 34
        self.bw = bw = 100e3
        self.samp_rate = samp_rate = 3e6
        self.freq_Passa_Faixa = freq_Passa_Faixa = vector[indice+1]
        self.freq_Passa_Baixa = freq_Passa_Baixa = vector[indice]
        self.down_rate = down_rate = 25e4
        self.ajuste = ajuste = 0
        self.LCF = LCF = (vector[indice+1] -vector[indice])-bw
        self.HCF = HCF = (vector[indice+1] -vector[indice])+bw

        ##################################################
        # Blocks
        ##################################################
        self._indice_range = Range(0, 39, 1, 34, 2)
        self._indice_win = RangeWidget(self._indice_range, self.set_indice, "indice", "counter", int)
        self.top_grid_layout.addWidget(self._indice_win, 3,4,1,3)
        self._ajuste_range = Range(-100e3, 100e3, 100, 0, 100)
        self._ajuste_win = RangeWidget(self._ajuste_range, self.set_ajuste, "ajuste", "counter_slider", float)
        self.top_grid_layout.addWidget(self._ajuste_win, 2,0,1,3)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(vector[indice], 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(2, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(2, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(70, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna('', 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)

        self.qtgui_freq_sink_x_1_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	vector[indice]+ (vector[indice +  1]- vector[indice]) + ajuste, #fc
        	samp_rate, #bw
        	'Filtro Passa Faixa', #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_1_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1_0.set_y_label('Ganho Relativo', 'dB')
        self.qtgui_freq_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_1_0.enable_grid(False)
        self.qtgui_freq_sink_x_1_0.set_fft_average(0.1)
        self.qtgui_freq_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_1_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_0_win, 4,3,1,3)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	vector[indice], #fc
        	samp_rate, #bw
        	'antes de filtrar', #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(0.05)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_1.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_win, 4,0,1,3)
        self._freq_Passa_Faixa_tool_bar = Qt.QToolBar(self)

        if None:
          self._freq_Passa_Faixa_formatter = None
        else:
          self._freq_Passa_Faixa_formatter = lambda x: eng_notation.num_to_str(x)

        self._freq_Passa_Faixa_tool_bar.addWidget(Qt.QLabel("freq_Passa_Faixa"+": "))
        self._freq_Passa_Faixa_label = Qt.QLabel(str(self._freq_Passa_Faixa_formatter(self.freq_Passa_Faixa)))
        self._freq_Passa_Faixa_tool_bar.addWidget(self._freq_Passa_Faixa_label)
        self.top_grid_layout.addWidget(self._freq_Passa_Faixa_tool_bar, 3,2,1,3)

        self._freq_Passa_Baixa_tool_bar = Qt.QToolBar(self)

        if None:
          self._freq_Passa_Baixa_formatter = None
        else:
          self._freq_Passa_Baixa_formatter = lambda x: eng_notation.num_to_str(x)

        self._freq_Passa_Baixa_tool_bar.addWidget(Qt.QLabel("freq_Passa_Baixa"+": "))
        self._freq_Passa_Baixa_label = Qt.QLabel(str(self._freq_Passa_Baixa_formatter(self.freq_Passa_Baixa)))
        self._freq_Passa_Baixa_tool_bar.addWidget(self._freq_Passa_Baixa_label)
        self.top_grid_layout.addWidget(self._freq_Passa_Baixa_tool_bar, 3,0,1,3)

        self.band_pass_filter = filter.fir_filter_ccf(8, firdes.band_pass(
        	2, samp_rate, LCF + ajuste, HCF + ajuste, 10e3, firdes.WIN_HAMMING, 6.76))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter, 0), (self.qtgui_freq_sink_x_1_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.band_pass_filter, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.qtgui_freq_sink_x_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_vector(self):
        return self.vector

    def set_vector(self, vector):
        self.vector = vector
        self.set_LCF((self.vector[self.indice+1] -self.vector[self.indice])-self.bw)
        self.set_HCF((self.vector[self.indice+1] -self.vector[self.indice])+self.bw)
        self.rtlsdr_source_0.set_center_freq(self.vector[self.indice], 0)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(self.vector[self.indice]+ (self.vector[self.indice +  1]- self.vector[self.indice]) + self.ajuste, self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(self.vector[self.indice], self.samp_rate)
        self.set_freq_Passa_Faixa(self._freq_Passa_Faixa_formatter(self.vector[self.indice+1]))
        self.set_freq_Passa_Baixa(self._freq_Passa_Baixa_formatter(self.vector[self.indice]))

    def get_indice(self):
        return self.indice

    def set_indice(self, indice):
        self.indice = indice
        self.set_LCF((self.vector[self.indice+1] -self.vector[self.indice])-self.bw)
        self.set_HCF((self.vector[self.indice+1] -self.vector[self.indice])+self.bw)
        self.rtlsdr_source_0.set_center_freq(self.vector[self.indice], 0)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(self.vector[self.indice]+ (self.vector[self.indice +  1]- self.vector[self.indice]) + self.ajuste, self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(self.vector[self.indice], self.samp_rate)
        self.set_freq_Passa_Faixa(self._freq_Passa_Faixa_formatter(self.vector[self.indice+1]))
        self.set_freq_Passa_Baixa(self._freq_Passa_Baixa_formatter(self.vector[self.indice]))

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw
        self.set_LCF((self.vector[self.indice+1] -self.vector[self.indice])-self.bw)
        self.set_HCF((self.vector[self.indice+1] -self.vector[self.indice])+self.bw)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(self.vector[self.indice]+ (self.vector[self.indice +  1]- self.vector[self.indice]) + self.ajuste, self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(self.vector[self.indice], self.samp_rate)
        self.band_pass_filter.set_taps(firdes.band_pass(2, self.samp_rate, self.LCF + self.ajuste, self.HCF + self.ajuste, 10e3, firdes.WIN_HAMMING, 6.76))

    def get_freq_Passa_Faixa(self):
        return self.freq_Passa_Faixa

    def set_freq_Passa_Faixa(self, freq_Passa_Faixa):
        self.freq_Passa_Faixa = freq_Passa_Faixa
        Qt.QMetaObject.invokeMethod(self._freq_Passa_Faixa_label, "setText", Qt.Q_ARG("QString", self.freq_Passa_Faixa))

    def get_freq_Passa_Baixa(self):
        return self.freq_Passa_Baixa

    def set_freq_Passa_Baixa(self, freq_Passa_Baixa):
        self.freq_Passa_Baixa = freq_Passa_Baixa
        Qt.QMetaObject.invokeMethod(self._freq_Passa_Baixa_label, "setText", Qt.Q_ARG("QString", self.freq_Passa_Baixa))

    def get_down_rate(self):
        return self.down_rate

    def set_down_rate(self, down_rate):
        self.down_rate = down_rate

    def get_ajuste(self):
        return self.ajuste

    def set_ajuste(self, ajuste):
        self.ajuste = ajuste
        self.qtgui_freq_sink_x_1_0.set_frequency_range(self.vector[self.indice]+ (self.vector[self.indice +  1]- self.vector[self.indice]) + self.ajuste, self.samp_rate)
        self.band_pass_filter.set_taps(firdes.band_pass(2, self.samp_rate, self.LCF + self.ajuste, self.HCF + self.ajuste, 10e3, firdes.WIN_HAMMING, 6.76))

    def get_LCF(self):
        return self.LCF

    def set_LCF(self, LCF):
        self.LCF = LCF
        self.band_pass_filter.set_taps(firdes.band_pass(2, self.samp_rate, self.LCF + self.ajuste, self.HCF + self.ajuste, 10e3, firdes.WIN_HAMMING, 6.76))

    def get_HCF(self):
        return self.HCF

    def set_HCF(self, HCF):
        self.HCF = HCF
        self.band_pass_filter.set_taps(firdes.band_pass(2, self.samp_rate, self.LCF + self.ajuste, self.HCF + self.ajuste, 10e3, firdes.WIN_HAMMING, 6.76))


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
