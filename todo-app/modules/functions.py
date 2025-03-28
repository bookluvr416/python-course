TODOS_FILE = '../todos.txt'

def get_todos(filepath=TODOS_FILE):
    """
    Opens a file and returns the list of todos in that file
    """
    with open(filepath, 'r') as opened_file:
        opened_todos = opened_file.readlines()
    return opened_todos

def write_todos(new_todos, filepath=TODOS_FILE):
    """
    Opens a file and writes the todos to that file
    Parameter: list of todos
    """
    with open(filepath, 'w') as opened_file:
        opened_file.writelines(new_todos)

# is not executed when the file is imported
if __name__ == "__main__":
    print(get_todos())