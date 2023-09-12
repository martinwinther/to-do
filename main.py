todos = []

commands = "add, show, edit or exit"

while True:
    user_action = input("Type one of the following commands: " + commands + ": ")

    match user_action.strip():
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'snow':
            for item in todos:
                print(str(todos.index(item) + 1) + ". " + item)

        case 'edit':
            for item in todos:
                print(str(todos.index(item) + 1) + ". " + item)
            number = int(input("Which number do you want to edit? "))
            existing_todo = todos[number - 1]
            print("Number " + str(number) + " is " + existing_todo)
            new_todo = input("Edit it to: ")
            todos[number - 1] = new_todo
            print("Edit saved!")
        case 'exit':
            break
        case _:
            print("Please enter one of the following commands: " + commands + ": ")

print("Here are your tasks: ")

for item in todos:
    print(str(todos.index(item) + 1) + ". " + item)

print("Bye!")





