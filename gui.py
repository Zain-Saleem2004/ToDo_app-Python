import functions
import PySimpleGUI as Sg

label = Sg.Text("Type in a to-do")
input_box = Sg.InputText(tooltip="Enter to-do", key="todo")
add_button = Sg.Button("Add")
listbox = Sg.Listbox(values=functions.get_todos(), key="todos",
                     enable_events=True, size=(45, 10))
edit_button = Sg.Button("Edit")

window = Sg.Window("My To-Do app",
                   layout=[[label], [input_box, add_button], [listbox, edit_button]],
                   font=("Helvetica", 18))
while True:
    event, values = window.read()
    print(1,event)
    print(2,values)
    print(3,values["todos"])
    match event:
        case "Add":
            Todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            Todos.append(new_todo)
            functions.write_todos(Todos)
            window["todos"].update(values=Todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values["todo"]
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "todos":
            window["todo"].update(value=values['todos'][0])
        case Sg.WIN_CLOSED:
            break
window.close()
