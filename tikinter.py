from tkinter import *
import sqlite3
#==========================================Database=================================================================
connection = sqlite3.connect('./users.db')
curser = connection.cursor()
sql = """
    CREATE TABLE IF NOT EXISTS user(
    name TEXT(60),
    family TEXT (60),
    password TEXT (60),
    email TEXT (60),
    is_login BOOLEAN
    );
"""
curser.execute(sql)
connection.commit()
#==========================================Tkinter==================================================================
root = Tk()
#==========Page main==========
root.title('Library Management')
root.geometry('600x374')
root.resizable(width=False,height=False)
root.iconbitmap('./icons/libraries_84323.ico')
root.configure(bg='#D5CEA3')

#===========Label=================
# label1=Label(root,bg='#1A120B',width=810,height=4)
# label1.place(x=0,y=0)
# label2=Label(root,text="Library Management",fg='#fafafa',font=('tahoma',17),bg='#1A120B')
# label2.place(x=270,y=15)
label3 = Label(root,text='Welcome to the Library Management',font=('tahoma',17),bg='#D5CEA3')
label3.place(x = 185,y=142)
label4 = Label(root,text='Register to get started',font=('tahoma',14),bg='#D5CEA3')
label4.place(x = 265,y=189)

label5=Label(root,bg='#3C2A21',width=21,height=374)
label5.place(x=0,y=0)
label6=Label(root,bg='#D5CEA3',width=17,height=12)
label6.place(x=13,y=80)
#==========Buttom=================
buttom1 = Button(root,text='Register',bg='#3C2A21',width=18,fg='#fafafa',height=3,border=0,command=lambda:sing_up())
buttom1.place(x = 10,y=68)
buttom2 = Button(root,text='Login',bg='#3C2A21',fg='#fafafa',width=18,height=3,border=0,command=lambda:log_in())
buttom2.place(x = 10,y=122)
buttom3 = Button(root,text='About',bg='#3C2A21',fg='#fafafa',width=18,height=3,border=0,command=lambda:information())
buttom3.place(x = 10,y=176)
buttom4 = Button(root,text='Contact us',bg='#3C2A21',fg='#fafafa',width=18,height=3,border=0,command=lambda:contact_us())
buttom4.place(x = 10,y=230)

#=============================================Buttom ming======================================
# Registration
def sing_up():
    git = Tk()
    git.title('Register')
    git.geometry('410x260')
    git.resizable(width=False, height=False)
    git.iconbitmap('./icons/libraries_84323.ico')
    git.configure(bg='#D5CEA3')
    entry1 = Entry(git,width=40,border=3)
    entry1.place(x=120, y=40)
    entry2 = Entry(git,width=40,border=3)
    entry2.place(x=120, y=85)
    entry3 = Entry(git,width=40,border=3)
    entry3.place(x=120, y=125)
    entry4 = Entry(git,width=40,border=3)
    entry4.place(x=120, y=165)
    labelg = Label(git, text='name:', font=('tahoma', 12),bg='#D5CEA3')
    labelg.place(x=15, y=37)
    labelg1 = Label(git, text='lastname:', font=('tahoma', 12),bg='#D5CEA3')
    labelg1.place(x=15, y=82)
    labelg2 = Label(git, text='email:', font=('tahoma', 12),bg='#D5CEA3')
    labelg2.place(x=15, y=122)
    labelg3 = Label(git, text='password:', font=('tahoma', 12),bg='#D5CEA3')
    labelg3.place(x=15, y=163)
    buttom3 = Button(git, text='Register', bg='#D06224', border=5, width=8,command=lambda:data(entry1, entry2, entry3, entry4))
    buttom3.place(x=210, y=210)

