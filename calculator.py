#!/usr/bin/env python3
import sys

IDs = []
Salarys = []
for arg in sys.argv[1:]:
	a = arg.split(':')
	try:
		IDs.append(int(a[0]))
		Salarys.append(int(a[1]))
	except:
		print("Parameter Error")

def Cal_fee(salary):  #计算五险一金费用
	fee = salary * 0.165
	return fee
def Cal_incoming_tax(salary,fee,start_point=3500): #计算应纳税所得额
	incoming_tax = salary - fee - start_point
	return incoming_tax
def Cal_tax(incoming_tax): #计算应纳税额
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
	
def Cal_salary_after_tax(salary,fee,tax):	#计算税后工资
	salary_after_tax = salary - fee - tax
	return salary_after_tax

if __name__ == '__main__':
	for salary in Salarys:
		num = 0
		fee = Cal_fee(salary)
		incoming_tax = Cal_incoming_tax(salary,fee)
		tax = Cal_tax(incoming_tax)
		salary_after_tax = Cal_salary_after_tax(salary,fee,tax)	
		print(IDs[num], end=':'
		print(salary_after_tax)
		num += 1



		
	 
