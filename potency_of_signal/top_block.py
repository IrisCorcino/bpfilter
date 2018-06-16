#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Jun 15 21:53:59 2018
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
        self.indice = indice = 0
        self.vector = vector = (88.1e6,89.1e6,89.7e6,90.1e6,90.5e6,90.9e6,91.3e6,92.1e6,92.5e6,92.9e6,93.7e6,94.1e6,94.7e6,95.3e6,95.7e6,96.1e6,96.5e6,96.9e6,97.3e6,97.7e6,98.1e6,98.5e6,98.9e6,99.3e6,100.1e6,100.9e6,101.3e6,101.5e6,101.7e6,102.1e6,102.5e6,103.3e6,104.1e6,104.3e6,104.7e6,105.1e6,105.7e6,106.3e6,106.9e6,107.3e6,107.9e6)
        self.ajuste = ajuste = 0
        self.FileNameCP = FileNameCP = "CP_"+str(indice)+".bin"
        self.FileNameCAS = FileNameCAS = "CAS_"+str(indice+1)+".bin"
        self.samp_rate = samp_rate = 2.4e6
        self.freq_Passa_Faixa_REAL = freq_Passa_Faixa_REAL = vector[indice]+ (vector[indice +  1]- vector[indice]) + ajuste
        self.freq_Passa_Faixa = freq_Passa_Faixa = vector[indice+1]
        self.freq_Passa_Baixa = freq_Passa_Baixa = vector[indice]
        self.down_rate = down_rate = 25e4
        self.bw = bw = 100e3
        self.Update_Interval = Update_Interval = 0.1
        self.AddressCas = AddressCas = "/home/iris/Desktop/medidas/"+ FileNameCAS
        self.AddressCP = AddressCP = "/home/iris/Desktop/medidas/"+ FileNameCP

        ##################################################
        # Blocks
        ##################################################
        self._indice_range = Range(0, 40, 1, 0, 2)
        self._indice_win = RangeWidget(self._indice_range, self.set_indice, "indice", "counter", int)
        self.top_grid_layout.addWidget(self._indice_win, 2,3,1,3)
        self._ajuste_range = Range(-600e3, 600e3, 100, 0, 300)
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

        self.qtgui_freq_sink_x_1_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	vector[indice], #fc
        	samp_rate, #bw
        	'Filtro Passa Baixa', #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1_1.set_y_label('Ganho Relativo', 'dB')
        self.qtgui_freq_sink_x_1_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1_1.enable_grid(False)
        self.qtgui_freq_sink_x_1_1.set_fft_average(0.1)
        self.qtgui_freq_sink_x_1_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1_1.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_1_1.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1_1.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_x_1_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_1_win, 6,0,1,3)
        self.qtgui_freq_sink_x_1_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	vector[indice]+ (vector[indice +  1]- vector[indice]) + ajuste, #fc
        	samp_rate, #bw
        	'Filtro Passa Faixa', #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1_0.set_update_time(Update_Interval/10)
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_0_win, 6,4,1,3)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	vector[indice], #fc
        	samp_rate, #bw
        	'antes de filtrar', #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(Update_Interval/10)
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_win, 5,0,1,6)
        self.low_pass_filter_0_1 = filter.fir_filter_ccf(8, firdes.low_pass(
        	2, samp_rate, 100e3, 10e3, firdes.WIN_HAMMING, 6.76))
        self._freq_Passa_Faixa_REAL_tool_bar = Qt.QToolBar(self)

        if None:
          self._freq_Passa_Faixa_REAL_formatter = None
        else:
          self._freq_Passa_Faixa_REAL_formatter = lambda x: eng_notation.num_to_str(x)

        self._freq_Passa_Faixa_REAL_tool_bar.addWidget(Qt.QLabel('Freq (Chanel +1) + ajuste (PF)'+": "))
        self._freq_Passa_Faixa_REAL_label = Qt.QLabel(str(self._freq_Passa_Faixa_REAL_formatter(self.freq_Passa_Faixa_REAL)))
        self._freq_Passa_Faixa_REAL_tool_bar.addWidget(self._freq_Passa_Faixa_REAL_label)
        self.top_grid_layout.addWidget(self._freq_Passa_Faixa_REAL_tool_bar, 3,5,1,3)

        self._freq_Passa_Faixa_tool_bar = Qt.QToolBar(self)

        if None:
          self._freq_Passa_Faixa_formatter = None
        else:
          self._freq_Passa_Faixa_formatter = lambda x: eng_notation.num_to_str(x)

        self._freq_Passa_Faixa_tool_bar.addWidget(Qt.QLabel('Freq(chanel + 1)'+": "))
        self._freq_Passa_Faixa_label = Qt.QLabel(str(self._freq_Passa_Faixa_formatter(self.freq_Passa_Faixa)))
        self._freq_Passa_Faixa_tool_bar.addWidget(self._freq_Passa_Faixa_label)
        self.top_grid_layout.addWidget(self._freq_Passa_Faixa_tool_bar, 3,3,1,3)

        self._freq_Passa_Baixa_tool_bar = Qt.QToolBar(self)

        if None:
          self._freq_Passa_Baixa_formatter = None
        else:
          self._freq_Passa_Baixa_formatter = lambda x: eng_notation.num_to_str(x)

        self._freq_Passa_Baixa_tool_bar.addWidget(Qt.QLabel('Freq (Chanel)'+": "))
        self._freq_Passa_Baixa_label = Qt.QLabel(str(self._freq_Passa_Baixa_formatter(self.freq_Passa_Baixa)))
        self._freq_Passa_Baixa_tool_bar.addWidget(self._freq_Passa_Baixa_label)
        self.top_grid_layout.addWidget(self._freq_Passa_Baixa_tool_bar, 3,0,1,3)

        self.blocks_rms_xx_1 = blocks.rms_cf(0.0001)
        self.blocks_rms_xx_0 = blocks.rms_cf(0.0001)
        self.blocks_nlog10_ff_0_1 = blocks.nlog10_ff(20, 1, 1)
        self.blocks_nlog10_ff_0_0 = blocks.nlog10_ff(20, 1, 1)
        self.blocks_file_sink_1 = blocks.file_sink(gr.sizeof_float*1, AddressCP, False)
        self.blocks_file_sink_1.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1, AddressCas, False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.band_pass_filter = filter.fir_filter_ccf(8, firdes.band_pass(
        	2, samp_rate, (vector[indice+1] -vector[indice])-bw + ajuste, (vector[indice+1] -vector[indice])+bw+ ajuste, 10e3, firdes.WIN_HAMMING, 6.76))
        self.POTENCIA_PASSA_FAIXA = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1
        )
        self.POTENCIA_PASSA_FAIXA.set_update_time(Update_Interval)
        self.POTENCIA_PASSA_FAIXA.set_title('POT_CAS (dB)')

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.POTENCIA_PASSA_FAIXA.set_min(i, -1)
            self.POTENCIA_PASSA_FAIXA.set_max(i, 1)
            self.POTENCIA_PASSA_FAIXA.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.POTENCIA_PASSA_FAIXA.set_label(i, "Data {0}".format(i))
            else:
                self.POTENCIA_PASSA_FAIXA.set_label(i, labels[i])
            self.POTENCIA_PASSA_FAIXA.set_unit(i, units[i])
            self.POTENCIA_PASSA_FAIXA.set_factor(i, factor[i])

        self.POTENCIA_PASSA_FAIXA.enable_autoscale(False)
        self._POTENCIA_PASSA_FAIXA_win = sip.wrapinstance(self.POTENCIA_PASSA_FAIXA.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._POTENCIA_PASSA_FAIXA_win, 4,3,1,3)
        self.POTENCIA_PASSA_BAIXA = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1
        )
        self.POTENCIA_PASSA_BAIXA.set_update_time(Update_Interval)
        self.POTENCIA_PASSA_BAIXA.set_title('POT_CP (dB)')

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.POTENCIA_PASSA_BAIXA.set_min(i, -1)
            self.POTENCIA_PASSA_BAIXA.set_max(i, 1)
            self.POTENCIA_PASSA_BAIXA.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.POTENCIA_PASSA_BAIXA.set_label(i, "Data {0}".format(i))
            else:
                self.POTENCIA_PASSA_BAIXA.set_label(i, labels[i])
            self.POTENCIA_PASSA_BAIXA.set_unit(i, units[i])
            self.POTENCIA_PASSA_BAIXA.set_factor(i, factor[i])

        self.POTENCIA_PASSA_BAIXA.enable_autoscale(False)
        self._POTENCIA_PASSA_BAIXA_win = sip.wrapinstance(self.POTENCIA_PASSA_BAIXA.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._POTENCIA_PASSA_BAIXA_win, 4,0,1,3)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter, 0), (self.blocks_rms_xx_0, 0))
        self.connect((self.band_pass_filter, 0), (self.qtgui_freq_sink_x_1_0, 0))
        self.connect((self.blocks_nlog10_ff_0_0, 0), (self.POTENCIA_PASSA_BAIXA, 0))
        self.connect((self.blocks_nlog10_ff_0_0, 0), (self.blocks_file_sink_1, 0))
        self.connect((self.blocks_nlog10_ff_0_1, 0), (self.POTENCIA_PASSA_FAIXA, 0))
        self.connect((self.blocks_nlog10_ff_0_1, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_rms_xx_0, 0), (self.blocks_nlog10_ff_0_1, 0))
        self.connect((self.blocks_rms_xx_1, 0), (self.blocks_nlog10_ff_0_0, 0))
        self.connect((self.low_pass_filter_0_1, 0), (self.blocks_rms_xx_1, 0))
        self.connect((self.low_pass_filter_0_1, 0), (self.qtgui_freq_sink_x_1_1, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.band_pass_filter, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.low_pass_filter_0_1, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.qtgui_freq_sink_x_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_indice(self):
        return self.indice

    def set_indice(self, indice):
        self.indice = indice
        self.rtlsdr_source_0.set_center_freq(self.vector[self.indice], 0)
        self.qtgui_freq_sink_x_1_1.set_frequency_range(self.vector[self.indice], self.samp_rate)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(self.vector[self.indice]+ (self.vector[self.indice +  1]- self.vector[self.indice]) + self.ajuste, self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(self.vector[self.indice], self.samp_rate)
        self.set_freq_Passa_Faixa_REAL(self._freq_Passa_Faixa_REAL_formatter(self.vector[self.indice]+ (self.vector[self.indice +  1]- self.vector[self.indice]) + self.ajuste))
        self.set_freq_Passa_Faixa(self._freq_Passa_Faixa_formatter(self.vector[self.indice+1]))
        self.set_freq_Passa_Baixa(self._freq_Passa_Baixa_formatter(self.vector[self.indice]))
        self.band_pass_filter.set_taps(firdes.band_pass(2, self.samp_rate, (self.vector[self.indice+1] -self.vector[self.indice])-self.bw + self.ajuste, (self.vector[self.indice+1] -self.vector[self.indice])+self.bw+ self.ajuste, 10e3, firdes.WIN_HAMMING, 6.76))
        self.set_FileNameCP("CP_"+str(self.indice)+".bin")
        self.set_FileNameCAS("CAS_"+str(self.indice+1)+".bin")

    def get_vector(self):
        return self.vector

    def set_vector(self, vector):
        self.vector = vector
        self.rtlsdr_source_0.set_center_freq(self.vector[self.indice], 0)
        self.qtgui_freq_sink_x_1_1.set_frequency_range(self.vector[self.indice], self.samp_rate)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(self.vector[self.indice]+ (self.vector[self.indice +  1]- self.vector[self.indice]) + self.ajuste, self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(self.vector[self.indice], self.samp_rate)
        self.set_freq_Passa_Faixa_REAL(self._freq_Passa_Faixa_REAL_formatter(self.vector[self.indice]+ (self.vector[self.indice +  1]- self.vector[self.indice]) + self.ajuste))
        self.set_freq_Passa_Faixa(self._freq_Passa_Faixa_formatter(self.vector[self.indice+1]))
        self.set_freq_Passa_Baixa(self._freq_Passa_Baixa_formatter(self.vector[self.indice]))
        self.band_pass_filter.set_taps(firdes.band_pass(2, self.samp_rate, (self.vector[self.indice+1] -self.vector[self.indice])-self.bw + self.ajuste, (self.vector[self.indice+1] -self.vector[self.indice])+self.bw+ self.ajuste, 10e3, firdes.WIN_HAMMING, 6.76))

    def get_ajuste(self):
        return self.ajuste

    def set_ajuste(self, ajuste):
        self.ajuste = ajuste
        self.qtgui_freq_sink_x_1_0.set_frequency_range(self.vector[self.indice]+ (self.vector[self.indice +  1]- self.vector[self.indice]) + self.ajuste, self.samp_rate)
        self.set_freq_Passa_Faixa_REAL(self._freq_Passa_Faixa_REAL_formatter(self.vector[self.indice]+ (self.vector[self.indice +  1]- self.vector[self.indice]) + self.ajuste))
        self.band_pass_filter.set_taps(firdes.band_pass(2, self.samp_rate, (self.vector[self.indice+1] -self.vector[self.indice])-self.bw + self.ajuste, (self.vector[self.indice+1] -self.vector[self.indice])+self.bw+ self.ajuste, 10e3, firdes.WIN_HAMMING, 6.76))

    def get_FileNameCP(self):
        return self.FileNameCP

    def set_FileNameCP(self, FileNameCP):
        self.FileNameCP = FileNameCP
        self.set_AddressCP("/home/iris/Desktop/medidas/"+ self.FileNameCP)

    def get_FileNameCAS(self):
        return self.FileNameCAS

    def set_FileNameCAS(self, FileNameCAS):
        self.FileNameCAS = FileNameCAS
        self.set_AddressCas("/home/iris/Desktop/medidas/"+ self.FileNameCAS)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_1_1.set_frequency_range(self.vector[self.indice], self.samp_rate)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(self.vector[self.indice]+ (self.vector[self.indice +  1]- self.vector[self.indice]) + self.ajuste, self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(self.vector[self.indice], self.samp_rate)
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(2, self.samp_rate, 100e3, 10e3, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter.set_taps(firdes.band_pass(2, self.samp_rate, (self.vector[self.indice+1] -self.vector[self.indice])-self.bw + self.ajuste, (self.vector[self.indice+1] -self.vector[self.indice])+self.bw+ self.ajuste, 10e3, firdes.WIN_HAMMING, 6.76))

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

    def get_freq_Passa_Baixa(self):
        return self.freq_Passa_Baixa

    def set_freq_Passa_Baixa(self, freq_Passa_Baixa):
        self.freq_Passa_Baixa = freq_Passa_Baixa
        Qt.QMetaObject.invokeMethod(self._freq_Passa_Baixa_label, "setText", Qt.Q_ARG("QString", self.freq_Passa_Baixa))

    def get_down_rate(self):
        return self.down_rate

    def set_down_rate(self, down_rate):
        self.down_rate = down_rate

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw
        self.band_pass_filter.set_taps(firdes.band_pass(2, self.samp_rate, (self.vector[self.indice+1] -self.vector[self.indice])-self.bw + self.ajuste, (self.vector[self.indice+1] -self.vector[self.indice])+self.bw+ self.ajuste, 10e3, firdes.WIN_HAMMING, 6.76))

    def get_Update_Interval(self):
        return self.Update_Interval

    def set_Update_Interval(self, Update_Interval):
        self.Update_Interval = Update_Interval
        self.qtgui_freq_sink_x_1_0.set_update_time(self.Update_Interval/10)
        self.qtgui_freq_sink_x_1.set_update_time(self.Update_Interval/10)
        self.POTENCIA_PASSA_FAIXA.set_update_time(self.Update_Interval)
        self.POTENCIA_PASSA_BAIXA.set_update_time(self.Update_Interval)

    def get_AddressCas(self):
        return self.AddressCas

    def set_AddressCas(self, AddressCas):
        self.AddressCas = AddressCas
        self.blocks_file_sink_0.open(self.AddressCas)

    def get_AddressCP(self):
        return self.AddressCP

    def set_AddressCP(self, AddressCP):
        self.AddressCP = AddressCP
        self.blocks_file_sink_1.open(self.AddressCP)


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
