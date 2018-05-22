#!/usr/bin/env python3
import sys
start_point = 3500
fee = salary*0.165
incoming_tax = salary - fee - start_point

def Cal_tax(*information):
	tax = 0
	global incoming_tax
	if incoming_tax <= 1500:
		tax = format(incoming_tax*0.03-0, ".2f")
	elif incoming_tax > 1500 and incoming_tax <=4500:
		tax = format(incoming_tax*0.1-105, ".2f")
	elif incoming_tax > 4500 and incoming_tax <=9000:               
                tax = format(incoming_tax*0.2-555, ".2f")
	elif incoming_tax > 9000 and incoming_tax <=35000:               
                tax = format(incoming_tax*0.25-1005, ".2f")
	elif incoming_tax > 35000 and incoming_tax <=55000:               
                tax = format(incoming_tax*0.3-2755, ".2f")
	elif incoming_tax > 55000 and incoming_tax <=80000:               
                tax = format(incoming_tax*0.35-5505, ".2f")
	else:
		tax = format(incoming_tax*0.45-13505, ".2f")
	return tax

undone

		
	 
