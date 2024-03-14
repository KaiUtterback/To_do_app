'''
Project Requirements
User Interface (UI):
Create a command-line interface (CLI) for the To-Do List Application.
Display a welcoming message and a menu with the following options:
Welcome to the To-Do List App!

Menu:
1. Add a task
2. View tasks
3. Mark a task as complete
4. Delete a task
5. Quit

To-Do List Features:

Implement the following features for the To-Do List:
Adding a task with a title (by default “Incomplete”).
Viewing the list of tasks with their titles and statuses (e.g., "Incomplete" or "Complete").
Marking a task as complete.
Deleting a task.
Quitting the application.

User Interaction:
Allow users to interact with the application by selecting menu options using input().
Implement input validation to handle unexpected user input gracefully.

Error Handling:
Implement error handling using try, except, else, and finally blocks to handle potential issues.

Code Organization:
Organize your code into functions to promote modularity and readability.
Use meaningful function names with appropriate comments and docstrings for clarity.

Testing and Debugging:
Thoroughly test your application to identify and fix any bugs.
Consider edge cases, such as empty task lists or incorrect user input.

Documentation:
Include a README file that explains how to run the application and provides a brief overview of its features.

Optional Features (Bonus):
If you feel adventurous, you can add extra features like task priorities, due dates, or color-coding tasks based on their status.

GitHub Repository:
Create a GitHub repository for your project.
Commit your code to the repository regularly.
Include a link to your GitHub repository in your project documentation.

Submission
Submit your project, including all source code files and the README, to your instructor or designated platform.

Project Tips
Start by designing a simple user interface and plan the program's structure.
Test your code frequently as you build each feature to ensure everything works as expected.
Collaborate with fellow learners and seek help when needed. Remember, learning is a communal effort!
By completing this project, you'll gain practical experience in Python programming and have a useful To-Do List Application to help you stay organized 
in your own life.
'''

incomplete_tasks = []
complete_tasks = []

def add_task():
    while True:
        print()
        a_task = input("Enter a task you'd like to add to your to-do list: ").lower()
        incomplete_tasks.append(a_task)

        continue_adding = input("Would you like to add another task? y or n? ").lower()
        if continue_adding == 'n':
            break
        else:
            continue

def view_tasks():
    while True:
        print()
        print("Incomplete Tasks:")
        print(incomplete_tasks)
        print()
        print("Completed Tasks:")
        print(complete_tasks)
        
        continue_view = input("Type x to exit: ").lower()
        if continue_view == 'x': 
            break
        else: 
            print("Try again")


def mark_complete():
    while True:
        print()
        print(incomplete_tasks)
        print()
        task = input('Enter the completed task from the list above: ').lower()
        for task in incomplete_tasks:
            if task in incomplete_tasks:
                complete_tasks.append(task)
                incomplete_tasks.remove(task)
                print(f"{task} has been marked as completed.\nView your tasks to see it in the completed tasks list.")
        complete_more = input("Would you like to complete another task? y or n: ").lower()
        if complete_more == 'n': break
        else: continue


def delete_task():
    while True:
        print()
        print('Incomplete Tasks:')
        print(incomplete_tasks)
        print()
        print("Completed Tasks:")
        print(complete_tasks)

        delete = input("Choose a task to delete: ").lower()
        if delete == incomplete_tasks:
            incomplete_tasks.remove(delete)
        elif delete == complete_tasks:
            complete_tasks.remove(delete)
        
        delete_again = input('Would you like to delete another task? y or n: ').lower()
        if delete_again == 'n':
            break
        else:
            continue

def run_app():
    while True:
        print()
        print("Welcome to Kai's To Do List!")
        print("Menu:")
        print('-' * 15)
        print('1: Add A Task')
        print('2: View Tasks')
        print('3: Mark A Task As Complete')
        print('4: Delete A Task')
        print('5: Quit')
        choice = int(input("Please enter a number: "))

        if choice == 1:
            add_task()
        if choice == 2:
            view_tasks()
        if choice == 3: 
            mark_complete()
        if choice == 4:
            delete_task()
        if choice == 5: 
            print("Thank you for using Kai's To Do List!")
            break
run_app()