# -*- coding: utf-8 -*-

import os.path

import wx

from system import getCurrentDir


class CutGaussPanel (wx.Panel):
    """
    Панель для настроек параметров сигнала в виде гауссова импульса
    """

    def __init__(self, parent):
        super().__init__(parent)

        self._createGui()

    def _createGui(self):
        mainSizer = wx.FlexGridSizer(cols=2)
        mainSizer.AddGrowableCol(0)
        mainSizer.AddGrowableCol(1)

        image = wx.Bitmap(os.path.join(getCurrentDir(), "img/gauss.png"))
        staticImage = wx.StaticBitmap(self, bitmap=image)

        sigmaLabel = wx.StaticText(self, label=u"\u03c3 (*10^-9)")
        self.sigmaText = wx.TextCtrl(self)
        self.sigmaText.SetMinSize((150, -1))

        muLabel = wx.StaticText(self, label=u"\u03bc (нс)")
        self.muText = wx.TextCtrl(self)
        self.muText.SetMinSize((150, -1))

        timeCutLabel = wx.StaticText(self, label=u"t0 (нс)")
        self.timeCutText = wx.TextCtrl(self)
        self.timeCutText.SetMinSize((150, -1))

        mainSizer.Add(staticImage,
                      flag=wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL | wx.ALL,
                      border=2
                      )

        mainSizer.AddSpacer(5)

        mainSizer.Add(sigmaLabel,
                      flag=wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL | wx.ALL,
                      border=2
                      )

        mainSizer.Add(self.sigmaText,
                      flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.ALL,
                      border=2
                      )

        mainSizer.Add(muLabel,
                      flag=wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL | wx.ALL,
                      border=2
                      )

        mainSizer.Add(self.muText,
                      flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.ALL,
                      border=2
                      )

        mainSizer.Add(timeCutLabel,
                      flag=wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL | wx.ALL,
                      border=2
                      )

        mainSizer.Add(self.timeCutText,
                      flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.ALL,
                      border=2
                      )

        self.SetSizer(mainSizer)

    @property
    def sigma(self):
        return float(self.sigmaText.GetValue())

    @sigma.setter
    def sigma(self, value):
        self.sigmaText.SetValue(str(value))

    @property
    def mu(self):
        return float(self.muText.GetValue())

    @mu.setter
    def mu(self, value):
        self.muText.SetValue(str(value))

    @property
    def t0(self):
        return float(self.timeCutText.GetValue())

    @t0.setter
    def t0(self, value):
        self.timeCutText.SetValue(str(value))
