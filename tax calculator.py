income = float(input("income: "))

def low(income):
	if income >= 0 and income <=2000:
		print(income * 0)
		print("0%")
	elif income>= 2001 and income <=4000:
		print(income * 0.15)
		print("15%")
	elif income>=  4001 and income <=7000:
		print(income*0.2)
		print("20%")
	elif income>= 7001 and income <=14000:
 	   print(income * 0.3)
	else:
		print(income * 0.35)
		print("35%")
        
low(income)
