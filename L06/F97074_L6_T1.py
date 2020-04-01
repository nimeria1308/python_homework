import wx

# Average weight for Europe is 70 kg
AVERAGE_WEIGHT = 70

# Average height for Bulgaria is 169 cm, round it to 170
AVERAGE_HEIGHT = 170

def compute_bmi(weight, height):
    return float(weight) / ((float(height) / 100) ** 2)

class MainWindow(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainWindow, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        # create the main panel
        self.panel = wx.Panel(self)

        # create the text elements
        wx.StaticText(self.panel, label="This program calculates the Body Mass Index (BMI)", pos=(20, 20))
        wx.StaticText(self.panel, label="Weight (kg)", pos=(20, 70))
        wx.StaticText(self.panel, label="Height (cm)", pos=(20, 120))

        # create the spinners
        self.weightCtrl = wx.SpinCtrl(self.panel, min=1, max=500, initial=AVERAGE_WEIGHT, pos=(150, 70))
        self.heightCtrl = wx.SpinCtrl(self.panel, min=1, max=500, initial=AVERAGE_HEIGHT, pos=(150, 120))

        # create the buttons
        self.computeButton = wx.Button(self.panel, label="Compute", pos=(20, 200))
        self.closeButton = wx.Button(self.panel, label="Close", pos=(200, 200))

        # bind the buttons to the event handlers
        self.computeButton.Bind(wx.EVT_BUTTON, self.OnCompute)
        self.closeButton.Bind(wx.EVT_BUTTON, self.OnClose)

    def OnCompute(self, e):
        weight = self.weightCtrl.GetValue()
        height = self.heightCtrl.GetValue()
        bmi = compute_bmi(weight, height)

        wx.MessageBox("The BMI for a {} kg {} cm person is {:.2f}".format(
                      weight, height, bmi),
                      "Computed BMI")

    def OnClose(self, e):
        self.Close()

# Create an application object.
app = wx.App()

# Create and show the main window
frm = MainWindow(None, title="Body Mass Index Calculator", size=(340, 280))
frm.Show()

# Start the event loop.
app.MainLoop()
