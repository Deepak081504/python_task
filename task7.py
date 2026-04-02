
# Task 1: Use super() properly
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)  
        self.dept = dept
        self.fees = fees

class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

s1 = Student("Deepak", 101, "CSE", 50000)
f1 = Faculty("Swetha", 201, 60000)
t1 = TempFaculty("Anand", 301, 40000, "6 Months")

print("Student:", s1.name, s1.id, s1.dept, s1.fees)
print("Faculty:", f1.name, f1.id, f1.salary)
print("Temp Faculty:", t1.name, t1.id, t1.salary, t1.duration)


# Task 2: Apply Abstraction
from abc import ABC, abstractmethod

class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass

class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}"

class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"Student -> Name: {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"

class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return f"Faculty -> Name: {self.name}, ID: {self.id}, Salary: {self.salary}"

class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def get_details(self):
        return f"TempFaculty -> Name: {self.name}, ID: {self.id}, Salary: {self.salary}, Duration: {self.duration}"

s1 = Student("Deepak", 101, "CSE", 50000)
f1 = Faculty("Swetha", 201, 60000)
t1 = TempFaculty("Anand", 301, 40000, "6 Months")

print(s1.get_details())
print(f1.get_details())
print(t1.get_details())


# Task 3: Sorting using key
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees


class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

students = [
    Student("Deepak", 101, "CSE", 50000),
    Student("Swetha", 102, "ECE", 30000),
    Student("Anand", 103, "IT", 40000)
]

students.sort(key=lambda x: x.fees)

print("Students sorted by fees:")
for s in students:
    print(s.name, s.fees)

faculties = [
    Faculty("Nobita", 201, 60000),
    Faculty("Gian", 202, 45000),
    Faculty("Sunio", 203, 55000)
]
faculties.sort(key=lambda x: x.salary)

print("\nFaculty sorted by salary:")
for f in faculties:
    print(f.name, f.salary)


# Task 4: Use map()
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees


students = [
    Student("Deepak", 101, "CSE", 50000),
    Student("Swetha", 102, "ECE", 30000),
    Student("Anand", 103, "IT", 40000)
]

names = list(map(lambda s: s.name, students))

print("Student Names:", names)    


# Task 5: Use filter()
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees


class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

students = [
    Student("Deepak", 101, "CSE", 50000),
    Student("Swetha", 102, "ECE", 60000),
    Student("Anand", 103, "IT", 70000)
]

faculties = [
    Faculty("Nobita", 201, 25000),
    Faculty("Gian", 202, 35000),
    Faculty("Sunio", 203, 45000)
]


# Filter students with fees > 50000
high_fee_students = list(filter(lambda s: s.fees > 50000, students))

# Filter faculty with salary > 30000
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculties))


print("Students with fees > 50000:")
for s in high_fee_students:
    print(s.name, s.fees)

print("\nFaculty with salary > 30000:")
for f in high_salary_faculty:
    print(f.name, f.salary)


# Task 6: Use reduce()
from functools import reduce

class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees


class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

students = [
    Student("Deepak", 101, "CSE", 50000),
    Student("Swetha", 102, "ECE", 60000),
    Student("Anand", 103, "IT", 70000)
]

faculties = [
    Faculty("Nobita", 201, 25000),
    Faculty("Gian", 202, 35000),
    Faculty("Sunio", 203, 45000)
]

total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)

total_salary = reduce(lambda acc, f: acc + f.salary, faculties, 0)


print("Total Fees Collected:", total_fees)
print("Total Faculty Salary:", total_salary)


# Task 7: Higher Order Function
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees


def process_users(users, func):
    return list(map(func, users))

students = [
    Student("Deepak", 101, "CSE", 50000),
    Student("Swetha", 102, "ECE", 60000),
    Student("Anand", 103, "IT", 70000)
]


names = process_users(students, lambda s: s.name)

fees = process_users(students, lambda s: s.fees)

print("Names:", names)
print("Fees:", fees)


# Final Challenge (Important)
from abc import ABC, abstractmethod
from functools import reduce

# ABSTRACT CLASS
class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass


# BASE CLASS 
class User(AbstractUser):
    users_count = 0  

    def __init__(self, name, id):
        self.name = name
        self.id = id
        User.users_count += 1

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}"


# STUDENT 
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"Student -> {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"


#  FACULTY 
class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return f"Faculty -> {self.name}, ID: {self.id}, Salary: {self.salary}"

students = [
    Student("Deepak", 101, "CSE", 50000),
    Student("Swetha", 102, "ECE", 60000),
    Student("Anand", 103, "IT", 70000)
]

faculties = [
    Faculty("Nobita", 201, 25000),
    Faculty("Gian", 202, 35000),
    Faculty("Sunio", 203, 45000)
]

print("\n All Student Details ")
for s in students:
    print(s.get_details())

print("\n All Faculty Details ")
for f in faculties:
    print(f.get_details())

students.sort(key=lambda s: s.fees)
faculties.sort(key=lambda f: f.salary)

print("\n Sorted Students (by Fees)")
for s in students:
    print(s.name, s.fees)

print("\n Sorted Faculty (by Salary) ")
for f in faculties:
    print(f.name, f.salary)

high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculties))

print("\n High Fee Students ")
for s in high_fee_students:
    print(s.name, s.fees)

print("\n High Salary Faculty ")
for f in high_salary_faculty:
    print(f.name, f.salary)


student_names = list(map(lambda s: s.name, students))
faculty_names = list(map(lambda f: f.name, faculties))

print("\nStudent Names:", student_names)
print("Faculty Names:", faculty_names)


total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculties, 0)

print("\nTotal Fees Collected:", total_fees)
print("Total Faculty Salary:", total_salary)


print("\nTotal Users Created:", User.users_count)
