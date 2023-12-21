def get_todos(filePath="todos.txt"):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filePath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos,filepath="todos.txt"):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos)

