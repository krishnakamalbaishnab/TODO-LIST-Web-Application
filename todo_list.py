class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def mark_completed(self, index):
        self.tasks[index].completed = True

    def delete_task(self, index):
        del self.tasks[index]

    def display_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "X" if task.completed else " "
            print(f"{i + 1}. [{status}] {task.description}")


def main():
    todo_list = ToDoList()

    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. Mark Task Completed")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            index = int(input("Enter task number to mark as completed: ")) - 1
            todo_list.mark_completed(index)
        elif choice == "3":
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
