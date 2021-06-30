from report import Report
from result import Result
from tkinter import *
import tkinter
from PIL import Image, ImageTk
from course import Course
from student import Student
from result import Result
from report import Report
from tkinter import messagebox
import os
import sqlite3

class RMS:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result Management System")
        root.iconbitmap('E:\RMS\Image\pencils_120694.ico')
        self.root.geometry("1920x1020+0+0")
        self.root.config(bg = "White")
        #----------Icon-----------
        self.dash_logo = ImageTk.PhotoImage(file = "E:\RMS\Image\dash_logo.jpg")
        #----------Title----------
        title = Label(self.root, text="Student Result Management System", padx=10, compound=LEFT, image = self.dash_logo, font=("goudy old style", 15, "bold"), 
                        bg="#033054", fg="white").place(x=0,y=0,relwidth=1,height=50)
        #---------Menu------------
        Menu_frame = LabelFrame(self.root,text="Menus",font = ("times new roman",15, "bold"),bg="white").place(x=10,y=70,width=1895,height=100)
        #--------Menu_Item--------
        btn_course = Button(Menu_frame,text="Course", font = ("times new roman",15, "bold"),bg="#033054", fg="white", cursor="hand2", command=self.add_course).place(x=20,y=100,width=250,height=60)
        btn_student = Button(Menu_frame,text="Student", font = ("times new roman",15, "bold"),bg="#033054", fg="white", cursor="hand2", command=self.add_student).place(x=280,y=100,width=250,height=60)
        btn_result = Button(Menu_frame,text="Result", font = ("times new roman",15, "bold"),bg="#033054", fg="white", cursor="hand2",command=self.add_result).place(x=540,y=100,width=250,height=60)
        btn_vsr = Button(Menu_frame,text="View Student Result", font = ("times new roman",15, "bold"),bg="#033054", fg="white", cursor="hand2", command=self.view_report).place(x=800,y=100,width=250,height=60)
        btn_feedback = Button(Menu_frame,text="Feedback", font = ("times new roman",15, "bold"),bg="#033054", fg="white", cursor="hand2").place(x=1060,y=100,width=250,height=60)
        btn_logout = Button(Menu_frame,text="Log Out", font = ("times new roman",15, "bold"),bg="#033054", fg="white", cursor="hand2",command=self.logout).place(x=1320,y=100,width=250,height=60)
        btn_exit = Button(Menu_frame,text="Exit", font = ("times new roman",15, "bold"),bg="#033054", fg="white", cursor="hand2",command=self.exit_).place(x=1580,y=100,width=250,height=60)

        #-----------content Label------
        self.bg_img = Image.open(r"E:\RMS\Image\bg.png")
        self.bg_img = self.bg_img.resize((1100,560),Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image = self.bg_img).place(x=800, y=180,width=1100,height=560)

        self.bg = Image.open(r"E:/RMS/Image/register_bg.jpg")
        self.bg = self.bg.resize((720,760),Image.ANTIALIAS)
        self.left=ImageTk.PhotoImage(self.bg)
        left=Label(self.root, image=self.left).place(x=10, y=180, width=720, height=760)

        #---------update_details-----
        self.lbl_course = Label(self.root,text="Total Course\n[ 0 ]", font=("goudy old style", 15),bd=10, relief=RIDGE, bg="#033054", fg="white")
        self.lbl_course.place(x=800,y=800,width=300,height=100)
        self.lbl_student = Label(self.root,text="Total Student\n[ 0 ]", font=("goudy old style", 15),bd=10, relief=RIDGE, bg="#0676ad", fg="white")
        self.lbl_student.place(x=1200,y=800,width=300,height=100)
        self.lbl_result = Label(self.root,text="Total Result\n[ 0 ]", font=("goudy old style", 15),bd=10, relief=RIDGE, bg="#038074", fg="white")
        self.lbl_result.place(x=1600,y=800,width=300,height=100)


        #----------Footer----------
        footer = Label(self.root, text="SRMS-Student Result Management System\nContact Us for any enquires: xyz@gmail.com", font=("goudy old style", 12), 
                        bg="#262626", fg="white").pack(side = BOTTOM, fill=X)
        self.update_detail()
    def update_detail(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            cr = cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")

            cur.execute("select * from student")
            cr = cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")

            cur.execute("select * from result")
            cr = cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")

            self.lbl_course.after(200,self.update_detail)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Course(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Student(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Result(self.new_win)   
    def view_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Report(self.new_win)   
    def logout(self):
        op = messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op == True:
            self.root.destroy()
            import login
    def exit_(self):
        op = messagebox.askyesno("Confirm","Do you really want to Exit?",parent=self.root)
        if op == True:
            self.root.destroy()


if __name__ == '__main__':
    root = Tk()
    obj = RMS(root)
    root.mainloop()