from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.iconbitmap('E:\RMS\Image\pencils_120694.ico')
        self.root.geometry("1200x480+80+170")
        self.root.config(bg = "White")
        self.root.focus_force()

        #----------Title----------
        title = Label(self.root, text="Manage Student Details", font=("goudy old style", 20, "bold"), 
                        bg="#033054", fg="white").place(x=10,y=15,width=1180,height=35)
        #-------variable----------
        self.var_rollno = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_a_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()

        #--------widget-----------
        #---------------Column 1------------
        lbl_roll = Label(self.root, text="Roll No", font=("goudy old style", 15, "bold"), bg="white").place(x=10,y=60)
        lbl_Name = Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white").place(x=10,y=100)
        lbl_email = Label(self.root, text="Email", font=("goudy old style", 15, "bold"), bg="white").place(x=10,y=140)
        lbl_Gender = Label(self.root, text="Gender", font=("goudy old style", 15, "bold"), bg="white").place(x=10,y=180)
        lbl_State = Label(self.root, text="State", font=("goudy old style", 15, "bold"), bg="white").place(x=10,y=220)
        lbl_city = Label(self.root, text="City", font=("goudy old style", 15, "bold"), bg="white").place(x=310,y=220)
        lbl_pin = Label(self.root, text="Pin", font=("goudy old style", 15, "bold"), bg="white").place(x=510,y=220)
        
        
        lbl_address = Label(self.root, text="Address", font=("goudy old style", 15, "bold"), bg="white").place(x=10,y=260)


        #--------Entry Field-------
        self.txt_roll = Entry(self.root, textvariable = self.var_rollno, font=("goudy old style", 15), bg="light yellow")
        self.txt_roll.place(x=150,y=60,width=200)
        txt_Name = Entry(self.root, textvariable = self.var_name, font=("goudy old style", 15), bg="light yellow").place(x=150,y=100,width=200)
        txt_email = Entry(self.root, textvariable = self.var_email, font=("goudy old style", 15), bg="light yellow").place(x=150,y=140,width=200)
        self.txt_gender = ttk.Combobox(self.root, textvariable = self.var_gender,values=("Select","Male","Female","Others"), font=("goudy old style", 15), state="readonly", justify=CENTER)
        self.txt_gender.place(x=150,y=180,width=200)
        self.txt_gender.current(0)
        txt_state = Entry(self.root, textvariable = self.var_state, font=("goudy old style", 15), bg="light yellow").place(x=150,y=220,width=150)
        txt_city= Entry(self.root, textvariable = self.var_city, font=("goudy old style", 15), bg="light yellow").place(x=380,y=220,width=100)   
        txt_pin = Entry(self.root, textvariable = self.var_pin, font=("goudy old style", 15), bg="light yellow").place(x=560,y=220,width=120)


        
        #-----------Column 2--------------
        lbl_dob = Label(self.root, text="D.O.B", font=("goudy old style", 15, "bold"), bg="white").place(x=360,y=60)
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15, "bold"), bg="white").place(x=360,y=100)
        lbl_admission = Label(self.root, text="Admission", font=("goudy old style", 15, "bold"), bg="white").place(x=360,y=140)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 15, "bold"), bg="white").place(x=360,y=180)

        #--------Entry Field 2-------
        self.course_list = []
        self.fetch_course()
        #-----------Function Call to update the list
        txt_dob = Entry(self.root, textvariable = self.var_dob, font=("goudy old style", 15), bg="light yellow").place(x=480,y=60,width=200)
        txt_contact = Entry(self.root, textvariable = self.var_contact, font=("goudy old style", 15), bg="light yellow").place(x=480,y=100,width=200)
        txt_admission = Entry(self.root, textvariable = self.var_a_date, font=("goudy old style", 15), bg="light yellow").place(x=480,y=140,width=200)
        self.txt_course = ttk.Combobox(self.root, textvariable = self.var_course,values=self.course_list, font=("goudy old style", 15), state="readonly", justify=CENTER)
        self.txt_course.place(x=480,y=180,width=200)
        self.txt_course.set("Select")
        
        #---------Text Address-----------------
        self.txt_address = Text(self.root, font=("goudy old style", 15), bg="light yellow")
        self.txt_address.place(x=150,y=260,width=500,height=100)

        #----------Button-----------
        self.btn_add = Button(self.root,text="Add", font = ("goudy old style", 15, "bold"),bg="#033054", fg="white", cursor="hand2",command=self.add).place(x=150,y=400,width=110,height=40)
        self.btn_update = Button(self.root,text="Update", font = ("goudy old style", 15, "bold"),bg="#4caf50", fg="white", cursor="hand2",command=self.update).place(x=270,y=400,width=110,height=40)
        self.btn_delete = Button(self.root,text="Delete", font = ("goudy old style", 15, "bold"),bg="#f44336", fg="white", cursor="hand2",command=self.delete).place(x=390,y=400,width=110,height=40)
        self.btn_Clear = Button(self.root,text="Clear", font = ("goudy old style", 15, "bold"),bg="#607d8b", fg="white", cursor="hand2",command=self.clear).place(x=510,y=400,width=110,height=40)

        #----------Search Panel------
        self.var_search = StringVar()
        lbl_search_roll = Label(self.root, text="Roll No.", font=("goudy old style", 15,"bold"), bg="white").place(x=720,y=60)
        txt_search_roll = Entry(self.root, textvariable = self.var_search, font=("goudy old style", 15), bg="light yellow").place(x=870,y=60,width=180)
        btn_search = Button(self.root,text="Search", font = ("goudy old style", 15, "bold"),bg="#03a9f4", fg="white", cursor="hand2",command=self.search).place(x=1070,y=60,width=120,height=28)

        #---------Content----------
        self.C_frame = Frame(self.root,bd=2,relief=RIDGE)
        self.C_frame.place(x=720,y=100,width=470,height=340)

        scrolly = Scrollbar(self.C_frame,orient=VERTICAL)
        scrollx = Scrollbar(self.C_frame,orient=HORIZONTAL)
        self.StudentTable = ttk.Treeview(self.C_frame,columns=("roll","name","email","gender","dob","contact","admission","course","state","city","pin","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.StudentTable.xview)
        scrolly.config(command=self.StudentTable.yview)
        self.StudentTable.heading("roll",text="Roll No.")
        self.StudentTable.heading("name",text="Name")
        self.StudentTable.heading("email",text="Email")
        self.StudentTable.heading("gender",text="Gender")
        self.StudentTable.heading("dob",text="DOB")
        self.StudentTable.heading("contact",text="Contact")
        self.StudentTable.heading("admission",text="Admission")
        self.StudentTable.heading("course",text="Course")
        self.StudentTable.heading("state",text="State")
        self.StudentTable.heading("city",text="City")
        self.StudentTable.heading("pin",text="Pin")
        self.StudentTable.heading("address",text="Address")
        self.StudentTable["show"] = 'headings'
        self.StudentTable.column("roll",width = 100)
        self.StudentTable.column("name",width = 100)
        self.StudentTable.column("email",width = 100)
        self.StudentTable.column("gender",width = 100)
        self.StudentTable.column("dob",width = 100)
        self.StudentTable.column("contact",width = 100)
        self.StudentTable.column("admission",width = 100)
        self.StudentTable.column("course",width = 100)
        self.StudentTable.column("state",width = 100)
        self.StudentTable.column("city",width = 100)
        self.StudentTable.column("pin",width = 100)
        self.StudentTable.column("address",width = 200)
        self.StudentTable.pack(fill=BOTH,expand=1)
        self.StudentTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

#----------------------------------------------------------------------Clear Function----------------------------------------------------------
    def clear(self):
        self.show() 
        self.var_rollno.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_a_date.set("")
        self.var_course.set("Select")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.txt_address.delete("1.0",END)
        self.txt_address.config(state=NORMAL)
        self.var_search.set("")
#------------------Delete Function--------------------------------------------
    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()

        try:
            if self.var_rollno.get()=="":
                messagebox.showerror("Error","Roll Number should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll = ?",(self.var_rollno.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select Student from the List",parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm","Do you Really Want to Delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from student where roll = ?",(self.var_rollno.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student Successfully Deleted",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    #------------------getdata Function--------------------------------------------
    def get_data(self,ev):
        self.txt_roll.config(state="readonly")
        r = self.StudentTable.focus()
        content = self.StudentTable.item(r)
        row = content["values"]
        self.var_rollno.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_a_date.set(row[6])
        self.var_course.set(row[7])
        self.var_state.set(row[8])
        self.var_city.set(row[9])
        self.var_pin.set(row[10])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[11])        
        

#------------------Add Function--------------------------------------------
    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()

        try:
            if self.var_rollno.get()=="":
                messagebox.showerror("Error","Roll Number should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll = ?",(self.var_rollno.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Roll Number already present",parent=self.root)
                else:
                    cur.execute("insert into student (roll,name,email,gender,dob,contact,admission,course,state,city,pin,address) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_rollno.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student added Successfully",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
#------------------Show Function--------------------------------------------
    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()

        try:
            cur.execute("select * from student")
            rows = cur.fetchall()
            self.StudentTable.delete(*self.StudentTable.get_children())
            for row in rows:
                self.StudentTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

#------------------Fetch Function--------------------------------------------
    def fetch_course(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()

        try:
            cur.execute("select name from course")
            rows = cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

#------------------search Function--------------------------------------------
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from student where roll=?",(self.var_search.get(),))
            row = cur.fetchone()
            if row != None:
                self.StudentTable.delete(*self.StudentTable.get_children())
                self.StudentTable.insert('',END,values=row)
            else:
                messagebox.showerror("Error","No Records Found!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

#--------------------Update Function---------------------------------------
    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()

        try:
            if self.var_rollno.get()=="":
                messagebox.showerror("Error","Roll Number should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll = ?",(self.var_rollno.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select student from list",parent=self.root)
                else:
                    cur.execute("update student set name = ?,email = ?,gender = ?,dob = ?,contact = ?,admission = ?,course = ?,state = ?,city = ?,pin = ?,address=? where roll = ?",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END),
                        self.var_rollno.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student Update Successfully",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
      
if __name__ == '__main__':
    root = Tk()
    obj = Student(root)
    root.mainloop()