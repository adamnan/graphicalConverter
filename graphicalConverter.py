#! /usr/bin/env python
import wx

Round = False
	
class wxFrame(wx.Frame):
	
	def fltSum(self, a, b, c, error1, error2):
		error1.Show(False)
		error2.Show(False)
		
		try:
			sum = float(a) + float(c) * float(b)
			
			if float(a) or float(b) < 0:
				error2.Show(True)
		
			else:
				return sum
		
		except ValueError:
			error1.Show(True)
	
	def __init__(self, parent):
		
		wx.Frame.__init__(self, parent, wx.ID_ANY, title = "Graphical Converter")
		self.panel = wx.Panel(self)
		
		self.checkBoxRound = wx.CheckBox(self.panel, label='Round to 2 decimal places', pos=(80, 250))
		self.checkBoxRound.Bind(wx.EVT_CHECKBOX, self.OnRound)
		
		self.prompt = wx.StaticText(self.panel, label="This program converts between SI and English units.", pos=(20,10))
		
		self.mLabel = wx.StaticText(self.panel, label="m", pos=(160,50))# labels
		self.cmLabel = wx.StaticText(self.panel, label="cm", pos=(290,50))
		self.ftLabel = wx.StaticText(self.panel, label="ft", pos=(160,150))
		self.inLabel = wx.StaticText(self.panel, label="in", pos=(290,150))
		
		self.mBox = wx.TextCtrl(self.panel, value="0", pos=(50,50))
		self.cmBox = wx.TextCtrl(self.panel, value="0", pos=(180,50))
		self.ftBox = wx.TextCtrl(self.panel, value="0", pos=(50,150))
		self.inBox = wx.TextCtrl(self.panel, value="0", pos=(180,150))
		
		self.mBox.Bind(wx.EVT_TEXT, self.OnConvert)
		self.cmBox.Bind(wx.EVT_TEXT, self.OnConvert)
		self.ftBox.Bind(wx.EVT_TEXT, self.OnConvert)
		self.inBox.Bind(wx.EVT_TEXT, self.OnConvert)
		
		self.TypeErrorSI = wx.StaticText(self.panel, label="This input must be a number", pos=(100,100))
		self.TypeErrorSI.Show(False)
		self.TypeErrorEng = wx.StaticText(self.panel, label="This input must be a number", pos=(100,200))
		self.TypeErrorEng.Show(False)
		
		self.ValueErrorSI = wx.StaticText(self.panel, label="This input can not be negative", pos=(100,100))
		self.ValueErrorSI.Show(False)
		self.ValueErrorEng = wx.StaticText(self.panel, label="This input can not be negative", pos=(100,200))
		self.ValueErrorEng.Show(False)
	
	def OnRound(self, e):
		global Round 
		Round = self.checkBoxRound.GetValue()
		self.OnConvert(e)
		
	def OnConvert(self, e):
		
		currentBox = e.GetEventObject()
		
		if(currentBox == self.mBox or currentBox == self.cmBox):
			
			cm = self.cmBox.GetValue()
			m = self.mBox.GetValue()
			
			lengthSI = self.fltSum(cm, m, 100, self.TypeErrorSI, self.ValueErrorSI)
			lengthEng = lengthSI / 2.54 
			ft = int(lengthEng // 12)
			inch = lengthEng - 12 * ft
			
			if(Round):
				inch = round(inch, 2) # round if needed
			
			self.ftBox.ChangeValue(str(ft))
			self.inBox.ChangeValue(str(inch))
		
		elif(currentBox == self.ftBox or currentBox == self.inBox):
			
			inch = self.inBox.GetValue()
			ft = self.ftBox.GetValue()
			
			lengthEng = self.fltSum(inch, ft, 12, self.TypeErrorEng, self.ValueErrorEng) 
			lengthSI = lengthEng * 2.54
			m = int(lengthSI // 100)
			cm = lengthSI - 100 * m
			
			if(Round):
				cm = round(cm, 2)
			
			self.mBox.ChangeValue(str(m))
			self.cmBox.ChangeValue(str(cm))
	
		else:
			inch = self.inBox.GetValue()
			inch = float(inch)
			
			cm = self.cmBox.GetValue()
			cm = float(cm)
			
			if(Round):
				inch = round(inch, 2)
				cm = round(cm, 2)
			
			self.inBox.ChangeValue(str(inch))
			self.cmBox.ChangeValue(str(cm))

# ----------- Main Program Below -----------------

# Define the app
app = wx.App(False)

# Create a regular old wx.Frame
frame = wxFrame(None)

# Show the frame
frame.Show()

# Make the app listen for clicks and other events
app.MainLoop()