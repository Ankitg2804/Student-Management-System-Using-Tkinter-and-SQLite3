from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class Result:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.iconbitmap('E:\RMS\Image\pencils_120694.ico')
        self.root.geometry("1200x480+80+170")
        self.root.config(bg = "White")
        self.root.focus_force()

        #----------Title----------
        title = Label(self.root, text="Add Student Result", font=("goudy old style", 20, "bold"), 
                        bg="#033054", fg="white").place(x=10,y=15,width=1180,height=35)
        #-------variable----------
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks_ob = StringVar()
        self.var_full_marks = StringVar()
        self.roll_list = []
        self.fetch_roll()

        #--------widget-----------
        lbl_select = Label(self.root, text="Select Student", font=("goudy old style", 15, "bold"), bg="white").place(x=50,y=100)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white").place(x=50,y=160)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 15, "bold"), bg="white").place(x=50,y=220)
        lbl_marks_ob = Label(self.root, text="Marks Obtained", font=("goudy old style", 15, "bold"), bg="white").place(x=50,y=280)
        lbl_full_marks = Label(self.root, text="Full Marks", font=("goudy old style", 15, "bold"), bg="white").place(x=50,y=340)
        
        #--------Entry Field-------
        self.txt_student = ttk.Combobox(self.root, textvariable = self.var_roll,values=self.roll_list, font=("goudy old style", 15), state="readonly", justify=CENTER)
        self.txt_student.place(x=280,y=100,width=200)
        self.txt_student.set("Empty")
        btn_search = Button(self.root,text="Search", font = ("goudy old style", 15, "bold"),bg="#03a9f4", fg="white", cursor="hand2",command=self.search).place(x=500,y=100,width=100,height=28)

        txt_name = Entry(self.root, textvariable = self.var_name, font=("goudy old style", 15), bg="light yellow",state="readonly").place(x=280,y=160,width=320)
        txt_course = Entry(self.root, textvariable = self.var_course, font=("goudy old style", 15), bg="light yellow",state="readonly").place(x=280,y=220,width=320)
        txt_marks_ob = Entry(self.root, textvariable = self.var_marks_ob, font=("goudy old style", 15), bg="light yellow").place(x=280,y=280,width=320)
        txt_full_marks = Entry(self.root, textvariable = self.var_full_marks, font=("goudy old style", 15), bg="light yellow").place(x=280,y=340,width=320)
        #----------Button-----------
        self.btn_submit = Button(self.root,text="Submit", font = ("goudy old style", 15, "bold"),bg="lightgreen", activebackground="lightgreen", cursor="hand2",command=self.add).place(x=300,y=420,width=120,height=35)
        self.btn_clear = Button(self.root,text="Clear", font = ("goudy old style", 15, "bold"),bg="lightgrey", activebackground="lightgrey", cursor="hand2",command=self.clear).place(x=430,y=420,width=120,height=35)
 
         #-----------content Label------
        self.bg_img = Image.open(r"E:\RMS\Image\result.jpg")
        self.bg_img = self.bg_img.resize((450,350),Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg = Label(self.root, image = self.bg_img).place(x=700, y=100,width=450,height=350)

#------------------Fetch Function--------------------------------------------
    def fetch_roll(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()

        try:
            cur.execute("select roll from student")
            rows = cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
#------------------search Function--------------------------------------------
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select name,course from student where roll=?",(self.var_roll.get(),))
            row = cur.fetchone()
            if row != None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error","No Records Found!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
#------------------Add Function--------------------------------------------
    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()

        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Please Search the Record!!",parent=self.root)
            else:
                cur.execute("select * from result where roll = ? and course = ?",(self.var_roll.get(),self.var_course.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Result already present",parent=self.root)
                else:
                    per = (int(self.var_marks_ob.get())*100)/int((self.var_full_marks.get()))
                    cur.execute("insert into result (roll, name, course, marks_obtain, full_marks, per) values(?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks_ob.get(),
                        self.var_full_marks.get(),
                        str(per)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Result added Successfully",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
#------------------Clear Function--------------------------------------------
    def clear(self):
        self.var_roll.set("Select"),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_marks_ob.set(""),
        self.var_full_marks.set("")

if __name__ == '__main__':
    root = Tk()
    obj = Result(root)
    root.mainloop()