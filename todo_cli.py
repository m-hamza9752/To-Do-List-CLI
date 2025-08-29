#!/usr/bin/env python3
"""
To-Do List CLI Application
A simple command-line interface for managing tasks
"""

import os
import json
from typing import List, Dict

class TodoList:
    def __init__(self, filename: str = "tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self) -> List[Dict[str, any]]:
        """Load tasks from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                return []
        return []
    
    def save_tasks(self):
        """Save tasks to JSON file"""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=2)
    
    def add_task(self, description: str):
        """Add a new task"""
        task = {
            "id": len(self.tasks) + 1,
            "description": description,
            "completed": False
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✅ Task added successfully!")
    
    def view_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("📝 No tasks found. Add some tasks to get started!")
            return
        
        print("\n📋 Your Tasks:")
        print("-" * 30)
        for task in self.tasks:
            status = "✓" if task["completed"] else "○"
            print(f"{task['id']}. [{status}] {task['description']}")
        print("-" * 30)
    
    def remove_task(self, task_id: int):
        """Remove a task by ID"""
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                removed_task = self.tasks.pop(i)
                # Reassign IDs to maintain sequential numbering
                for j in range(i, len(self.tasks)):
                    self.tasks[j]["id"] = j + 1
                self.save_tasks()
                print(f"🗑️ Task '{removed_task['description']}' removed successfully!")
                return
        
        print(f"❌ Task with ID {task_id} not found!")
    
    def mark_completed(self, task_id: int):
        """Mark a task as completed"""
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = not task["completed"]
                status = "completed" if task["completed"] else "uncompleted"
                self.save_tasks()
                print(f"✅ Task '{task['description']}' marked as {status}!")
                return
        
        print(f"❌ Task with ID {task_id} not found!")

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    """Display the main menu"""
    print("\n" + "=" * 40)
    print("            TO-DO LIST CLI - MADE BY MUHAMMAD HAMZA")
    print("=" * 40)
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Remove a Task")
    print("4. Mark Task as Complete/Incomplete")
    print("5. Exit")
    print("=" * 40)

def get_user_choice() -> int:
    """Get and validate user input"""
    while True:
        try:
            choice = int(input("\nEnter your choice (1-5): "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("❌ Please enter a number between 1 and 5!")
        except ValueError:
            print("❌ Please enter a valid number!")

def main():
    """Main application loop"""
    todo_list = TodoList()
    
    while True:
        clear_screen()
        show_menu()
        
        choice = get_user_choice()
        
        if choice == 1:
            # Add a Task
            print("\n➕ ADD A NEW TASK")
            print("-" * 20)
            description = input("Enter a new task: ").strip()
            if description:
                todo_list.add_task(description)
            else:
                print("❌ Task description cannot be empty!")
        
        elif choice == 2:
            # View Tasks
            print("\n👀 VIEW TASKS")
            print("-" * 20)
            todo_list.view_tasks()
        
        elif choice == 3:
            # Remove a Task
            print("\n🗑️  REMOVE A TASK")
            print("-" * 20)
            todo_list.view_tasks()
            if todo_list.tasks:
                try:
                    task_id = int(input("Enter task ID to remove: "))
                    todo_list.remove_task(task_id)
                except ValueError:
                    print("❌ Please enter a valid task ID!")
        
        elif choice == 4:
            # Mark Task as Complete/Incomplete
            print("\n✅ MARK TASK AS COMPLETE/INCOMPLETE")
            print("-" * 40)
            todo_list.view_tasks()
            if todo_list.tasks:
                try:
                    task_id = int(input("Enter task ID to toggle status: "))
                    todo_list.mark_completed(task_id)
                except ValueError:
                    print("❌ Please enter a valid task ID!")
        
        elif choice == 5:
            # Exit
            print("\n👋 Thanks for using To-Do List CLI!")
            print("Goodbye! 👋")
            break
        
        # Wait for user to continue
        if choice != 5:
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please try running the program again.")
