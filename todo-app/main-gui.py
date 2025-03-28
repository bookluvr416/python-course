from modules import functions
import FreeSimpleGUI as sG

label = sG.Text("Type in a to-do")
input_box = sG.InputText(tooltip="Enter todo", key="todo")
add_button = sG.Button("Add")

list_box = sG.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sG.Button("Edit")

layout = [[label, input_box, add_button], [list_box, edit_button]]

window = sG.Window('To-Do App',
                   layout=layout,
                   font=('Helvetica', 12))

while True:
    event, values = window.read()
    print(event)
    print(values)

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
            todo = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo)
            todos[index] = f"{new_todo}\n"

            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Complete":
            break
        case sG.WIN_CLOSED:
            break

window.close()
