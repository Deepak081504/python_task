#Task 1: Encapsulation (User Class)

class User:
    def __init__(self):
        self.__user_name = ""
        self.__pwd = ""

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name   

    def register(self):
        print(f"Registering user: {self.__user_name}")

    def login(self):
        print(f"Logging in: {self.__user_name}")

user = User()
user.set_user("Deepak", "1508")

user.register()
user.login()

# Task 2: Inheritance (User → Student, Faculty)

class User:
    def register(self):
        print("User registered")

    def login(self):
        print("User logged in")


class Student(User):
    def student_greet(self):
        print("Hello Student")


class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")


class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")


# Usage
s = Student()
f = Faculty()
t = TempFaculty()

# Parent methods
s.register()
s.login()

# Child methods
s.student_greet()

f.faculty_greet()

t.tempFaculty_greet()
t.register()   

#Task 3: Method Overriding

class User:
    def greet(self):
        print("Welcome User")


class Student(User):
    def greet(self):
        print("Welcome Student")


class Faculty(User):
    def greet(self):
        print("Welcome Faculty")


# Usage
student = Student()
faculty = Faculty()

student.greet()
faculty.greet()

#Task 4: Method Chaining

class User:
    def register(self):
        print("registered")
        return self

    def login(self):
        print("logined")
        return self

    def greet(self):
        print("enjoy everyone")
        return self


# Usage
user = User()
user.login().greet().register()

 #Task 5: Combined Task (Real-Time)

class User:
    users_count = 0   # class variable

    def __init__(self, name, pwd):
        self.__name = name
        self.__pwd = pwd
        User.users_count += 1

    def login(self):
        print(f"{self.__name} logged in")
        return self

    def register(self):
        print(f"{self.__name} registered")
        return self

    def greet(self):
        print("Welcome User")
        return self


class Student(User):
    def greet(self):
        print("Welcome Student")
        return self


class Faculty(User):
    def greet(self):
        print("Welcome Faculty")
        return self


# Usage
u1 = Student("john", "123")
u2 = Faculty("smith", "456")

u1.login().greet().register()
u2.login().greet().register()

print("Total Users:", User.users_count)