#===========Entering registration information in the database==========
def data(x,y,z,d):
    name = x.get()
    family = y.get()
    email = z.get()
    password = d.get()
    errors = {}
    error_count = 0
    if errors == {}:
        if len(name) < 3:
            errors['name'] = 'The name must be a maximum of 3 characters'
            error_count += 1
        if len(family) < 3:
            errors['family'] = 'The family must be a maximum of 3 characters'
            error_count += 1
        if email.find('@gmail.com') == -1:
            errors['email'] = 'The email is invalid'
            error_count += 1
        if len(password) < 8:
            errors['password'] = 'The password must be a maximum of 8 characters'
            error_count += 1
    if error_count == 0:
        curser.execute("INSERT INTO user (name,family,password,email,is_login) VALUES (?,?,?,?,?)",(name,family,password,email,1))
        connection.commit()
        git2 = Tk()
        git2.title('Library')
        git2.geometry('250x100')
        git2.configure(bg='#D5CEA3')
        git2.resizable(width=False, height=False)
        git2.iconbitmap('./icons/libraries_84323.ico')
        label6 = Label(git2, text='Registration was successful', font=('tahoma', 13), bg='#D5CEA3')
        label6.place(x=20, y=20)
        buttom4 = Button(git2, text='start', bg='#D06224', border=5, width=9, command=lambda: Page3(ps()))
        buttom4.place(x=80, y=60)
    else:
        git2 = Tk()
        git2.title('Library')
        git2.geometry('250x170')
        git2.resizable(width=False, height=False)
        git2.configure(bg='#D5CEA3')
        git2.iconbitmap('./icons/libraries_84323.ico')
        for error in errors:
            if error == 'name':
                x = errors['name']
                name_label = Label(git2, text=f'{x}', font=('tahoma', 13), bg='#D5CEA3')
                name_label.place(x=40, y=20)
            if error == 'family':
                x = errors['family']
                family_label = Label(git2, text=f'{x}', font=('tahoma', 13), bg='#D5CEA3')
                family_label.place(x=40, y=40)
            if error == 'email':
                x = errors['email']
                email_label = Label(git2, text=f'{x}', font=('tahoma', 13), bg='#D5CEA3')
                email_label.place(x=40, y=60)
            if error == 'password':
                x = errors['password']
                password_label = Label(git2, text=f'{x}', font=('tahoma', 13), bg='#D5CEA3')
                password_label.place(x=40, y=80)

        buttom4 = Button(git2, text='ok', bg='#D06224', border=5, width=9, command=lambda: sing_up())
        buttom4.place(x=80, y=120)

#================================Login======================================
def log_in():
    git3 = Tk()
    git3.title('Login')
    git3.geometry('410x160')
    git3.resizable(width=False, height=False)
    git3.iconbitmap('./icons/libraries_84323.ico')
    git3.configure(bg='#D5CEA3')
    entry1 = Entry(git3,width=40,border=3)
    entry1.place(x=120, y=40)
    entry2 = Entry(git3,width=40,border=3)
    entry2.place(x=120, y=85)
    labelg2 = Label(git3, text='password:', font=('tahoma', 12),bg='#D5CEA3')
    labelg2.place(x=15, y=85)
    labelg3 = Label(git3, text='email:', font=('tahoma', 12),bg='#D5CEA3')
    labelg3.place(x=15, y=40)
    buttom4 = Button(git3, text='Login', bg='#D06224',border=5, width=9, command=lambda: login_validation(entry1,entry2))
    buttom4.place(x=200, y=122)

#===========Checking the login information in the database============
def login_validation(x,y):
    email = x.get()
    password = y.get()
    user = list(curser.execute("SELECT * FROM user WHERE email=? AND password=?",(email,password)))
    if user == []:
        git23 = Tk()
        git23.title('Login failed')
        git23.geometry('300x100')
        git23.resizable(width=False, height=False)
        git23.iconbitmap('./icons/libraries_84323.ico')
        git23.configure(bg='#D5CEA3')
        label6 = Label(git23, text='Login failed', font=('tahoma', 11), bg='#D5CEA3')
        label6.place(x=20, y=20)
        buttom4 = Button(git23, text='ok', bg='#D06224', border=5, width=9, command=lambda: log_in())
        buttom4.place(x=115, y=60)
    else:
        git2 = Tk()
        git2.title('Library')
        git2.geometry('250x100')
        git2.configure(bg='#D5CEA3')
        git2.resizable(width=False, height=False)
        git2.iconbitmap('./icons/libraries_84323.ico')
        label6 = Label(git2, text='Login was successful', font=('tahoma', 13), bg='#D5CEA3')
        label6.place(x=20, y=20)
        buttom4 = Button(git2, text='start', bg='#D06224', border=5, width=9, command=lambda: Page3(ps()))
        buttom4.place(x=80, y=60)
    connection.commit()
#==============================Program information====================================
def information():
    inf = Tk()
    inf.title('About')
    inf.geometry('450x160')
    inf.resizable(width=False, height=False)
    inf.iconbitmap('./icons/libraries_84323.ico')
    inf.configure(bg='#D5CEA3')
    labelg223 = Label(inf, text='This program is made with python \nTkinter graphic module is used for its appearance \n and sqlite3 is used for its database \n you can use this program for To manage your library \n just enough to registred or Login if you have an account', font=('tahoma', 12),bg='#D5CEA3')
    labelg223.place(x=22, y=10)
    label46 = Label(inf, text='Mohammad Taha Afzali Nia', font=('tahoma', 13), bg='#D5CEA3')
    label46.place(x=128, y=118)
#====================================Contact us======================================
def contact_us():
    cal = Tk()
    cal.title('Contact us')
    cal.geometry('250x70')
    cal.resizable(width=False, height=False)
    cal.iconbitmap('./icons/4_122640.ico')
    cal.configure(bg='#D5CEA3')
    labelcal = Label(cal, text='Contact us:', font=('tahoma', 13), bg='#D5CEA3')
    labelcal.place(x=25, y=20)
    labelacal2 = Label(cal, text=' 09980104624', font=('tahoma', 13), bg='#D5CEA3')
    labelacal2.place(x=115, y=20)
