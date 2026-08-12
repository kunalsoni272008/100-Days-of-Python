# Text Analyzer
a="Python3 is powerful and Python3 is easy! 200"
lowercount=0
uppercount=0
digitcount=0
sapcecount=0
for i in a:
    if i.islower():
        lowercount+=1
    if i.isupper():
        uppercount+=1
    if i.isdigit():
        digitcount+=1
    if i.isspace():
        sapcecount+=1
print(f" THE STRING IS "
      f"{a}")
print(f"LENGHT OF THE STRING IS {len(a)}")
print(f"Lower count is {lowercount}")
print(f"upper count is {uppercount}")
print(f"space count is {sapcecount}")
print(f"digit count is {digitcount}")

# Username Validator

username = input("Enter username: ")

if (
    5 <= len(username) <= 15
    and username.isascii()
    and all(ch.isalnum() or ch == "_" for ch in username)
    and not username[0].isdigit()
    and " " not in username
    and any(ch.isalpha() for ch in username)
    and any(ch.isdigit() for ch in username)
):
    print("Valid username")
else:
    print("Invalid username")


# Duplicate Character Detector


a=input("Enter any word")
duplicate=[]
for i in a:
    if a.count(i)>1 and i  not in duplicate:
        duplicate.append(i)
print(f"duplicated characters are {duplicate}")

# Remove Punctuation

text = input("Enter a string: ")

punctuations = ".,:;'\"()[]{}_@#\\/|&+-*%!=<>!?-"

result = ""

for ch in text:
    if ch not in punctuations:
        result += ch

print("After removing punctuation:", result)

# Password Strength Analyzer

password=input("enter pass")
points=0
if len(password)>=12:
    points+=2
if any(ch.islower() for ch in password):
    points+=1
if any(ch.isupper() for ch in password):
    points+=1
if any(ch.isdigit() for ch in password):
    points+=1
if any(ch=="_" for ch in password):
    points-=2
if all(not  ch.isalnum() and ch != " " for ch in password):
    points+=1

if points <= 2:
    print("Weak")
elif points <= 4:
    print("Medium")
elif points <= 6:
    print("Strong")
else:
    print("Very Strong")



