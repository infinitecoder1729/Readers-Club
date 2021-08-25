import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
import datetime
from PIL import ImageTk,Image
from tkinter import messagebox
import time
runtime=datetime.datetime.now()
logfile=open("Program Log.txt", "a+")
logfile.write("\n\nDate and Time : {} - Application Accessed".format(runtime))
logfile.close()
def load_databases():
    print("Status : Connection Successful - Fetching Databases")
    host=h.get()
    user = Username.get()
    passw = password.get()
    try :
        con = mysql.connector.connect(host = host,user=user, passwd = passw)
        cur= con.cursor()
        cur.execute("Show Databases")
        l=tuple()
        for i in cur:
            l=l+i
        Database['values']=l
        runtime=datetime.datetime.now()
        logfile=open("Program Log.txt", "a+")
        logfile.write("\n\nDate and Time : {} - Login Successful : Databases Fetched".format(runtime))
        logfile.close()
    except:
        messagebox.showinfo('Warning - Incorrect Login Info','Error !!! , You entered incorrect Credentials.')
        
def logintodb(host,user, passw,db_con):
    print("User Action : Database Selected.")
    print("Data setup attempted. Ignore any errors that pop up here")
    db = mysql.connector.connect(host = host, user=user, passwd = passw, database =db_con)
    cursor = db.cursor()
    if db.is_connected:
        for widget in root.winfo_children():
            widget.destroy()
        img_con = Image.open("pysqlcon.jpg")
        resizefactor=0.8
        [imgwid1, imgh1] = img_con.size
        imageSizing=True
        newimgwid1 = int(imgwid1*resizefactor)
        if imageSizing:
            newimgh1 = int(imgh1*resizefactor) 
        else:
            newimgh1= int(imgh1/resizefactor)
        img_con = img_con.resize((newimgwid1,newimgh1),Image.ANTIALIAS)
        test = ImageTk.PhotoImage(img_con)
        label1 = tk.Label(root,image=test)
        label1.image = test
        label1.place(x=0, y=0)
        root.state('zoomed')
        messagebox.showinfo('Information',"Your Connection with MySql has been Setup\nThe Database has been initialized\nThe User-Interface is ready to be used\nClick 'OK' to Continue")
        time.sleep=(1.5)
        root.geometry("600x600")
        root.state('normal')
        cursor.execute('create table if not exists book_info(book_id varchar(5) primary key, book_title char(255), book_author varchar(255),book_status varchar(255) default "Available")')
        cursor.execute('create table if not exists transaction_info(book_id varchar(5) , issued_to char(255) not null,date_issued varchar(255) not null,date_returned varchar(255) default "Not Returned",fine integer(4) default 0)')
        runtime=datetime.datetime.now()
        logfile=open("Program Log.txt", "a+")
        logfile.write("\nDate and Time : {} - Database Selected : {}".format(runtime,db_con))
        logfile.close()
        try:
            cursor.execute('insert into book_info values("T9312","Wings of Fire","Dr.APJ Abdul Kalam","Available")')
            cursor.execute('insert into book_info values("Y9301","Godan","Munshi Premchand","Available")')
            cursor.execute('insert into book_info values("K4922","Algorithms","Robert Sedgewick","Issued")')
            cursor.execute('insert into book_info values("K1283","The Pricipia","Isaac Newton","Available")')
            cursor.execute('insert into transaction_info values("K1283","Priya R.","2021-04-02","2021-05-01",0)')
            cursor.execute('insert into transaction_info values("K4922","Abhay K.","2021-05-12","Not Returned",0)')
            cursor.execute('insert into transaction_info values("T9312","Sahay M.","2021-03-11","2021-04-14",0)')        
            cursor.execute('insert into transaction_info values("T9312","Abhay K.","2021-04-21","2021-06-12",50)')
            db.commit()
            menu(host,user, passw,db_con)
        except:
            db.commit()
            menu(host,user, passw,db_con)
            
