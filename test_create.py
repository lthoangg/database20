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
        self.mainloop()

    def home(self):
        self.buttons.append(Button(self,text="Let's go", command = self.signin))
        for button in self.buttons:
            button.pack()

    def signin(self):
        for button in self.buttons:
            button.destroy()
        host = Label(self,text='host:')
        user = Label(self, text='user:')
        password = Label(self, text='password:')
        self.labels = [host, user, password]

        host_pholder = Entry(self, fg='black', bg='white', width=25)
        user_pholder = Entry(self, fg='black', bg='white', width=25)
        pass_pholder = Entry(self, fg='black', bg='white', width=25)
        self.entries = [host_pholder, user_pholder, pass_pholder]

        for i in range(3):
            self.labels[i].grid(row=i, column=0, sticky=W, pady=3)
            self.entries[i].grid(row=i, column=1, pady=3)
        

        Connect_to_server = Button(self, text="Connect to server")
        Connect_to_server.grid(row=3, column=1, pady=3)

    def set_role(self):
        pass


def main():
    window = Window()

if __name__ == "__main__":
    main()