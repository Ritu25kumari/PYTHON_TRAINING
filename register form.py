from tkinter import*
root = Tk()
root.geometry('500x500')
root.title("Registration Form")

label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="Sr. no",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Name",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Roll NO",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

entry_3 = Entry(root)
entry_3.place(x=240,y=230)

label_4 = Label(root, text="Address:",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

entry_4 = Entry(root)
entry_4.place(x=240,y=280)

label_5 = Label(root, text="Branch",width=20,font=("bold", 10))
label_5.place(x=70,y=330)
lable_5= StringVar(root)
lable_5.set("Select one") 

dd= OptionMenu(root,lable_5,"CSE","IT","ECE","ME","EE")
dd.pack()
dd.place(x=210,y=325)

l_6 = Label(root,text="Gender:",width=20,font=("bold", 10))
l_6.place(x=75,y=380)
var = IntVar()
Radiobutton(root,text="Male",padx = 5, variable=var, value=1).place(x=200,y=380)
Radiobutton(root,text="Female",padx = 20, variable=var, value=2).place(x=270,y=380)

Button(root,text='Submit',width=20,bg='brown',fg='white').place(x=180,y=440)
root.mainloop()




Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)
# it is use for display the registration form on the window
root.mainloop()
print("registration form  seccussfully created...")
