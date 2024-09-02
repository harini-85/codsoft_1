import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image,ImageTk

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

root = tk.Tk()
root.title("To-Do List")

root.minsize(400,550)
root.maxsize(525,942)
bg = Image.open("bg3.jpeg") 
bgpic = ImageTk.PhotoImage(bg)

bg_label = tk.Label(root, image=bgpic)

bg_label.place(x=0, y=0, relwidth=1, relheight=1)



#GUI widgets
frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=40)

entry_task = tk.Entry(frame_tasks, width=40,font="Constantia 10",fg="#9194fb")
entry_task.pack(side=tk.LEFT, padx=10)
#"#9194fb"#
button_add_task = tk.Button(frame_tasks,text="Add Task",font="Constantia 10",bg="#9194fb",fg="white",activebackground="#7687f6", command=add_task)
button_add_task.pack(side=tk.LEFT, padx=10)

button_delete_task = tk.Button(frame_tasks, text="Delete Task",font="Constantia 10",bg="#9194fb",fg="white",activebackground="#7687f6", command=delete_task)
button_delete_task.pack(side=tk.LEFT, padx=10)

listbox_tasks = tk.Listbox(root, width=60, height=20,font="Constantia 10",fg="#7687f6",bg="white" )
listbox_tasks.pack(pady=10)


root.mainloop()

