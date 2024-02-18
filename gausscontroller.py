# -*- coding: utf-8 -*-

import numpy

from basegausscontroller import BaseGaussController
from gausspanel import GaussPanel


class GaussController(BaseGaussController):
    """
    Класс контроллера для отображения сигнала и спектра гауссова сигнала
    """

    def _createPanel(self):
        return GaussPanel(self.panelParent)

    @property
    def title(self):
        return "Гауссов импульс"

    def function(self, time):
        """
        Функция, задающая форму сигнала
        """
        return numpy.exp(-((time - self._mu) ** 2) / (self._sigma**2))
