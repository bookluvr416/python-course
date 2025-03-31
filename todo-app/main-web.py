import streamlit as st
from modules import functions

todos = functions.get_todos()

def create_header():
    st.title("My Todo App")

def create_checkboxes():
    for index, todo in enumerate(todos):
        checkbox = st.checkbox(todo.strip('\n'), key=todo)
        if checkbox:
            todos.pop(index)
            functions.write_todos(todos)
            del st.session_state[todo]
            st.rerun()

def add_todo():
    new_todo = st.session_state['new_todo']
    new_todo = f"{new_todo.capitalize()}\n"
    if new_todo not in todos:  # Add this if-condition to fix the issue
        print('needs to be added')
        todos.append(new_todo)
        functions.write_todos(todos)

def create_input():
    st.text_input(label="Enter a todo",
                  on_change=add_todo,
                  key="new_todo")

create_header()
create_checkboxes()
create_input()


