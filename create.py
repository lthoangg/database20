import sqlite3 as sql
import tkinter as tk

conn = sql.connect('')

#initiate tkinter window
window = tk.Tk()
window.title("SQL User Interface")
window.geometry("200x200")

def getRole():
    name = entry.get()
    if name == "Teacher":
        label= tk.Label(window, text="Hi, " + name + ". We are processing your GUI")
        label.pack()
        teacher_window = tk.Tk()
        teacher_window.title("Teacher GUI")
        teacher_window.geometry("800x800")



        teacher_window.mainloop()
    elif name == "Operator":
        label= tk.Label(window, text="Hi, " + name + ". We are processing your GUI")
        label.pack()
        operator_window = tk.Tk()
        operator_window.title("Operator GUI")
        operator_window.geometry("800x800")

        operator_window.mainloop()
    else:
        label= tk.Label(window, text="Wrong role received, Try again")
        label.pack()



#enter role
label = tk.Label(text="Enter your role")
entry = tk.Entry(fg="black", bg= "white", width = 25)
button = tk.Button(window, text="Confirm", command = getRole)


entry.pack()
label.pack()
button.pack()



window.mainloop() #allow the window to run