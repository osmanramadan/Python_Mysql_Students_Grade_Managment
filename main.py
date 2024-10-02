from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import font
from tkinter import messagebox
import webbrowser




class login:

    def start_gui(self,root):

        root.geometry("750x500+450+100")
        root.title("school system")
        root.resizable(False,False)
        root.config(bg="#1A5276")
        label1=Label(root,text="school system",bg="black",fg="#F1C40F",font=("Georgia",20))
        label1.pack(fill=X)
        frame1=Frame(root,bg="#1A5276")
        frame1.place(x=490,y=38,width=260,height=500)

        face_url="facebook.com"
        tele_url="telegram.com"
        you_url="https://www.youtube.com/watch?v=o5PdVuV-DeA"
        def ac1():
            webbrowser.open_new_tab(face_url)
        def ac2():
             webbrowser.open_new_tab(tele_url)
        def ac3():
            webbrowser.open_new_tab(you_url)

        def about_developer():
            messagebox.showinfo("about developer","osman ramadan")

        def about_project():
             messagebox.showinfo("about project","")  


    
        b1=Button(frame1,text="حسابنا على الفيس",height=2,fg="black",font=("fancay",18),width=257,relief=GROOVE,activebackground="#1A5276",activeforeground="yellow",command=ac1)
        b2=Button(frame1,text="حسابنا علي علي التليجرام",height=2,fg="black",font=("fancay",18),width=257,relief=GROOVE,activebackground="#1A5276",activeforeground="yellow",command=ac2)
        b3=Button(frame1,text="حسابنا علي اليوتيوب",fg="black",height=2,font=("fancay",18),width=257,relief=GROOVE,activebackground="#1A5276",activeforeground="yellow",command=ac3)
        b4=Button(frame1,text="لمحةعن المطور",fg="black",height=2,font=("fancay",18),width=257,relief=GROOVE,activebackground="#1A5276",activeforeground="yellow",command=about_developer)
        b5=Button(frame1,text="لمحة عن المشروع",fg="black",height=2,font=("fancay",18),width=257,relief=GROOVE,activebackground="#1A5276",activeforeground="yellow",command=about_project)
        b6=Button(frame1,text="اغلاق البرنامج",fg="black",height=3,font=("fancay",18),width=257,relief=GROOVE,activebackground="#1A5276",activeforeground="yellow",command=quit)
        b1.pack()
        b2.pack()
        b3.pack()
        b4.pack()
        b5.pack()
        b6.pack()


        user=StringVar()
        passw=StringVar()
        # image1=PhotoImage(file='bg.png')
        # lab=Label(root,image=image1)
        # lab.place(x=30,y=38,width=500,height=300)
        login=Label(root,text="enroll",bg="black",fg="white",font=("Georgia",20),width=30,height=1)
        login.place(x=2,y=338)
        lablo=Label(root,text="username:",fg="black",bg="white",font=("Georgia",15,font.BOLD))
        lablo.place(x=3,y=390)

        ent1=Entry(root,fg="blue",textvariable=user,bg="white",font=("Georgia",15))
        ent1.place(x=150,y=390)
        lablo=Label(root,text="password:",fg="black",bg="white",font=("Georgia",15,font.BOLD))
        lablo.place(x=3,y=430)
        ent2=Entry(root,show='*',fg="blue",textvariable=passw,bg="white",font=("Georgia",15))
        ent2.place(x=150,y=430)

        #authintation
        username="root"
        password="root"
        def pass_or_not():
            if user.get()==username and passw.get()==password:

                designwindow(root,title="students grade")
                               
            else:
                messagebox.showinfo("not allowed","not allowed to enter")
        blo=Button(root,text="login",fg="white",font=("fancay",18),bg="red",height=2,relief=GROOVE,activebackground="#1A5276",activeforeground="yellow",command=pass_or_not)
        blo.place(x=1,y=460,width=490,height=38)   
        root.mainloop()


