# -*- coding: utf-8 -*-

import wx


class SinPanel(wx.Panel):
    """
    Панель для настроек параметров сигнала в виде одной синусоиды
    """

    def __init__(self, parent):
        super(SinPanel, self).__init__(parent)

        self._createGui()

    def _createGui(self):
        mainSizer = wx.FlexGridSizer(cols=2)
        mainSizer.AddGrowableCol(0)
        mainSizer.AddGrowableCol(1)

        freqLabel = wx.StaticText(self, label="Частота (ГГц)")
        self.freqText = wx.TextCtrl(self)
        self.freqText.SetMinSize((150, -1))

        mainSizer.Add(
            freqLabel,
            1,
            flag=wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL | wx.ALL,
            border=2,
        )

        mainSizer.Add(
            self.freqText,
            1,
            flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.ALL,
            border=2,
        )

        self.SetSizer(mainSizer)

    @property
    def frequency(self):
        return float(self.freqText.GetValue())

    @frequency.setter
    def frequency(self, value):
        self.freqText.SetValue(str(value))
