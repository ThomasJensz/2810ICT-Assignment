import openpyxl
import wx
import datetime
import wx.lib.scrolledpanel as scrolled

wb = openpyxl.load_workbook("Crash Statistics Victoria.xlsx", read_only=True)
sheet = wb["Crash Statistics Victoria"]

def FindWithinDates(a, b):
    DateStart = StringToDate(a)
    DateEnd = StringToDate(b)
    rList = []
    List = []
    for row in sheet.rows:
        if type(row[4].value) == str:
            for cell in row:
                rList.append(cell.value)
            List.append(rList)
            rList = []
            continue
        if DateStart < row[4].value < DateEnd:
            for cell in row:
                rList.append(cell.value)
            List.append(rList)
            rList = []
    app = wx.App() 
    Example(None, title = 'Accident Within Given Date', results = List[0:25]) 
    app.MainLoop()
    wb.close()

def KeywordWithinDates(a, b, c):
    DateStart = StringToDate(a)
    DateEnd = StringToDate(b)
    rList = []
    List = []
    for row in sheet.rows:
        if type(row[4].value) == str:
            for cell in row:
                rList.append(cell.value)
            List.append(rList)
            rList = []
            continue
        if DateStart < row[4].value < DateEnd and c in row[9].value:
            for cell in row:
                rList.append(cell.value)
            List.append(rList)
            rList = []
    app = wx.App() 
    Example(None, title = 'Accident Within Given Date', results = List[0:25]) 
    app.MainLoop()
    wb.close()

def AlcoholAnalysis(a):
    controlList = [0,0,0,0,0,0,0,0,0,0,0,0]
    alcoholList = [0,0,0,0,0,0,0,0,0,0,0,0]
    darkList = [0,0,0,0,0,0,0,0,0,0,0,0]
    bothList = [0,0,0,0,0,0,0,0,0,0,0,0]
    for row in sheet.rows:
        if type(row[4].value) == str:
            continue
        if row[4].value.year == a:
            print(row[4].value.year)
            index = monthIndex(row[4].value.month)
            if "Dark" in row[11].value and row[45] == "Yes":
                bothList[index] += 1
            elif "Dark" in row[11].value:
                darkList[index] += 1
            elif row[45] == "Yes":
                alcoholList[index] += 1
            else: 
                controlList[index] += 1
        
    wb.close()

def StringToDate(data):
    split = data.split("-")
    try:
        year = int(split[0])
        month = int(split[1])
        day = int(split[2])
        date = datetime.datetime(year,month,day)
        print("Date Converted")
        return date
    except:
        print("First row skipped")
        return datetime.datetime(2000,1,1)

def monthIndex(a):
    if a == "01":
        return 0
    elif a == "02":
        return 1
    elif a == "03":
        return 2
    elif a == "04":
        return 3
    elif a == "05":
        return 4
    elif a == "06":
        return 5
    elif a == "07":
        return 6
    elif a == "08":
        return 7
    elif a == "09":
        return 8
    elif a == "10":
        return 9
    elif a == "11":
        return 10
    elif a == "12":
        return 11
    
class MyPanel(scrolled.ScrolledPanel):
    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1)
        self.SetAutoLayout(1)
        self.SetupScrolling()

class Example(wx.Frame): 
   
   def __init__(self, parent, title, results): 
      super(Example, self).__init__(parent, title = title,size = (300,200)) 
             
      self.InitUI(results) 
      self.Centre() 
      self.Show()      
         
   def InitUI(self, results): 

      self.SetSize(wx.Size(1280,720))
	
      p = MyPanel(self) 
         
      gr = wx.FlexGridSizer(len(results), len(results[0]), 10, 5)

      for i in results:
            for j in i:
                text = j
                gr.Add(wx.StaticText(p, label = str(text)))
            print("Row Added")       
                
      p.SetSizer(gr)