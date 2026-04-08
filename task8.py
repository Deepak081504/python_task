# Smart Expense Manager (Real-Time Project)

from abc import ABC, abstractmethod
import mysql.connector
from functools import reduce
from datetime import datetime
 
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class User(Database):
    def __init__(self, name):
        self.__name = name  
        self.user_id = None

    def connect(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Deepak123",
            database="final_task"
        )

    def get_name(self):
        return self.__name

    def create_user(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name) VALUES (%s)", (self.__name,))
        conn.commit()
        self.user_id = cursor.lastrowid
        conn.close()
        print(f"User {self.__name} created with ID {self.user_id}")

class Expense(User):
    def __init__(self, user_id, name, amount, category, description, date):
       
        super().__init__(name) 
        self.user_id = user_id
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    def add_expense(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO expenses (user_id, amount, category, description, date)
                          VALUES (%s, %s, %s, %s, %s)""",
                       (self.user_id, self.amount, self.category, self.description, self.date))
        conn.commit()
        conn.close()
        print("Expense added successfully!")

# VIEW WITH JOIN 

    def fetch_all_expenses(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""SELECT u.name, e.amount, e.category, e.description, e.date
                          FROM expenses e JOIN users u ON e.user_id = u.user_id
                          WHERE e.user_id = %s""", (self.user_id,))
        rows = cursor.fetchall()
        conn.close()
        return rows

# FUNCTIONAL PROGRAMMING & LOGIC

def total_expense(expenses):
    
    amounts = list(map(lambda x: x[1], expenses))
    return reduce(lambda a, b: a + b, amounts) if amounts else 0

def category_spending(expenses):
    
    categories = {exp[2] for exp in expenses}
    return {cat: sum(e[1] for e in expenses if e[2] == cat) for cat in categories}

def highest_expense(expenses):
   
    if not expenses: return None
    return reduce(lambda a, b: a if a[1] > b[1] else b, expenses)

def smart_insight(expenses):
    report = category_spending(expenses)
    if not report: return
    
    max_cat = max(report, key=report.get)
    
    if max_cat == "Food" and report[max_cat] > 2000:
        print(f"Smart Insight: You are spending too much on {max_cat} this month!")
    else:
        print(f"Insight: Your {max_cat} spending is the highest, but under control.")

    # DELETE EXPENSE 

def delete_expense(self, exp_id):
    conn = self.connect()
    cursor = conn.cursor()
    query = "DELETE FROM expenses WHERE exp_id = %s AND user_id = %s"
    cursor.execute(query, (exp_id, self.user_id))
    conn.commit()
    conn.close()
    print(f"Expense ID {exp_id} deleted successfully!")

    #  UPDATE EXPENSE 

def update_expense(self, exp_id, new_amount):
    conn = self.connect()
    cursor = conn.cursor()
    query = "UPDATE expenses SET amount = %s WHERE exp_id = %s AND user_id = %s"
    cursor.execute(query, (new_amount, exp_id, self.user_id))
    conn.commit()
    conn.close()
    print(f"Expense ID {exp_id} updated to {new_amount}!")
    
    
# EXECUTION

# 1. User creation
u1 = User("Deepak") 
u1.create_user()

# 2. Expense entry

e_obj = Expense(u1.user_id, u1.get_name(), 2500, "Food", "Dinner with team", "2026-04-08")
e_obj.add_expense()

# 3. Get Data from DB for Analysis
all_exp = e_obj.fetch_all_expenses()

# 4. Analysis
print("\n--- Expense Report ---")
print(f"Total Spent: {total_expense(all_exp)}")
print(f"Category Wise: {category_spending(all_exp)}")
print(f"Highest Single Expense: {highest_expense(all_exp)}")
smart_insight(all_exp)
