Section 1: Loop Basics (1–10)

# 1. Print numbers from 1 to 50 using for loop

for i in range(1,51):
    print(i)

# 2. Print even numbers from 1 to 100    

for i in range(1,101):
    if i%2 == 0:
        print(i)
   
# 3. Print odd numbers from 1 to 100

for i in range(1,101):
    if i%2 != 0:
       print(i)

# 4. Print multiplication table of 7

for i in range(1,11):
    print(i, "x", 7, "=", i * 7)

# 5. Find sum of numbers from 1 to 100

total = 0
for i in range(1,101):
    total +=i
print(total)    

# 6. Print numbers in reverse from 50 to 1

for i in range(50,0,-1):
    print(i)

# 7. Count how many numbers are divisible by 3 (1–100)

count = 0
for i in range(1,101):
    if i % 3 == 0:
        count +=1
print("count =",count)

# 8. Print squares of numbers from 1 to 10

for i in range(1,11):
    print(i*i)

# 9. Print cube of first 10 numbers

for i in range(1,11):
    print(i*i*i)

# 10. Take input n, print numbers from 1 to n

n = int(input("Enter the number ="))
for i in range(1,n+1):
    print(i)

# Section 2: While Loop (11–15)

# 11. Print numbers from 1 to 20 using while

i = 1
while (i<=20):
    print(i)
    i = i+1

# 12. Find factorial of a number using while

n = int(input("Enter the number ="))
i = 1
fact = 1

while i<=n:
    fact = fact * i
    i = i + 1
print("Factorial =",fact)   

# 13. Reverse a number using while

n = int(input("Enter the number ="))
rev = 0

while (n>0):
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print("Reverse =",rev)   

# 14. Count digits in a number

n = int(input("Enter the number ="))

count = 0

while (n > 0):
    n = n // 10
    count += 1
print("Digit =",count)    

# 15. Keep asking input until user enters "stop"

while True:
    word = input("Enter word: ")
    if word == "stop":
        break

# Section 3: Nested Loop (16–20)

# 16. Print pattern

# *
# **
# ***
# ****

for i in range(1,5):
    for j in range(i):
        print("*",end ="")
    print()        

# 17. Print pattern:

# 1
# 12
# 123
# 1234

for i in range(1,5):
    for j in range(1,i+1):
       print(j,end ="")
    print()   

# 18. Print multiplication table (1 to 5) using nested loop

for i in range(1, 6):          
    for j in range(1, 11):     
        print(j, "x", i, "=", i * j)
    print()   

# 19. Print

# A B C
# A B C
# A B C

for i in range(3):
    for j in range(3):
        print(chr(65 + j), end=" ")
    print()

# 20. Print

# 1 2 3
# 4 5 6
# 7 8 9

num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()

# Section 4: String Basics (21–25)

# 21. Count total characters in a string

text = input("Enter string: ")
count = 0
for i in text:
    count += 1
print("Characters =", count)

# 22. Count vowels in a string

text = input("Enter a string :")
vowels = "aeiouAEIOU"
count = 0
for i in text:
    if i in vowels:
        count += 1
print("Vowels =", count)

# 23. Count consonants in a string

text = input("Enter a string: ")
vowels = "aeiouAEIOU"

count = 0

for i in text:
    if i.isalpha() and i not in vowels:
        count += 1

print("Consonants =", count)

# 24. Reverse a string using loop

text = input("Enter a string: ")
rev = ""

for i in text:
    rev = i + rev

print("Reverse:", rev)

# 25. Check if string is palindrome

text = input("Enter a string: ")
rev = ""

for i in text:
    rev = i + rev

if text == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

# Section 5: String Slicing (26–30)

# 26. Print first 5 characters of a string

text = input("Enter a string: ")

print("First 5 characters:", text[:5])

# 27. Print last 3 characters

text = input("Enter a string: ")

print("Last 3 characters:", text[-3:])

# 28. Print string in reverse using slicing

text = input("Enter a string: ")

print("Reversed string:", text[::-1])

# 29. Print every 2nd character

text = input("Enter a string: ")

print("Every 2nd character:", text[::2])

# 30. Remove first and last character from string

text = input("Enter a string: ")

result = text[1:-1]

print("Result:", result)

# Section 6: List Basics (31–35)

# 31. Create a list of 5 numbers and print sum

l = [10,20,30,40,50]
total = 0
for i in l:
    total += i
print("Sum =", total)

# 32. Find maximum value in list

nums = [34, 23, 6, 89, 78]

max_val = nums[0]

for i in nums:
    if i > max_val:
        max_val = i

print("Maximum value:", max_val)

# 33. Find minimum value in list

nums = [2, 13, 27, 33, 15]

min_val = nums[0]

for i in nums:
    if i < min_val:
        min_val = i

print("Minimum value:", min_val)

# 34. Count total elements in list

nums = [15, 34, 32, 56, 89]

count = 0

for i in nums:
    count += 1

print("Total elements:", count)

# 35. Check if element exists in list

l = [23, 34, 45, 87, 90]

x = int(input("Enter element: "))

if x in l:
    print("Exists")
else:
    print("Not exists")

# Section 7: List Operations (36–40)

# 36. Section 7: List Operations (36–40)

Add 3 elements using append()

nums = []

nums.append(10)
nums.append(20)
nums.append(30)

print("List:", nums)

# 37. Insert element at specific index

nums = [23, 56, 20, 48]

nums.insert(2, 25)

print("List:", nums)

# 38. Remove element using remove()

num = [12, 45, 32, 67, 48]

num.remove(32)

print("List:", num)

# 39. Reverse list without using .reverse()

nums = [5, 6, 7, 8, 9]

rev = []

for i in nums:
    rev = [i] + rev

print("Reversed list:", rev)

# 40. Sort list without using .sort()

nums = [5 , 4 , 3 , 2 , 1]

for i in range(len(nums)):
    for j in range(len(nums) - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print("Sorted list:", nums) 
           




 


















    