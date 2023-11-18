#importing modules
from tkinter import *
from tkinter.font import BOLD
import mysql.connector
from tkinter import messagebox
 
#setting database connection
db = mysql.connector.connect(host ="127.0.0.1",user = "root",password = 'rkumari',database='db')
#make sure you enter your username and password in the above line
cursor = db.cursor()
 
#declaring main project window for Python Blood Bank Management System
root=Tk()
root.title("GNDEC BLOOD DONATION CAMP")
root.geometry("500x500")
 
#Label is a widget in tkinter that implements display box where we can place text
Label(root, font = ('arial', 20, 'bold'), text = "GNDEC BLOOD DONATION CAMP")
 
 
#function that alters the database and increase the units of the blood group 
def Donate_dbase():
 
    global bgrp    
    global bunits
 
    units=bunits.get()
    
    #setting database connection
    dbase = mysql.connector.connect(host ="127.0.0.1",user = "root",password = 'rkumari',database='db')
    cursor = dbase.cursor()
    
    #Debug statements to check the values,you may comment it
    print(bgrp)
    print(units)
 
    #storing sql query in a variable named sqlquery
    sqlquery="Select units from BloodBank where Blood_Grp='"+bgrp+"';"
    #executing the sql query
    cursor.execute(sqlquery)
 
    for i in cursor:
        print(i[0])
        #units holds the increased amount of the blood group
        units=str( int(i[0])+ int(units) )
        print(units)
 
    #sqlquery to update the units of blood group
    sqlquery= "Update BloodBank set units='"+ units + "' where Blood_Grp='"+bgrp+"';"
    print(sqlquery)
 
    try:
        #finally executing the sql query and updating the database
        cursor.execute(sqlquery)
        #saving the changes in the database
        dbase.commit()
 
        #displaying the message box showing "Blood Donated Successfully"
        messagebox.showinfo('Success',"Blood Donated Successfully")
    except:
        # if the sql query is not correct or the database connection is not set properly we are displaying a message box displaying "Cannot access Database"
        messagebox.showinfo("Error","Cannot access Database")
    
 
#method to ask the units of blood that the user wants to donate
def donate(*args, **kwargs):
    global bgrp
    global bunits
 
    #the first value of args holds the blood group, the user wants to donate
    bgrp=args[0]
    #printing the value of bgrp on command prompt to check if it is correct
    print(bgrp)
 
    #initializing a separate tkinter window
    root=Tk()
    root.title('GNDEC BLOOD DONATION CAMP')
 
    #displaying message "Donate Blood"
    greet = Label(root, font = ('arial', 20, 'bold'), text = "Donate Blood")
    greet.grid(row = 0,columnspan = 3)
 
    #----------bunits------------------
 
    #asking the user to enter the units of blood, he wants to donate
    L = Label(root, font = ('arial', 10, 'bold'), text = "Enter No. of Units: ")
    L.grid(row = 4, column = 1)
 
    L = Label(root, font = ('arial', 10, 'bold'), text = "   ")
    L.grid(row = 4, column = 2)
 
    bunits=Entry(root,width=5,font =('arial', 10))
    bunits.grid(row=4,column=3)
    
    #creating a submit button to donate the blood, this button calls Donate_dbase function to update the database.
    submitbtn=Button(root,text="Submit",command=Donate_dbase,bg="DodgerBlue2",fg="white",font = ('arial', 10))
    submitbtn.grid(row=8,columnspan=3)
        
    print("Donate")
 
 
#function that alters the database and decreases the units of the blood group if the request amount is available else it shows the appropriate message in Python Blood Bank System
def Request_dbase():
   
    global bgrp
    global bunits
 
    units=bunits.get()
 
    #setting database connection
    dbase = mysql.connector.connect(host ="127.0.0.1",
    user = "root",
    password = 'rkumari',
    database='dbase')
    cursor = dbase.cursor()
 
    #Debug statements to check the values,you may comment it
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
 
                #displaying the message box showing "Blood Request Successfully"
                messagebox.showinfo('Success',"Blood Request Successful")
            except:
                # if the sql query is not correct or the database connection is not set properly we are displaying a message box displaying "Cannot access Database"
                messagebox.showinfo("Error","Cannot access Database")
        else:
            #if the requested amount is not available, showing "Not Available"
            messagebox.showinfo("Error","Not Available")        
    
 
#method to ask the units of blood that the user wants
def request(*args, **kwargs):
    global bgrp
    global bunits
 
    #the first value of args holds the blood group, the user wants
    bgrp=args[0]
    #printing the value of bgrp on command prompt to check if it is correct
    print(bgrp)
 
    #initializing a separate tkinter window
    window=Tk()
    window.title('GNDEC BLOOD DONATION CAMP')
 
    #displaying message "Request Blood"
    Label(window, font = ('arial', 20, 'bold'), text = "Request Blood")
 
    #----------bunits------------------
    #asking the user to enter the units of blood, he wants 
    Label(window, font = ('arial', 10, 'bold'), text = "Enter Units Required: ")
    L.grid(row = 4, column = 1)
 
    L = Label(window, font = ('arial', 10, 'bold'), text = "   ")
    L.grid(row = 4, column = 2)
 
    bunits=Entry(window,width=5,font =('arial', 10))
    bunits.grid(row=4,column=3)
 
    #creating a submit button to request the blood, this button calls Request_dbase function to update the database.
    submitbtn=Button(window,text="Submit",command=Request_dbase,bg="DodgerBlue2",fg="white",font = ('arial', 10))
    submitbtn.grid(row=8,columnspan=3)
        
    print("Request")
 
#displaying all the records of the bloodbank table
#sql query to select all the entries of the table
sqlquery="Select * from BloodBank ;"
 
try:
    #executing the sql query
    cursor.execute(sqlquery)
 
    #displaying the table head
    L = Label(root, font = ('arial', 12,'bold'), text = "%-20s%-20s"%("Blood group","Units"))
    L.grid(row = 1,column=1)
 
    
    x=4
    for i in cursor:
        
        L = Label(root, font = ('arial', 10), text = "%-20s%-20s"%(i[0],i[1]))
        L.grid(row = x,column=1)
 
        bgrp=i[0]
        
        
        d=Button(root,text="Donate",command=lambda arg=i[0], kw="donate" : donate(arg, o1=kw),padx=10,pady=10,bg="DodgerBlue2",fg="red",font = ('arial', 15))
        d.grid(row=x,column=2)
        
        
        r=Button(root,text="Request",command=lambda arg=i[0], kw="request" : request(arg, o1=kw),padx=10,pady=10,bg="DodgerBlue2",fg="red",font = ('arial',15))
        r.grid(row=x,column=3)
 
        
        x+=1   
 
except:
    messagebox.showinfo("Error","Cannot Fetch data.")
 
root.mainloop()