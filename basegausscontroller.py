# -*- coding: utf-8 -*-

from abc import ABCMeta

import wx

from controller import Controller


class BaseGaussController (Controller, metaclass=ABCMeta):
    """
    Базовый класс для контроллеров на основе функции Гаусса
    """

    def __init__(self, canvas, panelParent):
        """
        canvas - экземпляр класса GraphCanvas,
        куда будут выводиться сигнал и его спектр
        panelParent - родитель панели с параметрами сигнала
        """
        super(BaseGaussController, self).__init__(canvas, panelParent)

        self._sigma = 0.5e-9
        self._mu = 4.0e-9

        self.panel.sigma = self._sigma / 1.0e-9
        self.panel.mu = self._mu / 1.0e-9

    def updateParams(self):
        try:
            self._sigma = self.panel.sigma * 1.0e-9
        except ValueError:
            wx.MessageBox(u"Ошибка формата в поле '\u03c3'",
                          u"Ошибка", wx.OK | wx.ICON_ERROR)
            return False

        try:
            self._mu = self.panel.mu * 1.0e-9
        except ValueError:
            wx.MessageBox(u"Ошибка формата в поле '\u03bc'",
                          u"Ошибка", wx.OK | wx.ICON_ERROR)
            return False

        return True
