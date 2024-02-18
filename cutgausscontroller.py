# -*- coding: utf-8 -*-

import numpy

from basegausscontroller import BaseGaussController
from cutgausspanel import CutGaussPanel


class CutGaussController (BaseGaussController):
    """
    Класс контроллера для отображения сигнала и спектра гауссова сигнала
    со ступенькой
    """

    def __init__(self, canvas, panelParent):
        super().__init__(canvas, panelParent)
        self._t0 = 5e-9
        self.panel.t0 = self._t0 / 1e-9

    def updateParams(self):
        if not super().updateParams():
            return False

        try:
            self._t0 = self.panel.t0 * 1.0e-9
        except ValueError:
            wx.MessageBox(u"Ошибка формата в поле 't0'",
                          u"Ошибка", wx.OK | wx.ICON_ERROR)
            return False

        return True

    def _createPanel(self):
        return CutGaussPanel(self.panelParent)

    @property
    def title(self):
        return u"Гауссов импульс со ступенькой"

    def function(self, time):
        """
        Функция, задающая форму сигнала
        """
        return numpy.array([1.0 / (self._sigma * numpy.sqrt(2.0 * numpy.pi)) * numpy.exp(-((t - self._mu) ** 2) / (2.0 * (self._sigma ** 2))) if t < self._t0 else 0
                            for t in time])
