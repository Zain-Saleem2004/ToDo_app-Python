import functions
import PySimpleGUI as Sg

label = Sg.Text("Type in a to-do")
input_box = Sg.InputText(tooltip="Enter to-do", key="todo")
add_button = Sg.Button("Add")

window = Sg.Window("My To-Do app",
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 18))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            Todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            Todos.append(new_todo)
            functions.write_todos(Todos)

        case Sg.WIN_CLOSED:
            break
window.close()
