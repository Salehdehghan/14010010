from googletrans import Translator, LANGUAGES
from tkinter import ttk, messagebox
from tkinter import *
from tkinter import messagebox

# Create the main application window
root = Tk()
root.title("Login Application")
root.geometry("400x300")
root.resizable(False, False)

# Function to check login credentials


def login():
    username = entry_username.get()
    password = entry_password.get()

    # Dummy credentials for example
    if username == "admin" and password == "123":
        messagebox.showinfo(
            "لاگین موفق", "به برنامه مترجم خوش امدید")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


# Create a frame for the login form
frame = Frame(root, padx=20, pady=20)
frame.pack(expand=True)

# Username label and entry
label_username = Label(frame, text="Username", font=("Arial", 14))
label_username.grid(row=0, column=0, pady=10)
entry_username = Entry(frame, font=("Arial", 14))
entry_username.grid(row=0, column=1, pady=10)

# Password label and entry
label_password = Label(frame, text="Password", font=("Arial", 14))
label_password.grid(row=1, column=0, pady=10)
entry_password = Entry(frame, font=("Arial", 14), show="*")
entry_password.grid(row=1, column=1, pady=10)

# Login button
btn_login = Button(frame, text="Login", font=("Arial", 14), command=login)
btn_login.grid(row=2, columnspan=2, pady=20)

# Run the main application loop
root.mainloop()
# پایان لاگین

# Initialize the main window
root = Tk()
root.title("Text Translator")
root.geometry("1080x400")
root.resizable(False, False)
root.configure(background="white")

# Function to update labels based on combobox selections


def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label.configure(text=LANGUAGES[c].capitalize())
    label2.configure(text=LANGUAGES[c1].capitalize())
    root.after(1000, label_change)

# Function to perform the translation


def translate_now():
    text_ = Text1.get(1.0, END).strip()
    if text_:
        try:
            T1 = Translator()
            trans_text = T1.translate(
                text_, src=combo1.get(), dest=combo2.get())
            trans_text = trans_text.text
            Text2.delete(1.0, END)
            Text2.insert(END, trans_text)
        except Exception as e:
            messagebox.showerror("Translation Error", str(e))
    else:
        messagebox.showwarning("Input Error", "Please enter text to translate")


# Icon
# Ensure 'images.png' exists in your directory
Image_icon = PhotoImage(file="images.png")
root.iconphoto(False, Image_icon)

# Arrow image
# Ensure 'img.png' exists in your directory
arrow_image = PhotoImage(file="img.png")
Image_label = Label(root, image=arrow_image, width=150)
Image_label.place(x=460, y=50)

# Language lists
languages = list(LANGUAGES.values())
lang_codes = list(LANGUAGES.keys())

# First combobox
combo1 = ttk.Combobox(root, values=lang_codes,
                      font="Roboto 14", state="readonly")
combo1.place(x=110, y=20)
combo1.set("en")

label = Label(root, text="English", font="segoe 30 bold",
              bg="white", width=18, bd=5, relief=GROOVE)
label.place(x=10, y=50)

# Second combobox
combo2 = ttk.Combobox(root, values=lang_codes,
                      font="Roboto 14", state="readonly")
combo2.place(x=730, y=20)
combo2.set("fa")

label2 = Label(root, text="Persian", font="segoe 30 bold",
               bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

# First frame for input text
f = Frame(root, bg="Black", bd=5)
f.place(x=10, y=118, width=440, height=210)

Text1 = Text(f, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
Text1.place(x=0, y=0, width=430, height=200)

Scrollbar1 = Scrollbar(f)
Scrollbar1.pack(side="right", fill='y')

Scrollbar1.configure(command=Text1.yview)
Text1.configure(yscrollcommand=Scrollbar1.set)

# Second frame for translated text
f1 = Frame(root, bg="Black", bd=5)
f1.place(x=620, y=118, width=440, height=210)

Text2 = Text(f1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
Text2.place(x=0, y=0, width=430, height=200)

Scrollbar2 = Scrollbar(f1)
Scrollbar2.pack(side="right", fill='y')

Scrollbar2.configure(command=Text2.yview)
Text2.configure(yscrollcommand=Scrollbar2.set)

# Translate button
Translate = Button(root, text="Translate", font=("Roboto", 15), activebackground="white",
                   cursor="hand2", bd=1, width=10, height=2, bg="black", fg="white", command=translate_now)
Translate.place(x=476, y=250)

label_change()

root.mainloop()
