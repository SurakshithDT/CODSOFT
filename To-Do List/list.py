#To-Do List


from tkinter import *
from tkinter import messagebox
import sqlite3 as db

def add_task():
    task_input = task_entry.get()
    if len(task_input) == 0:
        messagebox.showinfo('Error', 'Task field cannot be empty.')
    else:
        tasks.append(task_input)
        db_cursor.execute('INSERT INTO tasks_table VALUES (?)', (task_input,))
        update_task_display()
        task_entry.delete(0, 'end')

def update_task_display():
    clear_task_display()
    for task in tasks:
        task_listbox.insert('end', task)

def remove_task():
    try:
        selected_task = task_listbox.get(task_listbox.curselection())
        if selected_task in tasks:
            tasks.remove(selected_task)
            update_task_display()
            db_cursor.execute('DELETE FROM tasks_table WHERE task_name = ?', (selected_task,))
    except:
        messagebox.showinfo('Error', 'No task is selected to delete from the list.')

def remove_all_tasks():
    confirm = messagebox.askyesno('Delete All', 'Are you sure you want to delete all tasks in the list?')
    if confirm:
        tasks.clear()
        db_cursor.execute('DELETE FROM tasks_table')
        update_task_display()

def clear_task_display():
    task_listbox.delete(0, 'end')

def close_application():
    print(tasks)
    main_window.destroy()

def load_tasks_from_db():
    tasks.clear()
    for row in db_cursor.execute('SELECT task_name FROM tasks_table'):
        tasks.append(row[0])

if __name__ == "__main__":
    main_window = Tk()
    main_window.title("Task Manager")
    main_window.geometry("700x450+500+200")
    main_window.resizable(True, True)
    main_window.configure(bg="#D3CCE3")

    db_connection = db.connect('tasks_database.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute('CREATE TABLE IF NOT EXISTS tasks_table (task_name TEXT)')

    tasks = []

    frame = Frame(main_window, bg="white")
    frame.pack(side="top", expand=True, fill="both")

    title = Label(frame, text="TASK MANAGER\nEnter Task Below:", font=("arial", "16", "bold"), bg="black", fg="#F76C6C")
    title.place(x=20, y=30)

    task_entry = Entry(frame, font=("arial", "14"), width=42, fg="black", bg="white")
    task_entry.place(x=220, y=30)

    add_button = Button(frame, text="Add Task", width=15, bg='#FFB6C1', font=("arial", "14", "bold"), command=add_task)
    remove_button = Button(frame, text="Remove Task", width=15, bg='#FFB6C1', font=("arial", "14", "bold"), command=remove_task)
    remove_all_button = Button(frame, text="Remove All", width=15, font=("arial", "14", "bold"), bg='#FFB6C1', command=remove_all_tasks)
    exit_button = Button(frame, text="Exit", width=52, bg='#FFB6C1', font=("arial", "14", "bold"), command=close_application)

    add_button.place(x=18, y=80)
    remove_button.place(x=240, y=80)
    remove_all_button.place(x=460, y=80)
    exit_button.place(x=17, y=400)  # Adjusted y-coordinate to ensure it's below the list

    task_listbox = Listbox(frame, width=70, height=10, font="bold", selectmode='SINGLE', bg="white", fg="black", selectbackground="#C0D6DF", selectforeground="black")
    task_listbox.place(x=17, y=140)

    load_tasks_from_db()
    update_task_display()

    main_window.mainloop()

    db_connection.commit()
    db_cursor.close()
