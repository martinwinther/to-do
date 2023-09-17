commands = "add, show, edit, complete or exit"

while True:
    user_action = input("Type one of the following commands: " + commands + ": ")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:]  # adds the input after the character with index 4

        with open('todos.txt', 'r') as file:
            todos = file.readlines()
            
        # Check if the last item has a newline at the end, if not, add one
        if todos and not todos[-1].endswith('\n'):
            todos[-1] += '\n'

        todos.append(todo + '\n')

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index+1}. {item}")

    elif 'edit' in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index+1}. {item}")

        number = int(user_action[5:])
        existing_todo = todos[number - 1]
        print("Number " + str(number) + " is " + existing_todo)

        new_todo = input("Edit it to: ")
        todos[number-1] = new_todo + '\n'
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
        print("Edit saved!")

    elif 'complete' in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        number = int(user_action[9:])
        todo_to_remove = todos[number - 1].strip('\n')
        todos.pop(number - 1)
        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        print(f"Good job! \n{todo_to_remove} was removed from the list.")

    elif 'exit' in user_action:
        break

    else:
        print("Input is not valid.")

print("Here are your tasks: ")


with open('todos.txt', 'r') as file:
    todos = file.readlines()

for index, item in enumerate(todos):
    item = item.strip("\n")
    print(f"{index + 1}. {item}")

print("Bye!")





