# -*- coding: utf-8 -*-

import numpy
import wx

from controller import Controller
from rectpanel import RectPanel


class RectController(Controller):
    """
    Класс контроллера для отображения сигнала и спектра прямоугольного импульса
    """

    def __init__(self, canvas, panelParent):
        """
        canvas - экземпляр класса GraphCanvas, куда будут выводиться сигнал
        и его спектр
        panelParent - родитель панели с параметрами сигнала
        """
        super(RectController, self).__init__(canvas, panelParent)

        # Длительность сигнала (с)
        self._length = 1.0e-9

        # Амплитуда меандра
        self._amplitude = 1.0

        self.panel.length = self._length / 1e-9

    def updateParams(self):
        try:
            self._length = self.panel.length * 1.0e-9
        except ValueError:
            wx.MessageBox(
                "Ошибка формата в поле 'Длительность сигнала'",
                "Ошибка",
                wx.OK | wx.ICON_ERROR,
            )
            return False

        return True

    def _createPanel(self):
        return RectPanel(self.panelParent)

    @property
    def title(self):
        return "Прямоугольный импульс"

    def function(self, time):
        """
        Функция, задающая форму сигнала
        """
        return self._amplitude * numpy.array(
            [1.0 if t <= self._length else 0.0 for t in time]
        )
