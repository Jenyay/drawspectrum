# -*- coding: utf-8 -*-

import wx

import numpy
import matplotlib.figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg


class GraphCanvas(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self._createCanvas()

    def _createCanvas(self):
        """
        Создание канвы для рисования
        """
        canvasSizer = wx.FlexGridSizer(cols=1)
        canvasSizer.AddGrowableRow(0)
        canvasSizer.AddGrowableCol(0)

        # 1. Создание фигуры
        self.figure = matplotlib.figure.Figure()
        self.figure.subplots_adjust(0.1, 0.1, 0.95, 0.95)

        # 2. Создание осей
        # Оси для сигнала
        self.signalAxes = self.figure.add_subplot(2, 1, 1)

        # Оси для амплитудного спектра
        self.ampSpectrumAxes = self.figure.add_subplot(2, 1, 2)

        # 3. Создание панели для рисования с помощью Matplotlib
        self.canvas = FigureCanvasWxAgg(self, -1, self.figure)
        self.canvas.SetMinSize((100, 100))

        self.updateAxesView()

        canvasSizer.Add(self.canvas, 1, flag=wx.EXPAND | wx.ALL, border=2)

        self.SetSizer(canvasSizer)
        self.Layout()

    def drawSignal(self, time, values):
        self._draw(self.signalAxes, time / 1e-9, values)
        self.signalAxes.set_xlim([0, 10])

        ymargin = (numpy.max(values) - numpy.min(values)) * 0.1 / 2
        self.signalAxes.set_ylim(
            [numpy.min(values) - ymargin, numpy.max(values) + ymargin]
        )

        self.updateAxesView()
        self.canvas.draw()

    def drawSpectrum(self, freq, values):
        self._draw(self.ampSpectrumAxes, freq / 1e9, values)
        self.ampSpectrumAxes.set_xlim([-0.5, 10])

        self.updateAxesView()
        self.canvas.draw()

    def updateAxesView(self):
        self.signalAxes.set_xlabel(
            "t, с", fontdict={"family": "verdana", "size": "small"}
        )
        self.signalAxes.set_ylabel("В", fontdict={"family": "verdana", "size": "small"})

        self.ampSpectrumAxes.set_xlabel(
            "f, ГГц", fontdict={"family": "verdana", "size": "small"}
        )
        self.ampSpectrumAxes.set_ylabel(
            "В / Гц", fontdict={"family": "verdana", "size": "small"}
        )

    def _draw(self, axes, xval, yval):
        axes.clear()
        axes.plot(xval, yval)
        axes.grid()
