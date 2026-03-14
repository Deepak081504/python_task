#Bitwise operator Task(1 - 8)

#Task 1

a = 10
b = 6

print(a & b)

#Task 2

x = 12
y = 5

print(x | y)

#Task 3

num = 8

print(~ num)

#Task 4

a = 15
b = 9

print(a^b)

#Task 5

num = 7

print(num << 2)

#Task 6

num = 20

print(num >> 1)

#Task 7

a = int(input("Enter the Number 1 :"))
b = int(input("Enter the Number 2 :"))

print(a & b)

#Task 8

a = int(input("Enter the Number 1 :"))
b = int(input("Enter the Number 2 :"))

print(a ^ b)

#String Tasks (9 - 14)

#Task 9

a = "hi"

print(a * 4)

#Task 10

a = "python"

print(a * 3)

#Task 11

a = "super"
b = "man"

print(a + b)

#Task 12

a = "hello"
b = " "
c = "world"
print('"' +a + b + c + '"')

#Task 13

name = "Deepak "

print(name * 5)

#Task 14

str1 = input("Enter the first string :")
str2 = input("Enter the second string :")

print("concatenate :",str1 + str2)

#Input and Type Casting Task(15 - 20)

#Task 15

name = input("Enter the name :")

print("The Data Type is :",type(name))

#Task 16

age = input("The age is :")
age = int(age)
print(age)
print(type(age))

# Task 17

a = int(input("enter first number :"))
b = int (input("enter second number :"))

total = a + b

print("sum =",total)

# Task 18

mark1 = int(input("Enter the first mark ="))
mark2 = int(input("Enter the second mark ="))

print("The average is =",(mark1 + mark2)/2)

# Task 19

a = int(input("Enter first number :"))
b = int(input("Enter second number :"))

print(3 * a * 2 + b - 2)

# Task 20

num = int(input("Enter the number :"))

print("before type casting :",type(num))

num = str(num)

print("after type casting :",type(num))

# Unit Digit task (21 - 25)

# Task 21

num = input("Enter a number: ")

print("last digit :",num[-1])

# Task 22

num = int(input("Enter a number: "))
unit_digit = (num % 10)

print("unit digit :",unit_digit)

# Task 23

num = int(input("Enter a number: "))
result = num // 10


print(result)

# Task 24

num = int(input("Enter a number: "))
second_last = (num // 10) %10

print("second last digit :", second_last)

# Task 25

num = int(input("Enter a 5 digit number: "))
num1 = num % 10

print("last digit :",num1)

# if Statement Tasks (26 - 30)

# Task 26

if (10>=5):
   
    print("Good")

# Task 27

a = int(input("Enter the number :"))
if(a>50):
    print("the number is greater than 50")
  
# Task 28

age = int(input("Enter a age :"))

if (age>=18):
    print("Eligible")

# Task 29

num = int(input("Enter the number: "))

if (num>100):
    print("The number is greater than 100")

# Task 30

num = int(input("Enter a number: "))

if (num>=0):
    print("The number is greater than or equal to 0")

# if-else task (31 - 34)

# Task 31

num = int(input("Enter the number :"))

if(num % 2 == 0):
    print("even")
else:
    print("odd")

# Task 32

Mark = int(input("Enter the mark :"))

if (Mark>=35):
    print("pass")
else:
    print("fail") 

# Task 33

num = int(input("Enter the number :"))

if (num>=0):
    print("Positive")
else:
    print("Negative")

# Task 34

num = int(input("Enter the number :"))

if (num>10):
    print("Greater")
else:
    print("Smaller")

# Nested if (35 - 37)

# Task 35

age = int(input("Enter the age :"))
height = int(input("Enter the height :"))
weight = int(input("Enter the weight :"))

if (age>=18):
    if (height>=160):
        if (weight>=60):
            print("selected")
        else:
            print("rejected")
    else:
        print("rejected")
else:
    print("rejected")

# Task 36

mark = int(input("Enter the mark :" ))
age = int(input("Enter the age :"))

if (mark>=60):
    if (age>=17):
        print("Eligible for Admission")
    else:
        print("Not Eligible for Admission")
else:
    print("Not Eligible for Admission")

# Task 37

age = int(input("Enter the age :"))
height = int(input("Enter the height :"))
weight = int(input("Enter the weight :"))

if (age>=16):
    if (height>=150):
        if (weight>=50):
            print("selected")
        else:
            print("not selected")
    else:
        print("not selected")
else:
    print("not selected")

# Match Statement Task (38 - 40)

# Task 38

num = int(input("Number from 1-7 ="))
match num:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("invalid")

# Task 39

num = int(input("num 1 -3 ="))
match num:
    case 1:
        print("Red")
    case 2:
        print("Blue")
    case 3:
        print("Green")
    case _:
        print("invalid")

# Task 40

num = int(input("enter num ="))
match num:
    case 1:
        print("Apple")
    case 2:
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")
    case _:
        print("invalid")


   







          



















