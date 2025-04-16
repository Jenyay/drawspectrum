# -*- coding: utf-8 -*-

import numpy
import wx

from controller import Controller
from sinpanel import SinPanel


class SinController(Controller):
    """
    Класс контроллера для отображения сигнала и спектра одной синусоиды
    """

    def __init__(self, canvas, panelParent):
        """
        canvas - экземпляр класса GraphCanvas, куда будут выводиться сигнал
        и его спектр
        panelParent - родитель панели с параметрами сигнала
        """
        super(SinController, self).__init__(canvas, panelParent)

        # Частота синусоиды (в Гц)
        self._freq = 1.0e9

        # Начальная фаза (в градусах)
        self._phase = 90.0

        # Амплитуда синусоиды
        self._amplitude = 1.0

        self.panel.frequency = self._freq / 1e9

    def updateParams(self):
        try:
            self._freq = self.panel.frequency * 1.0e9
        except ValueError:
            wx.MessageBox(
                "Ошибка формата в поле 'Частота'", "Ошибка", wx.OK | wx.ICON_ERROR
            )
            return False

        return True

    def _createPanel(self):
        return SinPanel(self.panelParent)

    @property
    def title(self):
        return "cos"

    def function(self, time):
        """
        Функция, задающая форму сигнала
        """
        return self._amplitude * numpy.sin(
            2.0 * numpy.pi * self._freq * time + numpy.radians(self._phase)
        )
