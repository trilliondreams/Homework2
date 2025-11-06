print("1. Celsius to Fahrenheit")
print("2. Meter to feet")

choice = int(input("Enter your choice: "))

def cel_fah(temp):
    print(temp * 9/5 + 32)
def meter_feet(length):
    print(length * 3.280)
    
if choice == 1:
    temp = float(input("temperature: "))
    cel_fah(temp)
elif choice == 2:
    length = float(input("length: "))
    meter_feet(length)
else:
    print("Unknown option").