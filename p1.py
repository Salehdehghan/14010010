from tkinter import Entry, Label, Tk, Button, messagebox
window = Tk()
window.geometry("410x100")
window.title("my app Ssleh")
window.resizable(False, False)
x = int((window.winfo_screenwidth()-410)/2)
y = int((window.winfo_screenheight()-100)/2)
window.geometry(f'+{x}+{y}')


def CheckPassword():
    usr = e1.get()
    password = e2.get()
    if usr == "ali" and password == "123":
        lblResult.config(fg='white', bg='blue', Text='OK')
        messagebox.showinfo('ok', 'user and password is ok')
    else:
        lblResult.config(fg='white', bg='red', Text='NO')
        messagebox.showerror('ok', 'user and password is NOT OK!')


lbl1 = Label(window, text='enter username:')
lbl1.grid(row=0, column=0)

e1 = Entry(window)
e1.grid(row=0, column=1)

lbl2 = Label(window, text='enter password')
lbl2.grid(row=1, column=0)

e2 = Entry(window, show='*')
e2.grid(row=1, column=1)

btnOK = Button(window, text='OK', command=CheckPassword, padx=10,
               activebackground='pink', activeforeground='green')
btnOK.grid(row=2, column=0)

lblResult = Label(window)
lblResult.grid(row=2, column=1)

window.mainloop()
