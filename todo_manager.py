import os
import sys

TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from local file if it exists."""
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            for line in file:
                tasks.append(line.strip())
    return tasks

def save_tasks(tasks):
    """Save current tasks list into the local text file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    """Display all tasks with status indicators."""
    if not tasks:
        print("\n📭 Your To-Do list is currently empty!\n")
        return False
    
    print("\n========================================")
    print(" 📝 YOUR SMART TO-DO LIST               ")
    print("========================================")
    for index, task in enumerate(tasks, 1):
        print(f" {index}. {task}")
    print("========================================\n")
    return True

def add_task(tasks):
    """Add a new task to the list."""
    task_name = input("\nEnter the task description: ").strip()
    if task_name:
        tasks.append(f"[Pending] {task_name}")
        save_tasks(tasks)
        print(f"✅ Task added successfully!\n")
    else:
        print("❌ Task cannot be empty!\n")

def complete_task(tasks):
    """Mark a pending task as completed."""
    if not show_tasks(tasks):
        return
    
    try:
        choice = int(input("Enter the task number to mark as completed: "))
        if 1 <= choice <= len(tasks):
            if "[Completed]" in tasks[choice - 1]:
                print("⚠️ This task is already marked as completed!\n")
            else:
                # Replace [Pending] with [Completed]
                tasks[choice - 1] = tasks[choice - 1].replace("[Pending]", "[Completed]")
                save_tasks(tasks)
                print("🎉 Task marked as completed!\n")
        else:
            print("❌ Invalid task number!\n")
    except ValueError:
        print("❌ Please enter a valid number!\n")

def delete_task(tasks):
    """Delete a task from the list."""
    if not show_tasks(tasks):
        return
    
    try:
        choice = int(input("Enter the task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"🗑️ Deleted: {removed}\n")
        else:
            print("❌ Invalid task number!\n")
    except ValueError:
        print("❌ Please enter a valid number!\n")

def main():
    tasks = load_tasks()
    
    while True:
        print("========================================")
        print(" 🎯 SMART TO-DO LIST MANAGER            ")
        print("========================================")
        print("1. View Tasks")
        print("2. Add New Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ").strip()
        
        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("\nExiting Smart To-Do Manager. Keep crushing your goals! 👋\n")
            sys.exit()
        else:
            print("❌ Invalid choice! Please select between 1 to 5.\n")

if __name__ == "__main__":
    main()