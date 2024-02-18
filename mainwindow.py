# -*- coding: utf-8 -*-

import wx

from graphcanvas import GraphCanvas
from sincontroller import SinController
from sin2controller import Sin2Controller
from meandercontroller import MeanderController
from rectcontroller import RectController
from gausscontroller import GaussController
from diffgausscontroller import DiffGaussController
from cutgausscontroller import CutGaussController


class MainWindow(wx.Frame):
    """
    Главное окно, содержащее все элементы управления для рисования спектра
    """

    def __init__(self, *args, **kwds):
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        super(MainWindow, self).__init__(*args, **kwds)
        self.SetTitle("Рисование спектра сигнала")

        self.SetSize((900, 700))

        self._createGui()
        self.Center()

        self.controllers = [
            SinController(self.canvas, self.tabsCtrl),
            Sin2Controller(self.canvas, self.tabsCtrl),
            MeanderController(self.canvas, self.tabsCtrl),
            RectController(self.canvas, self.tabsCtrl),
            GaussController(self.canvas, self.tabsCtrl),
            DiffGaussController(self.canvas, self.tabsCtrl),
            CutGaussController(self.canvas, self.tabsCtrl),
        ]
        self._createTabs()

        self.updateBtn.Bind(wx.EVT_BUTTON, handler=self._onUpdate)

    def _onUpdate(self, _event):
        index = self.tabsCtrl.GetSelection()
        assert index >= 0

        self.controllers[index].updateAndDraw()

    def _createGui(self):
        """
        Создает элементы управления
        """
        mainSizer = wx.FlexGridSizer(cols=1)
        mainSizer.AddGrowableCol(0)
        mainSizer.AddGrowableRow(2)

        self.tabsCtrl = wx.Notebook(self)
        mainSizer.Add(self.tabsCtrl, 1, flag=wx.EXPAND | wx.ALL, border=2)

        self.updateBtn = wx.Button(self, label="Обновить")

        mainSizer.Add(self.updateBtn, 1, flag=wx.ALIGN_RIGHT | wx.ALL, border=2)

        self.canvas = GraphCanvas(self)
        mainSizer.Add(self.canvas, 1, flag=wx.EXPAND | wx.ALL, border=2)

        self.SetSizer(mainSizer)
        self.Layout()

    def _createTabs(self):
        for controller in self.controllers:
            self.tabsCtrl.AddPage(controller.panel, controller.title)
