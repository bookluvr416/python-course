from modules import functions
import FreeSimpleGUI as sG
import time

sG.theme("DarkPurple4")

label = sG.Text("Type in a to-do")
input_box = sG.InputText(tooltip="Enter todo", key="todo")
add_button = sG.Button("Add")
list_box = sG.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sG.Button("Edit")
complete_button = sG.Button("Complete")
exit_button = sG.Button("Exit")
timestamp = sG.Text("", key="timestamp")

layout = [[timestamp],
          [label, input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]

window = sG.Window('To-Do App',
                   layout=layout,
                   font=('Helvetica', 12))

while True:
    event, values = window.read(timeout=200)
    match event:
        case "todos":
            value = values['todos'][0].strip('\n')
            window['todo'].update(value=value)
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo'].strip() + '\n')
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo)
                todos[index] = f"{new_todo}\n"

                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sG.popup("Please select an item first.", font=("Helvetica", 12))
        case "Complete":
            try:
                todo = values['todos'][0]
                todos = functions.get_todos()
                index = todos.index(todo)
                todos.pop(index)

                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sG.popup("Please select an item first.", font=("Helvetica", 12))
        case "Exit":
            break
        case sG.WIN_CLOSED:
            break
        case _:
            window['timestamp'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

window.close()
