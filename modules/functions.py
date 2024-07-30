def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list of to-do items."""
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos

def write_todos(todo_arg, filepath="todos.txt"):
    """ Write a to-do item to a text file"""
    with open(filepath, 'w') as file:
        file.writelines(todo_arg)
