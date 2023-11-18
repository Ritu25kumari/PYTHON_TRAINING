from tkinter import*
from mysql import connector
from tkinter import messagebox


# from mysql import connector
def database():
    conn = connector.connect(
        user='root',
        password='rkumari',
        host='127.0.0.1',
        port='3306',
        database='pythonform_db')
    mycursor=conn.cursor()
    mycursor.execute('insert into pythonform_db values(%s,%s,%s,%s,%s)',(entry_1.get(),entry_2.get(),entry_3.get(),entry_5.get(),var.get()))
    
    conn.commit()
    messagebox.showinfo('info','submitted')

root = Tk()
root.geometry('500x500')
root.title("Registration Form")

label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=70,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Branch",width=20,font=("bold", 10))
label_2.place(x=70,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Email",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

entry_3 = Entry(root)
entry_3.place(x=240,y=230)

label_5 = Label(root, text="Age:",width=20,font=("bold", 10))
label_5.place(x=70,y=280)

entry_5 = Entry(root)
entry_5.place(x=240,y=280)

label_4 = Label(root, text="Gender",width=20,font=("bold", 10))
label_4.place(x=70,y=330)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=330)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=330)
Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=380)
# it is use for display the registration form on the window
root.mainloop()
print("registration form  seccussfully created...")