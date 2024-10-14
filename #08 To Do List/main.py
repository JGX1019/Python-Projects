import json
import os

folder_name = "Python-Projects\\#08 To Do List"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)
a = os.path.join(folder_name, 'data.json')

def get_user_input():
    description = input("\nEnter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (high/low): ")
    status = input("Enter status (complete/pending): ")
    print("Task added!")
    entry = {"description": description, "due_date": due_date, "priority": priority, "status": status}
    return entry

def list():
    n = 0
    try:
        with open(a) as f:
            data = json.load(f)
        print("\nTasks:\n")
        for task in data['data']:
            n = n + 1
            print(f"{str(n)}. {task['description']} - ({task['priority']}, {task['status']}) - {task['due_date']}")
    except FileNotFoundError:
        print("File not found please create data.json and try again\n")

def save_to_json(entry, a):
    try:
        with open(a, "r+") as f:
            data = json.load(f)
            data['data'].append(entry)
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
    except FileNotFoundError:
        with open(a, "w") as f:
            json.dump([entry], f, indent=4)

def delete_task(a):
    try:
        with open(a) as f:
            data = json.load(f)
        
        list()  

        task_number = int(input("\nEnter task number to delete: "))
        
        if 1 <= task_number <= len(data['data']):
            del data['data'][task_number - 1]
            with open(a, "w") as f:
                json.dump(data, f, indent=4)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("No tasks to delete.")
    except ValueError:
        print("Please enter a valid number")

def sort():
    with open(a) as f:
            data = json.load(f)
    print("\nSort by:\n1. Status\n2. Priority")

    while True:
        filter = input("\nChoose the filter method: ")

        if filter.isdigit() is True:
            filter = int(filter)

            if filter == 1:
                    status_grade = lambda task: task['status']
                    sorted_data = sorted(data['data'], key=status_grade)
                    print("\nSorted Tasks:")
                    for i, task in enumerate(sorted_data, start=1):
                        print(f"{i}. {task['description']} - ({task['priority']}, {task['status']}) - {task['due_date']}")
                    break
            elif filter == 2:
                    priority_grade = lambda task: task['priority']
                    sorted_data = sorted(data['data'], key=priority_grade)
                    print("\nSorted Tasks:")
                    for i, task in enumerate(sorted_data, start=1):
                        print(f"{i}. {task['description']} - ({task['priority']}, {task['status']}) - {task['due_date']}")
                    break
            else:
                print("Pick from 1 to 2")
        else:
            print("Invalid choice")
            
print("\n1. Add task \n2. List tasks \n3. Filter tasks \n4. Delete task \n5. Exit")

while True:
    Action = input("\nChoose a number from the options above: ")

    if Action.isdigit() is True:
        Action = int(Action)

        if Action == 1:
            new_task = get_user_input()
            save_to_json(new_task, a)  
        elif Action == 2:
            list()
        elif Action == 3:
            sort()
        elif Action == 4:
            delete_task(a)
        elif Action == 5:
            break
        else:
            print("Pick from 1 to 5")
        
    else:
        print("Invalid choice")