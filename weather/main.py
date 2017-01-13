#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Written By:
#		S.S.B
#		surajsinghbisht054@gmail.com
#		bitforestinfo.blogspot.com
#	
#
# Configuration
TIME_LAP= 3600 # In Seconds
ERROR_TIME_LAP = 10 # Seconds
RETRY=15

# Site For Scraping >> This Url Is For Indian Temperature 
site='https://darksky.net/forecast/22.3511,78.6677/ca12/en'

# Importing Module
import time
import weather
import view
import sys

# Creating Loop
while True:
	retry=0	 	# Retry Counting
	data=weather.DataExtraction(site)	# Here Retriving Data Handler
	try:
		while True:
			k=data.start() # Connecting To Website
			if k:
				# Showing Our GUI 
				view.GUI(k)
				time.sleep(TIME_LAP)
			else:
				print "RETRY"
				time.sleep(ERROR_TIME_LAP)
				retry=retry+1	# Counting Every Retry
				if retry==RETRY:	# Checking Retry Times
					print "Break"
					sys.exit(0)

	except Exception as e:
		print e


