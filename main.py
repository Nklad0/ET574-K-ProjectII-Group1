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
        
    def on_open(self, _evt):
        with wx.FileDialog(
            self,
            "Open Wine Quality CSV",
            wildcard="CSV files (*.csv)|*.csv",
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
        ) as dlg:
            if dlg.ShowModal() != wx.ID_OK:
                return
            path = dlg.GetPath()
        
    try:
        df = pd.read_csv(path)
        want = ["fixed_acidity", "volatile_acidity", "citric_acid", "residual_sugar", "chlorides", "free_sulfur_dioxide", "total_sulfur_dioxide", "density", "pH", "sulphates", "alcohol"]
        df.columns = [str(c).strip().lower().replace(" ", "_") for c in df.columns]
        if df.shape[1] == 5 and not set(want).issubset(df.columns):
            df.columns = want
        
        for c in ["fixed_acidity", "volatile_acidity", "quality"]:
            if c not in df.columns:
                raise ValueError("CSV needs to have 4 features + 'quality'.")
            

        plt.figure(figsize=(7.5, 5.0))
        for sp, sub in df.groupby("quality"):
            plt.bar(sub[X], sub[Y], s=40, alpha=0.85, label=str(sp))
        plt.title(f"Wine Quality: {X.replace('_',' ').title()} vs {Y.replace('_',' ').title()}")
        plt.xlabel(X.replace('_',' ').title())
        plt.ylabel(Y.replace('_',' ').title())
        plt.grid(True, linestyle="--", alpha=0.3)
        plt.legend(title="quality", frameon=True)
        plt.tight_layout()
        plt.show()

        
    except Exception as e:
              wx.MessageBox(f"Failed to load/plot file:\n{e}", "Error", wx.OK | wx.ICON_ERROR)

if __name__ == "__main__":
    app = wx.App(False)
    WineQualityRate()
    app.MainLoop()