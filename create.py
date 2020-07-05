import sqlite3 as sql
from tkinter import *

conn = sql.connect('')

#initiate tkinter window
window = Tk()
window.title("SQL User Interface")
window.geometry("400x400")

label_welcome = Label(window, bg = "black", fg= "white", text = "Welcome to User Interface", width= 400)
label_welcome.pack()
#creating left and right frames to work
#left = Frame(window, borderwidth=2, relief="solid")
#right = Frame(window, borderwidth=2, relief="solid")

def getRole():
    name = entry_role.get()
    if name == "Teacher" or "teacher":
        label= Label(window, text="Hi, " + name + ". We are processing your GUI")
        label.pack()
        #teacher_window = Tk()
        #teacher_window.title("Teacher GUI")
        #teacher_window.geometry("800x800")

        #teacher_window.mainloop()
    elif name == "Operator":
        label= Label(window, text="Hi, " + name + ". We are processing your GUI")
        label.pack()
        #operator_window = Tk()
        #operator_window.title("Operator GUI")
        #operator_window.geometry("800x800")

        #operator_window.mainloop()
    else:
        label= Label(window, text="Wrong role received, Try again")
        label.pack()

def signOut():
    label_succ.destroy()   
    entry_role.destroy()
    label_role.destroy()
    button_role.destroy()

    label_host.pack()
    entry_host.pack()

    label_username.pack()
    entry_username.pack()

    label_psswd.pack()
    entry_psswd.pack()
    button.pack()

#enter role
label_role = Label(window, text="Enter your role")
entry_role = Entry(window, fg="black", bg= "white", width = 25)
button_role = Button(window, text="Confirm your role!", command = getRole)
button_back = Button(window, text="Sign out", command = signOut)

#defintion of getting username and password
def signIn():
    host = entry_host.get()
    username = entry_username.get()
    password = entry_psswd.get()
    if host == "host" and username == "username" and password == "password":
        label_succ.pack()
        #destroy signin widgets
        label_host.destroy()
        entry_host.destroy()

        label_username.destroy()
        entry_username.destroy()

        label_psswd.destroy()  
        entry_psswd.destroy()
        button.destroy()
        
        
        label_succ.pack()   
        entry_role.pack()
        label_role.pack()
        button_role.pack()
        button_back.pack()
    else:
        label_fail.pack()


#enter host, username, etc
label_host = Label(window, text = "Enter host")
entry_host = Entry(window, fg="black", bg= "white", width = 25)

label_username = Label(window, text = "Enter username")
entry_username = Entry(window, fg="black", bg= "white", width = 25)

label_psswd = Label(window, text = "Enter password")
entry_psswd = Entry(window, show= "*", fg="black", bg= "white", width = 25)
button = Button(window,text = "Sign in", command = signIn)

#other labels
label_succ = Label(window, text = "Successfully signed in")
label_fail = Label(window, text = "Failed")

#print elements on the screen
#left.pack(side="left", expand = True, fill = "both")
#right.pack(side="right", expand = True, fill = "both")
label_host.pack()
entry_host.pack()

label_username.pack()
entry_username.pack()

label_psswd.pack()
entry_psswd.pack()
button.pack()

#allow the window to run
window.mainloop() 