# from functions import get_todos, write_todos
from modules import functions
import time

current_time = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is currently {current_time}")

while True:
    # get user input and strip out extra whitespace
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(f"{todo.capitalize()}\n")

        functions.write_todos(todos)

        print("Added!")
    elif 'show' == user_action or 'display' == user_action:
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            print(f"{index + 1}. {item.strip('\n')}")
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            index = number - 1

            todos = functions.get_todos()

            if number > len(todos) or number < 1:
                print("Invalid todo")
            else:
                todo = input("Enter edited todo:") + "\n"
                todos[index] = todo.capitalize()

                functions.write_todos(new_todos=todos)

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

            todos = functions.get_todos()

            if number > len(todos) or number < 1:
                print("Invalid todo")
            else:
                todo = todos.pop(index)

                functions.write_todos(new_todos=todos)

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