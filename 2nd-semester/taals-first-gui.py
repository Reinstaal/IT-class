from tkinter import *
from tkinter import ttk


root = Tk()
frm = ttk.Frame(root, padding=10)

def checkLogin():
    if usernameEntry.get() == "Taal":
        if passwordEntry.get() == "admin":
            root.destroy()


frm.grid()
title = ttk.Label(frm, font=22, text="Kebab boi Taal").grid(column=25, row=0)
textUsername = ttk.Label(frm, text="Username").grid(column=25, row=2)
usernameEntry = ttk.Entry(frm)
usernameEntry.grid(column=25, row=3)
testPassword = ttk.Label(frm, text="Password").grid(column=25, row=4)
passwordEntry = ttk.Entry(frm)
passwordEntry.grid(column=25, row=5)
emptyLabel = ttk.Label(frm, text="").grid(column=25, row=6)
loginButton = ttk.Button(frm, text="Login",  command=checkLogin).grid(column=1, row=50)
cancelLoginButton = ttk.Button(frm, text="Cancel", command=root.destroy).grid(column=50, row=50)
root.mainloop()