from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk #pip install pillow
import sqlite3
#import pymysql   #pip install pymysql
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration window")
        self.root.iconbitmap('E:\RMS\Image\pencils_120694.ico')
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        #Background Image
        self.bg = Image.open(r"E:/RMS/Image/left_bg.jpg")
        self.bg = self.bg.resize((1350,700),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(self.bg)
        bg=Label(self.root, image=self.bg).place(x=0, y=0, width=1350, height=700)

        #Left Image
        self.bg_img = Image.open(r"E:/RMS/Image/register_bg.jpg")
        self.bg_img = self.bg_img.resize((520,560),Image.ANTIALIAS)
        self.left=ImageTk.PhotoImage(self.bg_img)
        left=Label(self.root, image=self.left).place(x=80, y=75, width=520, height=560)

        #Register Frame
        frame1=Frame(self.root,bg="#FFF8DC")
        frame1.place(x=500, y=100, width=700, height=500)
        # frame1.attributes('-alpha',0.5)

        title=Label(frame1, text="REGISTER", font=("goudy old style",20, "bold"),bg="#FFE6EE").place(x=50, y=30)

        #------------------Row 1--------------------------
        # self.var_fname=StringVar()
        f_name=Label(frame1, text="FIRST NAME", font=("goudy old style",15, "bold"),bg="#FFE6EE").place(x=50, y=100)
        self.txt_fname=Entry(frame1,font=("goudy old style",15),bg="light yellow")
        self.txt_fname.place(x=50, y=130, width=250)

        l_name=Label(frame1, text="LAST NAME", font=("goudy old style",15, "bold"),bg="#FFE6EE").place(x=370, y=100)
        self.txt_lname=Entry(frame1,font=("goudy old style",15),bg="light yellow")
        self.txt_lname.place(x=370, y=130, width=250)

        #------------------Row 2--------------------------
        contact=Label(frame1, text="CONTACT NO.", font=("goudy old style",15, "bold"),bg="#FFE6EE").place(x=50, y=170)
        self.txt_contact=Entry(frame1,font=("goudy old style",15),bg="light yellow")
        self.txt_contact.place(x=50, y=200, width=250)
        
        email=Label(frame1, text="EMAIL", font=("goudy old style",15, "bold"),bg="#FFE6EE").place(x=370, y=170)
        self.txt_email=Entry(frame1,font=("goudy old style",15),bg="light yellow")
        self.txt_email.place(x=370, y=200, width=250)

        #------------------Row 3--------------------------
        question=Label(frame1, text="SECURITY QUESTION", font=("goudy old style",15, "bold"),bg="#FFE6EE").place(x=50, y=240)
        self.cmb_quest=ttk.Combobox(frame1,font=("goudy old style",13),state="readonly",justify=CENTER)
        self.cmb_quest['values']=("Select","Your First Pet Name", "Your birth place", "Your Best Friend Name")
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest.current(0)

        answer=Label(frame1, text="ANSWER", font=("goudy old style",15, "bold"),bg="#FFE6EE").place(x=370, y=240)
        self.txt_answer=Entry(frame1,font=("goudy old style",15),bg="light yellow")
        self.txt_answer.place(x=370, y=270, width=250)

        
        #------------------Row 4--------------------------
        password=Label(frame1, text="PASSWORD", font=("goudy old style",15, "bold"),bg="#FFE6EE").place(x=50, y=310)
        self.txt_password=Entry(frame1,font=("goudy old style",15),show='*',bg="light yellow")
        self.txt_password.place(x=50, y=340, width=250)

        cpassword=Label(frame1, text="CONFIRM PASSWORD", font=("goudy old style",15, "bold"),bg="#FFE6EE").place(x=370, y=310)
        self.txt_cpassword=Entry(frame1,font=("goudy old style",15),show='*',bg="light yellow")
        self.txt_cpassword.place(x=370, y=340, width=250)

        #Terms and Conditions
        self.var_chk=IntVar()
        chk=Checkbutton(frame1, text="I agree the Terms & Conditions",variable=self.var_chk,onvalue=1, offvalue=0,bg="#FFE6EE",font=("goudy old style",12)).place(x=50,y=380)

        # self.btn_img=ImageTk.PhotoImage(file="registerbutton.jpg")
        btn_register=Button(frame1,text="REGISTER",bg="lightgreen", activebackground="lightgreen",font=("goudy old style",20),cursor="hand2",command=self.register_data).place(x=80,y=420, width=250)

        btn_login=Button(frame1,text="SIGN IN",bg="lightblue", activebackground="lightblue",font=("goudy old style",20),cursor="hand2",command=self.login_window).place(x=350,y=420, width=180)

    
    def login_window(self):
        self.root.destroy()
        import login


    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.cmb_quest.current(0)

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_contact=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All fields are required", parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Password and confirm password should be same", parent=self.root)
        elif self.var_chk.get()==0:
             messagebox.showerror("Error","Please agree our terms & condition", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                # print(row)
                if row!=None:
                    messagebox.showerror("Error","User already exist, please try with another mail", parent=self.root)
                else:
                        
                    cur.execute("insert into employee (f_name, l_name, contact, email, question, answer, password) values(?,?,?,?,?,?,?)",
                                        (self.txt_fname.get(),
                                        self.txt_lname.get(),
                                        self.txt_contact.get(),
                                        self.txt_email.get(),
                                        self.cmb_quest.get(),
                                        self.txt_answer.get(),
                                        self.txt_password.get()
                                        )
                    )

                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Registered Successfully", parent=self.root)
                    self.clear()
                    self.login_window()

            except Exception as es:
                messagebox.showerror("Error",f"Error due to : {str(es)}", parent=self.root)
            


root=Tk()
obj=Register(root)
root.mainloop()