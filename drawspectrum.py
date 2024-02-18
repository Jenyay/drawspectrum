#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

from mainwindow import MainWindow


class DrawSpectrum(wx.App):
    """
    Класс приложения для рисования спектров
    """
    def __init__(self, *args, **kwds):
        wx.App.__init__(self, *args, **kwds)


    def OnInit(self):
        mainWnd = MainWindow(None, -1, "")
        mainWnd.Show()

        self.SetTopWindow(mainWnd)

        return True


if __name__ == "__main__":
    application = DrawSpectrum(False)
    application.MainLoop()
