import openpyxl
import wx
import datetime
import wx.lib.scrolledpanel as scrolled
import matplotlib.pyplot as plt

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
    alcoholList = [0,0,0,0,0,0,0,0,0,0,0,0]
    darkList = [0,0,0,0,0,0,0,0,0,0,0,0]
    alcoholInjList = [0,0,0,0,0,0,0,0,0,0,0,0]
    darkInjList = [0,0,0,0,0,0,0,0,0,0,0,0]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for row in sheet.rows:
        if type(row[4].value) == str:
            continue
        if row[4].value.year == int(a):
            index = row[4].value.month - 1
            if row[45].value == "Yes":
                if row[27].value > 0 or row[28].value > 0:
                    alcoholInjList[index] += 1
                    print("Alc Inj Added:" + months[index])
                else:
                    alcoholList[index] += 1
                    print("Alc Added:" + months[index])
            elif "Dark" in row[11].value:
                if row[27].value > 0 or row[28].value > 0:
                    darkInjList[index] += 1
                    print("Dark Inj Added:" + months[index])
                else:
                    darkList[index] += 1
                    print("Dark Added:" + months[index])

    plt.plot(months, alcoholList, label = "Alcohol (Non-Injury)")
    plt.plot(months, darkList, label = "Dark (Non-Injury)")
    plt.plot(months, alcoholInjList, label = "Alcohol (Injury/Fatality)")
    plt.plot(months, darkInjList, label = "Dark (Injury/Fatality)")

    plt.legend(loc = "upper left")
    plt.ylabel("Number of Accidents")
    plt.xlabel("Month")
    plt.title("Influnce of Alcohol to Accident Severity")

    plt.show()
      
    wb.close()

def HourlyWithinDates(a,b):
    DateStart = StringToDate(a)
    DateEnd = StringToDate(b)
    hoursData = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    hoursLabel = ["12am", "1am", "2am", "3am", "4am", "5am", "6am", "7am", "8am", "9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm", "5pm", "6pm", "7pm", "8pm", "9pm", "10pm", "11pm"]

    for row in sheet.rows:
        if type(row[4].value) == str:
            continue
        if DateStart < row[4].value < DateEnd:
            split = row[5].value.split('.')
            index = int(split[0])
            print(index)
            hoursData[index] += 1

    plt.plot(hoursLabel, hoursData)

    plt.ylabel("Number of Accidents")
    plt.xlabel("Time of Day (Hourly)")
    plt.title("Hourly Accident Frequency")

    plt.show()
      
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