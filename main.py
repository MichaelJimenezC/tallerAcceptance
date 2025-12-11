class Task:
    def __init__(self, title, description="", priority="Medium", status="Pending"):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

    def mark_completed(self):
        self.status = "Completed"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description="", priority="Medium"):
        task = Task(title, description, priority)
        self.tasks.append(task)

    def list_tasks(self):
        return self.tasks

    def clear_tasks(self):
        self.tasks = []

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                return True
        return False

    def delete_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]


def show_menu():
    print("\n==== TO-DO LIST MANAGER ====")
    print("1. Add task")
    print("2. List tasks")
    print("3. Mark task completed")
    print("4. Clear all tasks")
    print("5. Delete a task")
    print("6. Exit")
    print("============================")


def main():
    todo = ToDoList()

    while True:
        show_menu()
        option = input("Choose an option: ")

        if option == "1":
            title = input("Task title: ")
            todo.add_task(title)
            print("Task added!")

        elif option == "2":
            print("\nTasks:")
            if not todo.list_tasks():
                print("No tasks yet.")
            for task in todo.list_tasks():
                print(f"- {task.title} ({task.status})")

        elif option == "3":
            title = input("Task to complete: ")
            print("Done!" if todo.mark_task_completed(title) else "Task not found.")

        elif option == "4":
            todo.clear_tasks()
            print("All tasks cleared!")

        elif option == "5":
            title = input("Task to delete: ")
            todo.delete_task(title)
            print("Task deleted.")

        elif option == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
