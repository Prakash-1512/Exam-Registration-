import tkinter
from tkinter import ttk,messagebox
import mysql.connector
from tkinter import*
root=Tk()
root.geometry("800x500")
def getvalue(student):
 s1.insert(0,select['st_id'])
 s2.insert(0,select['st_name'])
 s3.insert(0,select['dob'])
 s4.insert(0,select['qualification'])
 s5.insert(0,select['address'])
 s6.insert(0,select['mobile_no'])
 s7.insert(0,select['email_id'])
 s8.insert(0,select['username'])
 s9.insert(0,select['password'])
def validate():
 student_name= s1.get()
 email_id= s7.get()
 country= c.get()
 if (student_name=="" or email_id=="" or country== 'Select your country' or
gender == 0):
 tkinter.messagebox.showinfo('Invalid Message Alert',"Fields cannot be left
empty!")
 else:
 tkinter.messagebox.showinfo('Success Message',"Successfully registered!")
def add():
 student_id=s1.get()
 student_name=s2.get()
 dob=s3.get()
 qualification=s4.get()
 address=s5.get()
 mobile_no=s6.get()
 email_id=s7.get()
 username=s8.get()
 password=s9.get()
 mysqldb=mysql.connector.connect(host="localhost",user="root",password="
",database="exam registration")
 mycursor=mysqldb.cursor()
 try;
 sql="insert into
registration(st_id,st_name,dob,qualification,address,mobile_no,email_id,username,
password)values(%d,%s,%d,%s,%s,%d,%s,%s,%d)"

val=(student_id,student_name,dob,qualification,address,mobile_no,email_id,usern
ame,password)
 mycursor.execute(sql,val)
 mysqldb.commit()
 lastid=mycursor.lastrowid
 messagebox.showinfo("information","details inserted successfully")
 e1.focus_set()
 except:
 print(e)
 mysqldb.rollback()
 mysqldb.close()
 def show():
 mysqldb=mysql.connector.connect(host="localhost",user="root",password="
",database="exam registration")
 mycursor=mysqldb.cursor()
 mycursor.execute("select
st_id,st_name,dob,qualification,address,mobile_no,email_id,username,password
from registration")
 records=mycursor.fetchall()
 print(records)
 for
i,(st_id,st_name,dob,qualification,address,mobile_no,email_id,username,password)
in enumerate(records,start=1):
 mysqldb.close()
def register():
 root=Tk()
 root.geometry("800x500")
 root.title("exam registration")
 global s1
 global s2
 global s3
 global s4
 global s5
 global s6
 global s7
 global s8
 global s9
 Label(root,text="Exam registration
form",fg="red",font=('calibri',30)).place(x=200,y=10)
 Label(root,text="student id").place(x=250,y=110)
 Label(root,text="student name").place(x=250,y=140)
 Label(root,text="dob").place(x=250,y=170)
 Label(root,text="qualification").place(x=250,y=260)
 Label(root,text="address").place(x=250,y=290)
 Label(root,text="mobile_no").place(x=250,y=320)
 Label(root,text="email_id").place(x=250,y=350)
 Label(root,text="username").place(x=250,y=380)
 Label(root,text="password").place(x=250,y=410)
 c=StringVar()
 var=IntVar()
 label_9=Label(root,text="city",width=20,font=("bold",10))
 label_9.place(x=180,y=230)
 list1=['sivakasi','madurai','sattur','kovilpatti','trichy','chennai'];
 c.set("Select your city")
 droplist=OptionMenu(root,c,*list1)
 droplist.config(width=15)
 droplist.place(x=320,y=225)
 label_8=Label(root,text="gender",width=20,font=("bold",10))
 label_8.place(x=190,y=200)

Radiobutton(root,text="male",padx=5,variable=var,value=1).place(x=320,y=200)


Radiobutton(root,text="female",padx=5,variable=var,value=2).place(x=380,y=200
)
 s1=Entry(root)
 s1.place(x=330,y=110)
 s2=Entry(root)
 s2.place(x=330,y=140)
 s3=Entry(root)
 s3.place(x=330,y=170)
 s4=Entry(root)
 s4.place(x=330,y=260)
 s5=Entry(root)
 s5.place(x=330,y=290)
 s6=Entry(root)
 s6.place(x=330,y=320)
 s7=Entry(root)
 s7.place(x=330,y=350)
 s8=Entry(root)
 s8.place(x=330,y=380)
 s9=Entry(root)
 s9.place(x=330,y=410)
 Button(root,text="submit to
verify",bg="#289166",command=validate,height=2,width=13).place(x=470,y=430
)
def login():
 root=Tk()
 root.title("Login")
 root.geometry("800x600")

 Label(root, text="").pack()
 Label(root, text="Username").pack()
 username_login_entry = Entry(root, textvariable="username")
 username_login_entry.pack()
 Label(root, text="").pack()
 Label(root, text="Password").pack()
 password__login_entry = Entry(root, textvariable="password", show= '*')
 password__login_entry.pack()
 Label(root, text="").pack()
 Button(root, text="Login", bg="#00EBE7",fg='black',width=10,
height=1).pack()
 root.mainloop()
text=Label(root,text="EXAM
REGISTRATION",foreground="blue",background="white",font=("algerian",35))
text.place(x=170,y=40)
Button(root,text="register",bg="#0059FF",command=register,height=5,width=40,f
ont=("calibri",10)).place(x=250,y=150)
Button(text="login",bg="#D000FF",height=5,command=login,width=40,font=("ca
libri",10)).place(x=250,y=300)
root.mainloop()