A simple command-line task management system built using Python and SQLite. This application allows users to add, view, update, delete, and filter tasks while ensuring persistent storage.

Features
✔ Add a new task with a description and optional deadline
✔ View all tasks or filter by pending or completed status
✔ Update a task (mark as completed or modify description)
✔ Delete a task
✔ Persistent storage using SQLite
✔ Simple text-based menu for easy interaction

Installation & Setup
1. Clone the Repository
git clone https://github.com/yourusername/task-manager-cli.git
cd task-manager-cli
2. Install Dependencies
This application only requires Python’s built-in libraries (sqlite3, datetime), so no extra dependencies are needed.

3. Run the Application
python task_manager.py
Usage
After running the script, you'll see a menu:

Task Manager
1. Add a task
2. View all tasks
3. View pending tasks
4. View completed tasks
5. Update a task
6. Delete a task
7. Exit
Select an option:
Follow the on-screen instructions to manage your tasks.

Example Usage:
Adding a Task
Enter task description: Complete project report
Enter deadline (YYYY-MM-DD) or leave blank: 2025-02-10
Task added successfully!

Viewing Tasks
[1] Complete project report | Deadline: 2025-02-10 | Status: pending

Marking a Task as Completed
Enter task ID to update: 1
1. Mark as completed
2. Change description
Choose an option: 1
Task updated successfully!
