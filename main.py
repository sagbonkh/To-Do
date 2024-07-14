# Todo app using Python
# Adds todos to a todos.txt file

prompt = "Do you want to add, show, edit, remove, or exit? "

while True:
    action = input(prompt)
    action = action.strip()

    match action:
        case 'add':
            todo = input("add a new item: ") + "\n"
            
            # Read data from todo text file
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)
            
            # write data to todo text file
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            
        case 'show':
            # Read data from todo text file
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            # Read data from todo text file
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            for item in todos:
                print(item)
            number = input("What is the number of todo to edit: ")
            number = int(number) - 1


            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            # write data to todo text file
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'remove':
            # Read data from todo text file
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            number = int(input("What is the number of todo to remove: "))
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            # write data to todo text file
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        case 'exit':
            break
            