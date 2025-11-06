income = float(input("income: "))

def low():
    print("0%")
def midlow():
    print("15%")
def highlow():
    print("20%")
def middle():
    print("30%")
def high():
    print("%")
	
if income >= 0 and income <=2000:
    low()
elif income>= 2001 and income <=4000:
    midlow()
elif income>=  4001 and income <=7000:
    highlow()
elif income>= 7001 and income <=14000:
    middle()
else:
    high()