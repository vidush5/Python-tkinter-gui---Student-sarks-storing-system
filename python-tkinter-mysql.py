# * * * Student Marks Storing System * * * #
# Usimg tkinter and mysql
# User enter the student id, name & english marks

#Importing packages
from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

root = Tk()
root.geometry("600x300")
root.title("Python+Tkinter+MySql")

def insert():
    id = e_id.get();
    name = e_name.get();
    english = e_english.get();

    if (id=="" or name=="" or english==""):
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        con = mysql.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "")
        cursor = con.cursor()
        cursor.execute("insert into student marks('"+ id +"','"+ name +"','"+ english +"')")
        cursor.execute("commit");


        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_english.delete(0, 'end')
        MessageBox.showinfo("Insert Status","Inserted Successfully");
        con.close();

def delete():
    if(e_id.get() == ""):
        MessageBox.showinfo("Delete Status", "ID is compolsary for delete")
    else:
        con = mysql.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "")
        cursor = con.cursor()
        cursor.execute("delete from student where is='"+ e_id.get() + "'")
        cursor.execute("commit");

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_english.delete(0, 'end')
        show()
        MessageBox.showinfo("Delete Status","Deleted Successfully");
        con.close();

def update():
    id = e_id.get();
    name = e_name.get();
    english = e_english.get();

    if (id=="" or name=="" or english==""):
        MessageBox.showinfo("Update Status", "All Fields are required")
    else:
        con = mysql.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "")
        cursor = con.cursor()
        cursor.execute("update student set name='"+ name +"', english'"+ english +"' where id ='" + id +"'")
        cursor.execute("commit");


        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_english.delete(0, 'end')
        show()
        MessageBox.showinfo("Update Status","Updatted Successfully");
        con.close();

def get():
    if(e_id.get() == ""):
        MessageBox.showinfo("Fetch Status", "ID is compolsary for delete")
    else:
        con = mysql.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "")
        cursor = con.cursor()
        cursor.execute("select * from student where is='"+ e_id.get() + "'")
        rows = cursor.fetchall()

        for row in rows:
            e_name.insert(0, row[1])
            e_english.insert(0, row[2])

        con.close();

def show():
    con = mysql.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "")
            cursor = con.cursor()
            cursor.execute("select * from student")
            rows = cursor.fetchall()
            list.delete(0, list.size())

            for row in rows:
                insertData = str(row[0])+'   '+ row[1]
                list.insert(list.size()+1, insertData)

            con.close()
    


id = Label(root, text='Enter ID', font=('bold', 10))
id.place(x=20, y=30);

name = Label(root, text='Enter Name', font=('bold', 10))
name.place(x=20, y=60);

english = Label(root, text='Enter English Marks', font=('bold', 10))
english.place(x=20, y=90);

e_id = Entry()
e_id.place(x=150, y=30)

e_name = Entry()
e_name.place(x=150, y=60)

e_english = Entry()
e_english.place(x=150, y=90)

insert = Button(root, text="insert", font=("italic", 10), bg="white", command=insert)
insert.place(x=20, y=140)

delete = Button(root, text="Delete", font=("italic", 10), bg="white", command=delete)
delete.place(x=70, y=140)

update = Button(root, text="Update", font=("italic", 10), bg="white", command=update)
update.place(x=130, y=140)

get = Button(root, text="Get", font=("italic", 10), bg="white", command=get)
get.place(x=190, y=140)


list = Listbox(root)
list.place(x=290, y=30)
show()


root.mainloop()
