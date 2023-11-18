# python traning project blood donation management system
from tkinter import *
from tkinter.font import BOLD
import mysql.connector
from tkinter import messagebox
#setting database connection
gndec_blooddonation = mysql.connector.connect(
    host ="127.0.0.1",
    user = "root",
    password = 'rkumari',
    database='gndec_blooddonation')
mycursor = gndec_blooddonation.cursor()
#declaring main project window for Python Blood Bank Management System
root=Tk()
root.title("WELCOME TO GNDEC BLOOD DONATION CAMP")
root.geometry("600x550")

greet = Label(root, font = ('arial', 20, 'bold'), text = "GNDEC BLOOD DONATION CAMP")
greet.grid(row = 0,columnspan = 3)

#function that alters the database and increase the units of the blood group 
def Donate_dbase():
    global bgrp    
    global bunits
    units=bunits.get()   
    dbase = mysql.connector.connect(
        host ="127.0.0.1",
        user = "root",
        password = 'rkumari',
        database='gndec_blooddonation')
    cursor = dbase.cursor() 
    print(bgrp)
    print(units)
    sqlquery="Select units from BloodBank where Blood_Grp='"+bgrp+"';"   
    cursor.execute(sqlquery)
 
    for i in cursor:
        print(i[0])
        
        units=str( int(i[0])+ int(units) )
        print(units)
 
    #sqlquery to update the units of blood group
    sqlquery= "Update BloodBank set units='"+ units + "' where Blood_Grp='"+bgrp+"';"
    print(sqlquery)
    try:
        cursor.execute(sqlquery)
        dbase.commit()
        messagebox.showinfo('Success',"Blood Donated Successfully")
    except:
        messagebox.showinfo("Error","Cannot access Database")

#method to ask the units of blood that the user wants to donate
def donate(*args, **kwargs):
    global bgrp
    global bunits
    bgrp=args[0]
    print(bgrp)
    root=Tk()
    root.title('GNDEC BLOOD DONATION CAMP')
    root.geometry("450x300")
 
    #displaying message "Donate Blood"
    greet = Label(root, font = ('arial', 30, 'bold'), text = "Donate Blood")
    greet.grid(row = 0,columnspan = 3)
 
    #----------bunits------------------
    L = Label(root, font = ('arial', 10, 'bold'), text = "Enter No. of Units: ")
    L.grid(row = 4, column = 1)
 
    L = Label(root, font = ('arial', 10, 'bold'), text = "   ")
    L.grid(row = 4, column = 2)
 
    bunits=Entry(root,width=5,font =('arial', 10))
    bunits.grid(row=4,column=3)
    
    
    submitbtn=Button(root,text="Submit",command=Donate_dbase,bg="red",fg="white",font = ('arial', 10))
    submitbtn.grid(row=8,columnspan=3)        
    print("Donate")

#function that alters the database and decreases the units of the blood group 
def Request_dbase():
    global bgrp
    global bunits
    units=bunits.get()
    #database connection
    dbase = mysql.connector.connect(
        host ="127.0.0.1",
        user = "root",
        password = 'rkumari',
        database='gndec_blooddonation')
    cursor = dbase.cursor()
    print(bgrp)
    print(units)
    sqlquery="Select units from BloodBank where Blood_Grp='"+bgrp+"';"
    cursor.execute(sqlquery)
 
    for i in cursor:
        if( int(i[0])>= int(units) ):
            units=str( int(i[0])-int(units) )
            print(units)

            sqlquery= "Update BloodBank set units='"+ units + "' where Blood_Grp='"+bgrp+"';";
            print(sqlquery)
            try:
               
                cursor.execute(sqlquery) 
                dbase.commit()
                messagebox.showinfo('Success',"Blood Request Successful")
            except:
                messagebox.showinfo("Error","Cannot access Database")
        else:
            messagebox.showinfo("Error","Not Available")        
    
#method to ask the units of blood that the user wants
def request(*args, **kwargs):
    global bgrp
    global bunits
    bgrp=args[0]
    print(bgrp)
    root=Tk()
    root.title('GNDEC BLOOD DONATION CAMP')
    root.geometry("450x300")
 
    #displaying message "Request Blood"
    greet = Label(root, font = ('arial', 20, 'bold'), text = "Request Blood")
    greet.grid(row = 0,columnspan = 3)
 
    #----------bunits------------------
    #asking the user to enter the units of blood, he wants 
    L = Label(root, font = ('arial', 10, 'bold'), text = "Enter Units Required: ")
    L.grid(row = 4, column = 1)
 
    L = Label(root, font = ('arial', 10, 'bold'), text = "   ")
    L.grid(row = 4, column = 2)
 
    bunits=Entry(root,width=5,font =('arial', 10))
    bunits.grid(row=4,column=3)
 
    #creating a submit button to request the blood
    submitbtn=Button(root,text="Submit",command=Request_dbase,bg="red",fg="white",font = ('arial', 10))
    submitbtn.grid(row=8,columnspan=3)    
    print("Request")

#displaying all the records of the bloodbank table
sqlquery="Select * from BloodBank ;" 
try:
    mycursor.execute(sqlquery)
    #displaying the table head
    L = Label(root, font = ('arial', 12,'bold'), text = "%-20s%-20s"%("Blood group","Units"))
    L.grid(row = 1,column=1)
    x=4
    for i in mycursor: 
        L = Label(root, font = ('arial', 10), text = "%-20s%-20s"%(i[0],i[1]))
        L.grid(row = x,column=1)
        bgrp=i[0]
        
        # creating a button to donate blood
        d=Button(root,text="Donate",command=lambda arg=i[0], kw="donate" : donate(arg, o1=kw),padx=10,pady=10,bg="red",fg="white",font = ('arial', 15))
        d.grid(row=x,column=2)
        
        #creating a button to request blood
        r=Button(root,text="Request",command=lambda arg=i[0], kw="request" : request(arg, o1=kw),padx=10,pady=10,bg="red",fg="white",font = ('arial',15))
        r.grid(row=x,column=3)
        x+=1   
 
except:
    messagebox.showinfo("Error","Cannot Fetch data.")
root.mainloop()

 
