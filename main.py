import wx
from display import *

class myGUI(wx.Frame):
    def __init__ (self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title)
        self.parent = parent
        self.initialise()

    def initialise(self):
        self.SetSize(wx.Size(900,350))
        pnl = wx.Panel(self)
        #UI for Function 1
        lbl1A = wx.StaticText(pnl,label="Find accident information within given dates.", pos=(25,25))
        lbl1B = wx.StaticText(pnl,label="Dates must be formatted as YYYY-MM-DD.", pos=(25,50))
        lbl1C = wx.StaticText(pnl,label="Start Date:", pos=(25,80)) 
        lbl1D = wx.StaticText(pnl,label="End Date:", pos=(200,80))   
        self.input1A = wx.TextCtrl(pnl, value = "", pos = (80, 75))
        self.input1B = wx.TextCtrl(pnl, value = "", pos = (255, 75))
        btn = wx.Button(pnl, pos = (225,110), label = "Display Accidents")
        #Logic for Function 1
        btn.Bind(wx.EVT_BUTTON, self.DateSearch)
        ##UI for Function 2
        lbl2A = wx.StaticText(pnl,label="Find hourly number of accidents for given date.", pos=(25,180))
        lbl2B = wx.StaticText(pnl,label="Date must be formatted as YYYY-MM-DD.", pos=(25,205))
        lbl2C = wx.StaticText(pnl,label="Date:", pos=(25,235))  
        self.input2A = wx.TextCtrl(pnl, value = "", pos = (80, 230))
        btn2 = wx.Button(pnl, pos = (225,265), label = "Accidents per Hour")
        ##UI for Function 3
        lbl3A = wx.StaticText(pnl,label="Find accident information with DCA-Code, within given dates.", pos=(525,25))
        lbl3B = wx.StaticText(pnl,label="Dates must be formatted as YYYY-MM-DD.", pos=(525,50))
        lbl3C = wx.StaticText(pnl,label="Start Date", pos=(525,80)) 
        lbl3D = wx.StaticText(pnl,label="End Date", pos=(700,80)) 
        lbl3E = wx.StaticText(pnl,label="Keyword entered must be capitalised.", pos=(525,100))
        lbl3F = wx.StaticText(pnl,label="Keyword:", pos=(525,130)) 
        self.input3A = wx.TextCtrl(pnl, value = "", pos = (580, 75))
        self.input3B = wx.TextCtrl(pnl, value = "", pos = (755, 75))
        self.input3C = wx.TextCtrl(pnl, value = "", pos = (580, 125))
        btn3 = wx.Button(pnl, pos = (755,160), label = "Search Keyword")
        #Logic for Function 1
        btn3.Bind(wx.EVT_BUTTON, self.KeywordSearch)
        ##UI for Function 4
        btn4 = wx.Button(pnl, pos = (755,250), label = "Impact of Alcohol")
        ##UI for Function 5
        btn5 = wx.Button(pnl, pos = (755,450), label = "???")
        
        self.Show()

    def DateSearch(self, event):
        FindWithinDates(self.input1A.GetValue(), self.input1B.GetValue())

    def KeywordSearch(self, event):
        KeywordWithinDates(self.input3A.GetValue(), self.input3B.GetValue(), self.input3C.GetValue())

if __name__ == "__main__":
    app = wx.App()
    mainFrame = myGUI(None, -1, "Victorian Traffic Accident Data Analysis")
    app.MainLoop()
#For user selected period, display the information of all accidents that happened in the period.

#For a user selected period, produce a chart to show the number of accidents in each hour of the day

#For a user selected period, retieve all accidents that contains a keyword (user entered) in the DCA_CODE, e.g. animal, ped

#Allow the user to analyse the impact of alcohol in accidents - i.e. trends over days, the relationship with dark street ligths, etc.

#Extra insight ???