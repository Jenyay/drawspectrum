# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod, abstractproperty


import numpy
import numpy.fft


class Controller (metaclass=ABCMeta):
    """
    Базовый класс контроллеров для разных сигналов
    """

    def __init__(self, canvas, panelParent):
        """
        canvas - экземпляр класса GraphCanvas,
        куда будут выводиться сигнал и его спектр
        panelParent - родитель панели с параметрами сигнала
        """
        self._canvas = canvas
        self._panelParent = panelParent

        # Количество отсчетов в сигнале
        self._signalLength = 1024 * 16

        # Расстояние между отсчетами в сек
        self._dt = 1e-11

        self._panel = self._createPanel()

    @abstractmethod
    def _createPanel(self):
        pass

    @abstractproperty
    def title(self):
        pass

    @abstractmethod
    def function(self, time):
        """
        Функция, задающая форму сигнала
        """

    @abstractmethod
    def updateParams(self):
        """
        Обновить параметры функции из GUI
        """

    @property
    def panel(self):
        return self._panel

    @property
    def panelParent(self):
        return self._panelParent

    @property
    def canvas(self):
        return self._canvas

    @property
    def dt(self):
        return self._dt

    @property
    def signalLength(self):
        return self._signalLength

    def updateAndDraw(self):
        if self.updateParams():
            time, signalValues = self.signal
            freq, spectrumValues = self.spectrum

            self.canvas.drawSignal(time, signalValues)
            self.canvas.drawSpectrum(freq, spectrumValues)

    @property
    def signal(self):
        time = numpy.arange(0.0, self.signalLength) * self.dt
        return (time, self.function(time))

    @property
    def spectrum(self):
        df = 1.0 / (self.signalLength * self.dt)
        freq = numpy.arange(self.signalLength / 2 + 1) * df
        spectrum = numpy.abs(numpy.fft.rfft(
            self.signal[1])) / self.signalLength

        return freq, spectrum
