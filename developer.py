# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 00:50:05 2021

@author: amitr
"""

from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk



class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1570x800+0+0")
        self.root.title("Face Recognition System")

        img = Image.open((r"clg_img\university1.jpg"))
        img = img.resize((100,100),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)


        #bg_image
        img1 = Image.open((r"clg_img\university.jpg"))
        img1 = img1.resize((1570,800),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=0,width=1570,height=800)

        #first label
        f_lbl = Label(bg_img,image=self.photoimg)
        f_lbl.place(x=1400,y=0,width=100,height=100)

        title_lbl = Label(bg_img,text="Developer",font=("time new roman",20,"bold"),fg="black")
        title_lbl.place(x=150,y=0,width=1200,height =45)

        #main label frame
        main_frame = Frame(bg_img,bd=2)
        main_frame.place(x=150,y=100,width=1200,height=630)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="First Developer",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=600,height=610)

        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Second Developer ",font=("times new roman",12,"bold"))
        Right_frame.place(x=620,y=10,width=560  ,height=610)

        f_lbl_left = Label(Left_frame,text="Amit Roy")
        f_lbl_left.place(x=10,y=0,width=500,height=40)

        f_lbl_right = Label(Right_frame,text="Khushi Tiwari")
        f_lbl_right.place(x=10,y=0,width=500,height=40)
        
        f1_lbl_left = Label(Left_frame,text="Amitroy3.ar@gmail.com")
        f1_lbl_left.place(x=10,y=60,width=500,height=40)

        f1_lbl_right = Label(Right_frame,text="rajatiwari95143@gmail.com")
        f1_lbl_right.place(x=10,y=60,width=500,height=40)
        
        f2_lbl_left = Label(Left_frame,text="+91 9990947679")
        f2_lbl_left.place(x=10,y=120,width=500,height=40)
        
        f2_lbl_right = Label(Right_frame,text="+91 7982247538")
        f2_lbl_right.place(x=10,y=120,width=500,height=40)

if __name__=="__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()