#==============================Library=========================================
# Add the book in the database
def data3(w,e,r,t,o,q):
    connect = sqlite3.connect('./my-tik.db')
    curso = connect.cursor()
    name_book = w.get()
    writer = e.get()
    publisher = r.get()
    data_of = t.get()
    age_cat = o.get()
    story = q.get()
    curso.execute("INSERT INTO user (name_book,writer,Date_of_Release,age_category,Story,publisher) VALUES (?,?,?,?,?,?)",(name_book,writer,data_of,age_cat,story,publisher))
    connect.commit()
    connect.close()
# Delete the book in the database
def data4(w):
    connect = sqlite3.connect('./my-tik.db')
    curso = connect.cursor()
    name_book = w.get()
    curso.execute("DELETE FROM user WHERE name_book=? ",(name_book,))
    connect.commit()
    connect.close()
# Searching the book in the database
def data5(x,y,z,m,g,l,s,se):
    connec = sqlite3.connect('./my-tik.db')
    curs = connec.cursor()
    name_book = x.get()
    curs.execute("SELECT * FROM user WHERE name_book=?",(name_book,))
    re = curs.fetchone()
    if re:
        y.config(text=re[0])
        z.config(text=re[1])
        m.config(text=re[2])
        g.config(text=re[3])
        l.config(text=re[4])
        s.config(text=re[5])
    else:
        se.config(text='Book not found')
    connec.commit()
    connec.close()
# Library
def Page3(y):
    pag3 = Tk()
    pag3.title('Library')
    pag3.geometry('810x320')
    pag3.resizable(width=False, height=False)
    pag3.iconbitmap('./icons/libraries_84323.ico')
    pag3.configure(bg='#D5CEA3')
    entry1 = Entry(pag3,width=40,border=2,bg='#fafafa')
    entry1.place(x=150, y=110)
    entry2 = Entry(pag3,width=40,border=2,bg='#fafafa')
    entry2.place(x=150, y=155)
    entry3 = Entry(pag3,width=40,border=2,bg='#fafafa')
    entry3.place(x=520, y=200)
    entry4 = Entry(pag3,width=40,border=2,bg='#fafafa')
    entry4.place(x=150, y=200)
    entry5 = Entry(pag3,width=40,border=2,bg='#fafafa')
    entry5.place(x=520, y=110)
    entry6 = Entry(pag3,width=40,border=2,bg='#fafafa')
    entry6.place(x=520, y=155)
    entry_search = Entry(pag3,width=80,border=3)
    entry_search.place(x=180, y=37)
    buttom1 = Button(pag3, text='search', bg='#D06224', width=8,height=1,command=lambda:data5(entry_search,label10,label11,label12,label13,label14,label15,label_search))
    buttom1.place(x=620, y=34)
    buttom2 = Button(pag3, text='add', bg='#D06224',border=3, width=8,command=lambda:Page3(data3(entry1,entry2,entry3,entry4,entry5,entry6)))
    buttom2.place(x=580, y=265)
    buttom3 = Button(pag3, text='delete', bg='#D06224',border=3, width=8,command=lambda:data4(entry_search))
    buttom3.place(x=690, y=265)
    label4 = Label(pag3, text='name book:', font=('tahoma',12),bg='#D5CEA3')
    label4.place(x=20, y=106)
    label5 = Label(pag3, text='author:', font=('tahoma', 12),bg='#D5CEA3')
    label5.place(x=20, y=152)
    label6 = Label(pag3, text='release date:', font=('tahoma', 12),bg='#D5CEA3')
    label6.place(x=20, y=198)
    label7= Label(pag3, text='age category:', font=('tahoma', 12),bg='#D5CEA3')
    label7.place(x=430, y=106)
    label8 = Label(pag3, text='gener:', font=('tahoma', 12),bg='#D5CEA3')
    label8.place(x=440, y=152)
    label9 = Label(pag3, text='publisher:', font=('tahoma', 12),bg='#D5CEA3')
    label9.place(x=440, y=198)
    label_search = Label(pag3, text='',bg='#D5CEA3')
    label_search.place(x=359, y=8)
    label10 = Label(pag3, text='',bg='#fafafa',height=0)
    label10.place(x=300, y=110)
    label11 = Label(pag3, text='',bg='#fafafa',height=0)
    label11.place(x=300, y=156)
    label12 = Label(pag3, text='',bg='#fafafa',height=0)
    label12.place(x=320, y=201)
    label13 = Label(pag3, text='',bg='#fafafa',height=0)
    label13.place(x=700, y=110)
    label14 = Label(pag3, text='',bg='#fafafa',height=0)
    label14.place(x=700, y=156)
    label15 = Label(pag3, text='',bg='#fafafa',height=0)
    label15.place(x=700, y=201)
    return y
def ps():
    pass
root.mainloop()
connection.close()
