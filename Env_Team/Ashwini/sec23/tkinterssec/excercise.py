from tkinter import *

window = Tk()

def converti():
    gms = float(evalue.get())*1000
    pounds= float(evalue.get())*2.20462
    ounces = float(evalue.get()) * 35.274

    t1.insert(END,gms)
    t2.insert(END, pounds)
    t3.insert(END, ounces)

l1 = Label(window ,text="kg")
l1.grid(row=0,column=0)

evalue = StringVar()
e1 = Entry(window, textvariable=evalue )
e1.grid(row=0,column=1)

b1 = Button(window , text="Convert" , command=converti)
b1.grid(row=0,column=2)

t1 = Text(window , height=4 ,width=8)
t1.grid(row=1,column=0)

t2 = Text(window , height=4 ,width=8)
t2.grid(row=1,column=1)

t3 = Text(window , height=4 ,width=8)
t3.grid(row=1,column=2)


window.mainloop()