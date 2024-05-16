
import tkinter as tk
from tkinter import simpledialog, messagebox


class ToDo:
    def __init__(self):
        self.todos = []
        self.completed = []

    def add_todo(self):
        todo = input("Enter a todo: ")
        self.todos.append(todo)
        print("Todo added!")

    def complete(self):
        if not self.todos:
            print("No todos to complete.")
            return
        self.display_todos()
        userInput = int(input("Enter the number of the completed todo: "))
        if 1 <= userInput <= len(self.todos):
            self.completed.append(self.todos[userInput - 1])
            self.todos.pop(userInput - 1)
            print("Todo marked as completed!")
        else:
            print("Enter a valid todo number")

    def display_todos(self):
        print("Todos:")
        for index, todo in enumerate(self.todos, start=1):
            print(f"{index}. {todo}")

    def display_completed(self):
        print("Completed:")
        for index, todo in enumerate(self.completed, start=1):
            print(f"{index}. {todo}")

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Add Todo")
            print("2. Complete Todo")
            print("3. Show Todos")
            print("4. Show Completed Todos")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.add_todo()
            elif choice == "2":
                self.complete()
            elif choice == "3":
                self.display_todos()
            elif choice == "4":
                self.display_completed()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ToDo App")

        self.todos = []
        self.completed = []

        self.create_widgets()

    def create_widgets(self):
        self.todo_label = tk.Label(self.root, text="Todos:")
        self.todo_label.pack()

        self.todo_listbox = tk.Listbox(self.root)
        self.todo_listbox.pack()

        self.add_button = tk.Button(self.root, text="Add Todo", command=self.add_todo)
        self.add_button.pack()

        self.complete_button = tk.Button(self.root, text="Complete Todo", command=self.complete_todo)
        self.complete_button.pack()

        self.completed_label = tk.Label(self.root, text="Completed:")
        self.completed_label.pack()

        self.completed_listbox = tk.Listbox(self.root)
        self.completed_listbox.pack()

    def add_todo(self):
        todo = simpledialog.askstring("Add Todo", "Enter a todo:")
        if todo:
            self.todos.append(todo)
            self.update_todo_listbox()

    def complete_todo(self):
        selected_indices = self.todo_listbox.curselection()
        if not selected_indices:
            messagebox.showwarning("Complete Todo", "Please select a todo to complete.")
            return

        for index in selected_indices[::-1]:  # reverse to avoid index shifting issues
            completed_todo = self.todos.pop(index)
            self.completed.append(completed_todo)

        self.update_todo_listbox()
        self.update_completed_listbox()

    def update_todo_listbox(self):
        self.todo_listbox.delete(0, tk.END)
        for todo in self.todos:
            self.todo_listbox.insert(tk.END, todo)

    def update_completed_listbox(self):
        self.completed_listbox.delete(0, tk.END)
        for todo in self.completed:
            self.completed_listbox.insert(tk.END, todo)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

# if __name__ == "__main__":
#     todo_app = ToDo()
#     todo_app.menu()