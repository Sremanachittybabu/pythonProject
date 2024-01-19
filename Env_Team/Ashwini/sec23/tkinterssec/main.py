from tkinter import *


window = Tk()

def km2mil():
    miles = float(evalue.get())*1.6
    t1.insert(END,miles)

#button
b1 = Button(window , text = "Convert",command=km2mil)
#b1.pack()
b1.grid(row=0,column=1)

evalue = StringVar()
e1 = Entry(window, textvariable=evalue )
e1.grid(row=0,column=0)

t1 = Text(window , height=4 ,width=20)
t1.grid(row=0,column=2)

window.mainloop()