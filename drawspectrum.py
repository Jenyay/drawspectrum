#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

import wx

from mainwindow import MainWindow


class DrawSpectrum(wx.App):
    """
    Класс приложения для рисования спектров
    """

    def __init__(self, *args, **kwds):
        os.environ["GTK_THEME"] = ":light"
        wx.App.__init__(self, *args, **kwds)

    def OnInit(self):
        mainWnd = MainWindow(None, -1, "")
        mainWnd.Show()

        self.SetTopWindow(mainWnd)

        return True


if __name__ == "__main__":
    application = DrawSpectrum(False)
    application.MainLoop()
