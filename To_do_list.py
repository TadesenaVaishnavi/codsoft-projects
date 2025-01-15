import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

class To_do_list:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("500x500")

        # Load and set the background image from URL
        image_url = "https://www.creativefabrica.com/wp-content/uploads/2022/09/06/Student-Daily-Planner-Todo-List-Template-Graphics-37891046-2-580x387.jpg"
        response = requests.get(image_url)
        if response.status_code == 200:
            image_data = BytesIO(response.content)
            self.background_image = Image.open(image_data)
            self.background_image = self.background_image.resize((500, 500), Image.Resampling.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(self.background_image)
            self.bg_label = tk.Label(self.root, image=self.bg_photo)
            self.bg_label.place(relwidth=1, relheight=1)
        else:
            print("Failed to fetch the background image.")

        # Task list to store tasks
        self.tasks = []

        # Create UI elements
        self.create_widgets()

    # Rest of the code remains the same

    def create_widgets(self):
        # Frame to hold widgets, placed over the background
        frame = tk.Frame(self.root, bg="#ffffff", relief=tk.RAISED, bd=5)
        frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=600)

        # Title label
        self.label = tk.Label(frame, text="To-Do List", font=("Arial", 20, "bold"), bg="#ffffff", fg="#333333")
        self.label.pack(pady=10)

        # Task entry
        self.task_entry = tk.Entry(frame, width=35, font=("Arial", 14))
        self.task_entry.pack(pady=10)

        # Add button
        self.add_button = tk.Button(frame, text="Add Task", font=("Arial", 12), bg="#4caf50",
                                    command=self.add_task, width=15)
        self.add_button.pack(pady=5)

        # Task listbox
        self.listbox = tk.Listbox(frame, height=10, width=40, font=("Arial", 12), selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)

        # Remove button
        self.remove_button = tk.Button(frame, text="Remove Task", font=("Arial", 12), bg="#f44336", 
                                       command=self.remove_task, width=15)
        self.remove_button.pack(pady=5)

        # Mark as completed button
        self.mark_button = tk.Button(frame, text="Mark as Completed", font=("Arial", 12), bg="#2196f3", 
                                      command=self.mark_completed, width=15)
        self.mark_button.pack(pady=5)

        # Update button
        self.update_button = tk.Button(frame, text="Update Task", font=("Arial", 12), bg="#ffc107", fg="black",
                                       command=self.update_task, width=15)
        self.update_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def remove_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")

    def mark_completed(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            completed_task = self.tasks[selected_task_index] + " (Completed)"
            self.tasks[selected_task_index] = completed_task
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

    def update_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[selected_task_index] = new_task
                self.update_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Please enter a new task.")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to update.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = To_do_list(root)
    root.mainloop()
