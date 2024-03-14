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
        try:
            a_task = input("Enter a task you'd like to add to your to-do list: ").lower()
        except Exception as e:
            print("An error occurred while getting the task:", e)
            continue

        incomplete_tasks.append(a_task)

        try:
            continue_adding = input("Would you like to add another task? y or n? ").lower()
        except Exception as e:
            print("An error occurred while getting user input:", e)
            continue

        if continue_adding == 'n':
            break

def view_tasks():
    while True:
        print()
        try:
            print("Incomplete Tasks:")
            print("-" * 20)
            for task in incomplete_tasks:
                print(task)
            print()

            print("Completed Tasks:")
            print("-" * 20)
            for task in complete_tasks:
                print(task)
            
            continue_view = input("Type x to exit: ").lower()
        except Exception as e:
            print("An error occurred while displaying tasks:", e)
            continue

        if continue_view == 'x':
            break
        else:
            print("Invalid input. Please try again.")

def mark_complete():
    while True:
        print()
        try:
            print("Incomplete Tasks:")
            print("-" * 20)
            for task in incomplete_tasks:
                print(task)
            print()
            task = input('Enter the completed task from the list above: ').lower()
        except Exception as e:
            print("An error occurred while getting the completed task:", e)
            continue

        try:
            if task in incomplete_tasks:
                complete_tasks.append(task)
                incomplete_tasks.remove(task)
                print(f"{task} has been marked as completed.\nView your tasks to see it in the completed tasks list.")
        except Exception as e:
            print("An error occurred while marking the task as complete:", e)
            continue

        try:
            complete_more = input("Would you like to complete another task? y or n: ").lower()
        except Exception as e:
            print("An error occurred while getting user input:", e)
            continue

        if complete_more == 'n':
            break

def delete_task():
    while True:
        print()
        try:
            print('Incomplete Tasks:')
            print("-" * 20)
            for task in incomplete_tasks:
                print(task)
            print()

            print("Completed Tasks:")
            print("-" * 20)
            for task in complete_tasks:
                print(task)
            print()

            delete = input("Choose a task to delete: ").lower()
        except Exception as e:
            print("An error occurred while getting the task to delete:", e)
            continue

        try:
            if delete in incomplete_tasks:
                incomplete_tasks.remove(delete)
            elif delete in complete_tasks:
                complete_tasks.remove(delete)
        except Exception as e:
            print("An error occurred while deleting the task:", e)
            continue

        try:
            delete_again = input('Would you like to delete another task? y or n: ').lower()
        except Exception as e:
            print("An error occurred while getting user input:", e)
            continue

        if delete_again == 'n':
            break

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
        
        try:
            choice = int(input("Please enter a number: "))
        except Exception as e:
            print("An error occurred while getting user input:", e)
            continue

        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3: 
            mark_complete()
        elif choice == 4:
            delete_task()
        elif choice == 5: 
            print("Thank you for using Kai's To Do List!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
            
run_app()
