🐍 Day 04 — Lists, Tuples & Data Processing

Day 04 of 100 Days of Python 🚀

Day 04 introduced Python’s collection data types, with a focus on lists and tuples.

Instead of practicing isolated list operations, I used collections to work with structured student data, perform analysis, clean records, search information, and generate reports.

⸻

🎯 Objectives

* Understand lists
* Access list elements using indexes
* Slice lists
* Modify mutable lists
* Use list methods
* Understand tuples
* Work with immutable records
* Use tuple unpacking
* Iterate through collections
* Search structured data
* Perform basic data analysis
* Practice data-cleaning logic

⸻

📚 Concepts Practiced

🔹 Lists

Lists allow multiple values to be stored in a single collection.

students = [
    ("Kunal", "AI", 87),
    ("Rahul", "CSE", 72),
    ("Priya", "AI", 94)
]

Lists can be modified using operations such as:

append()
insert()
remove()
pop()
sort()
reverse()

⸻

🔹 List Indexing & Slicing

Individual records and portions of lists can be accessed using indexes and slices.

students[0]
students[1:3]

⸻

🔹 Tuples

Tuples were used to represent fixed student records:

student = ("Kunal", "AI", 87)

A tuple is immutable, making it suitable for representing a record whose structure should not be modified directly.

⸻

🔹 Tuple Unpacking

Instead of accessing every value individually:

name = student[0]
branch = student[1]
marks = student[2]

tuple unpacking allows the values to be extracted directly:

name, branch, marks = student

⸻

🧩 Challenges

01 — Student Dataset Analyzer 📊

Worked with a collection of student records containing:

Name
Branch
Marks

The program calculates:

* Total students
* Highest marks
* Lowest marks
* Average marks
* Top performer
* Lowest performer
* Department-wise student counts
* Department-wise averages

⸻

02 — Student Ranking System 🏆

Processed the student dataset to generate a ranking based on marks.

Example:

1. Priya → 94
2. Riya  → 91
3. Kunal → 87

This introduced sorting structured records based on a specific value.

⸻

03 — Data Cleaning

Introduced intentionally invalid and duplicate records.

The program identifies:

Duplicate records

Rahul, CSE, 72

Invalid names

Missing name

Invalid marks

Marks outside the valid range:

0–100

The program then separates valid records from invalid records.

⸻

04 — List Operations

Practiced modifying and analyzing lists through:

* Adding values
* Removing values
* Inserting values
* Sorting
* Reversing
* Finding minimum and maximum values
* Calculating statistics

The logic was first explored manually before using Python’s built-in functions.

⸻

05 — Tuple Unpacking

Used tuple unpacking to work with structured records more efficiently.

name, branch, marks = student

This became particularly useful while iterating through the student dataset.

⸻

06 — Student Search Engine 🔎

Built a simple search system capable of finding students using:

* Name
* Branch
* Marks

Example:

Search by branch: AI

Output:

Kunal → 87
Priya → 94
Neha  → 81
Arjun → 76

⸻

🏆 Mini Project

🎓 Student Performance System

Combined the day’s concepts into a menu-driven student management and analysis system.

Features

1. Show all students
2. Search student
3. Show top performers
4. Show lowest performers
5. Department statistics
6. Show average marks
7. Add student
8. Remove student
9. Sort students
10. Exit

The application processes the underlying list/tuple data and produces useful reports.

⸻

⭐ Bonus Project

💰 Expense Analyzer

Applied the same collection-processing concepts to financial data.

Example:

expenses = [
    ("Food", 250),
    ("Transport", 120),
    ("Food", 180),
    ("Shopping", 500)
]

The analyzer calculates:

* Total expense
* Category-wise expenses
* Highest spending category
* Category totals

This provides an early bridge toward data analysis with Python.

⸻

🧠 Key Takeaways

1. Lists are mutable

List contents can be added, removed, sorted and modified.

2. Tuples are useful for fixed records

A tuple can represent structured information such as:

(Name, Branch, Marks)

3. Collections become powerful with iteration

A list of records can be processed to calculate meaningful statistics.

4. Data structures matter

Choosing the right structure makes programs easier to design and maintain.

5. Python collections are the foundation of data processing

The same ideas will later become important when working with:

CSV
JSON
NumPy
Pandas
Databases
Machine Learning datasets

⸻

💻 Code

All Day 04 implementations are available in:

day04.py

⸻

📊 Progress

Day 04 / 100
████░░░░░░░░░░░░░░░░  4%

Status: ✅ Completed

⸻

🚀 Skills Added

Lists
  ↓
Indexing & Slicing
  ↓
List Manipulation
  ↓
Tuples
  ↓
Tuple Unpacking
  ↓
Structured Data
  ↓
Data Cleaning
  ↓
Data Analysis
  ↓
Mini Application

⸻

🏁 Day 04 Complete

Don’t just store data. Learn how to work with it.

04 / 100 🐍

Keep Coding. Keep Building. Keep Learning. 🚀
