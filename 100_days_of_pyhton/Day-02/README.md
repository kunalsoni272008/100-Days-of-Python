# 🐍 Day 02 — Python Practice

Day 02 of 100 Days of Python 🚀

Day 02 focused on strengthening my Python fundamentals through practical programs involving user input, arithmetic operations, variables, type conversion, modules, and formatted output. Instead of only learning theory, I practiced by building small programs from scratch.

---

## 📚 Topics Practiced

- User Input with `input()`
- Type Conversion
- Variables
- Arithmetic Operators
- Mathematical Formulas
- f-Strings
- Variable Swapping
- Random Number Generation
- Python Modules (`random`, `calendar`)
- Unit Conversion
- Temperature Conversion

---

## 🧠 What I Learned

**1. 🔺 Area of a Triangle**

Created a program to calculate the area of a triangle using its base and height.

```python
area = (base * height) / 2
```

**2. 🔄 Swap Two Variables**

Created a program to swap the values of two variables using arithmetic instead of a temp variable.

```python
b = a + b
a = b - a
b = b - a
```

**3. 🎲 Random Number Generator**

Used Python's built-in `random` module to generate a random number between 1 and 100.

```python
import random
random.randint(1, 100)
```

**4. 🌍 Kilometers to Miles**

Created a unit conversion program that converts kilometers into miles.

```python
miles = km * 0.621
```

**5. 🌡️ Celsius to Fahrenheit**

Created a temperature conversion program.

```python
fahrenheit = (celsius * 9 / 5) + 32
```

**6. 📅 Calendar Generator**

Used Python's `calendar` module to display the calendar for a selected month and year.

```python
import calendar
calendar.month(year, month)
```

---

## 🧩 Challenges Completed

| Challenge | Description | Status |
|:---:|---|:---:|
| 01 | Area of a Triangle | ✅ |
| 02 | Swap Two Variables | ✅ |
| 03 | Random Number Generator | ✅ |
| 04 | Kilometers to Miles Converter | ✅ |
| 05 | Celsius to Fahrenheit Converter | ✅ |
| 06 | Calendar Generator | ✅ |

---

## 🛠️ Mini Project

Day 02 didn't have a single combined mini project — instead it was a set of six small, focused programs, each turning a real-world formula or built-in module into a working script. This "small daily reps" approach is part of the challenge's broader learning philosophy.

---

## 💻 Files

[Day02.py](./Day02.py)

---

## 💡 Key Takeaways

- User input is received as a string by default, so numerical calculations require type conversion (e.g. `float(input(...))`).
- f-strings make formatted output much cleaner than string concatenation.
- Python's standard library (`random`, `calendar`) provides a lot of functionality without writing it from scratch.
- Turning small, real-world formulas into code is one of the fastest ways to build fluency.

---

## 📈 Progress

**Day 02 / 100**

`██░░░░░░░░░░░░░░░░░░` **2%**

**Status:** ✅ Completed

---

## 🚀 What's Next?

[Day 03 →](../Day-03/)

[← Back to 100 Days of Python](../README.md)
