from tkinter import *
import time

window = Tk()
window.title('digital clock')
window.geometry('600x400')


def myTime():
    # hour = time.strftime("%H") به صور ت ساع ت 21
    hour = time.strftime("%I")  # به صوت عدد 5
    minute = time.strftime("%M")
    second = time.strftime("%S")
    am_pm = time.strftime("%p")
    day = time.strftime("%A")
    zone = time.strftime("%z")

    myText = hour + ":" + minute + ":" + second + " " + am_pm
    myText2 = day + ", " + zone
    myLabel.config(text=myText)
    myLabel12.config(text=myText2)
    myLabel.after(1000, myTime)


myLabel = Label(window, text="HELO  WORLD!", font=(
    'Arial', 72), fg="white", bg='green')
myLabel.pack()
myLabel12 = Label(window, text="H", font=("Arial", 24))
myLabel12.pack()

myTime()
window.mainloop()
