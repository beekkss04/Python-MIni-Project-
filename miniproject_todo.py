print("\n-------------------- TASK FLOW --------------------")

tasks = []  

def add_task():
    task = input("\nEnter a Task: ")
    tasks.append({"Task": task, "Status": "pending"})
    print("\nTask Added Successfully!")

def view_task():
    if len(tasks) == 0:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks to-do:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t['Task']} - {t['Status']}")

def delete_task():
    if len(tasks) == 0:
        print("\nNo Tasks to delete!")
    else:
        t_no = int(input("\nEnter the task no. you want to delete: ")) - 1
        if 0 <= t_no < len(tasks):
            rm_t = tasks.pop(t_no)
            print(f"\nTask Removed: {rm_t['Task']}")
        else:
            print("\nInvalid Task Number Entered")

def mark_done():
    if len(tasks) == 0:
        print("\nTasks list is empty!")
    else:
        t_no = int(input("\nEnter the task no. you want to mark as done: ")) - 1
        if 0 <= t_no < len(tasks):
            tasks[t_no]['Status'] = 'done'
            print(f"\nTask '{tasks[t_no]['Task']}' has been marked as Done")
        else:
            print("\nInvalid Task Number Entered")

def menu():
    while True:
        print("\n********** Main Menu **********")
        print("\n1. Add a New Task")
        print("2. View All Tasks")
        print("3. Remove a Task")
        print("4. Mark Task as Done")
        print("5. Exit")

        choice = int(input("\nChoose an option (1-5): "))

        if choice == 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            mark_done()
        elif choice == 5:
            print("\tThank you!\nExiting the application...")
            exit()
        else:
            print("Invalid Choice!!! Please choose from option 1-5")

menu()
