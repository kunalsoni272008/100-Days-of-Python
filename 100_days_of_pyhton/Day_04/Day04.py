# Student Dataset Analyzer
students = [
    ("Kunal", "AI", 87),
    ("Rahul", "CSE", 72),
    ("Priya", "AI", 94),
    ("Aman", "CSE", 65),
    ("Neha", "AI", 81),
    ("Riya", "CSE", 91),
    ("Arjun", "AI", 76)
]

marks = []

for student in students:
    marks.append(student[2])

print("Total Students :", len(students))
print("Highest Marks  :", max(marks))
print("Lowest Marks   :", min(marks))
print("Average Marks  :", sum(marks) / len(marks))




# Ranking System
students = [
    ("Kunal", "AI", 87),
    ("Rahul", "CSE", 72),
    ("Priya", "AI", 94),
    ("Rahul", "CSE", 72),
    ("Aman", "CSE", 65),
    ("Neha", "AI", 81),
    ("", "AI", 76),
    ("Riya", "CSE", 105)
]

data = students.copy()

# Duplicate records

unique = []
Duplicate = []

for student in students:
    if student in unique:
        Duplicate.append(student)
        data.remove(student)
    else:
        unique.append(student)

print("Duplicate Records:", Duplicate)


# Invalid names

for student in students:
    if student[0] == "":
        print("Invalid Record:", student, "→ Name is missing")
        data.remove(student)


# Invalid marks

for student in students:
    if student[2] < 0 or student[2] > 100:
        print("Invalid Record:", student, "→ Invalid marks")
        data.remove(student)


print("Valid Data:", data)

# Tuple Unpacking

students = [
    ("Kunal", "AI", 87),
    ("Rahul", "CSE", 72),
    ("Priya", "AI", 94),
    ("Rahul", "CSE", 72),
    ("Aman", "CSE", 65),
    ("Neha", "AI", 81),
    ("", "AI", 76),
    ("Riya", "CSE", 105)
]

for student in students:
    for ch in student:
        print(ch,end=" ")
    print("  ")

# Search Engine

name=input("enter student name ")
for student in students:
    if student[0].lower()==name.lower():
        print(student)


# Expense Analyzer
expenses = [
    ("Food", 250),
    ("Transport", 120),
    ("Food", 180),
    ("Shopping", 500),
    ("Transport", 80),
    ("Food", 300)
]


expense=[]
for items in expenses:
    expense.append(items[1])
highest = max(expenses, key=lambda x: x[1])



print(f"Total expense={sum(expense)} ")

print(f"Highest category = {highest[0]}")
print(f"Highest expense = {highest[1]}")