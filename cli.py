import functions
import time

COMMANDS = "add, show, edit, complete or exit"

now = time.strftime("%b %d, %Y %H:%M:%S")
(print("It is", now))

while True:
    user_action = input("Type one of the following commands: " + COMMANDS + ": ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]  # adds the input after the character with index 4
        todos = functions.get_todos()
        todos.append(todo + '\n')
        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()
        functions.print_todos(todos)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            todos = functions.get_todos()

            # Check if the number is within the valid range
            if 1 <= number <= len(todos):
                functions.print_todos(todos)

                existing_todo = todos[number - 1]
                print("Number " + str(number) + " is " + existing_todo)

                new_todo = input("Edit it to: ")
                todos[number - 1] = new_todo + '\n'
                functions.write_todos(todos)
                print("Edit saved!")
            else:
                print("Your command is not valid")
                continue
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            todos = functions.get_todos()

            number = int(user_action[9:])
            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)
            functions.write_todos(todos)

            print(f"Good job! \n{todo_to_remove} was removed from the list.")
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Input is not valid.")

print("Here are your tasks: ")

todos = functions.get_todos()

functions.print_todos(todos)

print("Bye!")
