
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql

# Initialize tasks list
tasks = []

# Function to add a task to the list and database
def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
        tasks.append(task_string)
        the_cursor.execute('insert into tasks values (?)', (task_string,))
        list_update()
        task_field.delete(0, 'end')

# Function to update the listbox with tasks
def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)

# Function to delete a task from the list and database
def delete_task():
    try:
        the_value = task_listbox.get(task_listbox.curselection())
        if the_value in tasks:
            tasks.remove(the_value)
            list_update()
            the_cursor.execute('delete from tasks where title = ?', (the_value,))
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

# Function to delete all tasks from the list and database
def delete_all_tasks():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')
    if message_box == True:
        while len(tasks) != 0:
            tasks.pop()
        the_cursor.execute('delete from tasks')
        list_update()

# Function to clear the listbox
def clear_list():
    task_listbox.delete(0, 'end')

# Function to close the application
def close():
    print(tasks)
    guiWindow.destroy()

# Function to retrieve tasks from the database
def retrieve_database():
    while len(tasks) != 0:
        tasks.pop()
    for row in the_cursor.execute('select title from tasks'):
        tasks.append(row[0])

if __name__ == "__main__":
    # Create the main window
    guiWindow = tk.Tk()
    guiWindow.title("To-Do List Manager")
    guiWindow.geometry("600x600")
    guiWindow.minsize(350, 250)
    guiWindow.maxsize(600, 600)
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg="bisque")

    # Connect to the database
    the_connection = sql.connect('listOfTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('create table if not exists tasks (title text)')

    # Create frames
    header_frame = tk.Frame(guiWindow, bg="bisque")
    functions_frame = tk.Frame(guiWindow, bg="bisque")
    listbox_frame = tk.Frame(guiWindow, bg="bisque")
    header_frame.pack(fill="both")
    functions_frame.pack(side="left", expand=True, fill="both")
    listbox_frame.pack(side="right", expand=True, fill="both")

    # Create labels and entry field
    header_label = ttk.Label(header_frame, text="The To-Do List", font=("Comic Sans MS Italic", "35", "bold", "underline"), background="bisque", foreground="black")
    header_label.pack(padx=20, pady=20)
    everyday_task_label = ttk.Label(header_frame, text="Everyday Task", font=("Vladimir Script", 30, "bold"), background="bisque", foreground="black")
    everyday_task_label.pack(padx=20, pady=20)
    task_label = ttk.Label(functions_frame, text="Enter the Task:", font=("Consolas", "11", "bold"), background="bisque", foreground="#000000")
    task_label.place(x=60, y=30)
    task_field = ttk.Entry(functions_frame, font=("Consolas", "12"), width=18, background="#FFF8DC", foreground="#A52A2A")
    task_field.place(x=70, y=80)

    # Create buttons
    add_button = ttk.Button(functions_frame, text="Add Task", width=24, command=add_task)
    del_button = ttk.Button(functions_frame, text="Delete Task", width=24, command=delete_task)
    del_all_button = ttk.Button(functions_frame, text="Delete All Tasks", width=24, command=delete_all_tasks)
    exit_button = ttk.Button(functions_frame, text="Exit", width=24, command=close)
    add_button.place(x=30, y=120)
    del_button.place(x=30, y=160)
    del_all_button.place(x=30, y=200)
    exit_button.place(x=30, y=240)

    # Create listbox
    task_listbox = tk.Listbox(listbox_frame, width=26, height=13, selectmode='SINGLE', background="#FFFFFF", foreground="#000000", selectbackground="#CD853F", selectforeground="#FFFFFF")
    task_listbox.place(x=10, y=80)

    # Retrieve tasks from the database and update listbox
    retrieve_database()
    list_update()

    # Run the main event loop
    guiWindow.mainloop()

    # Commit changes and close database connection
    the_connection.commit()
    the_cursor.close()

