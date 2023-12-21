#from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)

while True:
    user_input = input("Type add , show , edit , complete or exit: ").lower().strip()
    filePath = "todos.txt"

    if user_input.startswith("add") or user_input.startswith("new"):
        todo = user_input[4:].title()

        if todo != "":
            todos = functions.get_todos()

            todos.append(todo + "\n")
            user_input.title()
            functions.write_todos(todos)

    elif user_input.startswith("show"):
        todos = functions.get_todos()

        todos = [item.strip("\n") for item in todos]

        for idx,todo in enumerate(todos):
            print(f"{idx+1}.{todo}")

    elif user_input.startswith("edit"):
        try:
            edit_idx = int(user_input[5:])
            edit_idx = edit_idx - 1
            todos = functions.get_todos()

            new_value = input("Enter a new todo:").strip() + "\n"
            todos[edit_idx] = new_value

            for idx, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{idx+1}.{item}")
            functions.write_todos(todos)
        except (ValueError,IndexError):
            print("Sorry, Your Command is Invalid. Kindly input a valid number after 'edit'")
            continue

    elif user_input.startswith("complete"):
        try:
            todos = functions.get_todos()
            idx = int(user_input[9:])-1
            todo = todos.pop(idx)
            print(f"{todo.strip()} is marked as complete.")
            functions.write_todos(todos)

            for idx,item in enumerate(todos):
                item = item.strip("\n")
                print(f"{idx+1}.{item}")
        except (IndexError,ValueError):
            print("Kindly input a Valid Number after 'complete'")
            continue

    elif user_input.startswith("exit"):
        break
    else:
        print("Enter a valid input")

print("Bye")