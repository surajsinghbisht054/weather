#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Written By:
#		S.S.B
#		surajsinghbisht054@gmail.com
#		bitforestinfo.blogspot.com
#
#
# Importing Modules
try:
	import Tkinter
except:
	import tkinter as Tkinter
import weather	
import time


# Configurations 
WIDTH=300		# Set Width Of Widget
HEIGHT=300		# Set Height
LOOP_TURN=100	# Update Loop Turns
LOOP_WAIT=0.2	# Time For Waiting On Every Loop Turn

class GUI(Tkinter.Tk):
	def __init__(self, DATAVALUE):
		Tkinter.Tk.__init__(self)
		self.DATAVALUE=DATAVALUE
		self.main_function_handler()

	# Creating Function for Handling Other Functions
	def main_function_handler(self):
		self.creating_function_for_appereance()
		self.coordinate_position()
		self.creating_canvas_board()
		self.creating_Gui_valiadilty()
		return

	# Creating Function For Showing Data
	def creating_canvas_board(self):
		canvas=Tkinter.Canvas(self,bg='skyblue')
		canvas.create_text(50,10,text=u''.join(self.DATAVALUE.pop('temperature')), font=('arial 100 bold'),anchor='nw', fill='gray5') # Temperature
		canvas.create_text(130,150,text=u''.join(self.DATAVALUE.pop('next summary').upper()), font=('arial 10 bold'),fill='Blue') # Next Summary
		for i,j in enumerate(self.DATAVALUE.iteritems()):
			num=i
			(label,value)=j
			canvas.create_text(50,180+(20*i),text=u'{}'.format(label.upper()), font=('arial 10 italic'),anchor='nw', fill='gray10')
			canvas.create_text(150,180+(20*i),text=u'{}'.format(value), font=('arial 10 italic'),anchor='nw', fill='gray20')
		canvas.pack(expand='yes',fill='both')
		return

	# Close Function
	def close_widget(self):
		self.destroy()
		return

	# Function For Handling GUI Apperance Style
	def creating_function_for_appereance(self):
		self.focus_force()
		self['bg']='gray'
		self.overrideredirect(True)
		return

	# Function Fon Handling GUI Position
	def coordinate_position(self):
		self.geometry("%dx%d+%d+%d" % (WIDTH,HEIGHT,\
			self.winfo_screenwidth()/1.5-(WIDTH/1.5),\
			self.winfo_screenheight()/1.5-(HEIGHT),\
			))

	# Function For Handling GUI Loop Timing
	def creating_Gui_valiadilty(self):
		x=1.0
		for i in range(LOOP_TURN):
			time.sleep(LOOP_WAIT)
			self.update_idletasks()
			self.update()
			self.attributes('-alpha',x)
			x=x-0.01
		self.destroy()
		return


# Main Trigger
if __name__ == '__main__':
	# This Data Is only For Testing GUI
	DATAVALUE={'next summary': u'                Clear throughout the\xa0day.      ', 'temperature': u'21\u02da', u'Humidity:': u'25%', u'Rain': u'0mm', u'Visibility:': u'10+km', u'Wind:': u'5kph\u2191', u'UV Index:': u'8', u'Pressure:': u'1016hPa', 'summary': u'Clear.', u'Dew Pt:': u'0\u02da'}
	# Starting GUI Function
	GUI(DATAVALUE)