from tkinter import*
from mysql import connector
from tkinter import messagebox
def register():
    conn=connector.connect(
        user='root',
        password='rkumari',
        host='127.0.0.1',
        port='3306',
        database='pythonform_db')
    mycursor=conn.cursor()
    mycursor.execute("insert into pythonform_db value (%s,%s,%s,%s)",(Nameentry.get(),Phoneentry.get(),Genderentry.get(),Emailentry.get()))
    messagebox.showinfo("INFO","Registered")
    conn.commit()


root=Tk()
root.title("Registration")
root.geometry("500x500")

Label(root,text="Python Registration form",font="arial 25").pack(pady=50)

Label(text="Name",font=23).place(x=100,y=150)
Label(text="Phone",font=23).place(x=100,y=200)
Label(text="Gender",font=23).place(x=100,y=250)
Label(text="Email",font=23).place(x=100,y=300)
#entry
NameValue=StringVar()
PhoneValue=StringVar()
GenderValue=StringVar()
EmailValue=StringVar()

Nameentry=Entry(root,textvariable=NameValue,width=30,bd=2,font=20)
Phoneentry=Entry(root,textvariable=PhoneValue,width=30,bd=2,font=20)
Genderentry=Entry(root,textvariable=GenderValue,width=30,bd=2,font=20)
Emailentry=Entry(root,textvariable=EmailValue,width=30,bd=2,font=20)

Nameentry.place(x=200,y=150)
Phoneentry.place(x=200,y=200)
Genderentry.place(x=200,y=250)
Emailentry.place(x=200,y=300)

#check button
checkValue=IntVar
checkbtn=Checkbutton(text="remeber me?",variable=checkValue)
checkbtn.place(x=200,y=350)

log=Button(root,text='Register',fg='Black',bg='light blue',command=register,width=15,height=1,bd=2,highlightbackground='black', highlightcolor='black', highlightthickness=1)
log.place(x=200,y=400)

root.mainloop()