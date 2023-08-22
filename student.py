from tkinter import *
from tkinter import ttk

from PIL import Image,ImageTk #for image showing
class Student:
    def __init__(self,root):  #constructor initialize
        self.root=root
        self.root.geometry('2400x1000+0+0') #for window display
        self.root.title('STUDENT MANGEMENT SYSTEM')
        #1st image
        img=Image.open(r'college_images\7th.jpg')
        img=img.resize((600,160),Image.ANTIALIAS) #convert high level image to low level image
        self.photoimg=ImageTk.PhotoImage(img)
        
        self.btn_1=Button(self.root,image=self.photoimg,cursor='hand2')
        self.btn_1.place(x=0,y=0,width=600,height=160)

        #2nd image
        img_2=Image.open(r'college_images\3rd.jpg')
        img_2=img_2.resize((600,160),Image.ANTIALIAS) #convert high level image to low level image
        self.photoimg_2=ImageTk.PhotoImage(img_2)
        
        self.btn_2=Button(self.root,image=self.photoimg_2,cursor='hand2')
        self.btn_2.place(x=600,y=0,width=600,height=160)

        #3rd image
        img_3=Image.open(r'college_images\9th.jpg')
        img_3=img_3.resize((600,160),Image.ANTIALIAS) #convert high level image to low level image
        self.photoimg_3=ImageTk.PhotoImage(img_3)
        
        self.btn_3=Button(self.root,image=self.photoimg_3,cursor='hand2')
        self.btn_3.place(x=1200,y=0,width=600,height=160)

        #background image
        img_4=Image.open(r'college_images\university.jpg')
        img_4=img_4.resize((2400,1000),Image.ANTIALIAS) #convert high level image to low level image
        self.photoimg_4=ImageTk.PhotoImage(img_4)

        bg_label=Label(self.root,image=self.photoimg_4,bd=2,relief=RIDGE)
        bg_label.place(x=0,y=160,width=2400,height=1000)

        #label title

        lbl_title=Label(bg_label,text='STUDENT MANAGEMENT SYSTEM',relief=GROOVE, font=('times new roman',37,'bold'),fg='red',bg='yellow')
        lbl_title.place(x=0,y=0,width=2000,height=50)

        #create frame

        frame=Frame(bg_label,bd=2,relief=RIDGE,bg='white')
        frame.place(x=15,y=55,width=1500,height=790)

        #create student manage frame
        manage_frame=Frame(bg_label,bd=2,relief=RIDGE,bg='white')
        manage_frame.place(x=15,y=55,width=500,height=790)
        #creating left frame for student information

        dataleftframe=Label(manage_frame,relief=GROOVE,text='Student information',font=('times new roman',20,'bold'),fg='blue',bg='white')
        #dataleftframe.place(x=10,y=10,width=400,height=790)
        dataleftframe.grid(row=0,columnspan=2,pady=20)
       
      




        



if __name__=='__main__':
    root=Tk() #toolkit
    obj=Student(root)
    root.mainloop()



