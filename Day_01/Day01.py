# 🧩 Challenge 1 — Hello Python
# Write a program that prints:
# Hello, Python! 🐍
# Welcome to my 100 Days of Python journey.
# Day 01 starts today!
#

print("""Hello , Python
Welcome to my 100 days of Python journey
Day 01 starts today!""")



# 🧩 Challenge 2 — About Me
# Create variables for:
# * Your name
# * Your age
# * Your college
# * Your branch
# * Your goal
# Then print them in a clean format.
# Expected style:
# Name: Kunal
# Age: 18
# College: ...
# Branch: ...
# Goal: ...

name=input("Enter your name ")
age=input("Enter your age ")
college=input("Enter your college ")
branch=input("Enter your branch ")
goal=input("Enter your goal")
print("Name :", name )
print("Age :", age )
print("College :", college )
print("Branch :", branch )
print("Goal :", goal)



# 🧩 Challenge 3 — Data Type Detective 🔍

name= "Kunal"
Age=18
weight = 62.5
is_student = True

print(type(name))
print(type(Age))
print(type(weight))
print(type(is_student))



# 🧩 Challenge 4 — User Introduction
name=input("What is your name ")
age=int(input("What is your age "))
weigth=input("What is your weight")
is_student=input("Are you a student")

print(f"Hello {name}!")
print(f"You are {age} years old")
print(f"Your weight is {weight}")
print(f"Is_student{is_student}")



# 🧩 Challenge 5 — Age Calculator 🎂

# Ask the user for their birth year and calculate their approximate age.

current_year=int(input("Enter the current year : "))
birth_year=int(input("Enter your birth year : "))
age=current_year-birth_year
print(f"You are {age} years old")


# 🧩 Challenge 6 — Simple Calculator 🧮
#
# Ask the user for two numbers.
#
# Calculate:
#
# * Addition
# * Subtraction
# * Multiplication
# * Division
# * Modulus


num_1=int(input("Enter the first number "))
num_2=int(input("Enter the second number "))

add=num_1+num_2
sub=num_1-num_2
multiply=num_1*num_2
division=num_1/num_2
print(f"Addition = {add}")
print(f"Subtraction = {sub}")
print(f"Multiplication = {multiply}")
print(f"Division = {division}")




# 🔥 Challenge 7 — Mini Project
#
# 🪪 Personal Profile Generator
#
# Build a program that asks for:
#     Name
#     Age
#     City
#     College
#     Branch
#     Programming
#     Language
#     Career
#     Goal


name = input(" Enter name : ")
Age=int(input("Enter your age : "))
City=input("Enter your cty : ")
college=input("Enter your college ")
branch=input("Enter your branch ")
Programming=input("Enter your programming language")
Language=input("Enter tour language")
career=input("Enter the field you want o make career in ")
Goal=input("Enter goal of your life")

print(f"""
          ------------------------------------------------
                       MY Pyhton Profile 
          ------------------------------------------------
          Name : {name}
          Age  : {Age}
          City : {City}
          College : {college}
          Branch  : {branch}
          Programming language : {Programming}
          Language :{Language}
          Career Goal: {Goal}
          ------------------------------------------------
          ------------------------------------------------""")