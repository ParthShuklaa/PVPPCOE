from tkinter import *
root=Tk()

expression = ""

equ = StringVar()

def press(num):
    global expression

    expression += num

    equ.set(expression)

def equate():
    global expression

    expression  = str(eval((equ.get())))
    equ.set(expression)

def clear():
    global expression
    
    expression = ""
    equ.set("")

e1=Entry(root,textvariable=equ)
e1.grid(columnspan=6,ipadx=65,ipady=10)




Dot=Button(root,text=".",height=2, width=7).grid(row=5,column=1)
Mod=Button(root,text="Mod",height=2, width=7,bg="yellow",command = lambda:press('%')).grid(row=2,column=4)
Div=Button(root,text="Div",height=2, width=7,bg="yellow",command = lambda:press('/')).grid(row=1,column=3)
Mul=Button(root,text="Mul",height=2, width=7,bg="yellow",command = lambda:press('*')).grid(row=1,column=4)
Add=Button(root,text="Add",height=2, width=7,bg="yellow",command = lambda:press('+')).grid(row=1,column=1)
Subs=Button(root,text="Subs",height=2, width=7,bg="yellow",command = lambda:press('-')).grid(row=1,column=2,)

Zero=Button(root,text="0",height=2, width=16,command = lambda:press("0") )
One=Button(root,text="1",height=2, width=7,command = lambda:press("1"))
Two=Button(root,text="2",height=2, width=7,command = lambda:press("2"))
Three=Button(root,text="3",height=2, width=7,command = lambda:press('3'))
Four=Button(root,text="4",height=2, width=7,command = lambda:press('4'))
Five=Button(root,text="5",height=2, width=7,command = lambda:press('5'))
Six=Button(root,text="6",height=2, width=7,command = lambda:press('6'))
Seven=Button(root,text="7",height=2, width=7,command = lambda:press('7'))
Eight=Button(root,text="8",height=2, width=7,command = lambda:press('8'))
Nine=Button(root,text="9",height=2, width=7,command = lambda:press('9'))

Seven.grid(row=2,column=1)
Eight.grid(row=2,column=2)
Nine.grid(row=2,column=3)
Four.grid(row=3,column=1)
Five.grid(row=3,column=2)
Six.grid(row=3,column=3)
One.grid(row=4,column=1)
Two.grid(row=4,column=2)
Three.grid(row=4,column=3)
Zero.grid(row=5,column=2,columnspan=2)



Delete=Button(root,text="Delete",height=2, width=7,bg="red",command=lambda :clear())
Enter=Button(root,text="Enter",height=5, width=7,bg="blue",command = equate)
Delete.grid(row=3,column=4)
Enter.grid(row=4,column=4,rowspan=2)

root.mainloop()
