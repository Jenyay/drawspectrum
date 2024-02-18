# -*- coding: utf-8 -*-

import wx


class RectPanel(wx.Panel):
    """
    Панель для настроек параметров сигнала в виде одиночного видеоимпульса
    """

    def __init__(self, parent):
        super(RectPanel, self).__init__(parent)

        self._createGui()

    def _createGui(self):
        mainSizer = wx.FlexGridSizer(cols=2)
        mainSizer.AddGrowableCol(0)
        mainSizer.AddGrowableCol(1)

        lengthLabel = wx.StaticText(self, label="Длительность импульса (нс)")
        self.lengthText = wx.TextCtrl(self)
        self.lengthText.SetMinSize((150, -1))

        mainSizer.Add(
            lengthLabel,
            1,
            flag=wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL | wx.ALL,
            border=2,
        )

        mainSizer.Add(
            self.lengthText,
            1,
            flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.ALL,
            border=2,
        )

        self.SetSizer(mainSizer)

    @property
    def length(self):
        return float(self.lengthText.GetValue())

    @length.setter
    def length(self, value):
        self.lengthText.SetValue(str(value))
