#!/bin/python3
# -*- coding: utf-8 -*-

from time import sleep
from core.colors import Colors

class Horloge:
	def __init__(self, hours = 0, minutes = 0, seconds = 0):
		self.__arr		= [hours, minutes, seconds]
		self.__step		= 1
		self.name		= "Horloge"

	def __update(self):
		self.__arr[2] += self.__step

		for i in [2,1]:
			if(self.__arr[i] > 59):
				self.__arr[i] = 0
				self.__arr[i-1] += self.__step

	def get(self, index):
		time = {
			"hours": self.__arr[0],
			"minutes": self.__arr[1],
			"seconds": self.__arr[2],
		}

		return time[index]

	def dispTime(self):
		print("{}{}{}{}{}:{}{}{}{}{}:{}{}{}".format(
			Colors.red, self.__arr[0] if(self.__arr[0] > 9) else "0"+str(self.__arr[0]), Colors.bold, Colors.yellow, Colors.end,
			Colors.green, self.__arr[1] if(self.__arr[1] > 9) else "0"+str(self.__arr[1]), Colors.bold, Colors.yellow, Colors.end,
			Colors.blue, self.__arr[2] if(self.__arr[2] > 9) else "0"+str(self.__arr[2]), Colors.end
		), end = "\r")

	def start(self):
		while(self.__arr[0] < 24):
			self.__update()
			self.dispTime()
			sleep(1)
