# Todo app using Python

prompt = "Do you want to add, show, edit, remove, or exit? "

# Todo list
todos = []

while True:
    action = input(prompt)
    action = action.strip()

    match action:
        case 'add':
            todo = input("add a new item: ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            for item in todos:
                print(item)
            number = input("What is the number of todo to edit: ")
            number = int(number) - 1
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo
        case 'remove':
            number = int(input("What is the number of todo to remove: "))
            todos.pop(number)
        case 'exit':
            break
            