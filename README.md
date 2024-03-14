## Kai's To-Do List Application

### Overview
This is a command-line interface (CLI) application designed to help users manage their tasks efficiently. The application provides a simple menu-driven interface allowing users to add tasks, view tasks, mark tasks as complete, delete tasks, and quit the application.

### Features
- **Adding Tasks**: Users can add tasks to the to-do list with an option to specify the priority level (high, medium, or low).
- **Viewing Tasks**: Users can view both incomplete and completed tasks. Incomplete tasks are color-coded based on their priority level for easy identification.
- **Marking Tasks as Complete**: Users can mark tasks as complete, moving them from the incomplete tasks list to the completed tasks list.
- **Deleting Tasks**: Users can delete tasks from both the incomplete and completed tasks lists.
- **Error Handling**: The application includes error handling mechanisms to gracefully handle unexpected user input or errors during task management operations.

### Usage
1. Upon launching the application, users are greeted with a menu displaying various options.
2. Users can select options from the menu using numeric input.
3. To add a task, users choose option 1 and provide the task name along with its priority level.
4. To view tasks, users choose option 2. Incomplete tasks are displayed with priority-based color coding, and completed tasks are listed separately.
5. To mark a task as complete, users choose option 3 and enter the name of the completed task.
6. To delete a task, users choose option 4 and select the task to delete.
7. To quit the application, users choose option 5.

### Installation and Setup
1. Clone the repository from GitHub
2. Ensure you have Python installed on your system.
3. Navigate to the directory containing the application files.
4. Run the `todo_list.py` file using Python.
5. Follow the on-screen instructions to manage your tasks.

### Optional Features
- Task Prioritization: Users can assign priority levels to tasks (high, medium, low).
- Color-Coding: Tasks are color-coded based on their priority level for visual distinction.
