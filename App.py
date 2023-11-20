from tkinter import *
from tkinter import ttk
import sqlite3
from PIL import Image,ImageTk
from convertcod.internal_Loginstorge import get_loginAll,get_item
from LoginPage import LoginPage
from convertcod.processor import resource_path
# from multiprocessing import freeze_support
import pyglet

class App(Tk):
    def __init__(self,*args,**kwargs):
        Tk.__init__(self,*args,**kwargs)
        self.title('نظام الوقود')
        pyglet.font.add_file(resource_path("fount/Tajawal-Medium.ttf"))
        # pyglet.font.add_file(os.path.join("fount","Tajawal-Medium.ttf"))
        img = Image.open(resource_path("assets\\uzarh.png"))
        img.save(resource_path("assets\\uzarh2.png"))
        self.bgbuttom=ImageTk.PhotoImage(file=resource_path('assets\\uzarh.png'))
        self.bg=ImageTk.PhotoImage(file=resource_path("assets\\station2.png"))
        container = ttk.Frame(self,padding=(5,5))
        container.pack(side="top",fill="both", expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.style = ttk.Style(self)
        self.tk.call('source',resource_path("azure.tcl"))
        self.tk.call("set_theme", "dark")
        self.option_add("*tearOff", False)
        self.option_add("*Font",("Tajawal-Medium",15,"bold"))
        self.style.configure("Treeview", rowheight=40)
      
        # freeze_support()
   
        self.aciton= StringVar(value='new')
        self.creat_databise()
        from StartPage import StartPage
        self.page1 = StartPage
        self.page2 = LoginPage
        self.frames={}
        if get_loginAll() is not None or len(get_loginAll) > 0:
            self.usercount = get_loginAll()  
        else:
            self.usercount = []
        self.DataLoginNew=  get_item()
        for F in (self.page1,self.page2):
            frame= F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
        if len(self.usercount) > 0 :
            countentr = self.page2 
        else:
             countentr = self.page1
        self.Show_frame(countentr)
    def Show_frame(self,context):
        frame = self.frames[context]
        frame.tkraise()
    def creat_databise(self):
            conn = sqlite3.connect(resource_path("assets\\backup\\data.db"))
            # conn = sqlite3.connect(resource_path(".\\assets\\backup\\data.db"))
            table_create_Station = '''CREATE TABLE IF NOT EXISTS station 
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,incomingquantity INTEGER NOT NULL ,
            receivedData DATE NOT NULL, amountٍٍSpent INTEGER NULL, thermen INTEGER NULL ,
            DoneF TEXT NULL,expiryDate DATE NULL,aciton TEXT NOT NULL,classifyProcess TEXT NOT NULL ,Arrayjson JSON NULL)
            '''    
            table_create_qureypablic = '''CREATE TABLE IF NOT EXISTS station_pablic 
            (idusers INTEGER NOT NULL UNIQUE ,nameusefly TEXT NOT NULL ,  quantityOIL INTEGER NOT NULL,
            quantitydiesel INTEGER NOT NULL,DoneSub TEXT NULL, oprtionPush TEXT NULL,ACcrditionStatediesel TEXT NULL,
            ACcrditionStateOIL TEXT NULL,datatim DATE NULL,aciton TEXT NOT NULL,Arraypash JSON NULL )
            '''
            table_create_qurey = '''CREATE TABLE IF NOT EXISTS station_MonthD 
            (ID INTEGER PRIMARY KEY AUTOINCREMENT ,idHom INTEGER NULL ,idusers INTEGER NOT NULL ,
            nameusefly TEXT NOT NULL , quantityOIL INTEGER NOT NULL,quantitydiesel INTEGER NOT NULL, amountٍٍSpentOIL INTEGER  NULL, thermenOIL INTEGER  NULL ,
            amountٍٍSpentdiesel INTEGER  NULL, thermendiesel INTEGER  NULL,DoneSub TEXT NULL,ACcrditionStatediesel TEXT NULL,ACcrditionStateOIL TEXT NULL,
            datatim DATE  NULL DEFAULT  CURRENT_DATE,aciton TEXT NOT NULL,Arraypash JSON NULL)
            '''
            try:
                conn.execute(table_create_Station)
                conn.execute(table_create_qureypablic)
                conn.execute(table_create_qurey)
                # private python or python specificWWW
                #private insert named credits pablic 
            except sqlite3.IntegrityError:
                print("couldn't add Python twice")
            conn.commit() 
            conn.close()
            conecticion = sqlite3.connect(resource_path("assets\\backup\\data_storng.db"))
            # conecticion = sqlite3.connect(resource_path(".\\assets\\backup\\data_storng.db"))
            try:
                tabelNavigetion = '''CREATE TABLE IF NOT EXISTS movement (ID INTEGER PRIMARY KEY AUTOINCREMENT, userName TEXT NOT NULL,datamovement  DATE NULL DEFAULT CURRENT_DATE,
                kindMovement TEXT NULL , stayuser TEXT NOT NULL,dataExet DATE NULL, arrayMovement JSON NULL)'''
                tabelLogin = '''CREATE TABLE IF NOT EXISTS logtion (ID INTEGER PRIMARY KEY AUTOINCREMENT, userName TEXT NOT NULL UNIQUE, passwordUSER  TEXT NOT NULL,
                Responsibilities TEXT NOT NULL, jsonResponsibilities JSON NULL,datatim DATE NULL DEFAULT CURRENT_DATE) '''
                tabelLoginActivite = '''CREATE TABLE IF NOT EXISTS logtionActivite (ID INTEGER PRIMARY KEY AUTOINCREMENT, userName TEXT NOT NULL , passwordUSER  TEXT NOT NULL,
                Responsibilities TEXT NOT NULL,activity TEXT NOT NULL,jsonResponsibilities JSON NULL ,datatim DATE NULL DEFAULT CURRENT_DATE) '''
                tableselecter = '''CREATE TABLE IF NOT EXISTS selectAdddir (ID INTEGER PRIMARY KEY AUTOINCREMENT, dircarteAdd TEXT NOT NULL)'''
                table = '''CREATE TABLE IF NOT EXISTS selectPrinter (ID INTEGER PRIMARY KEY AUTOINCREMENT, dircarteUsb TEXT NOT NULL)'''
                tableData = '''CREATE TABLE IF NOT EXISTS selectData (ID INTEGER PRIMARY KEY AUTOINCREMENT, dirDatabase TEXT NOT NULL)'''
                tableSpent= '''CREATE TABLE IF NOT EXISTS cumulativeSum (ID INTEGER PRIMARY KEY AUTOINCREMENT, SumOIL INTEGER  NULL, Sumdiesel INTEGER  NULL)'''
                conecticion.execute(tabelNavigetion)
                conecticion.execute(tabelLogin)
                conecticion.execute(tabelLoginActivite)
                conecticion.execute(tableselecter)
                conecticion.execute(table)
                conecticion.execute(tableData)
                conecticion.execute(tableSpent)
            except sqlite3.IntegrityError:
                print("couldn't add python twice")
            conecticion.close()
if __name__ == "__main__":
    app = App()
    # app.update()
    app.attributes("-fullscreen",True)

    # app.overrideredirect(True)
    app.state("zoomed")
    app.minsize(app.winfo_width(),app.winfo_height())
    x_continer = int((app.winfo_screenwidth() /2) - (app.winfo_width()/2))
    y_continer = int((app.winfo_screenheight()/2) - (app.winfo_height()/2))
    app.geometry("+{}+{}".format(x_continer,y_continer -20))
    # .eval('tk::PlaceWindow . center')
    app.mainloop()