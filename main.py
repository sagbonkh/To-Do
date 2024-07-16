# Todo app using Python
# Adds todos to a todos.txt file

prompt = "Do you want to add, show, edit, remove, or exit? "

while True:
    action = input(prompt)
    action = action.strip()

    if action.startswith("add"):
        todo = action[4:]
        
        # Read data from todo text file
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo + '\n')
        
        # write data to todo text file
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
            
    elif action.startswith('show'):
        # Read data from todo text file
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif action.startswith('edit'):
        # Read data from todo text file
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        number = int(action[5:])
        number = number - 1
        
        new_todo = input("Enter a new todo: ")
        todos[number] = new_todo + '\n'

        # write data to todo text file
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif action.startswith('remove'):
        # Read data from todo text file
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        number = int(action[7:])
        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        # write data to todo text file
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
        message = f"Todo {todo_to_remove} was removed from the list."
        print(message)

    elif action.startswith('exit'):
        break
    else:
        print("Enter a valid command")
            