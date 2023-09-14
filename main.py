commands = "add, show, edit, complete or exit"

while True:
    user_action = input("Type one of the following commands: " + commands + ": ")

    match user_action.strip():
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('todos.txt', 'r')  # opens and reads the existing txt
            todos = file.readlines()  # adds the existing txt to a list called todos
            file.close()  # closes the file

            todos.append(todo)  # appends the new to-do to the list

            file = open('todos.txt', 'w')  # opens the todos in write mode
            file.writelines(todos)  # overwrites the file with the new txt
            file.close()

        case 'show' | 'snow':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                print(f"{index+1}. {item}")

        case 'edit':
            for index, item in enumerate(todos):
                print(f"{index+1}. {item}")

            number = int(input("Which number do you want to edit? "))
            existing_todo = todos[number - 1]
            print("Number " + str(number) + " is " + existing_todo)
            new_todo = input("Edit it to: ")
            todos[number - 1] = new_todo
            print("Edit saved!")

        case 'complete':
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item}")
            number = int(input("Which number do you want to complete? "))
            todos.pop(number - 1)
            print("Good job!")

        case 'exit':
            break

        case _:
            print("Please enter one of the following commands: " + commands + ": ")

print("Here are your tasks: ")

for item in todos:
    print(str(todos.index(item) + 1) + ". " + item)

print("Bye!")





