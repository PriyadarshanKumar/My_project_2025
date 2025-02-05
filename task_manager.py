import sqlite3
from datetime import datetime

# Database connection
conn = sqlite3.connect("tasks.db")
c = conn.cursor()

# Create table if not exists
c.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        deadline TEXT,
        status TEXT CHECK(status IN ('pending', 'completed')) NOT NULL DEFAULT 'pending'
    )
''')
conn.commit()

# Function to add a task
def add_task():
    description = input("Enter task description: ")
    deadline = input("Enter deadline (YYYY-MM-DD) or leave blank: ")
    if deadline.strip():
        try:
            datetime.strptime(deadline, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format! Use YYYY-MM-DD.")
            return
    else:
        deadline = None
    
    c.execute("INSERT INTO tasks (description, deadline) VALUES (?, ?)", (description, deadline))
    conn.commit()
    print("Task added successfully!")

def view_tasks(status_filter=None):
    if status_filter:
        c.execute("SELECT * FROM tasks WHERE status = ?", (status_filter,))
    else:
        c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"[{task[0]}] {task[1]} | Deadline: {task[2] or 'N/A'} | Status: {task[3]}")

def update_task():
    task_id = input("Enter task ID to update: ")
    c.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    task = c.fetchone()
    if not task:
        print("Task not found!")
        return
    
    print("1. Mark as completed")
    print("2. Change description")
    choice = input("Choose an option: ")
    
    if choice == "1":
        c.execute("UPDATE tasks SET status = 'completed' WHERE id = ?", (task_id,))
    elif choice == "2":
        new_desc = input("Enter new description: ")
        c.execute("UPDATE tasks SET description = ? WHERE id = ?", (new_desc, task_id))
    else:
        print("Invalid choice!")
        return
    
    conn.commit()
    print("Task updated successfully!")

def delete_task():
    task_id = input("Enter task ID to delete: ")
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    print("Task deleted successfully!")

def main():
    while True:
        print("\nTask Manager")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. View pending tasks")
        print("4. View completed tasks")
        print("5. Update a task")
        print("6. Delete a task")
        print("7. Exit")
        choice = input("Select an option: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks("pending")
        elif choice == "4":
            view_tasks("completed")
        elif choice == "5":
            update_task()
        elif choice == "6":
            delete_task()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid option! Please choose again.")

if __name__ == "__main__":
    main()

conn.close()