def menu(host,user, passw,db_con):
    print("Data initialization Successful. UI is working seamlessly. Menu Opened")
    runtime=datetime.datetime.now()
    logfile=open("Program Log.txt", "a+")
    logfile.write("\nDate and Time : {} - Application UI Initialized".format(runtime))
    logfile.write("\nDate and Time : {} - Menu Displayed to the User".format(runtime))
    logfile.close()
    conn= mysql.connector.connect(host = host, user=user, passwd = passw, database =db_con)
    cur = conn.cursor()
    menu = tk.Toplevel()
    menu.iconbitmap('readersclubicon.ico')
    menu.title("Reader's Club")
    menu['bg']='Dark Blue'
    menu.minsize(width=400,height=400)
    menu.state('zoomed')
    sizing=True
    bg_img =Image.open("readers.jpg")
    [imgwid, imgh] = bg_img.size
    newimgwid = int(imgwid*0.9)
    if sizing:
        newimgh = int(imgh*1.35) 
    else:
        newimgh = int(imgh/1.35) 
    bg_img = bg_img.resize((newimgwid,newimgh),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(bg_img)
    Canvas_img = Canvas(menu)
    Canvas_img.create_image(300,340,image = img)      
    Canvas_img.config(bg="Dark Blue",width = newimgwid, height = newimgh)
    Canvas_img.pack(fill=BOTH)
    headingFrame1 = Frame(menu,bg="Red",bd=5)
    headingFrame1.place(relx=0.58,rely=0.05,relwidth=0.4,relheight=0.2)
    headingLabel = Label(headingFrame1, text="Welcome to Reader's Club",bg='Black' ,fg='Pink', font=('Comic Sans Ms',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    addbook = Button(menu,text="Add Book Information to the Database",bg='Violet', fg='black',command=lambda:addbookuicall(host,user, passw,db_con),font=('Comic Sans Ms',12))
    addbook.place(relx=0.63,rely=0.3, relwidth=0.3,relheight=0.1)
    issuebook= Button(menu,text="Issue a Book to a Member",bg='Black', fg='yellow',font=('Comic Sans Ms',12),command = lambda : issuebookcall(host,user, passw,db_con))
    issuebook.place(relx=0.63,rely=0.41, relwidth=0.3,relheight=0.1)
    viewbook = Button(menu,text="View Database Information in a Structured Way",bg='Red', fg='White',font=('Comic Sans Ms',12),command=lambda:viewmenucall(host,user, passw,db_con))
    viewbook.place(relx=0.63,rely=0.52, relwidth=0.3,relheight=0.1)
    retbook = Button(menu,text="Register a Return",bg='Pink', fg='red',font=('Comic Sans Ms',12),command=lambda : retbookcall(host,user, passw,db_con))
    retbook.place(relx=0.63,rely=0.63, relwidth=0.3,relheight=0.1)
    delbook = Button(menu,text="Delete Book Information from the Database",bg='Purple', fg='white',font=('Comic Sans Ms',12),command=lambda : delbookcall(host,user, passw,db_con))
    delbook.place(relx=0.63,rely=0.74, relwidth=0.3,relheight=0.1)
    infolbl=Label(menu,text="Made by : Nikhil Handa",bg="Dark Blue",fg="White",font=('Comic Sans Ms',13))
    infolbl.place(relx=0.63,rely=0.9,relwidth=0.3,relheight=0.09)
    menu.mainloop()

def addbookuicall(host,user, passw,db_con):
    runtime=datetime.datetime.now()
    logfile=open("Program Log.txt", "a+")
    logfile.write("\nDate and Time : {} - Add Book UI Initialized".format(runtime))
    logfile.close()
    def addbookdatafetch(host,user, passw,db_con):
        bookid = book_id.get()
        booktitle = book_title.get()
        bookauthor = book_author.get()
        bookstatus = book_status.get()
        addbook(host,user, passw,db_con,bookid,booktitle,bookauthor,bookstatus)
    print("Add Book Command Accessed. This is to create new entries in the Database")
    addbookui = tk.Toplevel()
    addbookui.title("Reader's Club - Add Book")
    addbookui.iconbitmap('readersclubicon.ico')
    addbookui.minsize(width=400,height=400)
    addbookui.state("zoomed")
    con= mysql.connector.connect(host = host, user=user, passwd = passw, database =db_con)
    cur = con.cursor()
    sizing=True
    addbookui['bg']='Dark BLue'
    background_image1 =Image.open("readers.jpg")
    [imgwid, imgh] = background_image1.size
    newimgwid = int(imgwid*0.9)
    if sizing:
        newimgh = int(imgh*1.35) 
    else:
        newimgh = int(imgh/1.35) 
    background_image1 = background_image1.resize((newimgwid,newimgh),Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(background_image1)
    Canvasadu = Canvas(addbookui)
    Canvasadu.create_image(300,340,image = img1)      
    Canvasadu.config(bg="Dark Blue",width = newimgwid, height = newimgh)
    Canvasadu.pack(fill=BOTH)
    head = Frame(addbookui,bg="Red",bd=5)
    head.place(relx=0.6,rely=0.05,relwidth=0.3,relheight=0.1)
    headLabel = Label(head, text="Add Book Information to Database", bg='Black', fg='Cyan', font=('Comic Sans Ms',15))
    headLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    label1 = Label(addbookui,text="Book ID : ", bg='Brown', fg='pink',font=('Comic Sans Ms',12))
    label1.place(relx=0.55,rely=0.2, relwidth=0.08,relheight=0.1)
    book_id = Entry(addbookui,font=('Comic Sans Ms',12))
    book_id.place(relx=0.65,rely=0.21, relwidth=0.3, relheight=0.08)
    label2 = Label(addbookui,text="Title : ", bg='Purple', fg='white',font=('Comic Sans Ms',12))
    label2.place(relx=0.55,rely=0.35, relwidth=0.08,relheight=0.1)
    book_title = Entry(addbookui,font=('Comic Sans Ms',12))
    book_title.place(relx=0.65,rely=0.36, relwidth=0.3, relheight=0.08)
    lb3 = Label(addbookui,text="Author : ", bg='Pink', fg='Red',font=('Comic Sans Ms',12))
    lb3.place(relx=0.55,rely=0.5, relwidth=0.08,relheight=0.1)
    book_author = Entry(addbookui,font=('Comic Sans Ms',12))
    book_author.place(relx=0.65,rely=0.51, relwidth=0.3, relheight=0.08)
    lb4 = Label(addbookui,text="Status : ", bg='Blue', fg='cyan',font=('Comic Sans Ms',12))
    lb4.place(relx=0.55,rely=0.65, relwidth=0.08,relheight=0.1)
    book_status=tk.StringVar()
    book_stat= ttk.Combobox(addbookui,textvariable=book_status,font=('Comic Sans Ms',12))
    book_stat.place(relx=0.65,rely=0.66, relwidth=0.3, relheight=0.08)
    book_stat['state']='readonly'
    book_stat['values']=['Available','Issued']
    Subbtn = Button(addbookui,text="Submit",bg='Dark Green', fg='light green',command=lambda : addbookdatafetch(host,user, passw,db_con),font=('Comic Sans Ms',12))
    Subbtn.place(relx=0.55,rely=0.8, relwidth=0.1,relheight=0.08)
    quitBtn = Button(addbookui,text="Back", fg='white',bg='red', command=addbookui.destroy,font=('Comic Sans Ms',12))
    quitBtn.place(relx=0.85,rely=0.8, relwidth=0.1,relheight=0.08)
    infolbl=Label(addbookui,text="Made by : Nikhil Handa",bg="Dark Blue",fg="White",font=('Comic Sans Ms',13))
    infolbl.place(relx=0.55,rely=0.9,relwidth=0.4,relheight=0.09)
    addbookui.mainloop()
    
def addbook(host,user, passw,db_con,bookid,booktitle,bookauthor,bookstatus):
    print("Book Details Accepted. Trying to add",bookid,booktitle,bookauthor,bookstatus,"to the database")
    con= mysql.connector.connect(host = host, user=user, passwd = passw, database =db_con)
    cur = con.cursor()
    try:
        cur.execute("insert into book_info(book_id , book_title , book_author ,book_status) values('{}','{}','{}','{}')".format(bookid,booktitle,bookauthor,bookstatus))
        con.commit()
        logfile=open("Program Log.txt", "a+")
        runtime=datetime.datetime.now()
        logfile.write("\nDate and Time : {} - Book Added to Database with details as : {} {} {} {}".format(runtime,bookid,booktitle,bookauthor,bookstatus))
        logfile.close()
        messagebox.showinfo('Successful Operation',"Book has been Added to the Database Successfully")
    except:
        messagebox.showinfo("Error !","Can't add book into the database\nReasons might include :\n1.Violation of Prescribed Formats\n2.Empty Fields\n3.Duplicate Book Ids")
        runtime=datetime.datetime.now()
        logfile=open("Program Log.txt", "a+")
        logfile.write("\nDate and Time : {} - Error in Adding the Book to the database".format(runtime))
        logfile.close()
        
def viewmenucall(host,user, passw,db_con):
    print('Information Fetched from database for structured display')
    runtime=datetime.datetime.now()
    logfile=open("Program Log.txt", "a+")
    logfile.write("\nDate and Time : {} - View Menu Accessed".format(runtime))
    logfile.close()
    conn= mysql.connector.connect(host = host, user=user, passwd = passw, database =db_con)
    cur = conn.cursor()
    viewmenu = tk.Toplevel()
    viewmenu.iconbitmap('readersclubicon.ico')
    viewmenu['bg']='Dark Blue'
    viewmenu.title("Reader's Club - View Information in A Structured Way")
    viewmenu.minsize(width=400,height=400)
    viewmenu.state('zoomed')
    same=True
    background_image =Image.open("readers.jpg")
    [imgwid, imgh] = background_image.size
    newimgwid = int(imgwid*0.9)
    if same:
        newimgh = int(imgh*1.35) 
    else:
        newimgh = int(imgh/1.35) 
    background_image = background_image.resize((newimgwid,newimgh),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)
    Canvas1 = Canvas(viewmenu)
    Canvas1.create_image(300,340,image = img)      
    Canvas1.config(bg="Dark Blue",width = newimgwid, height = newimgh)
    Canvas1.pack(fill=BOTH)
    headingFrame1 = Frame(viewmenu,bg="Red",bd=5)
    headingFrame1.place(relx=0.58,rely=0.05,relwidth=0.4,relheight=0.1)
    headingLabel = Label(headingFrame1, text="Reader's Club - View Information",bg='Black' ,fg='Pink', font=('Comic Sans Ms',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    viewbookinfo = Button(viewmenu,text="View All Books",bg='Violet', fg='black',command=lambda:viewbooks(host,user, passw,db_con),font=('Comic Sans Ms',12))
    viewbookinfo.place(relx=0.63,rely=0.2, relwidth=0.3,relheight=0.1)
    transinfo= Button(viewmenu,text="View All Transactions",bg='Black', fg='yellow',font=('Comic Sans Ms',12),command=lambda : viewtrans(host,user, passw,db_con))
    transinfo.place(relx=0.63,rely=0.31, relwidth=0.3,relheight=0.1)
    memdinfo = Button(viewmenu,text="View Transactions for a Specific Member",bg='Dark Blue', fg='cyan',font=('Comic Sans Ms',12),command=lambda:transbymem(host,user, passw,db_con))
    memdinfo.place(relx=0.63,rely=0.42, relwidth=0.3,relheight=0.1)
    bookspec = Button(viewmenu,text="View Information for a Specific Book",bg='Pink', fg='red',font=('Comic Sans Ms',12),command=lambda : infobybook(host,user, passw,db_con))
    bookspec.place(relx=0.63,rely=0.53, relwidth=0.3,relheight=0.1)
    bookstatinfo = Button(viewmenu,text="View Statistics",bg='Dark Green', fg='white',font=('Comic Sans Ms',12),command=lambda : viewstats(host,user, passw,db_con))
    bookstatinfo.place(relx=0.63,rely=0.64, relwidth=0.3,relheight=0.1)
    quitBtn = Button(viewmenu,text="Exit this Menu",bg='Red', fg='White', command=viewmenu.destroy,font=('Comic Sans Ms',11))
    quitBtn.place(relx=0.63,rely=0.75, relwidth=0.3,relheight=0.08)
    infolbl=Label(viewmenu,text="Made by : Nikhil Handa",bg="Dark Blue",fg="White",font=('Comic Sans Ms',13))
    infolbl.place(relx=0.63,rely=0.9,relwidth=0.3,relheight=0.09)
    viewmenu.mainloop()

def viewbooks(host,user, passw,db_con):
    runtime=datetime.datetime.now()
    logfile=open("Program Log.txt", "a+")
    logfile.write("\nDate and Time : {} - Displaying Information for All Books".format(runtime))
    logfile.close()
    print('Displaying Book Information')
    con= mysql.connector.connect(host = host, user=user, passwd = passw, database =db_con)
    cur = con.cursor()
    viewbookui =tk.Toplevel()
    viewbookui.iconbitmap('readersclubicon.ico')
    viewbookui.title("Reader's Club - View Book Details")
    viewbookui.minsize(width=400,height=400)
    viewbookui.state('zoomed')
    sizing=True
    background_image1 =Image.open("readers.jpg")
    [imgwid, imgh] = background_image1.size
    newimgwid = int(imgwid*0.8)
    if sizing:
        newimgh = int(imgh*1.35) 
    else:
        newimgh = int(imgh/1.35) 
    background_image1 = background_image1.resize((newimgwid,newimgh),Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(background_image1)
    Canvasvbu = Canvas(viewbookui)
    Canvasvbu.create_image(300,340,image = img1)      
    Canvasvbu.config(bg="Dark Blue",width = newimgwid, height = newimgh)
    Canvasvbu.pack(expand=True,fill=BOTH)
    headFrame=Frame(viewbookui,bg="Pink",bd=5)
    headFrame.place(relx=0.49,rely=0.02,relwidth=0.49,relheight=0.1)    
    headLabel = Label(headFrame, text="View Book Information Stored in the Database", bg='black', fg='Yellow', font=('Comic  Sans Ms',15))
    headLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    infolabelFrame = Frame(viewbookui,bg='Dark Blue')
    infolabelFrame.place(relx=0.483,rely=0.2,relwidth=0.5,relheight=0.6)
    infoLabel=Label(infolabelFrame,text="Book Information ",bg='Dark BLue',fg='cyan',font=('Comic Sans Ms',14)).place(relx=0,rely=0.02)
    relydef = 0.1
    cur.execute('select * from book_info')
    colorlis=['pink','cyan']
    co=1
    for i in cur:
        if co==1:
            co=0
        else:
            co=1
        infoLabel=Label(infolabelFrame, text="Book Id : {0:^5} - Title : {1:^2} - Author : {2:^5} - Status : {3:^2}".format(i[0],i[1],i[2],i[3]),bg='dark blue',fg=colorlis[co],font=('Comic Sans Ms',12)).place(relx=0,rely=relydef)
        relydef=relydef+0.1
    cur.execute("select count(*) from book_info")
    for i in cur:
        infoLabel=Label(infolabelFrame, text="Total Number of Books in Club = {}".format(i[0]),bg='dark blue',fg='yellow',font=('Comic Sans Ms',12)).place(relx=0.01,rely=relydef)    
    relydef=relydef+0.1
    cur.execute("select count(*) from book_info where book_status='Issued'")
    for i in cur:
        infoLabel=Label(infolabelFrame, text="Number of Books currently issued = {}".format(i[0]),bg='dark blue',fg='yellow',font=('Comic Sans Ms',12)).place(relx=0.01,rely=relydef)    
    quitBtn = Button(viewbookui,text="Back",bg='Red', fg='White', command=viewbookui.destroy)
    quitBtn.place(relx=0.49,rely=0.82, relwidth=0.49,relheight=0.07)
    infolbl=Label(viewbookui,text="Made by : Nikhil Handa",bg="Dark Blue",fg="White",font=('Comic Sans Ms',13))
    infolbl.place(relx=0.483,rely=0.92,relwidth=0.5,relheight=0.07)
    viewbookui.mainloop()

def viewstats(host,user, passw,db_con): 
    runtime=datetime.datetime.now()
    logfile=open("Program Log.txt", "a+")
    logfile.write("\nDate and Time : {} - Displaying Stats".format(runtime))
    logfile.close()
    print('Displaying Statistical Information')
    con= mysql.connector.connect(host = host, user=user, passwd = passw, database =db_con)
    cur = con.cursor()
    viewstatui =tk.Toplevel()
    viewstatui['bg']='Dark Blue'
    viewstatui.iconbitmap('readersclubicon.ico')
    viewstatui.title("Reader's Club - View Statistical Information")
    viewstatui.minsize(width=400,height=400)
    viewstatui.state('zoomed')
    sizing=True
    background_image1 =Image.open("readers.jpg")
    [imgwid, imgh] = background_image1.size
    newimgwid = int(imgwid*0.9)
    if sizing:
        newimgh = int(imgh*1.35) 
    else:
        newimgh = int(imgh/1.35) 
    background_image1 = background_image1.resize((newimgwid,newimgh),Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(background_image1)
    Canvasvbu = Canvas(viewstatui)
    Canvasvbu.create_image(300,340,image = img1)      
    Canvasvbu.config(bg="Dark Blue",width = newimgwid, height = newimgh)
    Canvasvbu.pack(expand=True,fill=BOTH)
    headFrame=Frame(viewstatui,bg="Cyan",bd=5)
    headFrame.place(relx=0.55,rely=0.01,relwidth=0.4,relheight=0.11)    
    headLabel = Label(headFrame, text="View Statistical Information", bg='black', fg='pink', font=('Comic  Sans Ms',15))
    headLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    infolabelFrame = Frame(viewstatui,bg='Dark Blue')
    infolabelFrame.place(relx=0.55,rely=0.15,relwidth=0.4,relheight=0.6)
    infoLabel=Label(infolabelFrame, text="Statistics for Members and Books ",bg='Dark Blue',fg='cyan',font=('Comic Sans Ms',14)).place(relx=0,rely=0.01)
    relydef = 0.1
    cur.execute('select book_id,count(*) as total from transaction_info group by book_id order by total desc')
    for i in cur:
        infoLabel=Label(infolabelFrame, text="Book Identity : %-7s Number of Issues : %-20s"%(i[0],i[1]),bg='Dark Blue',fg='yellow',font=('Comic Sans Ms',12)).place(relx=0,rely=relydef)
        relydef=relydef+0.1
    cur.execute("select issued_to,count(*) as total from transaction_info group by issued_to order by total desc ")
    for i in cur:
        infoLabel=Label(infolabelFrame, text="Member Name: %-7s Number of Issues : %-20s"%(i[0],i[1]),bg='Dark Blue',fg='light green',font=('Comic Sans Ms',12)).place(relx=0,rely=relydef)    
        relydef=relydef+0.1
    quitbutton = Button(viewstatui,text="Back",bg='Red', fg='White', command=viewstatui.destroy)
    quitbutton.place(relx=0.55,rely=0.8, relwidth=0.4,relheight=0.08)
    infolbl=Label(viewstatui,text="Made by : Nikhil Handa",bg="Dark Blue",fg="White",font=('Comic Sans Ms',13))
    infolbl.place(relx=0.55,rely=0.9,relwidth=0.4,relheight=0.09)
    viewstatui.mainloop()

def viewtrans(host,user, passw,db_con): 
    runtime=datetime.datetime.now()
    logfile=open("Program Log.txt", "a+")
    logfile.write("\nDate and Time : {} - Displaying Transactions".format(runtime)) 
    logfile.close()
    print('Displaying Transactional Information')
    con= mysql.connector.connect(host = host, user=user, passwd = passw, database =db_con)
    cur = con.cursor()
    viewtransui =tk.Toplevel()
    viewtransui.iconbitmap('readersclubicon.ico')
    viewtransui.title("Reader's Club - View Transaction Details")
    viewtransui['bg']='Dark Blue'
    viewtransui.minsize(width=400,height=400)
    viewtransui.state('zoomed')
    sizing=True
    background_image1 =Image.open("readers.jpg")
    [imgwid, imgh] = background_image1.size
    newimgwid = int(imgwid*0.8)
    if sizing:
        newimgh = int(imgh*1.35) 
    else:
        newimgh = int(imgh/1.35) 
    background_image1 = background_image1.resize((newimgwid,newimgh),Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(background_image1)
    Canvasvbu = Canvas(viewtransui)
    Canvasvbu.create_image(300,340,image = img1)      
    Canvasvbu.config(bg="Dark Blue",width = newimgwid, height = newimgh)
    Canvasvbu.pack(expand=True,fill=BOTH)
    headFrame=Frame(viewtransui,bg="Purple",bd=5)
    headFrame.place(relx=0.49,rely=0.01,relwidth=0.49,relheight=0.11)    
    headLabel = Label(headFrame, text="View Transactional Information Stored in the Database", bg='black', fg='Cyan', font=('Comic  Sans Ms',15))
    headLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    infolabelFrame = Frame(viewtransui,bg='black')
    infolabelFrame.place(relx=0.49,rely=0.15,relwidth=0.49,relheight=0.6)
    infoLabel=Label(infolabelFrame, text="Transactional Information ",bg='dark blue',fg='cyan',font=('Comic Sans Ms',14)).place(relx=0,rely=0)
    relydef = 0.12
    cur.execute('select * from transaction_info')
    for i in cur:
        infoLabel=Label(infolabelFrame, text="Book Id : {0:^2} - Issued to : {1:^2} - Date of Issue: {2:^2} - Date of Return: {3:^2} - Fine: {4:^2}".format(i[0],i[1],i[2],i[3],i[4]),bg='black',fg='pink',font=('Comic Sans Ms',10)).place(relx=0.01,rely=relydef)
        relydef=relydef+0.1
    cur.execute("select count(*) from transaction_info where date_returned='Not Returned' ")
    for i in cur:
        infoLabel=Label(infolabelFrame, text="Total Number of Books Issued and Not Returned = {}".format(i[0]),bg='black',fg='pink',font=('Comic Sans Ms',12)).place(relx=0.02,rely=relydef)    
    relydef=relydef+0.1
    cur.execute("select count(*) from transaction_info")
    for i in cur:
        infoLabel=Label(infolabelFrame, text="Number of Transactions = {}".format(i[0]),bg='black',fg='pink',font=('Comic Sans Ms',12)).place(relx=0.02,rely=relydef)    
    quitBtn = Button(viewtransui,text="Back",bg='Red', fg='White', command=viewtransui.destroy)
    quitBtn.place(relx=0.5,rely=0.8, relwidth=0.46,relheight=0.08)
    infolbl=Label(viewtransui,text="Made by : Nikhil Handa",bg="Dark Blue",fg="White",font=('Comic Sans Ms',13))
    infolbl.place(relx=0.49,rely=0.9,relwidth=0.49,relheight=0.09)
    viewtransui.mainloop()

def transbymem(host,user, passw,db_con):
    print('Segregating Transactions for specific Members')
    con= mysql.connector.connect(host = host, user=user, passwd = passw, database =db_con)
    cur = con.cursor()
    transmemui=tk.Toplevel()
    transmemui.title("Reader's Club - Viewing Transactions for specific Members")
    transmemui.minsize(width=400,height=400)
    transmemui.state("zoomed")
    transmemui.iconbitmap('readersclubicon.ico')
    sizing=True
    background_image1 =Image.open("readers.jpg")
    [imgwid, imgh] = background_image1.size
    newimgwid = int(imgwid*0.9)
    if sizing:
        newimgh = int(imgh*1.35) 
    else:
        newimgh = int(imgh/1.35) 
    background_image1 = background_image1.resize((newimgwid,newimgh),Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(background_image1)
    Canvasibu = Canvas(transmemui)
    Canvasibu.create_image(300,340,image = img1)      
    Canvasibu.config(bg="Dark Blue",width = newimgwid, height = newimgh)
    Canvasibu.pack(expand=True,fill=BOTH)
    head= Frame(transmemui,bg="Red",bd=5)
    head.place(relx=0.54,rely=0.01,relwidth=0.45,relheight=0.13)
    headlbl = Label(head, text="View Transactions for a Specific Member", bg='black', fg='Violet', font=('Comic Sans Ms',15))
    headlbl.place(relx=0,rely=0, relwidth=1, relheight=1)
    lblFrame = Frame(transmemui,bg='black')
    lblFrame.place(relx=0.54,rely=0.2,relwidth=0.45,relheight=0.5)
    lb1 = Label(lblFrame,text="Member Name : ", bg='black', fg='Pink', font=('Comic Sans Ms',12))
    lb1.place(relx=0,rely=0.01)
    memname=tk.StringVar()
    mem = ttk.Combobox(lblFrame, font=('Comic Sans Ms',12),textvariable=memname)
    cur.execute('select distinct issued_to from transaction_info')
    lis=[]
    for i in cur:
        for a in i:
            lis.append(a)
    mem['values']=lis
    mem['state']='readonly'
    mem.place(relx=0.3,rely=0.01, relwidth=0.4)
    def transmemuidet(host,user, passw,db_con):
        detBtn.destroy()
        name=mem.get()
        runtime=datetime.datetime.now()
        logfile=open("Program Log.txt", "a+")
        logfile.write("\nDate and Time : {} - Displaying Details for the User : {}".format(runtime,name))
        logfile.close()
        con= mysql.connector.connect(host = host, user=user, passwd = passw, database =db_con)
        cur = con.cursor()
        cur.execute('select * from transaction_info where issued_to = "{}"'.format(name))
        relydef=0.15
        for i in cur:
            lb1=Label(lblFrame, text="Book Id : {0:^2} - Date of Issue : {1:^2} - Date of Return : {2:^2} - Fine : {3:^2}".format(i[0],i[2],i[3],i[4]),bg='black',fg='pink',font=('Comic Sans Ms',10))
            lb1.place(relx=0,rely=relydef)
            relydef=relydef+0.1
        cur.execute('select sum(fine) from transaction_info where issued_to = "{}" '.format(name))
        for i in cur:
            lb1=Label(lblFrame, text="Total fine paid : {}".format(i[0]),bg='black',fg='pink',font=('Comic Sans Ms',12))
            lb1.place(relx=0,rely=relydef)
    detBtn = Button(lblFrame,text="View Details",bg='Dark Green', fg='white', command=lambda : transmemuidet(host,user, passw,db_con), font=('Comic Sans Ms',12))
    detBtn.place(relx=0.72,rely=0, relwidth=0.24)
    quitBtn = Button(transmemui,text="Back",bg='red', fg='white', command=transmemui.destroy, font=('Comic Sans Ms',12))
    quitBtn.place(relx=0.55,rely=0.8, relwidth=0.43,relheight=0.08)
    infolbl=Label(transmemui,text="Made by : Nikhil Handa",bg="Dark Blue",fg="White",font=('Comic Sans Ms',13))
    infolbl.place(relx=0.55,rely=0.9,relwidth=0.45,relheight=0.09)
    transmemui.mainloop()

def infobybook(host,user, passw,db_con):
    print('Displaying Information for a specific Book')
    con= mysql.connector.connect(host = host, user=user, passwd = passw, database =db_con)
    cur = con.cursor()
    infobybookui=tk.Toplevel()
    infobybookui.title("Reader's Club - Book Information for a specific book")
    infobybookui.minsize(width=400,height=400)
    infobybookui.state("zoomed")
    infobybookui.iconbitmap('readersclubicon.ico')
    sizing=True
    background_image1 =Image.open("readers.jpg")
    [imgwid, imgh] = background_image1.size
    newimgwid = int(imgwid*0.9)
    if sizing:
        newimgh = int(imgh*1.35) 
    else:
        newimgh = int(imgh/1.35) 
    background_image1 = background_image1.resize((newimgwid,newimgh),Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(background_image1)
    Canvasibu = Canvas(infobybookui)
    Canvasibu.create_image(300,340,image = img1)      
    Canvasibu.config(bg="Dark Blue",width = newimgwid, height = newimgh)
    Canvasibu.pack(expand=True,fill=BOTH)
    head= Frame(infobybookui,bg="White",bd=5)
    head.place(relx=0.55,rely=0.02,relwidth=0.44,relheight=0.13)
    headlbl = Label(head, text="View Book Information for a Specific Book", bg='black', fg='Violet', font=('Comic Sans Ms',15))
    headlbl.place(relx=0,rely=0, relwidth=1, relheight=1)
    lblFrame = Frame(infobybookui,bg='black')
    lblFrame.place(relx=0.55,rely=0.2,relwidth=0.44,relheight=0.52)
    lb1 = Label(lblFrame,text="Book Id : ", bg='black', fg='Yellow', font=('Comic Sans Ms',12))
    lb1.place(relx=0,rely=0.02)
    bookname=tk.StringVar()
    idb = ttk.Combobox(lblFrame, font=('Comic Sans Ms',12),textvariable=bookname)
    cur.execute('select book_id from book_info')
    lis=[]
    for i in cur:
        for a in i:
            lis.append(a)
    idb['values']=lis
    idb['state']='readonly'
    idb.place(relx=0.15,rely=0.02, relwidth=0.2)
    def infobybookuidet(host,user, passw,db_con):
        detBtn.destroy()
        bookid=idb.get()
        logfile=open("Program Log.txt", "a+")
        runtime=datetime.datetime.now()
        logfile.write("\nDate and Time : {} - Displaying Information for Book {}".format(runtime,bookid))
        logfile.close()
        con= mysql.connector.connect(host = host, user=user, passwd = passw, database =db_con)
        cur = con.cursor()
        cur.execute('select * from book_info where book_id = "{}"'.format(bookid))
        relydef=0.15
        for i in cur:
            lb1=Label(lblFrame, text="Book Id : {0:^5} - Title : {1:^2} - Author : {2:^5} - Status : {3:^2}".format(i[0],i[1],i[2],i[3]),bg='black',fg='pink',font=('Comic Sans Ms',10))
            lb1.place(relx=0,rely=relydef)
        relydef=relydef+0.1
        cur.execute('select * from transaction_info where book_id = "{}"'.format(bookid))
        for i in cur:
            lb1=Label(lblFrame, text="Issued to : {0:^2} - Date of Issue: {1:^2} - Date of Return: {2:^2}".format(i[1],i[2],i[3]),bg='black',fg='pink',font=('Comic Sans Ms',10))
            lb1.place(relx=0,rely=relydef)
            relydef=relydef+0.1
        cur.execute('select count(*) from transaction_info where book_id = "{}"'.format(bookid))
        for i in cur:
            lb1=Label(lblFrame, text="Number of Transactions = {} ".format(i[0]),bg='black',fg='pink',font=('Comic Sans Ms',10))
            lb1.place(relx=0,rely=relydef)
    detBtn = Button(lblFrame,text="View Details",bg='Dark Green', fg='white', command=lambda : infobybookuidet(host,user, passw,db_con), font=('Comic Sans Ms',11))
    detBtn.place(relx=0.4,rely=0.02, relwidth=0.4)
    quitBtn = Button(infobybookui,text="Back",bg='red', fg='white', command=infobybookui.destroy, font=('Comic Sans Ms',11))
    quitBtn.place(relx=0.56,rely=0.8, relwidth=0.42,relheight=0.08)
    infolbl=Label(infobybookui,text="Made by : Nikhil Handa",bg="Dark Blue",fg="White",font=('Comic Sans Ms',13))
    infolbl.place(relx=0.55,rely=0.9,relwidth=0.44,relheight=0.09)
    infobybookui.mainloop()


def issuebookcall(host,user, passw,db_con):
    runtime=datetime.datetime.now()
    logfile=open("Program Log.txt", "a+")
    logfile.write("\nDate and Time : {} - Issue Book Window Opened".format(runtime)) 
    logfile.close()
    con= mysql.connector.connect(host = host, user=user, passwd = passw, database =db_con)
    cur = con.cursor()
    issuebookui=tk.Toplevel()
    issuebookui.title("Reader's Club - Issue Books")
    issuebookui.minsize(width=400,height=400)
    issuebookui.state("zoomed")
    issuebookui['bg']='Dark Blue'
    issuebookui.iconbitmap('readersclubicon.ico')
    sizing=True
    background_image1 =Image.open("readers.jpg")
    [imgwid, imgh] = background_image1.size
    newimgwid = int(imgwid*0.9)
    if sizing:
        newimgh = int(imgh*1.35) 
    else:
        newimgh = int(imgh/1.35) 
    background_image1 = background_image1.resize((newimgwid,newimgh),Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(background_image1)
    Canvasibu = Canvas(issuebookui)
    Canvasibu.create_image(300,340,image = img1)      
    Canvasibu.config(bg="Dark Blue",width = newimgwid, height = newimgh)
    Canvasibu.pack(expand=True,fill=BOTH)
    head= Frame(issuebookui,bg="Green",bd=5)
    head.place(relx=0.55,rely=0.02,relwidth=0.44,relheight=0.13)
    headlbl = Label(head, text="Issue a Book", bg='black', fg='Violet', font=('Comic Sans Ms',15))
    headlbl.place(relx=0,rely=0, relwidth=1, relheight=1)
    lblFrame = Frame(issuebookui,bg='black')
    lblFrame.place(relx=0.55,rely=0.2,relwidth=0.44,relheight=0.5)
    lb1 = Label(lblFrame,text="Book ID : ", bg='black', fg='Pink', font=('Comic Sans Ms',12))
    lb1.place(relx=0,rely=0.02)
    book_id=tk.StringVar()
    bookids = ttk.Combobox(lblFrame, font=('Comic Sans Ms',12),textvariable=book_id)
    cur.execute('select book_id from book_info where book_status="Available"')
    lis=[]
    for i in cur:
        lis.append(i)
    bookids['values']=lis
    bookids['state']='readonly'
    bookids.place(relx=0.25,rely=0.02, relwidth=0.7)
    lbl2 = Label(lblFrame,text="Issued To : ", bg='black', fg='Cyan', font=('Comic Sans Ms',12))
    lbl2.place(relx=0,rely=0.2)
    issuedto = Entry(lblFrame, font=('Comic Sans Ms',12))
    issuedto.place(relx=0.25,rely=0.2,relwidth=0.7)
    issueBtn = Button(issuebookui,text="Issue",bg='Dark Green', fg='Light Green', font=('Comic Sans Ms',12),command=lambda :  issuebookdatafetch(host,user, passw,db_con))
    issueBtn.place(relx=0.55,rely=0.8, relwidth=0.1,relheight=0.08)
    def issuebookdatafetch(host,user, passw,db_con):
        bookid = bookids.get()
        issued_to=issuedto.get()
        issuebook(host,user, passw,db_con,bookid,issued_to)
        issuebookui.destroy()
    quitBtn = Button(issuebookui,text="Back",bg='red', fg='white', command=issuebookui.destroy, font=('Comic Sans Ms',12))
    quitBtn.place(relx=0.85,rely=0.8, relwidth=0.1,relheight=0.08)
    infolbl=Label(issuebookui,text="Made by : Nikhil Handa",bg="Dark Blue",fg="White",font=('Comic Sans Ms',13))
    infolbl.place(relx=0.55,rely=0.9,relwidth=0.44,relheight=0.09)
    issuebookui.mainloop()

def issuebook(host,user, passw,db_con,bookid,issued_to):
    runtime=datetime.datetime.now()
    logfile=open("Program Log.txt", "a+")
    logfile.write("\nDate and Time : {} - Issuing Book {} to {} ".format(runtime,bookid,issued_to))
    logfile.close()
    print('Issuing Book {} to {} '.format(bookid,issued_to))
    datetimeinput=datetime.date.today()
    con= mysql.connector.connect(host = host, user=user, passwd = passw, database =db_con)
    cur = con.cursor()
    cur.execute("insert into transaction_info(book_id,issued_to,date_issued) values('{}','{}','{}')".format(bookid,issued_to,datetimeinput))
    con.commit()
    cur.execute("update book_info set book_status='Issued' where book_id = '{}' ".format(bookid))
    con.commit()
    messagebox.showinfo('Operation Successful',"Book Status Changed to 'Issued' Successfully")

def delbookcall(host,user, passw,db_con):    
    runtime=datetime.datetime.now()
    logfile=open("Program Log.txt", "a+")
    logfile.write("\nDate and Time : {} - Delete Book Window Opened".format(runtime))    
    logfile.close()
    delbookui = tk.Toplevel()
    delbookui.title("Reader's Club - Delete Book Information from the Database")
    delbookui.minsize(width=400,height=400)
    delbookui.state("zoomed")
    delbookui.iconbitmap('readersclubicon.ico')
    con= mysql.connector.connect(host = host, user=user, passwd = passw, database =db_con)
    cur = con.cursor()
    sizing=True
    background_image1 =Image.open("readers.jpg")
    [imgwid, imgh] = background_image1.size
    newimgwid = int(imgwid*0.9)
    if sizing:
        newimgh = int(imgh*1.35) 
    else:
        newimgh = int(imgh/1.35) 
    background_image1 = background_image1.resize((newimgwid,newimgh),Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(background_image1)
    Canvasdbu = Canvas(delbookui)
    Canvasdbu.create_image(300,340,image = img1)      
    Canvasdbu.config(bg="Dark Blue",width = newimgwid, height = newimgh)
    Canvasdbu.pack(expand=True,fill=BOTH)      
    headingFrame1 = Frame(delbookui,bg="Pink",bd=5)
    headingFrame1.place(relx=0.55,rely=0.02,relwidth=0.44,relheight=0.13)  
    headingLabel = Label(headingFrame1, text="Delete Book Information from Database", bg='Dark Blue', fg='White', font=('Comic Sans Ms',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(delbookui,bg='Dark Blue')
    labelFrame.place(relx=0.55,rely=0.2,relwidth=0.44,relheight=0.5)
    bookidd=tk.StringVar()
    lb2 = Label(labelFrame,text="Book ID : ", bg='Dark Blue', fg='white' , font=('Comic Sans Ms',12))
    lb2.place(relx=0,rely=0.5)    
    bookInfo1 = ttk.Combobox(labelFrame,textvariable=bookidd,font=('Comic Sans Ms',12))
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    cur.execute('select book_id from book_info')
    lis=[]
    for i in cur:
        lis.append(i)
    bookInfo1['values']=lis
    bookInfo1['state']='readonly'
    SubmitBtn = Button(delbookui,text="SUBMIT",font=('Comic Sans Ms',12),bg='Dark Green', fg='White',command=lambda : delbookfetchdata(host,user, passw,db_con))
    SubmitBtn.place(relx=0.55,rely=0.8, relwidth=0.15,relheight=0.08)
    quitBtn = Button(delbookui,text="Back",bg='Red', fg='White', font=('Comic Sans Ms',12),command=delbookui.destroy)
    quitBtn.place(relx=0.83,rely=0.8, relwidth=0.15,relheight=0.08)
    infolbl=Label(delbookui,text="Made by : Nikhil Handa",bg="Dark Blue",fg="White",font=('Comic Sans Ms',13))
    infolbl.place(relx=0.55,rely=0.9,relwidth=0.44,relheight=0.09)
    def delbookfetchdata(host,user, passw,db_con):
        bookid = bookInfo1.get()
        delbook(host,user, passw,db_con,bookid)
    delbookui.mainloop()

def delbook(host,user, passw,db_con,bookid):
    print('Deleting Book {} from the database'.format(bookid))
    logfile=open("Program Log.txt", "a+")
    runtime=datetime.datetime.now()
    logfile.write("\nDate and Time : {} - Deleting Book {} from the database ".format(runtime,bookid))
    logfile.close()
    con= mysql.connector.connect(host = host, user=user, passwd = passw, database =db_con)
    cur = con.cursor()
    cur.execute("delete from book_info where book_id='{}'".format(bookid))
    con.commit()
    cur.execute("update transaction_info set book_id='NA' where book_id='{}'".format(bookid))
    cur.execute("update transaction_info set date_returned='Never Returned' where book_id='{}'".format(bookid))
    con.commit()
    messagebox.showinfo('Success',"Book Information has benn Deleted Successfully and all the Transaction Records have been updated to Not Available (NA) ")  

def retbookcall(host,user, passw,db_con):     
    runtime=datetime.datetime.now()
    logfile=open("Program Log.txt", "a+")
    logfile.write("\nDate and Time : {} - Return Book Window Accessed".format(runtime))
    logfile.close()
    retbookui = tk.Toplevel()
    retbookui.title("Reader's Club - Record a Return")
    retbookui.state=("zoomed")
    retbookui['bg']='Dark Blue'
    retbookui.iconbitmap('readersclubicon.ico')
    con= mysql.connector.connect(host = host, user=user, passwd = passw, database =db_con)
    cur = con.cursor()
    sizing=True
    background_image1 =Image.open("readers.jpg")
    [imgwid, imgh] = background_image1.size
    newimgwid = int(imgwid*0.9)
    if sizing:
        newimgh = int(imgh*1.35) 
    else:
        newimgh = int(imgh/1.35) 
    background_image1 = background_image1.resize((newimgwid,newimgh),Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(background_image1)
    Canvasrbu = Canvas(retbookui)
    Canvasrbu.create_image(300,340,image = img1)      
    Canvasrbu.config(bg="Dark Blue",width = newimgwid, height = newimgh)
    Canvasrbu.pack(expand=True,fill=BOTH)
    headingFrame1 = Frame(retbookui,bg="Red",bd=5)
    headingFrame1.place(relx=0.55,rely=0.02,relwidth=0.44,relheight=0.13)    
    headingLabel = Label(headingFrame1, text="Record a Return", bg='Cyan', fg='Dark Blue',font=('Comic Sans Ms',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(retbookui,bg='black')
    labelFrame.place(relx=0.55,rely=0.16,relwidth=0.44,relheight=0.5)       
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='pink',font=('Comic Sans Ms',12))
    lb1.place(relx=0.05,rely=0.5)
    retid=tk.StringVar()
    bookInfo1 = ttk.Combobox(labelFrame,textvariable=retid,font=('Comic Sans Ms',12))
    cur.execute('select book_id from transaction_info where date_returned="Not Returned"')
    lis=[]
    for i in cur:
        lis.append(i)
    bookInfo1['values']=lis
    bookInfo1['state']='readonly'
    bookInfo1.place(relx=0.2,rely=0.5, relwidth=0.62)
    SubmitBtn = Button(retbookui,text="Return",bg='Dark Green', fg='White',command=lambda : retbookfetchdata(host,user, passw,db_con),font=('Comic Sans Ms',12))
    SubmitBtn.place(relx=0.55,rely=0.8, relwidth=0.15,relheight=0.08)
    quitBtn = Button(retbookui,text="Quit",bg='Red', fg='White',font=('Comic Sans Ms',12), command=retbookui.destroy)
    quitBtn.place(relx=0.83,rely=0.8, relwidth=0.15,relheight=0.08)
    infolbl=Label(retbookui,text="Made by : Nikhil Handa",bg="Dark Blue",fg="White",font=('Comic Sans Ms',13))
    infolbl.place(relx=0.55,rely=0.9,relwidth=0.44,relheight=0.09)
    def retbookfetchdata(host,user, passw,db_con):
        bookid = bookInfo1.get()
        retbook(host,user, passw,db_con,bookid)
    retbookui.mainloop()

def retbook(host,user, passw,db_con,bookid):
    runtime=datetime.datetime.now()
    logfile=open("Program Log.txt", "a+")
    logfile.write("\nDate and Time : {} - Book {} Returned ".format(runtime,bookid))
    print('Recording a Return')
    logfile.close()
    con= mysql.connector.connect(host = host, user=user, passwd = passw, database =db_con)
    cur = con.cursor()
    datetimeinput=datetime.date.today()
    cur.execute("select date_issued from transaction_info where book_id='{}' and date_returned='Not Returned' ".format(bookid))
    for i in cur:
        a=i[0]
        a=datetime.datetime.strptime(a, '%Y-%m-%d').date()
        daysdiff=(datetimeinput-a).days
        if daysdiff > 30:
            mon=daysdiff%30
            fine=mon*50
            cur.execute("select issued_to from transaction_info where book_id='{}' and date_returned='Not Returned' ".format(bookid))
            for a in cur:
                violator=a[0]
            cur.execute("update transaction_info set fine={} where book_id='{}' and date_returned='Not Returned' ".format(fine,bookid))
            finefile=open("Fine History.txt", "a+")
            finefile.write("\nName of Violator : {} Book Id : {} Days Kept : {} Fine : {} Payment Id : By Cash".format(violator,bookid,daysdiff,fine))
            finefile.close()
            runtime=datetime.datetime.now()
            logfile.write("\n\nDate and Time : {} - Fine Imposed on {} for Late Return".format(runtime,violator))
            messagebox.showinfo('Fine to be Paid',"Fine of Rs. {} is to be paid for the violation of Return Rules. The Challan Document has been saved to your folder.".format(fine))
        else :
            fine=0  
    cur.execute("update transaction_info set fine={} where book_id='{}' and date_returned='Not Returned' ".format(fine,bookid))
    cur.execute("update transaction_info set date_returned='{}' where book_id='{}' and date_returned='Not Returned' ".format(datetimeinput,bookid))
    con.commit()
    cur.execute("update book_info set book_status='Available' where book_id='{}'".format(bookid))
    con.commit()
    messagebox.showinfo('Success',"Book Status has benn Updated Successfully and the Transaction Record have been updated with Return Date ")
           
def connect():
    host=h.get()
    user = Username.get()
    passw = password.get()
    db_con=Database.get()
    logintodb(host,user, passw,db_con)
    
        
root = tk.Tk()
myFont = font.Font(family='Comic Sans Ms', size=10, weight='bold')
root['bg']='Dark Blue'
root.geometry("440x300")
root.iconbitmap('readersclubicon.ico')
root.title("Login - Reader's Club ")
lblfrstrow = tk.Label(root, text ="Host :",bg='Dark Blue',fg='White')
lblfrstrow['font']=myFont
lblfrstrow.place(x=50,y=20,height=20)
h = tk.Entry(root, width = 45)
h['font']=myFont
h.place(x = 150, y = 20, width = 100,height=22)

lblsecrow = tk.Label(root, text ="Username :",bg='Dark Blue',fg='White' )
lblsecrow['font']=myFont
lblsecrow.place(x=50,y=50,height=20,)
Username = tk.Entry(root, width = 45)
Username['font']=myFont
Username.place(x = 150, y = 50, width = 100,height=22)

lblthirdrow = tk.Label(root, text ="Password :",bg='Dark Blue',fg='White')
lblthirdrow['font']=myFont
lblthirdrow.place(x=50,y=80,height=20,)
password = tk.Entry(root,show='*', width = 45)
password['font']=myFont
password.place(x = 150, y = 80, width = 100,height=22)

lblfthrow = tk.Label(root, text ="Database :",bg='Dark Blue',fg='White')
lblfthrow['font']=myFont
lblfthrow.place(x = 50, y = 110,height=20)
Ldbtn = tk.Button(root, text ="Load Databases",bg ='Blue',fg='white', command = load_databases)
Ldbtn['font']=myFont
Ldbtn.place(x = 280, y = 110, width = 150, height=25)
Db=tk.StringVar()
Database = ttk.Combobox(root, width = 45,textvariable=Db)
Database.place(x = 150, y = 110,width = 100,height=22)
Database['font']=myFont
Database['state'] = 'readonly'

submitbtn = tk.Button(root, text ="Connect to Database",bg ='green',fg='white', command = connect)
submitbtn.place(x = 100, y = 170, width = 200,height=30)
submitbtn['font']=myFont

lblnamerow = tk.Label(root, text ="Made By Nikhil Handa",bg='Red',fg='White')
lblnamerow['font']=myFont
lblnamerow.place(x=100,y=250,width=200)

messagebox.showinfo('Information',"Select the Database where you want to initiate the Reader's Club. If you are an existing user, then select the database where you stored the previous data ")
root.mainloop()
