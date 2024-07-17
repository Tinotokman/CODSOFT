import tkinter as tk

def add_task():
    task = entry_tasks.get()
    if task:
        list_task.insert(tk.END, task)
        entry_tasks.delete(0, tk.END)

def del_task():
    select = list_task.curselection()
    if select:
        list_task.delete(select)

def modify_task():
    select = list_task.curselection()
    if select:
        new_task = entry_tasks.get()
        if new_task:
            list_task.delete(select)
            list_task.insert(select, new_task)
            entry_tasks.delete(0, tk.END)

def mark_task():
    select = list_task.curselection()
    for index in select:
        list_task.itemconfig(index, {'bg':'light green'})

def unmark_task():
    select = list_task.curselection()
    for index in select:
        list_task.itemconfig(index, {'bg':'white'})

# Create the principal window of the program
window = tk.Tk()
window.title("List of tasks")

entry_tasks = tk.Entry(window)
entry_tasks.pack()

add_button = tk.Button(window, text="Add task", command=add_task)
add_button.pack()

button_del = tk.Button(window, text="Delete task", command=del_task)
button_del.pack()

button_modify = tk.Button(window, 
                          text= "Modify task",
                          command= modify_task)
button_modify.pack()

mark_button = tk.Button(window, text="Mark task", command=mark_task)
mark_button.pack()

unmark_button = tk.Button(window, text="Unmark task", command=unmark_task)
unmark_button.pack()

list_task = tk.Listbox(window, selectmode=tk.MULTIPLE)
list_task.pack()

window.mainloop()

list_task = tk.Listbox(window)
list_task.pack()



window.mainloop()