class designwindow:
    def __init__(self,root,title):
          # main of window
          self.root=root
          self.root.title(title)
          self.root.geometry("1350x690+0+0")
          self.root.config(background="silver")
          # variables
          self.Col1=StringVar()
          self.Col2=StringVar()
          self.Col3=StringVar()
          self.Col4=StringVar()
          self.Col5=StringVar()
          self.Col6=StringVar()
          self.Col7=StringVar()
          self.Col8=StringVar()
          self.Col9=StringVar()
          self.Col10=StringVar()
          self.Col11=StringVar()
          self.Col12=StringVar()
          self.Col13=StringVar()
          self.Col14=StringVar()
          self.Col15=StringVar()
          self.Col16=StringVar()
          self.Col17=StringVar()
          self.add=StringVar()
          self.gen=StringVar()
          self.cert=StringVar()
          self.ph=StringVar()
          self.ema=StringVar()
          self.name=StringVar()
          self.num=StringVar()
          self.delete=StringVar()
          self.intr_search=StringVar()
          self.select_search=StringVar()

          # frames
          ###########################  the First frame ######################################
          frame1=Frame(self.root,background="white")
          frame1.place(x=1130,y=1,width=290,height=700)

          Col1=Label(frame1,text="الرقم التسلسلي")
          Col1.pack()
          Col1_input=Entry(frame1,bd="3",textvariable=self.Col1)
          Col1_input.pack()
          
          Col2=Label(frame1,text="الاسم")
          Col2.pack()
          Col2_input=Entry(frame1,bd="3",textvariable=self.Col2)
          Col2_input.pack()

          Col3=Label(frame1,text="Grade")
          Col3.pack()
          Col3_input=Entry(frame1,bd="3",textvariable=self.Col3)
          Col3_input.pack()

          Col4=Label(frame1,text="تقييم قصير_1")
          Col4.pack()
          Col4_input=Entry(frame1,bd="3",textvariable=self.Col4)
          Col4_input.pack()

          
          Col5=Label(frame1,text="تقييم قصير_2")
          Col5.pack()
          Col5_input=Entry(frame1,bd="3",textvariable=self.Col5)
          Col5_input.pack()

          
          Col6=Label(frame1,text="تقييم قصير_3")
          Col6.pack()
          Col6_input=Entry(frame1,bd="3",textvariable=self.Col6)
          Col6_input.pack()

          
          Col7=Label(frame1,text="تقييم قصير_4")
          Col7.pack()
          Col7_input=Entry(frame1,bd="3",textvariable=self.Col7)
          Col7_input.pack()

          
          Col8=Label(frame1,text="تقييم قصير_5")
          Col8.pack()
          Col8_input=Entry(frame1,bd="3",textvariable=self.Col8)
          Col8_input.pack()

          
          Col9=Label(frame1,text="تقييم قصير_6")
          Col9.pack()
          Col9_input=Entry(frame1,bd="3",textvariable=self.Col9)
          Col9_input.pack()


          ##### the sub first frame #######
          subframe1=Frame(self.root,background="white")
          subframe1.place(x=1480,y=1,width=240,height=700)
          Col15=Label(subframe1,text='درجة NSIS')
          Col15.pack()
          Col15_input=Entry(subframe1,bd="3",textvariable=self.Col15)
          Col15_input.pack()

          Col16=Label(subframe1,text='phone')
          Col16.pack()
          Col16_input=Entry(subframe1,bd="3",textvariable=self.Col16)
          Col16_input.pack()

          Col17=Label(subframe1,text='id')
          Col17.pack()
          Col17_input=Entry(subframe1,bd="3",textvariable=self.Col17)
          Col17_input.pack()
          subframe1.place(x=900,y=1,width=230,height=700)

          Col10=Label(subframe1,text="الواجبات")
          Col10.pack()
          Col10_input=Entry(subframe1,bd="3",textvariable=self.Col10)
          Col10_input.pack()

          Col11=Label(subframe1,text='المشروع')
          Col11.pack()
          Col11_input=Entry(subframe1,bd="3",textvariable=self.Col11)
          Col11_input.pack()

          
          Col12=Label(subframe1,text='المشاركة الصفية')
          Col12.pack()
          Col12_input=Entry(subframe1,bd="3",textvariable=self.Col12)
          Col12_input.pack()

          Col13=Label(subframe1,text='التقييمات القصيرة')
          Col13.pack()
          Col13_input=Entry(subframe1,bd="3",textvariable=self.Col13)
          Col13_input.pack()

          Col14=Label(subframe1,text='المجموع')
          Col14.pack()
          Col14_input=Entry(subframe1,bd="3",textvariable=self.Col14)
          Col14_input.pack()

          del_student=Label(subframe1,text="id حذف الطالب بواسطة")
          del_student.pack()
          del_student_input=Entry(subframe1,bd="3",textvariable=self.delete)
          del_student_input.pack()


          ###########################  the second frame #################################
          frame2=Frame(self.root)
          frame2.place(x=920,y=465,width=400,height=240)    
          la1=Label(frame2,text="لوحة التحكم",font=("monoface",14),fg="white",background="blue")
          la1.pack(fill=X)
          ########################### Starting buttons   #################################
          bn1_del=Button(frame2,text="حذف الطالب",width=40,background="#2980B9",command=self.delete_id)
          bn1_del.pack()
          bn2_update=Button(frame2,text="تحديث البيانات",width=40,background="#2980B9",command=self.update)
          bn2_update.pack()
          bn3_empty=Button(frame2,text="افراغ الحقول",width=40,background="#2980B9",command=self.clear)
          bn3_empty.pack()
          bn4_aboutus=Button(frame2,text="من نحن ",width=40,background="#2980B9",command=self.about_us)
          bn4_aboutus.pack()
          bn5_exit=Button(frame2,text=" الخروج من البرنامج",width=40,background="#2980B9",command=root.quit)
          bn5_exit.pack()
          bn6_insert=Button(frame2,text="اضافة طالب",width=40,background="#2980B9" ,command=self.add_student)
          bn6_insert.pack()         
          ##############################  Searching frame    ###############################
          search_frame=Frame(self.root,background="white")
          search_frame.place(x=1,y=2,width=900,height=100)
          search_label=Label(search_frame,text=": بالاسم البحث عن الطالب",font=("monospace",19),background="white")
          search_label.place(x=870,y=20,width=240,height=30)


          search_entry=Entry(search_frame,justify="center",bd=4,textvariable=self.intr_search)
          search_entry.place(x=610,y=23,height=35,width=150)
          but=Button(search_frame,text="ID بحث بواسطة",bg="blue",fg="white",command=self.search)
          but.place(x=490,y=23,height=35,width=120)
          but=Button(search_frame,text="عرض بيانات الطلاب",bg="blue",fg="white",command=self.fetchelements)
          but.place(x=355,y=23,height=35,width=120)
          # details frame students data
          detail=Frame(self.root,bg="white")
          detail.place(x=1,y=110,width=900,height=600)
          
          ###############################    Set up scroll   ############################
          scroll_x=Scrollbar(detail,orient=HORIZONTAL)
          scroll_y=Scrollbar(detail,orient=VERTICAL)

          ##############################     Treeview        ############################

          self.student_table=ttk.Treeview(detail,columns=("Col 1","Col 2","Col 3","Col 4","Col 5","Col 6","Col 7","Col 8","Col 9","Col 10","Col 11","Col 12","Col 13","Col 14","Col 15","Col 16","Col 17"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
          self.student_table.place(x=1,y=1,width=1670,height=600)
          scroll_x.pack(side=BOTTOM,fill=X)
          scroll_y.pack(side=LEFT,fill=Y)
          scroll_x.config(command=self.student_table.xview)
          scroll_y.config(command=self.student_table.yview)

          # the SHOW OF VIEWTREE 
          #  //////////////////////////////////////////  #/////////////////////   #///////////////////   #/////////
          self.student_table["show"]="headings"
          
          self.student_table.heading('Col 1',text="الرقم")
          self.student_table.heading('Col 2',text='الاسم')
          self.student_table.heading('Col 3',text='Grade')
          self.student_table.heading('Col 4',text='تقييم قصير_1') 
          self.student_table.heading('Col 5',text='تقييم قصير_2')
          self.student_table.heading('Col 6',text='تقييم قصير_3')
          self.student_table.heading('Col 7',text='تقييم قصير_4')
          self.student_table.heading('Col 8',text='تقييم قصير_5')
          self.student_table.heading('Col 9',text='تقييم قصير_6')
          self.student_table.heading('Col 10',text='الواجبات')
          self.student_table.heading('Col 11',text='المشروع')
          self.student_table.heading('Col 12',text='المشاركة الصفية')
          self.student_table.heading('Col 13',text='التقييمات القصيرة')
          self.student_table.heading('Col 14',text='المجموع')
          self.student_table.heading('Col 15',text='درجة NSIS')
          self.student_table.heading('Col 16',text='phone')
          self.student_table.heading('Col 17',text='id')

          self.student_table.column('Col 1',width=51)
          self.student_table.column('Col 2',width=51)
          self.student_table.column('Col 3',width=51)
          self.student_table.column('Col 4',width=51)
          self.student_table.column('Col 5',width=51)
          self.student_table.column('Col 6',width=51)
          self.student_table.column('Col 7',width=51)
          self.student_table.column('Col 8',width=51)
          self.student_table.column('Col 9',width=51)
          self.student_table.column('Col 10',width=51)
          self.student_table.column('Col 11',width=51)
          self.student_table.column('Col 12',width=51)
          self.student_table.column('Col 13',width=51)
          self.student_table.column('Col 14',width=51)
          self.student_table.column('Col 15',width=51)
          self.student_table.column('Col 16',width=51)
          self.student_table.column('Col 17',width=51)
          self.student_table.pack(fill=BOTH, expand=1)
          self.student_table.bind("<ButtonRelease-1>",self.curser_item)
          ######### calling the program    
          self.root.mainloop()
    def add_student(self):
            con=pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="students"
                    )
            cur=con.cursor()    
            cur.execute(f"""
                       INSERT INTO `arbic_students_degrees`(`COL 1`, `COL 2`, `COL 3`, `COL 4`, `COL 5`, `COL 6`, `COL 7`,
                         `COL 8`, `COL 9`, `COL 10`, `COL 11`, `COL 12`, `COL 13`, `COL 14`,
                         `COL 15`, `COL 16`, `COL 17`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        """
                        
              ,(
              self.Col1.get(),
              self.Col2.get(),
              self.Col3.get(),
              self.Col4.get(),
              self.Col5.get(),
              self.Col6.get(),
              self.Col7.get(),  
              self.Col8.get(),  
              self.Col9.get(),  
              self.Col10.get(),  
              self.Col11.get(),  
              self.Col12.get(),  
              self.Col13.get(),  
              self.Col14.get(), 
              self.Col15.get(), 
              self.Col16.get(), 
              self.Col17.get(),  
              ))
            con.commit()   
            self.fetchelements()
            con.close()
            
    def fetchelements(self):
        con=pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="students"
                  )
        cur=con.cursor()
        cur.execute("select * from arbic_students_degrees")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
              self.student_table.insert("",END,value=row)
            con.commit()
        con.close()
        
    def delete_id(self):
      con=pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="students"
      )
      cur=con.cursor()
      cur.execute(f"DELETE FROM `arbic_students_degrees` WHERE  `arbic_students_degrees`.`Col 17` =%s",self.delete.get())
      con.commit()
      self.fetchelements()
      con.close()
    def update(self):
      con=pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="students"
      )
      cur=con.cursor()
      cur.execute(f"""
      UPDATE `arbic_students_degrees`
      SET `COL 1` = %s, `COL 2` = %s, `COL 3` = %s, `COL 4` = %s, `COL 5` = %s, 
        `COL 6` = %s, `COL 7` = %s, `COL 8` = %s, `COL 9` = %s, `COL 10` = %s, 
        `COL 11` = %s, `COL 12` = %s, `COL 13` = %s, `COL 14` = %s, `COL 15` = %s, 
        `COL 16` = %s, `COL 17` = %s
      WHERE `COL 16` = %s
      """, (
      self.Col1.get(),
      self.Col2.get(),
      self.Col3.get(),
      self.Col4.get(),
      self.Col5.get(),
      self.Col6.get(),
      self.Col7.get(),
      self.Col8.get(),
      self.Col9.get(),
      self.Col10.get(),
      self.Col11.get(),
      self.Col12.get(),
      self.Col13.get(),
      self.Col14.get(),
      self.Col15.get(),
      self.Col16.get(),
      self.Col17.get(),
      self.Col16.get()  # Assuming you need to match the ID field for update
    ))

      con.commit()
      self.fetchelements()
      con.close()
    def clear(self):
          self.Col1.set('')
          self.Col2.set('')
          self.Col3.set('')
          self.Col4.set('')
          self.Col5.set('')
          self.Col6.set('')
          self.Col7.set('')
          self.Col8.set('')
          self.Col9.set('')
          self.Col10.set('')
          self.Col11.set('')
          self.Col12.set('')
          self.Col13.set('')
          self.Col14.set('')
          self.Col15.set('')
          self.Col16.set('')
          self.Col17.set('')
    def about_us(self):
        messagebox.showinfo("by osman  ramadan","the name of school")
    def search(self):
        con=pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="students"
      )
        cur=con.cursor()

        cur.execute(f"SELECT * FROM `arbic_students_degrees` WHERE `Col 16` like %s",self.intr_search.get())
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
              self.student_table.insert("",END,values=row)           
            con.commit()
        con.close()

    def curser_item(self, event):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        row = content['values']
        # Set entry fields based on selected row
        self.Col1.set(row[0])
        self.Col2.set(row[1])
        self.Col3.set(row[2])
        self.Col4.set(row[3])
        self.Col5.set(row[4])
        self.Col6.set(row[5])
        self.Col7.set(row[6])
        self.Col8.set(row[7])
        self.Col9.set(row[8])
        self.Col10.set(row[9])
        self.Col11.set(row[10])
        self.Col12.set(row[11])
        self.Col13.set(row[12])
        self.Col14.set(row[13])
        self.Col15.set(row[14])
        self.Col16.set(row[15])
        self.Col17.set(row[16])

root=Tk()

login=login()
login.start_gui(root)
