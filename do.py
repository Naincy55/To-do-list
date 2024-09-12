def task():
    tasks=[];   #Empty List
    print("TO DO LIST")
    
    total_task= int(input("Enter the task how many task do you want to add: "))
    for i in range(1, total_task+1):
        task_name= input(f'Enter the task {i}: ')   #Enter the task 1
        tasks.append(task_name)
    print(f"Today's tasks are \n {tasks}")
    
    while True:
        print("Enter the opeartions:")
        operations = int(input("Enter 1-Add\n 2-Delete\n 3-Update\n 4-View\n 5-Exit/Stop\n"))
        if operations == 1:
            add = input("Enter the task you want to add:")
            tasks.append(add)
            print(f"Tasks {add} has been succesfully added....")
            
        elif operations ==2:
            delete_val= input("Enter the task you want to delete...")
            if delete_val in tasks:
                ind = tasks.index(delete_val)
                del tasks[ind]
                print(f"Task {delete_val} has been deleted")
            
        elif operations ==3:
             updated_val= input("Enter the task you want to update:..")
             if updated_val in tasks:
                up = input("Enter the new task: ")
                ind = tasks.index(updated_val)
                tasks[ind]= up
                print(f"Updates task is {up}")
                
        elif operations ==4:
            print(f'The total Tasks is{tasks}')
            
        elif operations ==5:
            print(f"Closing the program....")
            break
        else:
            print(f"Invalid input")

             
task()