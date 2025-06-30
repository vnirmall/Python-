import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get().strip()
    if task:
        if task not in tasks_list.get(0, tk.END):
            tasks_list.insert(tk.END, task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Oops!", "You already added this task!")
    else:
        messagebox.showwarning("Wait a second!", "You can't add an empty task.")

def remove_task():
    try:
        selected_task = tasks_list.curselection()[0]
        tasks_list.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Hey!", "You need to select a task first.")

def mark_done():
    try:
        selected_task = tasks_list.curselection()[0]
        task_text = tasks_list.get(selected_task)
        tasks_list.delete(selected_task)
        tasks_list.insert(tk.END, f"✔ {task_text} (Done!)")
    except IndexError:
        messagebox.showwarning("Oops!", "Select a task to mark as done.")

# GUI Setup
root = tk.Tk()
root.title("Your To-Do List")
root.geometry("400x400")
root.configure(bg="#f7f5f2")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

tasks_list = tk.Listbox(root, width=50, height=15)
tasks_list.pack(pady=10)

add_button = tk.Button(root, text="➕ Add Task", command=add_task)
add_button.pack()

remove_button = tk.Button(root, text="❌ Remove Task", command=remove_task)
remove_button.pack()

mark_done_button = tk.Button(root, text="✅ Mark Done", command=mark_done)
mark_done_button.pack()

root.mainloop()