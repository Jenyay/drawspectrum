# -*- coding: utf-8 -*-

import numpy

from basegausscontroller import BaseGaussController
from gausspanel import GaussPanel


class GaussController (BaseGaussController):
    """
    Класс контроллера для отображения сигнала и спектра гауссова сигнала
    """

    def _createPanel(self):
        return GaussPanel(self.panelParent)

    @property
    def title(self):
        return u"Гауссов импульс"

    def function(self, time):
        """
        Функция, задающая форму сигнала
        """
        return 1.0 / (self._sigma * numpy.sqrt(2.0 * numpy.pi)) * numpy.exp(-((time - self._mu) ** 2) / (2.0 * (self._sigma ** 2)))
