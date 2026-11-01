

import random

print("Welcome to the Toolkit!")

while True:
    print("\nMenu:")
    print("1. Play Number Guessing Game")
    print("2. Manage To-Do List")
    print("3. Use Simple Calculator")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        # Number Guessing Game
        def number_guessing_game():
            """A game where the user tries to guess a random number between 1 and 100."""
            number = random.randint(1, 100)
            attempts = 0
            while True:
                guess = input("Guess a number between 1 and 100: ")
                if not guess.isdigit():
                    print("Invalid input. Please enter a number.")
                    continue
                guess = int(guess)
                attempts += 1
                if guess < number:
                    print("Too low!")
                elif guess > number:
                    print("Too high!")
                else:
                    print(f"Congratulations! You guessed the number in {attempts} attempts.")
                    break
        number_guessing_game()
    elif choice == "2":
        # To-Do List
        def todo_list():
            """A simple to-do list where users can add, remove, and view tasks."""
            tasks = []
            while True:
                print("\nTo-Do List Menu:")
                print("1. Add task")
                print("2. Remove task")
                print("3. View tasks")
                print("4. Back to main menu")
                task_choice = input("Choose an option: ")
                if task_choice == "1":
                    task = input("Enter a task: ")
                    tasks.append(task)
                    print(f"Task '{task}' added.")
                elif task_choice == "2":
                    if not tasks:
                        print("No tasks to remove.")
                        continue
                    print("Tasks:")
                    for i, task in enumerate(tasks, start=1):
                        print(f"{i}. {task}")
                    task_num = input("Enter task number to remove: ")
                    if not task_num.isdigit() or int(task_num) < 1 or int(task_num) > len(tasks):
                        print("Invalid task number.")
                        continue
                    task_num = int(task_num)
                    removed_task = tasks.pop(task_num - 1)
                    print(f"Task '{removed_task}' removed.")
                elif task_choice == "3":
                    if not tasks:
                        print("No tasks.")
                        continue
                    print("Tasks:")
                    for i, task in enumerate(tasks, start=1):
                        print(f"{i}. {task}")
                elif task_choice == "4":
                    break
                else:
                    print("Invalid choice. Please try again.")
        todo_list()
    elif choice == "3":
        # Simple Calculator
        def simple_calculator():
            """A basic calculator that performs addition, subtraction, multiplication, and division."""
            while True:
                print("\nCalculator Menu:")
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")
                print("5. Back to main menu")
                calc_choice = input("Choose an operation: ")
                if calc_choice in ["1", "2", "3", "4"]:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                    if calc_choice == "1":
                        print(f"{num1} + {num2} = {num1 + num2}")
                    elif calc_choice == "2":
                        print(f"{num1} - {num2} = {num1 - num2}")
                    elif calc_choice == "3":
                        print(f"{num1} * {num2} = {num1 * num2}")
                    elif calc_choice == "4":
                        if num2 != 0:
                            print(f"{num1} / {num2} = {num1 / num2}")
                        else:
                            print("Cannot divide by zero.")
                elif calc_choice == "5":
                    break
                else:
                    print("Invalid choice. Please try again.")
        simple_calculator()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
