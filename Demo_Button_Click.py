from tkinter import *
w=Tk()
import datetime
dt=datetime.datetime.now()

def call():
    btn=Button(w,text=dt,fg="Blue")
    btn.place(x=60,y=120)

w.title('My_GUI')
btn1=Button(w,text="Click ME",command=call,fg="Blue")
btn1.place(x=75,y=75)

w.mainloop()
