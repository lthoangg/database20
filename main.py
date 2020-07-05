from tkinter import *

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
                pass
        else:
            try:
                for thing in typ:
                    thing.destroy()
            except:
                print('error')

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

        host_pholder = Entry(self, fg='black', bg='white', width=25)
        user_pholder = Entry(self, fg='black', bg='white', width=25)
        pass_pholder = Entry(self, fg='black', bg='white', width=25, show="*")
        self.entries = [host_pholder, user_pholder, pass_pholder]

        for i in range(3):
            self.labels[i].grid(row=i, column=0, sticky=W, pady=3)
            self.entries[i].grid(row=i, column=1, pady=3)

        

        self.buttons = [Button(self, text="Connect to server", command=self.set_role)]
        self.buttons[0].grid(row=3, column=1, pady=3)


    def set_role(self):
        self.clear()
        ask = Label(self, text="What is your name:")
        who = Label(self, text='Which role are you?')

        name = Entry(self)

        roles = ("Operator", "Teacher")
        var = StringVar(self)
        var.set(roles[0])
        role = OptionMenu(self, var, roles[0], roles[1])
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
def main():
    window = Window()
    window.mainloop()

if __name__ == "__main__":
    main()