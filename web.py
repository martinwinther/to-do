import streamlit as st
import functions


def add_todo():
    """
    Adds a new to-do item to the list
    """
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("To Do List")
st.subheader("Add a new task")
st.write("Type your task below and press enter.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,  key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label='Enter a new task', label_visibility='hidden', placeholder="Add a new task:",
              on_change=add_todo, key='new_todo')
