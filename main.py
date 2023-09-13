todos = []

commands = "add, show, edit, complete or exit"

while True:
    user_action = input("Type one of the following commands: " + commands + ": ")

    match user_action.strip():
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'snow':
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





