import sqlite3
from datetime import datetime

# Connect to DB
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    category TEXT,
    date TEXT,
    note TEXT
)
""")
conn.commit()

def add_expense(amount, category, note=""):
    date = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO expenses (amount, category, date, note) VALUES (?, ?, ?, ?)",
                   (amount, category, date, note))
    conn.commit()
    print("✅ Expense added successfully!")

def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def summary():
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rows = cursor.fetchall()
    print("\n📊 Expense Summary by Category:")
    for row in rows:
        print(f"{row[0]}: ₹{row[1]}")

# Menu
while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Summary")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        amt = float(input("Enter amount: "))
        cat = input("Enter category: ")
        note = input("Enter note: ")
        add_expense(amt, cat, note)
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        summary()
    elif choice == "4":
        break
    else:
        print("❌ Invalid choice!")
