# -*- coding: utf-8 -*-

import numpy

from basegausscontroller import BaseGaussController
from diffgausspanel import DiffGaussPanel


class DiffGaussController (BaseGaussController):
    """
    Класс контроллера для отображения сигнала и спектра сигнала в виде
    дифференцированного гауссова импульса
    """
    def _createPanel(self):
        return DiffGaussPanel(self.panelParent)

    @property
    def title(self):
        return u"Дифференцированный гауссов импульс"

    def function(self, time):
        """
        Функция, задающая форму сигнала
        """
        return -(time - self._mu) / ((self._sigma ** 3) * numpy.sqrt(2.0 * numpy.pi)) * numpy.exp(-((time - self._mu) ** 2) / (2.0 * (self._sigma ** 2)))
