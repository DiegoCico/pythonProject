import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from typing import List

from GroupPlanner.Processor import Processor


class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Group Planner")

        self.setup_ui()

    def setup_ui(self):
        # Create and place labels and entry widgets
        self.create_label_entry("Total Periods:", 0)
        self.create_label_entry("Lunch Period:", 1)
        self.create_label_entry("Duration of Day:", 2)
        self.create_label_entry("Activities (comma-separated):", 3)
        self.create_label_entry("Number of Groups:", 4)

        # Create and place the submit button
        self.submit_button = tk.Button(self.root, text="Generate Planner", command=self.generate_planner)
        self.submit_button.grid(row=5, column=1, pady=10)

    def create_label_entry(self, label_text, row):
        label = tk.Label(self.root, text=label_text)
        label.grid(row=row, column=0, padx=10, pady=5, sticky="e")

        entry = tk.Entry(self.root)
        entry.grid(row=row, column=1, padx=10, pady=5, sticky="w")

        setattr(self, f"entry_{row}", entry)

    def generate_planner(self):
        try:
            total_periods = int(self.entry_0.get())
            lunch_period = int(self.entry_1.get())
            duration_of_day = float(self.entry_2.get())
            activities = self.entry_3.get().split(',')
            group = int(self.entry_4.get())

            processor = Processor(total_periods, lunch_period, duration_of_day, activities, group)
            processor.create_table()

            messagebox.showinfo("Success", "The planner has been generated successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()

