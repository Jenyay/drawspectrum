# -*- coding: utf-8 -*-

import numpy
import wx

from controller import Controller
from meanderpanel import MeanderPanel


class MeanderController(Controller):
    """
    Класс контроллера для отображения сигнала и спектра меандра
    """

    def __init__(self, canvas, panelParent):
        """
        canvas - экземпляр класса GraphCanvas, куда будут выводиться сигнал
        и его спектр
        panelParent - родитель панели с параметрами сигнала
        """
        super(MeanderController, self).__init__(canvas, panelParent)

        # Период повторения (в с)
        self._period = 2.0e-9

        # Амплитуда меандра
        self._amplitude = 1.0

        # Скважность
        self._duty = 0.2

        self.panel.period = self._period / 1e-9
        self.panel.duty = self._duty

    def updateParams(self):
        try:
            self._period = self.panel.period * 1.0e-9
        except ValueError:
            wx.MessageBox(
                "Ошибка формата в поле 'Период'", "Ошибка", wx.OK | wx.ICON_ERROR
            )
            return False

        try:
            self._duty = self.panel.duty
        except ValueError:
            wx.MessageBox(
                "Ошибка формата в поле 'Скважность'", "Ошибка", wx.OK | wx.ICON_ERROR
            )
            return False

        return True

    def _createPanel(self):
        return MeanderPanel(self.panelParent)

    @property
    def title(self):
        return "Последовательность видеоимпульсов"

    def function(self, time):
        """
        Функция, задающая форму сигнала
        """
        newtime = (
            numpy.arcsin(numpy.sin(2.0 * numpy.pi / self._period * time + numpy.pi / 2))
            + numpy.pi / 2
        )
        return self._amplitude * numpy.array(
            [1.0 if t <= numpy.pi * self._duty else 0.0 for t in newtime]
        )
