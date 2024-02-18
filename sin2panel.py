# -*- coding: utf-8 -*-

import wx


class Sin2Panel(wx.Panel):
    """
    Панель для настроек параметров сигнала в виде одной синусоиды
    """

    def __init__(self, parent):
        super(Sin2Panel, self).__init__(parent)

        self._createGui()

    def _createGui(self):
        mainSizer = wx.FlexGridSizer(cols=2)
        mainSizer.AddGrowableCol(0)
        mainSizer.AddGrowableCol(1)

        # Параметры первой гармоники
        freqLabel1 = wx.StaticText(self, label="Частота 1 (ГГц)")
        self.freqText1 = wx.TextCtrl(self)
        self.freqText1.SetMinSize((150, -1))

        ampLabel1 = wx.StaticText(self, label="Амплитуда 1 (В)")
        self.ampText1 = wx.TextCtrl(self)
        self.ampText1.SetMinSize((150, -1))

        # Параметры второй гармоники
        freqLabel2 = wx.StaticText(self, label="Частота 2 (ГГц)")
        self.freqText2 = wx.TextCtrl(self)
        self.freqText2.SetMinSize((150, -1))

        ampLabel2 = wx.StaticText(self, label="Амплитуда 2 (В)")
        self.ampText2 = wx.TextCtrl(self)
        self.ampText2.SetMinSize((150, -1))

        mainSizer.Add(
            freqLabel1,
            1,
            flag=wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL | wx.ALL,
            border=2,
        )

        mainSizer.Add(
            self.freqText1,
            1,
            flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.ALL,
            border=2,
        )

        mainSizer.Add(
            ampLabel1,
            1,
            flag=wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL | wx.ALL,
            border=2,
        )

        mainSizer.Add(
            self.ampText1,
            1,
            flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.ALL,
            border=2,
        )

        mainSizer.Add(
            freqLabel2,
            1,
            flag=wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL | wx.ALL,
            border=2,
        )

        mainSizer.Add(
            self.freqText2,
            1,
            flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.ALL,
            border=2,
        )

        mainSizer.Add(
            ampLabel2,
            1,
            flag=wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL | wx.ALL,
            border=2,
        )

        mainSizer.Add(
            self.ampText2,
            1,
            flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.ALL,
            border=2,
        )

        self.SetSizer(mainSizer)

    @property
    def frequency1(self):
        return float(self.freqText1.GetValue())

    @frequency1.setter
    def frequency1(self, value):
        self.freqText1.SetValue(str(value))

    @property
    def amplitude1(self):
        return float(self.ampText1.GetValue())

    @amplitude1.setter
    def amplitude1(self, value):
        self.ampText1.SetValue(str(value))

    @property
    def frequency2(self):
        return float(self.freqText2.GetValue())

    @frequency2.setter
    def frequency2(self, value):
        self.freqText2.SetValue(str(value))

    @property
    def amplitude2(self):
        return float(self.ampText2.GetValue())

    @amplitude2.setter
    def amplitude2(self, value):
        self.ampText2.SetValue(str(value))
