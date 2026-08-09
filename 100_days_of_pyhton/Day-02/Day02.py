# Write a Python program to find the area of a triangle.

height=float(input("Enter the height of the triangle : "))
base=float(input("Enter the base of the triangle : "))
area=(base*height)/2
print(f"Area of the trangle is {area}")


# Write a Python program to swap two variables.

a=int(input("Enter any value for a : "))
b=int(input("enter any value for b : "))
print(f"Before swaping values of a & b are {a} & {b}")
b=a+b
a=b-a
b=b-a
print(f"After swaping values of a & b are {a} & {b}")

# Write a Python program to generate a random number
import random
print(f"Random number is {random.randint(1,100)}")

# Write a Python program to convert kilometers to miles.

km=float(input("Enter the distance in kilometers"))
miles = km*0.621
print(f" Thier are {miles} miles in {km} kilometer")


# Write a Python program to convert Celsius to Fahrenheit
Celsius_temp=float(input("enter the temperature in celsius : "))
Fahrenheit_temp=(Celsius_temp*9/5)+32
print(f"{Celsius_temp}celsius = {Fahrenheit_temp}Fahrenheit")


# Write a Python program to display calendar.

import calendar
year=int(input("Enter the year"))
month=int(input("Enter the month"))
cal=calendar.month(year,month)
print(cal)