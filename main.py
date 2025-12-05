import wx
import pandas as pd
import matplotlib.pyplot as plt

X = "Wine_red"
Y = "Wine_white"

class WineQualityRate(wx.Frame):
    def __init__(self, parent=None, title="Wine Quality app"):
        super().__init__(parent, title=title, size=(820, 520))
        self.SetMinSize((760, 480))
        panel = wx.Panel(self)

        open_btn = wx.Button(panel, label="Click here to Open the Wine Quality chart...")
        font = open_btn.GetFont()
        font.PointSize += 2
        open_btn.SetFont(font)
        open_btn.Bind(wx.EVT_BUTTON, self.on_open)

        sizer = wx.BoxSizer(wx.VERTICAL) 
        sizer.AddStretchSpacer(1)
        sizer.Add(open_btn, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        sizer.AddStretchSpacer(2)
        panel.SetSizer(sizer)
        
        self.Centre()
        self.Show()