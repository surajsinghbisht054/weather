#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Written By:
#		S.S.B
#		surajsinghbisht054@gmail.com
#		bitforestinfo.blogspot.com
#
#
# Return Data Format : Dictionary
#
# Example
#	'next summary'	: u'                Clear throughout the\xa0day.      ', 
#	'temperature'	: u'21\u02da', 
#	'Humidity:'		: u'25%', 
#	'Rain'			: u'0mm', 
#	'Visibility:'	: u'10+km', 
#	'Wind:'			: u'5kph\u2191', 
#	'UV Index:'		: u'8', 
#	'Pressure:'		: u'1016hPa', 
#	'summary'		: u'Clear.', 
#	'Dew Pt:'		: u'0\u02da'
#
#
# Site For Scraping >> This Url Is For Indian Temperature 
site='https://darksky.net/forecast/22.3511,78.6677/ca12/en'

# Importing Modules
import urllib2
import bs4
import re

# Creating Class For Data Handling
class DataExtraction:
	def __init__(self, site):
		self.site=site

	# Creating Function For HTML Code Retrive
	def create_page_handler(self):
		try:
			# Retreive html Page
			html=urllib2.urlopen(self.site)
		except:
			print "Please Check Your Internet Connection!"
			html=None
		if html:
			# Feeding Html Data Into BeautifulSoup
			self.page=bs4.BeautifulSoup(html.read(),'html.parser')
		else:
			self.page=None
		return

	# Creating Function For Extracting Data
	def extract_data_from_page(self):

		# Content Class Configuration
		labels  	=self.page.findAll(class_='label swip')
		labelvalue	=self.page.findAll(class_='val swap')

		self.ExtractedValues={} 	# Dictionary For Storing Data

		# Checking Data Is Ready For Extracting Automatically
		if len(labels)==len(labelvalue):
			for i in xrange(len(labels)):
				self.ExtractedValues[labels[i].text.replace('\n','')]=labelvalue[i].get_text().replace('\n','')

			self.ExtractedValues['temperature']   = self.page.find('span',{'class':'temp swip'}).get_text().replace('\n','')
	    	self.ExtractedValues['summary']       = self.page.find('span',{'class':'summary swap'}).get_text().replace('\n','')
    		self.ExtractedValues['next summary']  = self.page.find('span',{'class':'next swap'}).get_text().replace('\n','')
    		return self.ExtractedValues
		return  

    # Trigger of All Function 
	def start(self):
		self.create_page_handler()
		if self.page:
			return self.extract_data_from_page()

    	

# Testing Function
if __name__=='__main__':
	handler=DataExtraction(site)
	print handler.start()
