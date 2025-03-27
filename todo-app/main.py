TODOS_FILE = 'todos.txt'

def get_todos():
    with open(TODOS_FILE, 'r') as opened_file:
        opened_todos = opened_file.readlines()
    return opened_todos

def write_todos(new_todos):
    with open(TODOS_FILE, 'w') as opened_file:
        opened_file.writelines(new_todos)


while True:
    # get user input and strip out extra whitespace
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(f"{todo.capitalize()}\n")

        write_todos(todos)

        print("Added!")
    elif 'show' == user_action or 'display' == user_action:
        todos = get_todos()

        for index, item in enumerate(todos):
            print(f"{index + 1}. {item.strip('\n')}")
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            index = number - 1

            todos = get_todos()

            if number > len(todos) or number < 1:
                print("Invalid todo")
            else:
                todo = input("Enter edited todo:") + "\n"
                todos[index] = todo.capitalize()

                write_todos(new_todos=todos)

                print("Edited!")
        except IndexError:
            print("Invalid todo")
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            index = number - 1

            todos = get_todos()

            if number > len(todos) or number < 1:
                print("Invalid todo")
            else:
                todo = todos.pop(index)

                write_todos(new_todos=todos)

                print(f"Completed {todo.strip('\n')}!")
        except IndexError:
            print("Invalid todo")
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action == 'exit':
        break;
    else:
        print("Unknown command entered.")

print("Bye!")