import tkinter as tk
a=tk.Tk()
a.geometry('500x600')
a.title('calculator')
def add():
    a=int(e1.get())
    b=int(e2.get())
    c=a+b
    l=tk.Label(text=c)
    l.place(x=200,y=210)
def sub():
    a=int(e1.get())
    b=int(e2.get())
    c=a-b
    l=tk.Label(text=c)
    l.place(x=200,y=210)
def mul():
    a=int(e1.get())
    b=int(e2.get())
    c=a*b
    l=tk.Label(text=c)
    l.place(x=200,y=210)
def div():
    a=int(e1.get())
    b=int(e2.get())
    c=a/b
    l=tk.Label(text=c)
    l.place(x=200,y=210)
l=tk.Label(text="first value")
l.place(x=130,y=150)
l=tk.Label(text="first value")
l.place(x=130,y=180)
e1=tk.Entry(a)
e1.place(x=200,y=150)
e2=tk.Entry(a)
e2.place(x=200,y=180)
b1=tk.Button(text='add', command=add)
b1.place(x=130,y=240)
b1=tk.Button(text='sub', command=sub)
b1.place(x=170,y=240)
b1=tk.Button(text='mul', command=mul)
b1.place(x=210,y=240)
b1=tk.Button(text='div', command=div)
b1.place(x=250,y=240)
#t.pack()
a.mainloop()