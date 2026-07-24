import math

print ("==Welcome to Calculations of Areas==")
print ("1. Area of a Triangle")
print ("2. Area of a Rectangle")
print ("3. Area of a Circle")

choice = input("From numbers 1-3, select your number: ")

if choice == "1":
	print ("You selected: Area of a Triangle")
	base = float(input("Enter the triangle's base: "))
	height = float(input("Enter the triangle's height: "))
	area = (base * height) / 2
	print(f"The area of the triangle is {area:.2f}")

elif choice == "2":
	print ("You selected: Area of a Rectangle")
	base = float(input("Enter the rectangle's base: "))
	height = float(input("Enter the rectangle's height: "))
	area = base * height
	print(f"The area of the rectangle is {area:.2f}")

elif choice == "3":
	print ("You selected: Area of a Circle")
	radius = float(input("Enter the circle's radius: "))
	area = math.pi * radius ** 2
	print(f"The area of the circle is {area:.2f}")

else:
	print("Sorry, that was an invalid choice. You need to pick number 1-3 only.")
