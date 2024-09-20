#Basic To-Do List Application
#which appends a txt file to create save data
loop = True
def load_tasks():
    #Function loads tasks from the external text file.
    try:
        with open("task.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    #Function save tasks to the external text file.
    with open("task.txt", "a") as file:
        for task in tasks:
            file.write(task + "\n")

while loop == True:
    print("\nto-do list menu") #menu with all choices 
    print("1. add task")
    print("2. view tasks")
    print("3. delete task")
    print("4. exit")
    choice = input("choose an option (1-4): ")

    if choice == '1':
        task = input("enter the task: ") 
        with open("task.txt", "a") as file: #appends task to external file
            file.write(task + "\n")
        print(f"task '{task}' added to the list.") #prints output

    elif choice == '2':
        tasks = load_tasks()
        if not tasks: #checks if file is empty
            print("your to-do list is empty.")
        else:
            print("\nyour tasks")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == '3':
        tasks = load_tasks()
        if tasks:
            try:
                task_num = int(input("enter the number of the task to delete: "))
                removed_task = tasks.pop(task_num - 1) #since starts from index 0
                save_tasks(tasks) #pulls save_task function 
                print(f"task '{removed_task}' deleted.")
            except (ValueError, IndexError): #if system receives invalid input, loops
                print("invalid input. please enter a valid task number.")
        else:
            print("no tasks to delete.")

    elif choice == '4':
        print("thank you, come again")
        loop = False #ends the loop, ending the program

    else:
        print("invalid choice, select another option.") #if input is not 1-4. loops until correct input 
