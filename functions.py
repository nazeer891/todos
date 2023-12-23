FILEPATH = "todos.txt"

def get_todos(filePath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filePath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos,filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos)

