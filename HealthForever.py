
from tkinter import *
from tkinter import messagebox
from sqlite3 import *
import re
import requests as r
import bs4 as b

class Rajat:

    def __init__(s):
        global num
        num=0
        s.num=num
        global count
        count=0
        s.count=count
        s.con=connect("mydata.db")
        s.scr=Tk()
        s.scr.geometry('1200x800+0+0')
        try:
            global cu
            s.cu=s.con.cursor()
            s.cu.execute("create table user(name varchar(50),password varchar(20),email varchar(100))")
            s.con.commit()
        except:
            pass
        s.login()

    def login(s):
        s.scr.title("login page")
        l=Label(s.scr,text="Medical Assistant",font=('default',40,'bold'),bg='#E8E8E8',fg='dark blue')
        l.pack(side=TOP,fill=X)
        f=Canvas(s.scr)
        i=PhotoImage(file='n:/pills-png-33140.png')
        f.create_image(600,400,image=i)
        f.pack(fill=BOTH,expand=120)
        l1=Label(f,text='Username',font=('times',20,'bold'),bg='white',fg='black')
        l1.place(x=200,y=100)
        l2=Label(f,text='Password',font=('times',20,'bold'),bg='white',fg='black')
        l2.place(x=200,y=200)
        u=Entry(f,font=('times',20,'bold'),bg='#F5F5F5')
        u.place(x=350,y=100)
        p=Entry(f,show='*',font=('times',20,'bold'),bg='#F5F5F5')
        p.place(x=350,y=200)
        b=Button(f,text='Register',font=('times',15,'bold'),command=s.register)
        b.place(x=400,y=300)
        b1=Button(f,text='Login',font=('times',15,'bold'),command=lambda :s.logpage(u.get(),p.get()))
        b1.place(x=550,y=300)
        s.scr.mainloop()
        
    def logpage(s,u,p):
        global d
        d=s.cu.execute('select count(*) from user where name=%r and password=%r'%(u,p))
        if list(d)[0][0]!=0:
            if s.num==0:
                s.scr.destroy()
                s.num+=1
            else:
                pass
            root=Tk()
            root.title('search page')
            root.geometry('1200x800+0+0')
            l=Label(root,text="Medical Assistant",font=('default',40,'bold'),bg='#E8E8E8',fg='dark blue')
            l.pack(side=TOP,fill=X)
            f=Canvas(root)
            i=PhotoImage(file='n:/pills-png-33140.png')
            f.create_image(600,400,image=i)
            f.pack(fill=BOTH,expand=120)
            global mn
            mn=Entry(f,font=('times',30,'bold'),bg='light grey',fg='black')
            mn.place(x=398,y=100)
            b1=Button(f,text='Go',font=('times',20,'bold'),bg='#F5F5F5',command=lambda :s.Info(mn.get()))
            b1.place(x=565,y=200)
            root.mainloop()        
        else:
            messagebox.showinfo("login","invalid credentials")
            
    def register(s):
        s.scr.destroy()
        global t1
        t1=Tk()
        t1.geometry('1200x800+0+0')
        t1.title("registeration page")
        l=Label(t1,text="Medical Assistant",font=('default',40,'bold'),bg='#E8E8E8',fg='dark blue')
        l.pack(side=TOP,fill=X)
        
        f=Canvas(t1)
        i=PhotoImage(file='n:/pills-png-33140.png')
        k=Label(f,image=i)
        k.i=i
        k.pack()
        f.pack(fill=BOTH,expand=120)
        l1=Label(f,text='Username',font=('times',20,'bold'),bg='white',fg='black')
        l1.place(x=200,y=100)
        l2=Label(f,text='Password',font=('times',20,'bold'),bg='white',fg='black')
        l2.place(x=200,y=150)
        u=Entry(f,font=('times',20,'bold'),bg='#F5F5F5')
        u.place(x=450,y=100)
        p=Entry(f,show='*',font=('times',20,'bold'),bg='#F5F5F5')
        p.place(x=450,y=150)
        l3=Label(f,text='Reype password',font=('times',20,'bold'),bg='white',fg='black')
        l3.place(x=200,y=200)
        rp=Entry(f,show='*',font=('times',20,'bold'),bg='#F5F5F5')
        rp.place(x=450,y=200)
        l4=Label(f,text='Email ID',font=('times',20,'bold'),bg='white',fg='black')
        l4.place(x=200,y=250)
        ei=Entry(f,font=('times',20,'bold'),bg='#F5F5F5')
        ei.place(x=450,y=250)
        b=Button(f,text='Submit',font=('times',15,'bold'),command=lambda :s.check(u.get(),p.get(),ei.get(),rp.get()))
        b.place(x=650,y=320)
        f.pack(fill=BOTH,expand=120)
        t1.mainloop()
    
    def check(s,u,p,ei,rp):
        global alrd
        alrd=Label(t1,text='Email ID already taken',font=('times',20),bg='white')
        global l5
        l5=Label(t1,text='Invalid Email ID',font=('times',20),bg='white')
        global l6
        l6=Label(t1,text='Incorrect password',font=('times',20),bg='white')
        d=('select count(*) from user where email=?')
        srch=s.cu.execute(d,[(ei)])
        if (srch.fetchall())[0][0]==0:
            alrd.config(text='')
            alrd.place(x=750,y=322)
            if len(re.findall(r"[\w|_|.|'@']+@\w+[.]\w{2,3}$",ei))!=0:
                l5.config(text='')
                l5.place(x=750,y=322)
                if p==rp:
                    l6.config(text='')
                    inst=("insert into user (name,password,email) values(?,?,?)")
                    insrt=s.cu.execute(inst,[(u),(p),(ei)])
                    l6.place(x=750,y=270)
                    t1.destroy()
                    s.scr=Tk()
                    s.scr.geometry('1200x800+0+0')
                    s.login()
                    
                else:
                    l6.place(x=750,y=270)
                    pass
            else:
                l5.place(x=750,y=322)
                pass
        else:
            alrd.place(x=750,y=322)
            pass
        s.con.commit()
    def Info(s,mn):
        try:
            if s.count==0:
                global screen
                screen=Tk()
            else:
                screen.destroy()
                screen=Tk()
            screen.title("Info")
            screen.geometry('800x500+0+0')
            dt=r.request('get','https://www.1mg.com/search/all?name=%s'%mn)
            s1=b.BeautifulSoup(dt.text,'html.parser')
            s.count+=1
            i=list(s1.findAll('div',{'class':'col-md-3 col-sm-4 col-xs-6 style__container___jkjS2'}))[s.count]
            try:
                dts=r.request('get','https://www.1mg.com'+i.find('a').get('href'))
                s1=b.BeautifulSoup(dts.text,'html.parser')
                l=Label(screen,text="Medical Assistant",font=('default',40,'bold'),bg='#E8E8E8',fg='dark blue')
                l.pack(side=TOP,fill=X)
                global f
                f=Canvas(screen,bg='white')
                t=Text(f)
                t.insert(END,str(s1.find('div',{'class':'ProductDescription__product-description___1PfGf'}).text))
                t.pack()
                b2=Button(f,text='Next>',font=('times',20,'bold'),command=lambda:s.Info(mn))
                b2.place(x=600,y=300)
                f.pack(fill=BOTH,expand=120)
            except:
                s.Info(mn)
                pass
        except:
            s.count=0
            s.Info(mn)
Rajat()
