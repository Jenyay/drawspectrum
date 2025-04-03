# -*- coding: utf-8 -*-

import wx


class MeanderPanel(wx.Panel):
    """
    Панель для настроек параметров сигнала в виде меандра
    """

    def __init__(self, parent):
        super(MeanderPanel, self).__init__(parent)

        self._createGui()

    def _createGui(self):
        mainSizer = wx.FlexGridSizer(cols=2)
        mainSizer.AddGrowableCol(0)
        mainSizer.AddGrowableCol(1)

        periodLabel = wx.StaticText(self, label="Период (нс)")
        self.periodText = wx.TextCtrl(self)
        self.periodText.SetMinSize((150, -1))

        dutyLabel = wx.StaticText(self, label="Коэффициент заполнения")
        self.dutyText = wx.TextCtrl(self)
        self.dutyText.SetMinSize((150, -1))

        mainSizer.Add(
            periodLabel,
            1,
            flag=wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL | wx.ALL,
            border=2,
        )

        mainSizer.Add(
            self.periodText,
            1,
            flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.ALL,
            border=2,
        )

        mainSizer.Add(
            dutyLabel,
            1,
            flag=wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL | wx.ALL,
            border=2,
        )

        mainSizer.Add(
            self.dutyText,
            1,
            flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.ALL,
            border=2,
        )

        self.SetSizer(mainSizer)

    @property
    def period(self):
        return float(self.periodText.GetValue())

    @period.setter
    def period(self, value):
        self.periodText.SetValue(str(value))

    @property
    def duty(self):
        return float(self.dutyText.GetValue())

    @duty.setter
    def duty(self, value):
        self.dutyText.SetValue(str(value))
