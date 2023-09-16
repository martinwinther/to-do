commands = "add, show, edit, complete or exit"

while True:
    user_action = input("Type one of the following commands: " + commands + ": ")

    match user_action.strip():
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'sow':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index+1}. {item}")

        case 'edit':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index+1}. {item}")

            number = int(input("Which number do you want to edit? "))
            existing_todo = todos[number - 1]
            print("Number " + str(number) + " is " + existing_todo)

            new_todo = input("Edit it to: ")
            todos[number-1] = new_todo + '\n'
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            print("Edit saved!")

        case 'complete':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index + 1}. {item}")

            number = int(input("Which number do you want to complete? "))
            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            print(f"Good job! \n{todo_to_remove} was removed from the list.")

        case 'exit':
            break

        case _:
            print("Please enter one of the following commands: " + commands + ": ")

print("Here are your tasks: ")


with open('todos.txt', 'r') as file:
    todos = file.readlines()

for index, item in enumerate(todos):
    item = item.strip("\n")
    print(f"{index + 1}. {item}")

print("Bye!")





