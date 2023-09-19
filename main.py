def get_todos():
    with open('todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


commands = "add, show, edit, complete or exit"

while True:
    user_action = input("Type one of the following commands: " + commands + ": ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]  # adds the input after the character with index 4

        todos = get_todos()
            
        # Check if the last item has a newline at the end, if not, add one
        if todos and not todos[-1].endswith('\n'):
            todos[-1] += '\n'

        todos.append(todo + '\n')

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index+1}. {item}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])

            todos = get_todos()

            # Check if the number is within the valid range
            if 1 <= number <= len(todos):
                for index, item in enumerate(todos):
                    item = item.strip("\n")
                    print(f"{index+1}. {item}")

                existing_todo = todos[number - 1]
                print("Number " + str(number) + " is " + existing_todo)

                new_todo = input("Edit it to: ")
                todos[number-1] = new_todo + '\n'
                with open('todos.txt', 'w') as file:
                    file.writelines(todos)
                print("Edit saved!")
            else:
                print("Your command is not valid")
                continue
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            todos = get_todos()

            number = int(user_action[9:])
            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            print(f"Good job! \n{todo_to_remove} was removed from the list.")
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Input is not valid.")

print("Here are your tasks: ")


todos = get_todos()

for index, item in enumerate(todos):
    item = item.strip("\n")
    print(f"{index + 1}. {item}")

print("Bye!")





