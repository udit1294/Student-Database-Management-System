from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk #for image showing
import mysql
import mysql.connector

class Student:
    def __init__(self,root):  #constructor initialize
        self.root=root
        self.root.geometry('2080x790+0+0') #for window display
        self.root.title('STUDENT MANGEMENT SYSTEM')

        #Variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_phno=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        #1st image
        img=Image.open(r'college_images\7th.jpg')
        img=img.resize((540,160),Image.ANTIALIAS) #convert high level image to low level image
        self.photoimg=ImageTk.PhotoImage(img)
        
        self.btn_1=Button(self.root,image=self.photoimg,cursor='hand2')
        self.btn_1.place(x=0,y=0,width=540,height=160)

        #2nd image
        img_2=Image.open(r'college_images\3rd.jpg')
        img_2=img_2.resize((540,160),Image.ANTIALIAS) #convert high level image to low level image
        self.photoimg_2=ImageTk.PhotoImage(img_2)
        
        self.btn_2=Button(self.root,image=self.photoimg_2,cursor='hand2')
        self.btn_2.place(x=540,y=0,width=540,height=160)

        #3rd image
        img_3=Image.open(r'college_images\9th.jpg')
        img_3=img_3.resize((540,160),Image.ANTIALIAS) #convert high level image to low level image
        self.photoimg_3=ImageTk.PhotoImage(img_3)
        
        self.btn_3=Button(self.root,image=self.photoimg_3,cursor='hand2')
        self.btn_3.place(x=1000,y=0,width=540,height=160)

        #background image
        img_4=Image.open(r'college_images\university.jpg')
        img_4=img_4.resize((2080,790),Image.ANTIALIAS) #convert high level image to low level image
        self.photoimg_4=ImageTk.PhotoImage(img_4)

        bg_label=Label(self.root,image=self.photoimg_4,bd=2,relief=RIDGE)
        bg_label.place(x=0,y=160,width=2080,height=790)

       
        #label title

        lbl_title=Label(bg_label,text='STUDENT MANAGEMENT SYSTEM',relief=GROOVE, font=('times new roman',37,'bold'),fg='red',bg='yellow')
        lbl_title.place(x=0,y=0,width=1600,height=50)

        #create frame
        manage_frame=Frame(bg_label,bd=2,relief=RIDGE,bg='white')
        manage_frame.place(x=15,y=55,width=1500,height=600)
        
        #create left frame
        dataleftframe=LabelFrame(manage_frame,bd=4,relief=RIDGE,padx=2,text='Student information',font=('times new roman',15,'bold'),fg='blue',bg='white')
        dataleftframe.place(x=10,y=10,width=620,height=600)

        img_5=Image.open(r'college_images\11th.jpg')
        img_5=img_5.resize((600,125),Image.ANTIALIAS) #convert high level image to low level image
        self.photoimg_5=ImageTk.PhotoImage(img_5)

        my_image=Label(dataleftframe,image=self.photoimg_5,bd=2,relief=RIDGE,bg='white')
        my_image.place(x=10,y=8,width=600,height=125)

        #current course labelframe information

        std_lbl_info_frame=LabelFrame(dataleftframe,bd=4,relief=RIDGE,padx=2,text='Current course labelframe information',font=('times new roman',15,'bold'),fg='purple',bg='white')
        std_lbl_info_frame.place(x=10,y=135,width=600,height=133)

        #labels and combobox

        #Department
        lbl_dep=Label(std_lbl_info_frame,text='Department: ',font=('arial',12,'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)
        combo_dep=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_dep,font=('arial',12,'bold'),width=16,state='readonly') #create combobox for choosing values
        combo_dep['values']=('Select department','Computer','IT','Civil','ECE','MATH')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #Course
        course_std=Label(std_lbl_info_frame,text='Courses: ',font=('arial',12,'bold'),bg='white')
        course_std.grid(row=0,column=2,padx=2,pady=10,sticky=W)
        com_course=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_course,font=('arial',12,'bold'),width=16,state='readonly')
        com_course['values']=('Select Course','Fy','Sy','Ty','Fy')
        com_course.current(0)
        com_course.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        current_year=Label(std_lbl_info_frame,text='Year: ',font=('arial',12,'bold'),bg='white')
        current_year.grid(row=1,column=0,padx=2,pady=10,sticky=W)
        com_year=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_year,font=('arial',12,'bold'),width=16,state='readonly')
        com_year['values']=('Select Year','2021-22','2022-23','2023-24','2024-25')
        com_year.current(0)
        com_year.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        label_semester=Label(std_lbl_info_frame,text='Semester: ',font=('arial',12,'bold'),bg='white')
        label_semester.grid(row=1,column=2,padx=2,pady=10,sticky=W)
        com_Semester=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_sem,font=('arial',12,'bold'),width=16,state='readonly')
        com_Semester['values']=('Select Semester','semester-1','semester-2')
        com_Semester.current(0)
        com_Semester.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #Student class labelframe information
        std_lbl_class_frame=LabelFrame(dataleftframe,bd=4,relief=RIDGE,padx=2,text='Student class labelframe information',font=('times new roman',15,'bold'),fg='purple',bg='white')
        std_lbl_class_frame.place(x=10,y=270,width=600,height=220)
        
        #labels 

        #Student_id
        label_id=Label(std_lbl_class_frame,text='Student_ID: ',font=('arial',12,'bold'),bg='white')
        label_id.grid(row=0,column=0,padx=2,pady=7,sticky=W)
        id_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_id,font=('arial',12,'bold'),width=12)
        id_entry.grid(row=0,column=1,padx=2,pady=7,sticky=W)

        #Name
        label_name=Label(std_lbl_class_frame,text='Name: ',font=('arial',12,'bold'),bg='white')
        label_name.grid(row=0,column=2,padx=2,pady=7,sticky=W)
        id_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_name,font=('arial',11,'bold'),width=18)
        id_entry.grid(row=0,column=3,padx=2,pady=7,sticky=W)

        #Division
        label_Division=Label(std_lbl_class_frame,text='Division: ',font=('arial',12,'bold'),bg='white')
        label_Division.grid(row=1,column=0,padx=2,pady=7,sticky=W)
        com_Division=ttk.Combobox(std_lbl_class_frame,textvariable=self.var_div,font=('arial',12,'bold'),width=13,state='readonly')
        com_Division['values']=('Select Division','S','A','B','C','D','E','P','F')
        com_Division.current(0)
        com_Division.grid(row=1,column=1,padx=2,pady=7,sticky=W)

        #Roll
        label_roll=Label(std_lbl_class_frame,text='Roll:',font=('arial',12,'bold'),bg='white')
        label_roll.grid(row=1,column=2,padx=2,pady=7,sticky=W)
        roll_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_roll,font=('arial',11,'bold'),width=11)
        roll_entry.grid(row=1,column=3,padx=2,pady=7,sticky=W)

        #Gender
        label_Gender=Label(std_lbl_class_frame,text='Gender: ',font=('arial',12,'bold'),bg='white')
        label_Gender.grid(row=2,column=0,padx=2,pady=7,sticky=W)
        com_Gender=ttk.Combobox(std_lbl_class_frame,textvariable=self.var_gender,font=('arial',12,'bold'),width=12,state='readonly')
        com_Gender['values']=('Select Gender','Male','Female','Transgender')
        com_Gender.current(0)
        com_Gender.grid(row=2,column=1,padx=2,pady=7,sticky=W)

        #Date of Birth
        label_Dob=Label(std_lbl_class_frame,text='Dob:',font=('arial',12,'bold'),bg='white')
        label_Dob.grid(row=2,column=2,padx=1,pady=5,sticky=W)
        Dob_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_dob,font=('arial',11,'bold'),width=18)
        Dob_entry.grid(row=2,column=3,padx=1,pady=5,sticky=W)

        #Phone
        label_Phone=Label(std_lbl_class_frame,text='Phone:',font=('arial',12,'bold'),bg='white')
        label_Phone.grid(row=3,column=0,padx=2,pady=5,sticky=W)
        Phone_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_phno,font=('arial',11,'bold'),width=10)
        Phone_entry.grid(row=3,column=1,padx=2,pady=6,sticky=W)


        #Email
        label_Email=Label(std_lbl_class_frame,text='Email:',font=('arial',12,'bold'),bg='white')
        label_Email.grid(row=3,column=2,padx=2,pady=6,sticky=W)
        Email_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_email,font=('arial',11,'bold'),width=22)
        Email_entry.grid(row=3,column=3,padx=2,pady=6,sticky=W)

        #Teacher
        label_Teacher=Label(std_lbl_class_frame,text='Teacher:',font=('arial',12,'bold'),bg='white')
        label_Teacher.grid(row=4,column=0,padx=2,pady=6,sticky=W)
        Teacher_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_teacher,font=('arial',11,'bold'),width=15)
        Teacher_entry.grid(row=4,column=1,padx=2,pady=6,sticky=W)

        #Address
        label_Address=Label(std_lbl_class_frame,text='Address:',font=('arial',12,'bold'),bg='white')
        label_Address.grid(row=4,column=2,padx=2,pady=5,sticky=W)
        Address_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_address,font=('arial',11,'bold'),width=30)
        Address_entry.grid(row=4,column=3,padx=2,pady=6,sticky=W)

        #Button Frame
        button_frame=Frame(dataleftframe,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=10,y=500,width=600,height=40)
        
        btn_add=Button(button_frame,text='Add',font=('arial',12,'bold'),width=14,bg='green',fg='white',cursor='hand2')
        btn_add.grid(row=0,column=0,sticky=W,padx=1)

        btn_update=Button(button_frame,text='Update',command=self.update_data,font=('arial',12,'bold'),width=14,bg='blue',fg='white',cursor='hand2')
        btn_update.grid(row=0,column=1,sticky=W,padx=1)

        btn_delete=Button(button_frame,text='Delete',font=('arial',12,'bold'),width=14,bg='red',fg='white',cursor='hand2')
        btn_delete.grid(row=0,column=2,sticky=W,padx=1)

        btn_reset=Button(button_frame,text='Reset',font=('arial',12,'bold'),width=14,bg='yellow',fg='white',cursor='hand2')
        btn_reset.grid(row=0,column=3,sticky=W,padx=1)




        #create right frame
        datarightframe=LabelFrame(manage_frame,bd=4,relief=RIDGE,padx=2,text='Student Details',font=('times new roman',15,'bold'),fg='green',bg='white')
        datarightframe.place(x=640,y=10,width=860,height=600)

        img_6=Image.open(r'college_images\photo.png')
        img_6=img_6.resize((840,150),Image.ANTIALIAS) #convert high level image to low level image
        self.photoimg_6=ImageTk.PhotoImage(img_6)

        my_image1=Label(datarightframe,image=self.photoimg_6,bd=2,relief=RIDGE,bg='white')
        my_image1.place(x=5,y=5,width=840,height=150)

        search_frame=LabelFrame(datarightframe,bd=4,relief=RIDGE,padx=2,text='Search Student Details',font=('times new roman',15,'bold'),fg='magenta',bg='white')
        search_frame.place(x=5,y=160,width=840,height=65)

        #search by 
        search_by=Label(search_frame,text='Search by: ',font=('arial',11,'bold'),fg='red',bg='green')
        search_by.grid(row=0,column=0,sticky=W,padx=2,pady=7)

        com_search=ttk.Combobox(search_frame,font=('arial',12,'bold'),width=20,state='readonly')
        com_search['values']=('Select Option','Roll','Phone','Student_id')
        com_search.current(0)
        com_search.grid(row=0,column=1,padx=2,pady=7,sticky=W)

        txt_search=ttk.Entry(search_frame,font=('arial',11,'bold'),width=25)
        txt_search.grid(row=0,column=2,padx=2,pady=7,sticky=W)

        #button key

        btn_Search=Button(search_frame,text='Search',font=('arial',12,'bold'),width=15,bg='blue',fg='white',cursor='hand2')
        btn_Search.grid(row=0,column=3,sticky=W,padx=1)

        btn_Showall=Button(search_frame,text='Showall',font=('arial',12,'bold'),width=15,bg='cyan',fg='black',cursor='hand2')
        btn_Showall.grid(row=0,column=4,sticky=W,padx=1)

        #=====================Student table=========================

        table_frame=Frame(datarightframe,bd=4,relief=GROOVE)
        table_frame.place(x=5,y=230,width=840,height=305)

        #create scroll
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=('dep','course','year','sem','id','name','div','roll','gender','dob','email','ph_no','address','teacher',),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set) 
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('dep',text='Department')
        self.student_table.heading('course',text='Course')
        self.student_table.heading('year',text='Year')
        self.student_table.heading('sem',text='Semester')
        self.student_table.heading('id',text='Student_id')
        self.student_table.heading('div',text='Division')
        self.student_table.heading('name',text='Name')
        self.student_table.heading('roll',text='Roll no')
        self.student_table.heading('gender',text='Gender')
        self.student_table.heading('dob',text='DOB')
        self.student_table.heading('email',text='Email')
        self.student_table.heading('ph_no',text='Phone')
        self.student_table.heading('address',text='Address')
        self.student_table.heading('teacher',text='Teacher')

        self.student_table['show']='headings'

        self.student_table.column('dep',width=100)
        self.student_table.column('course',width=100)
        self.student_table.column('year',width=100)
        self.student_table.column('sem',width=100)
        self.student_table.column('id',width=100)
        self.student_table.column('div',width=100)
        self.student_table.column('name',width=100)
        self.student_table.column('roll',width=100)
        self.student_table.column('gender',width=100)
        self.student_table.column('dob',width=100)
        self.student_table.column('email',width=100)
        self.student_table.column('ph_no',width=100)
        self.student_table.column('address',width=100)
        self.student_table.column('teacher',width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind('<ButtonRelease>',self.get_cursor) #for binding
        self.fetch_data()
    

  
   #Fetch Function

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='sdms')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from student')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #Get_Cursor Function

    def get_cursor(self,event=''): #for binding the cursor with table
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        data=content['values']
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_id.set(data[4])
        self.var_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phno.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])

    #Update Function

    def update_data(self):
        if self.var_dep.get()=='' or self.var_name.get()=='' or self.var_id.get()=='':
            messagebox.showerror('Error','Add all data!!')
        else:
            try:
                update=messagebox.askyesno('Update','Are you Sure to update this student data',parent=self.root)
                if update>0:
                   conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='sdms')
                   my_cursur=conn.cursor()
                   my_cursur.execute("update student set dep=%s,course=%s,year=%s,semester=%s,stu_name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,ph_no=%s,address=%s,teacher=%s where student_id=%s",(    
                                                                                                                                                              self.var_dep.get(),
                                                                                                                                                              self.var_course.get(),
                                                                                                                                                              self.var_year.get(),
                                                                                                                                                              self.var_sem.get(),
                                                                                                                                                              self.var_name.get(),
                                                                                                                                                              self.var_div.get(),
                                                                                                                                                              self.var_roll.get(),
                                                                                                                                                              self.var_gender.get(),
                                                                                                                                                              self.var_dob.get(),
                                                                                                                                                              self.var_email.get(),
                                                                                                                                                              self.var_phno.get(),
                                                                                                                                                              self.var_address.get(),
                                                                                                                                                              self.var_teacher.get(),
                                                                                                                                                              self.var_id.get()
                                                                                                    
                                                                                                                                                            
                                                                                                                                                              
                                                                                                                                                              ))
                

                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo('Success','Student Successfully Updated',parent=self.root)
            except Exception as es:
                messagebox.showerror('error',f"due to:{str(es)}",parent=self.root)





if __name__=='__main__':
    root=Tk() #toolkit
    obj=Student(root)
    root.mainloop()



