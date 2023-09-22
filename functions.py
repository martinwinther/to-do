
def get_todos(filepath="todos.txt"):
    """
    Read a text file and return the list of to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """
    Writes a to-do item to a text file and checks for newLine
    """
    # Check if the last item has a newline at the end, if not, add one
    if todos_arg and not todos_arg[-1].endswith('\n'):
        todos_arg[-1] += '\n'
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


def print_todos(todos_arg):
    """
    Prints the context of the text file and strips newLines
    """
    for index, item in enumerate(todos_arg):
        item = item.strip("\n")
        print(f"{index + 1}. {item}")