# 🎯 To-Do List CLI

A simple and intuitive command-line interface (CLI) application for managing your daily tasks. Built with Python, this application provides a clean and efficient way to organize your to-do list directly from the terminal.

## ✨ Features

- **➕ Add Tasks**: Easily add new tasks with descriptions
- **👀 View Tasks**: Display all your tasks with completion status
- **🗑️ Remove Tasks**: Delete tasks by their ID number
- **✅ Mark Complete**: Toggle task completion status
- **💾 Persistent Storage**: Tasks are automatically saved to a JSON file
- **🎨 Beautiful UI**: Clean, emoji-enhanced interface for better user experience
- **🔄 Cross-Platform**: Works on Windows, macOS, and Linux

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

### Quick Start
1. Clone or download this repository
2. Navigate to the project directory
3. Run the application

```bash
# Navigate to project directory
cd To-Do-List-CLI

# Run the application
python todo_cli.py
```

## 📖 Usage

### Starting the Application
```bash
python todo_cli.py
```

### Main Menu
When you start the application, you'll see a clean menu:

```
========================================
           🎯 TO-DO LIST 🎯
========================================
1. ➕ Add a Task
2. 👀 View Tasks
3. 🗑️  Remove a Task
4. ✅ Mark Task as Complete/Incomplete
5. 🚪 Exit
========================================
```

### Adding a Task
1. Select option `1` from the main menu
2. Enter your task description
3. Press Enter to confirm
4. Your task will be automatically saved

**Example:**
```
Enter a new task: Buy groceries
✅ Task added successfully!
```

### Viewing Tasks
1. Select option `2` from the main menu
2. All your tasks will be displayed with their status

**Example Output:**
```
📋 Your Tasks:
------------------------------
1. [○] Buy groceries
2. [✓] Complete Python project
3. [○] Call dentist
------------------------------
```

**Status Indicators:**
- `○` = Task not completed
- `✓` = Task completed

### Removing a Task
1. Select option `3` from the main menu
2. View your current tasks
3. Enter the ID number of the task you want to remove
4. Confirm the removal

**Example:**
```
Enter task ID to remove: 2
🗑️ Task 'Complete Python project' removed successfully!
```

### Marking Tasks as Complete/Incomplete
1. Select option `4` from the main menu
2. View your current tasks
3. Enter the ID number of the task to toggle its status
4. The task status will be updated

**Example:**
```
Enter task ID to toggle status: 1
✅ Task 'Buy groceries' marked as completed!
```

### Exiting the Application
- Select option `5` from the main menu
- Or use `Ctrl+C` to interrupt the program

## 💾 Data Storage

- Tasks are automatically saved to a `tasks.json` file
- The file is created in the same directory as the application
- Data persists between application sessions
- No manual save required

### Sample tasks.json Structure
```json
[
  {
    "id": 1,
    "description": "Buy groceries",
    "completed": false
  },
  {
    "id": 2,
    "description": "Complete Python project",
    "completed": true
  }
]
```

## 🛠️ Technical Details

### File Structure
```
To-Do-List-CLI/
├── todo_cli.py          # Main application file
├── tasks.json           # Task storage file (auto-generated)
├── requirements.txt     # Dependencies (none required)
└── README.md           # This file
```

### Key Components
- **TodoList Class**: Core functionality for task management
- **JSON Storage**: Persistent data storage using JSON format
- **Input Validation**: Robust error handling for user inputs
- **Cross-Platform**: Compatible with Windows, macOS, and Linux

### Error Handling
- Invalid menu selections
- Empty task descriptions
- Non-existent task IDs
- File I/O errors
- Keyboard interrupts (Ctrl+C)

## 🔧 Customization

### Changing the Storage File
Modify the `filename` parameter in the `TodoList` class:

```python
todo_list = TodoList("my_tasks.json")
```

### Adding New Features
The modular design makes it easy to extend:
- Add task priorities
- Include due dates
- Add task categories
- Implement task search

## 🐛 Troubleshooting

### Common Issues

**"Python not found" error:**
- Ensure Python is installed and added to your system PATH
- Try using `python3` instead of `python`

**Permission errors:**
- Ensure you have write permissions in the current directory
- Run as administrator if necessary (Windows)

**File corruption:**
- If `tasks.json` becomes corrupted, simply delete it
- The application will create a new, empty file

## 🤝 Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Submitting pull requests
- Improving documentation

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with Python standard library
- Inspired by the need for a simple, efficient task management tool
- Enhanced with modern Python features and best practices

---

**Happy task managing! 🎉**
