import csv
import os
from tkinter import *
from tkinter import messagebox


def new_entry():
    my_entry = entry.get()
    # writing entry in a file
    if my_entry != "":
        task_list.append(my_entry)
        with open(todo_list, "w", encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            for tsk in task_list:
                writer.writerow([tsk])
        lst.insert(END, my_entry)
        # delete entry from the entry field
        entry.delete(0, "end")

    else:
        # error if entry empty
        messagebox.showwarning("error", "Please enter some task.")


def delete_entry():
    # deleting task from a list and a file
    selection = lst.curselection()
    lst.delete(selection)
    task_list.remove(task_list[selection[0]])
    # updating the file
    with open(todo_list, "w", encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        for tsk in task_list:
            writer.writerow([tsk])


if __name__ == "__main__":

    # checking if todo_list exists, if not creating it
    todo_list = "todo_list.csv"
    if not os.path.exists(todo_list):
        f = open(todo_list, "w")
        f.close()
    else:
        pass

    # temporary var for todo_list
    task_list = []

    # saving contents of todo_list.csv to a list
    with open(todo_list, "r", encoding='UTF8', newline='') as r:
        reader = csv.reader(r)

        for row in reader:
            task_list.append(row[0])

    # creating app
    app = Tk()
    app.geometry('500x450+500+200')
    app.title('To Do List')
    app.config(bg='#645CBB')
    app.resizable(width=False, height=False)

    # creating frame for a listbox
    frame = Frame(app)
    frame.pack(pady=10)

    # creating listbox to show the contents of a file
    lst = Listbox(
        frame,
        width=25,
        height=8,
        font=('Times', 18),
        bd=0,
        fg='#464646',
        highlightthickness=0,
        selectbackground='#a6a6a6',

    )
    lst.pack(side=LEFT, fill=BOTH)

    # displaying tasks
    for item in task_list:
        lst.insert(END, item)

    # creating scrollbar
    sb = Scrollbar(frame)
    sb.pack(side=RIGHT, fill=BOTH)

    # setting scrollbar to scroll vertically
    lst.config(yscrollcommand=sb.set)
    sb.config(command=lst.yview)

    # getting input
    entry = Entry(app, font=('times', 24))
    entry.pack(pady=20)

    # creating button frame
    button_frame = Frame(app)
    button_frame.pack(pady=20)

    # creating entry button
    add_entry_button = Button(
        button_frame,
        text='Add Task',
        font='times 14',
        bg='#c5f776',
        padx=20,
        pady=10,
        command=new_entry
    )
    add_entry_button.pack(fill=BOTH, expand=True, side=LEFT)

    # creating delete button
    del_entry_button = Button(
        button_frame,
        text='Delete Task',
        font='times 14',
        bg='#ff8b61',
        padx=20,
        pady=10,
        command=delete_entry
    )
    del_entry_button.pack(fill=BOTH, expand=True, side=LEFT)

    # main loop
    app.mainloop()
