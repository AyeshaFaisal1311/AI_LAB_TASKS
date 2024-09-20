class to_do_list:
    def __init__(self):
        self.tasks = []

    def add(self,task_name):
        self.tasks.append(task_name)
        print(f"Task '{task_name}' added in list.")

    def view(self):
        if not self.tasks:
            print("No tasks in list")
        else:
            print("Your tasks:",self.tasks)

    def update(self,previous_task,updated_task):
        if previous_task in self.tasks:
            self.tasks.remove(previous_task)
            self.tasks.append(updated_task)
            print(f"Task '{updated_task}' in list.")
        else:
                print(f"Task not found")
            
    def remove(self,task_name):
        if task_name in self.tasks:
           self.tasks.remove(task_name)
           print(f"Task '{task_name}' removed from list.") 
        else:
            print("Task not Found")  

def main():
    list = to_do_list()
    while True:
        print("\n1. Add task")
        print("2. View tasks")
        print("3. Update task")
        print("4. Remove task")
        print("5. Exit")

        choice=int(input("Enter your choice."))

        if choice==1:
            task_name = input("Enter task name: ")
            list.add(task_name)

        elif choice==2:
            list.view()

        elif choice==3:
            previous_task = input("Enter task name to update: ")
            updated_task = input("Enter new task name:") 
            list.update(previous_task,updated_task)

        elif choice==4:
            task_name = input("Enter task name to remove: ")
            list.remove(task_name)

        elif choice==5:
            print("Existing todo_list")
            break
        
if __name__=='__main__':
    main()
        
