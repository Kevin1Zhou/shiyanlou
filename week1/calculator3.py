#!/usr/bin/env python3

import sys
import csv

class Args(object):
	def __init__(self):
		self.args = sys.argv[1:]
	def get_content_of_option(self, option):
		self.index = self.args.index(option)
		self.content = self.args[self.index+1]
		return self.content
args = Args()

class Config(object):
	def __init__(self, configfile):
		self._config = {}
		with open(configfile) as file:
			for line in file:
				temp = line.strip().split('=')
				for i, value in enumerate(temp):
					temp[i] = value.strip()
				try:
					self._config[temp[0]] = float(temp[1])
				except:
					print("Parameter Error in Config File")
	def get_config(self, dataname):
		return self._config[dataname]

class UserData(object):
	def __init__(self, userdatafile):
		self._userdata = {}
		with open(userdatafile) as file:
			for line in file:
				temp = line.strip().split(',')
				try:
					self._userdata[int(temp[0])] = int(temp[1])
				except:
					print("Parameter Error in Userdata file")
	def get_userdata(self):
		return self._userdata
				
class Calculator(object):
	
