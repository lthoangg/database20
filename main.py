from tkinter import *
import mysql.connector as connector

class Window(Tk):
    def __init__(self, screenName=None, baseName=None, className= None, useTk=1, sync=0, use=None):
        super().__init__(screenName=screenName, baseName=baseName, className="Window", useTk=useTk, sync=sync, use=use)
        self.title("SQL GUI")
        self.minsize(300, 300)
        self.maxsize(600, 600)
        self.geometry('300x300')
        self.labels = []
        self.entries = []
        self.buttons = []
        self.home()
    
    def clear(self, typ = None):
        if typ is None:
            try:
                for label in self.labels:
                    label.destroy()
                for entry in self.entries:
                    entry.destroy()
                for button in self.buttons:
                    button.destroy()
            except:
                print('error 1')
        else:
            try:
                for thing in typ:
                    thing.destroy()
            except:
                print('error 2')

    def home(self):
        self.buttons.append(Button(self,text="Let's go", command = self.signin))
        for button in self.buttons:
            button.pack()

    def signin(self):
        self.clear(self.buttons)
        host = Label(self,text='host:')
        user = Label(self, text='user:')
        password = Label(self, text='password:')
        self.labels = [host, user, password]

        self.host_pholder = Entry(self, fg='black', bg='white', width=25)
        self.user_pholder = Entry(self, fg='black', bg='white', width=25)
        self.pass_pholder = Entry(self, fg='black', bg='white', width=25, show="*")

        self.entries = [self.host_pholder, self.user_pholder, self.pass_pholder]
        for i in range(3):
            self.labels[i].grid(row=i, column=0, sticky=W, pady=3)
            self.entries[i].grid(row=i, column=1, pady=3)

        self.buttons = [Button(self, text="Connect to server", command=self.check_server)]
        self.buttons[0].grid(row=3, column=1, pady=3)

    def check_server(self):
        try:
            self.mydb = connector.connect(
                # host = self.host_pholder.get(),
                # user = self.user.get(),
                # password = self.pass_pholder.get()
                host = "localhost",
                user = "root",
                password = "123456",
                database= "project2020"
            )
            print("Server connected")
            self.Exec = self.mydb.cursor()
            print("Server worked")
        except:
            print("No server! Try again")
            self.signin()
        else:
            self.set_role()

    def set_role(self):
        self.clear()
        ask = Label(self, text="What is your name:")
        who = Label(self, text='Which role are you?')

        name = Entry(self)

        roles = ("Operator", "Teacher")
        var = StringVar(self)
        var.set(roles[0])
        role = OptionMenu(self, var, roles[0], roles[1])

        if var.get() == roles[0]:
            submit = Button(self, text="submit", command=self.operator)
        elif role.get() == roles[1]:
            submit = Button(self, text="submit", command=self.teacher)
        else:
            submit = Button(self, text="submit", command=None)
            
        self.labels = [ask, who]
        self.entries = [name]
        self.buttons = [role, submit]
        for i in range(2):
            self.labels[i].grid(row=i, column=0, sticky=W)
            if i == 0:
                self.entries[0].grid(row=i, column=1, sticky=W)
        for i in range(1, 3):
            self.buttons[i-1].grid(row=i, column = 1, sticky=W)

    def operator(self):
        name = self.entries[0].get()
        self.clear()
        hello = Label(self, text= f"Hello operator {name}")
        
        classes = Button(self, text="Show classes", command= self.show_class)
        teachers = Button(self, text="Show teachers", command = self.show_teacher)
        students = Button(self, text="Show students", command= self.show_student)
        self.labels = [hello]
        self.buttons = [classes, teachers, students]
        for i in range(3):
            self.buttons[i].grid(row=0, column=i, sticky=W)

    def show_class(self):
        try:
            self.Exec.execute("select * from classes;")
            for data in self.Exec:
                print(data)
        except:
            label = Label(self, text="No data")
            label.grid(row=2, column=0, sticky = W)
            print('none')

    def show_teacher(self):
        try:
            data = self.Exec.execute("select * from teachers;")
        except:
            print('none')

    def show_student(self):
        pass




    def teacher(self):
        name = self.entries[0].get()
        self.clear()
        hello = Label(self, text = f"Hello teacher {name}")
        

def main():
    window = Window()
    window.mainloop()

if __name__ == "__main__":
    main()