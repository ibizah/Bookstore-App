from tkinter import *

window = Tk()
#******************************************************

l1=Label(window,text='Tittle',fg='red')
l1.grid(column=0, row=0)

l2=Label(window,text='Year',fg='red')
l2.grid(column=0, row=1)

l3=Label(window,text='Author',fg='red')
l3.grid(column=2, row=0)

l4=Label(window,text='ISBN',fg='red')
l4.grid(column=2, row=1)

title= StringVar()
e1=Entry(window, textvariable='title', fg='blue')
e1.grid(column=1,row=0)

year=StringVar()
e2=Entry(window, textvariable='year', fg='blue')
e2.grid(column=1,row=1)

author=StringVar()
e3=Entry(window, textvariable='author', fg='blue')
e3.grid(column=3,row=0)

isbn=StringVar()
e1=Entry(window,textvariable='isbn', fg='blue')
e1.grid(column=3,row=1)

b1=Button(window,text='View all', width=10, fg='red')
b1.grid(column=3, row=2)

b2=Button(window,text='Search entry', width=10, fg='red')
b2.grid(column=3, row=3)

b3=Button(window,text='Add entry', width=10, fg='red')
b3.grid(column=3, row=4)

b4=Button(window,text='Update', width=10, fg='red')
b4.grid(column=3, row=5)

b5=Button(window,text='Delete', width=10, fg='red')
b5.grid(column=3, row=6)

b1=Button(window,text='Close', width=10, fg='red')
b1.grid(column=3, row=7)

li=Listbox(window, fg='blue',height=6, width=35)
li.grid(row=2,column=0, rowspan=6,columnspan=2)

scroll= Scrollbar(window)
scroll.grid(row=2,column=2,rowspan=6)

li.configure(yscrollcommand=scroll.set)
scroll.configure(command=li.yview)



#******************************************************
window.mainloop()
