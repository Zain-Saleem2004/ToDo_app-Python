from functions import get_todos, write_todos
import time
completedToDo = []
now = time.strftime("%b %d,%Y %H:%M:%S")
print(f"It is {now}")
while True:
    user_action = input("Enter add,show,edit,compete,delete or exit: ")

    if user_action.startswith("add"):
        toDo = user_action[4:]+"\n"
        ToDos = get_todos()
        ToDos.append(toDo.capitalize())
        write_todos(ToDos, "todos.txt")

    elif user_action.startswith("show"):
        ToDo = get_todos()
        for index, item in enumerate(ToDo):
            print(f"{index+1}-{item}", end="")

    elif user_action.startswith("edit"):
        try:
            i = int(user_action[5:])
            ToDos = get_todos()
            new_toDo = input("Enter the new ToDo: ") + "\n"
            ToDos[i-1] = new_toDo
            write_todos(ToDos, "todos.txt")
        except ValueError:
            print("please enter the number of the todo item after the edit")

    elif user_action.startswith("complete"):
        try:
            i = int(user_action[9:])
            ToDos = get_todos()
            removed_todo = ToDos[i-1].strip("\n")
            completedToDo.append(removed_todo)
            ToDos.pop(i-1)
            write_todos(ToDos, "todos.txt")
            print(f"Todo {removed_todo} was removed from the list.")
        except IndexError:
            print("There is no item with that number!")

    elif user_action.startswith("exit"):
        break

    else:
        print("command is not valid!")

print("Bye!")
