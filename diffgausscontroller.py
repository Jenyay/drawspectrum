# -*- coding: utf-8 -*-

import numpy

from basegausscontroller import BaseGaussController
from diffgausspanel import DiffGaussPanel


class DiffGaussController(BaseGaussController):
    """
    Класс контроллера для отображения сигнала и спектра сигнала в виде
    дифференцированного гауссова импульса
    """

    def _createPanel(self):
        return DiffGaussPanel(self.panelParent)

    @property
    def title(self):
        return "Дифференцированный гауссов импульс"

    def function(self, time):
        """
        Функция, задающая форму сигнала
        """
        return (
            -2 * (time - self._mu)
            / self._sigma
            * numpy.exp(-((time - self._mu) ** 2) / (self._sigma**2))
        )
