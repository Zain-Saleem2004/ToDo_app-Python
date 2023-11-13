import functions
import PySimpleGUI as Sg

label = Sg.Text("Type in a to-do")
input_box = Sg.InputText(tooltip="Enter to-do", key="todo")
add_button = Sg.Button("Add")
listbox = Sg.Listbox(values=functions.get_todos(), key="todos",
                     enable_events=True, size=(45, 10))
edit_button = Sg.Button("Edit")
complete_button = Sg.Button("Complete")
exit_button = Sg.Button("Exit")

window = Sg.Window("My To-Do app",
                   layout=[[label],
                           [input_box, add_button],
                           [listbox, edit_button, complete_button],
                           [exit_button]],
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
            # realtime change on the Input area when clicking on a todo
            window["todo"].update(value=values['todos'][0])

        case "Complete":
            todo_to_complete = values["todos"][0]
            todos = functions.get_todos()
            index = todos.index(todo_to_complete)
            todos.pop(index)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")

        case "Exit":
            break

        case Sg.WIN_CLOSED:
            break
window.close()
