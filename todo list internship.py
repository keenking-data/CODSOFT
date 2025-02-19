#A To-Do List application is a useful project that helps users manage and organize their tasks efficiently. 
#This project aims to create a command-line or GUI-based application using Python, 
# allowing users to create, update, and track their to-do lists ###

def todo ():
    todo_list = []
    while true: # type: ignore
        print("YOUR TO DO LIST APLICATION")
        print("\n-------------------------")
        print("1 View tasks: ")
        print("2 Add task: ")
        print("3 Remove task: ")
        print("4 close :")

        value = int(input("Enter your choice:"))

        if value == '1' :
            if not todo_list:  
                print("\nNo tasks in the to-do list.")  
            else: 
                print("\nTo-Do List:")  
                for idx, item in enumerate(todo_list, start=1):  
                    status = "Completed" if item["completed"] else "Not Completed"  
                    print(f"{idx}. {item['task']} - {status}")
        elif value == '2':
            task = input("Enter the task: ") 
            todo_list.append({"task": task, "completed": False})  
            print("Task added.") 
        elif value == '4':  
            print("Exiting To-Do List Application.")  
            break  
todo() 
        

