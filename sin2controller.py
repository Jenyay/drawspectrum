# -*- coding: utf-8 -*-

import numpy
import wx

from controller import Controller
from sin2panel import Sin2Panel


class Sin2Controller(Controller):
    """
    Класс контроллера для отображения сигнала и спектра двух синусоид
    """

    def __init__(self, canvas, panelParent):
        """
        canvas - экземпляр класса GraphCanvas, куда будут выводиться сигнал
        и его спектр
        panelParent - родитель панели с параметрами сигнала
        """
        super(Sin2Controller, self).__init__(canvas, panelParent)

        # Частоты синусоид (в Гц)
        self._freq = [1.0e9, 2.0e9]

        # Начальная фаза (в градусах)
        self._phase = [90.0, 90.0]

        # Амплитуда синусоид
        self._amplitude = [1.0, 0.5]

        self.panel.frequency1 = self._freq[0] / 1e9
        self.panel.frequency2 = self._freq[1] / 1e9
        self.panel.amplitude1 = self._amplitude[0]
        self.panel.amplitude2 = self._amplitude[1]

    def updateParams(self):
        try:
            self._freq[0] = float(self.panel.frequency1) * 1.0e9
            self._freq[1] = float(self.panel.frequency2) * 1.0e9
        except ValueError:
            wx.MessageBox(
                "Ошибка формата в поле 'Частота'", "Ошибка", wx.OK | wx.ICON_ERROR
            )
            return False

        try:
            self._amplitude[0] = float(self.panel.amplitude1)
            self._amplitude[1] = float(self.panel.amplitude2)
        except ValueError:
            wx.MessageBox(
                "Ошибка формата в поле 'Амплитуда'", "Ошибка", wx.OK | wx.ICON_ERROR
            )
            return False

        return True

    def _createPanel(self):
        return Sin2Panel(self.panelParent)

    @property
    def title(self):
        return "cos + cos"

    def function(self, time):
        """
        Функция, задающая форму сигнала
        """
        result = 0
        for freq, phase, amp in zip(self._freq, self._phase, self._amplitude):
            result = result + amp * numpy.sin(
                2.0 * numpy.pi * freq * time + numpy.radians(phase)
            )

        return result
