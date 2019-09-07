from tkinter import *
#from custumpage import *
#from hackthon1 import *
import pandas as pd
import datetime
import time
from tkinter import messagebox

def Admin():
    def command2(event):
        if entry1.get() == 'user' and entry2.get() == 'pass':
            root.deiconify()
            top.destroy()

    def command1():
       if entry1.get() != 'praveen' or entry2.get() != 'pass':
           r=Tk()
           q=Label(r,text="wrong")
           q.pack()
       if entry1.get() == 'praveen' and entry2.get() == 'pass':
           #root.deiconify()
           #top.destroy()
           top.destroy()
           root.destroy()
           #sys.exit()
           #m=Tk()
           page()
           #w.pack()
        
    root = Tk()
    #root.bind('<Return>',Admin())
    top = Toplevel()
    top.geometry('300x260')
    top.title('LOGIN SCREEN')
    top.configure(background='white')
    #photo2 = PhotoImage(file='lock.gif')
    #photo = Label(top,image=photo2, bg='white')
    lbl1 = Label(top, text = 'Username:', font = {'Helvetica',10})
    entry1 = Entry(top)
    lbl2 = Label(top, text = 'Password:', font = {'Helvetica',10})
    entry2 = Entry(top, show = "*")
    button2 = Button(top,text='enter', command=lambda:command1())
    lbl3 = Label(top, text = '@Copyright Login screen 2019..', font = {'Arial',7})
    entry2.bind('<Return>', command1)
    #photo.pack()
    lbl1.pack()
    entry1.pack()
    lbl2.pack()
    entry2.pack()
    button2.pack()
    lbl3.pack()

    root.title('Main Screen')
    root.configure(background='black')
    root.geometry('855x650')
    root.withdraw()
    root.mainloop()

def page():
    global staff_name
    def submit():
        c=datetime.datetime.now()
        day=c.strftime('%A')
        
        df = pd.read_excel("sheet2.xlsx", sheet_name= day.lower())

        t=time.localtime()
        x=time.strftime('%H:%M', t)
        #y="11:30"                                       # TIME
        y=list(x.split(":"))
        #y=x
        if int('08')>int(y[0]) or int(y[0])>=int('15'):
            messagebox.showerror("Error","not available,please comeback in working hours")

        if int('08')<=int(y[0])<int('09'):
            r="08:00-09:00"
        elif int('09')<=int(y[0])<int('10'):
            r="09:00-10:00"
        elif int('10')<=int(y[0])<int('11'):
            if int('00')<=int(y[1])<int('15'):
                r="10:00-10:15"
            else:
                r="10:15-11:15"
        elif int('11')<=int(y[0])<int('12'):
            if int('15')<=int(y[1])<=int('59'):
                r="11:15-12:00"
            else:
                r="10:15-11:15"
        elif int('12')<=int(y[0])<int('13'):
            r="12:00-13:00"
        elif int('13')<=int(y[0])<int('14'):
            r="13:00-14:00"
        elif int('14')<=int(y[0])<int('15'):
            r="14:00-15:00"
        
        #print(df)
        #print(df.columns)

        df= df.set_index('sno')
        #sname=(staff_name.get()).upper()
        #print(df)
        #print(df.loc[r,staff_name.get()])
        l2=Label(w,text="Current Status:")
        l2.place(x=120,y=80)
        info=StringVar()
        e2=Entry(w,textvariable=info)
        e2.place(x=200,y=80)
        info.set(df.loc[r,staff_name.get()])

    def details(event):
        root=Tk()
    
        df3=pd.read_excel("Copy of FACULTY DATA(646).xlsx")
        df3=df3.set_index("FACULTY")
        l=list(df3.loc[e1.get()])
        #fra=Frame(root,height=25,width=25)
        #img=PhotoImage(file=r"D:\codes\car.png")
        #lab1=Label(root,image=img,height=150,width=150)
        root.geometry("400x400")
        #fra.grid(row=0, column=0)
        #lab1.grid(row=0, column=0)
        lab2=Label(root,text=e1.get(),font=("GEORGIA",14))
        lab3=Label(root,text=l[0],font=("ARIAL",10))
        lab4=Label(root,text=l[1],font=("ARIAL",10))
        lab5=Label(root,text=l[-1],font=("ARIAL",10))
        lab6=Label(root,text="CONTACT INFO:",font=("ARIAL",10))
        lab7=Label(root,text=l[3],font=("GEORGIA",10))
        lab8=Label(root,text=l[2],font=("GEORGIA",10))
        lab2.grid(row=2,column=1)
        lab3.grid(row=3,column=1)
        lab4.grid(row=4,column=1)
        lab5.grid(row=5,column=1)
        lab6.grid(row=6,column=1)
        lab7.grid(row=7,column=0)
        lab8.grid(row=7,column=2)
        root.mainloop()

        
    w=Tk()

    w.geometry("400x400")

    l1=Label(w, text="Name:")
    l1.place(x=50,y=0)
    global staff_name
    staff_name=StringVar()
    e1=Entry(w, textvariable=staff_name)
    e1.place(x=150,y=1)

    b1= Button(w, text="Submit", command=submit )
    b1.place(x=150, y=50)
    b2= Button(w, text="Custom", command=ff )
    b2.place(x=300, y=50)
    
    b3=Button(w,text="Details")
    b3.bind("<Button-1>",details)
    b3.place(x=200, y=50)

    mainloop()
def ff():
    def find():
        global staff_name
        #da=e1.get() # custom day name 
        df = pd.read_excel("sheet2.xlsx", sheet_name=(e1.get()).lower())
        #print(df)
        y=e2.get()
        y=list(y.split(":"))
        if int('08')<=int(y[0])<int('09'):
            r="08:00-09:00"
        elif int('09')<=int(y[0])<int('10'):
            r="09:00-10:00"
        elif int('10')<=int(y[0])<int('11'):
            if int('00')<=int(y[1])<int('15'):
                r="10:00-10:15"
            else:
                r="10:15-11:15"
        elif int('11')<=int(y[0])<int('12'):
            if int('15')<=int(y[1])<=int('59'):
                r="11:15-12:00"
            else:
                r="10:15-11:15"
        elif int('12')<=int(y[0])<int('13'):
            r="12:00-13:00"
        elif int('13')<=int(y[0])<int('14'):
            r="13:00-14:00"
        elif int('14')<=int(y[0])<int('15'):
            r="14:00-15:00"
              
            #print(df)
            #print(df.columns)

        df= df.set_index('sno')

            #print(df)
        print(df.loc[r,staff_name.get()])#here
        a=(df.loc[r,staff_name.get()])
        l2=Label(w,text="Staff Status:")
        l2.place(x=100,y=250)
        info=StringVar()
        e3=Entry(w,textvariable=info)
        e3.place(x=150,y=250)
        info.set(df.loc[r,staff_name.get()]) #here
        e3.insert(0,a)
        
    w=Tk()
    w.geometry("400x400")
    f=Frame(w,height=100,width=100)
    f.grid(row=0,column=0)
    l1=Label(w, text="day")
    l1.grid(row=0,column=1)
    #global D
    D=StringVar()
    e1=Entry(w, textvariable=D)
    e1.grid(row=0,column=2)
    l2=Label(w, text="time")
    l2.grid(row=1,column=1)

    T=StringVar()
    e2=Entry(w, textvariable=T)
    e2.grid(row=1,column=2)
    b1= Button(w, text="FETCH!", command=find )
    b1.grid(row=2, column=2)    

Admin()

#staff_name=""


    

