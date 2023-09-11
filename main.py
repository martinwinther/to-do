todos = []

while True:
    user_action = input("Type add, show or exit: ")

    match user_action.strip():
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'snow':
            for item in todos:
                print(item)
        case 'exit':
            break
        case _:
            print("Please enter a correct command")
print("Bye!")




