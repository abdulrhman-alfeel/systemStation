from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from classupAdd import MyClassAdd
from classupPush import MyClassPush
from classupStationAdd import StationAdd
from classupEidteSindrs import *
from convertcod.SumAll import *
from QurySerch import *
from PrintStatment import PrintStatment
from sqiltyFoun import StationMonthSqly
from datetime import datetime  
from Print.PrintDay import *
from convertcod.internal_storage import *
from Register import Register
from RegisterEdite import RegisterEdite
from convertcod.internal_Loginstorge import *
from graph import graph
from Print.viewpdf import switchMonth
from convertcod.userfind import findUser ,responsebletUser
from convertcod.insertSelectprinter import SelectPrinter, conectionEngneer,cumulative
import gc
from classupSpent import Spentincomeng 
import pyglet
from convertcod.backup import Backup ,BackupView
# aciton = 'new'
class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        # Navber = ttk.Frame(self,padding=5)
        pyglet.font.add_file("fount/Tajawal-Medium.ttf")
        global Reducing
        global widgets_frame
        # global fromAdd
        # global buttond
        global fromer_import
        global Print
        # Navber.pack(side='top', expand=True)
        

    
        def toggle_mode():
            if mode_switch.instate(["selected"]): 
                controller.call("set_theme","light")
                controller.style.configure("Treeview", font=('Tajawal', 16),rowheight=40)
            else: 
                controller.call("set_theme","dark")
                
        # ba1 = ttk.Frame(Navber)
        # # ba1.grid(row=0,column=0)
        # ba1.pack(side='right',anchor='n',padx=10)

        amounteSp = ttk.Frame(self)
        amounteSp.pack(side="top",anchor="ne")
        # amounteSp.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        # amounteSp.place(x=650,y=10)
        viewSpenِAllstationnavber = ttk.Frame(amounteSp)
        viewSpenِAllstationnavber.pack(side='right',anchor='ne',pady=2,padx=5)
        buttona = ttk.Button(viewSpenِAllstationnavber,style="Accent.TButton", 
                             text="اغلاق", command=lambda:self.Exetjop('exit','') )
        buttona.grid(row=0, column=8, padx=5, pady=2, sticky="nsew")
        buttonf = ttk.Button(viewSpenِAllstationnavber,style="Accent.TButton", 
                             text="تسجيل الخروج", command=lambda:self.Exetjop('exitUser',controller) )
        buttonf.grid(row=0, column=7, padx=5, pady=2, sticky="nsew")
        buttones = ttk.Button(viewSpenِAllstationnavber,style="Accent.TButton", 
                              text="فتح حساب", command=lambda:self.Show_frame(self.page7,'openAcount'))
        buttones.grid(row=0, column=6, padx=5, pady=2, sticky="nsew")
        buttonq = ttk.Button(viewSpenِAllstationnavber,style="Accent.TButton",
                             text="تعديل صلاحيات ",command=lambda:self.Show_frame(self.page8,'powers'))
        buttonq.grid(row=0, column=5, padx=5, pady=2, sticky="nsew")
        buttond = ttk.Button(viewSpenِAllstationnavber,style="Accent.TButton", 
                             text="حركة الدخول", command=self.postPopUpMenu)
        buttond.grid(row=0, column=4, padx=5, pady=2, sticky="nsew")
        quryserch = ttk.Button(viewSpenِAllstationnavber,style="Accent.TButton", text="البحث والاستعلام", command=lambda:self.Show_frame(self.page3,'search'))
        quryserch.grid(row=0, column=3, padx=5, pady=2, sticky="nsew")
        Print = ttk.Button(viewSpenِAllstationnavber,style="Accent.TButton", text="طباعة", command=self.printOprtion)
        Print.grid(row=0, column=2, padx=5, pady=2, sticky="nsew")
        Reducing = ttk.Button(viewSpenِAllstationnavber,style="Accent.TButton", text="خيارات",command=self.Readucing)
        Reducing.grid(row=0, column=1, padx=5, pady=2, sticky="nsew")
 
        mode_switch = ttk.Checkbutton(viewSpenِAllstationnavber, text="تبديل", style="Switch.TCheckbutton", command=toggle_mode)
        mode_switch.grid(row=0,column=0)

        viewSpen = ttk.LabelFrame(self)
        # viewSpen.grid(row=1,column=0,sticky="nsew",padx=40,pady=10)
        viewSpen.pack(side='top',padx=10,pady=5)
#  اجمالي الديزل
        viewSpenDiesel = ttk.Frame(viewSpen)
        viewSpenDiesel.pack(side="right",anchor='ne',fill='both',padx=10,pady=5)
        viewSpenِAllstationdiesel = ttk.Frame(viewSpenDiesel)
        viewSpenِAllstationdiesel.grid(row=1,column=0,padx=5,pady=5,sticky="nsew")
        viewAlldiesel= ttk.Frame(viewSpenDiesel)
        viewAlldiesel.grid(row=0,column=0,padx=5,pady=5,sticky='nsew')
        # viewAlldiesel.anchor('n')
        textSpenAlldieseltext = ttk.Label(viewAlldiesel, text="الديزل",font=("Tajawal",18))
        textSpenAlldieseltext.grid(row=1,column=3,padx=5,pady=5,sticky="nsew")
        # textSpenAlldiesel.place(x=600,y=40)
        textSpenAlldiesel = ttk.Label(viewAlldiesel, text="اجمالي التراكمي ",font=("Tajawal",18))
        textSpenAlldiesel.grid(row=0,column=2,padx=5,pady=5)
        self.textnuberAlldiesel = ttk.Label(viewAlldiesel)
        self.textnuberAlldiesel.grid(row=1,column=2,padx=25,pady=5,sticky='nsew')
        textSpendiesel = ttk.Label(viewAlldiesel, text="اجمالي الحمولة لهذا الشهر",font=("Tajawal",18))
        textSpendiesel.grid(row=0,column=1,padx=25,pady=5,sticky="nsew")
        self.textnuberAllMonthdiesel = ttk.Label(viewAlldiesel)
        self.textnuberAllMonthdiesel.grid(row=1,column=1,padx=25,pady=5,sticky='nsew')
        # # اجمالية الحمولة المتبقية 
        textSpenthermdiesel = ttk.Label(viewSpenِAllstationdiesel, text=":اجمالي المتبقي الكلي",font=("Tajawal",18))
        textSpenthermdiesel.grid(row=0,column=5,padx=11,pady=5,sticky="nsew")
        self.textnuberdiesel = ttk.Label(viewSpenِAllstationdiesel)
        self.textnuberdiesel.grid(row=1,column=5,padx=11,pady=5,sticky='nsew')
        # اجمالية الحمولة المتبقية الشهري
        textSpenmonthdiesel = ttk.Label(viewSpenِAllstationdiesel, text=":اجمالي المتبقي من حمولة الشهر",font=("Tajawal",18))
        textSpenmonthdiesel.grid(row=0,column=7,padx=11,pady=5,sticky="nsew")
        self.textnubermonthdiesel = ttk.Label(viewSpenِAllstationdiesel)
        self.textnubermonthdiesel.grid(row=1,column=7,padx=11,pady=5,sticky='nsew')
        # اجمالي الصرف اليوم 
        textSpendaydisel = ttk.Label(viewSpenِAllstationdiesel, text=":اجمالي الصرف اليوم ",font=("Tajawal",18))
        textSpendaydisel.grid(row=0,column=9,padx=11,pady=5,sticky="nsew")
        self.nuberdiesel = ttk.Label(viewSpenِAllstationdiesel)
        self.nuberdiesel.grid(row=1,column=9,padx=11,pady=5,sticky='nsew')
        # اجمالي البترول
        # اجمالي الحمولة التراكمية 
        viewSpenOil = ttk.Frame(viewSpen)
        viewSpenOil.pack(side="right",anchor='ne',fill='both',padx=10,pady=5)
        viewSpenِAllstation = ttk.Frame(viewSpenOil)
        viewSpenِAllstation.grid(row=1,column=0,padx=5,pady=5)
        viewAll= ttk.Frame(viewSpenOil)
        viewAll.grid(row=0,column=0,padx=5,pady=5)
        textSpenAlltext = ttk.Label(viewAll, text="البترول",font=("Tajawal",18))
        textSpenAlltext.grid(row=1,column=5,padx=11,pady=5)
        textSpenAll = ttk.Label(viewAll, text="اجمالي التراكمي",font=("Tajawal",18))
        textSpenAll.grid(row=0,column=4,padx=11,pady=5)
        self.textnuberAll = ttk.Label(viewAll)
        self.textnuberAll.grid(row=1,column=4,padx=25,pady=5,sticky='nsew')
        textSpentext = ttk.Label(viewAll, text="اجمالي الحمولة لهذا الشهر",font=("Tajawal",18))
        textSpentext.grid(row=0,column=2,padx=25,pady=5,sticky="nsew")
        self.textnuberAllMonth = ttk.Label(viewAll)
        self.textnuberAllMonth.grid(row=1,column=2,padx=25,pady=5,sticky='nsew')
        # # اجمالية الحمولة المتبقية 
        textSpentexts = ttk.Label(viewSpenِAllstation, text=":اجمالي المتبقي الكلي",font=("Tajawal",18))
        textSpentexts.grid(row=0,column=5,padx=11,sticky="nsew")
        self.textnuber = ttk.Label(viewSpenِAllstation)
        self.textnuber.grid(row=1,column=5,padx=11,sticky='nsew')
        # اجمالية الحمولة المتبقية الشهري
        textSpenmonth = ttk.Label(viewSpenِAllstation, text=":اجمالي المتبقي من حمولة الشهر",font=("Tajawal",18))
        textSpenmonth.grid(row=0,column=7,padx=11,sticky="nsew")
        self.textnubermonth = ttk.Label(viewSpenِAllstation)
        self.textnubermonth.grid(row=1,column=7,padx=11,sticky='nsew')
        # اجمالي الصرف اليوم 
        textSpen = ttk.Label(viewSpenِAllstation, text=":اجمالي الصرف اليوم",font=("Tajawal",18))
        textSpen.grid(row=0,column=9,padx=11,sticky="nsew")
        self.nuber = ttk.Label(viewSpenِAllstation)
        self.nuber.grid(row=1,column=9,padx=11,sticky='nsew')
        # frame.place(y=-40)      
        container = ttk.LabelFrame(self)
        container.pack(side="top",fill='both',anchor="center", expand=True)
        # fromAdd = ttk.Frame(container,padding=(2,2),width=150)
        # # fromAdd.place(x=1685,y=50)
        # fromAdd.grid(row=1,column=1,sticky='nsew')
        widgets_frame = ttk.LabelFrame(container)
        widgets_frame.grid(row=1,column=1,padx=10,pady=10)
        lable_list = ttk.Button(widgets_frame,text="حساب اعتماد جديد",
                                command=lambda:self.Show_frame(self.page4,{'ACount'}),width=17)
        lable_list.grid(row=0,column=0,padx=6, pady=10)
        lable_cash = ttk.Button(widgets_frame,text="صرف بترول",width=17,command=self.founPush)
        lable_cash.grid(row=1, column=0,padx=6, pady=10)
        lable_cash = ttk.Button(widgets_frame,text="صرف ديزل",width=17,command=self.founPushDISBLI)
        lable_cash.grid(row=2, column=0,padx=6, pady=10)
        lable_import = ttk.Button(widgets_frame,text="حمولة جديدة",
                                  command=lambda:self.Show_frame(self.page5,{'ALL'}),width=17)
        lable_import.grid(row=3, column=0,padx=6, pady=10)
        sindrs_import = ttk.Button(widgets_frame,text="تعديل حساب النثريات",
                                   command=lambda:self.Show_frame(self.page2,{'sinders'}),width=17)
        sindrs_import.grid(row=5, column=0,padx=6, pady=10)
        fromer_import = ttk.Button(widgets_frame,text="سحب باقي الحمولة ",width=17,
                                   command=lambda:self.postPopUpMenuFarmer("drag"))
        fromer_import.grid(row=7, column=0,padx=6, pady=10)      
      
        self.page1 = MyClassPush
        self.page2 = SindrsEdit
        self.page3 = QurySerch
        self.page4= MyClassAdd
        self.page5= StationAdd
        self.page6= PrintStatment
        self.page7 = Register
        self.page8= RegisterEdite   
        self.page9 = graph
        self.page10 = Spentincomeng
        self.usercount = controller.usercount
        self.frames={}
        
        currentpage = self.page1 if len(self.usercount) > 0 else self.page7
        for F in (self.page1,self.page2,self.page3,self.page4,self.page5,self.page6,self.page8,self.page7,self.page9,self.page10):
            frame= F(container,self)
            self.frames[F] = frame
            frame.grid(row=1,column=0,sticky='nsew')
        self.Show_frame(currentpage,{"name1" : 'OIL',"name2":'new',"Time":datetime.now().date()})
        self.SumAcon()
    def Show_frame(self,context,kind):
        self.framCash = tk.StringVar()
        users = findUser()
        if users == True:
            empty = {"userName":""}
            self.getuser = get_item() if len(get_item()) > 0 else empty
            usersactyle = responsebletUser()
            if context == self.page1:
                        self.startworking(users,context)
                        self.framCash.set(kind)
                        self.page1.empytePage(self)
                        self.page1.lodKindPage(self,kind)
                        self.page1.load_data(self,"اعتمادات")
                        # self.empyate(context=self.page1)
                        if kind['name2'] == 'previous':
                            set_itemx(self.getuser['userName'],'حساب سابق بترول'if kind['name1'] == 'OIL' else 'حساب سابق ديزل')
                        else:
                            set_itemx(self.getuser['userName'],'بترول'if kind['name1'] == 'OIL' else 'ديزل')
            elif context == self.page2:
                if usersactyle['Responsibilities'].replace(" ","") == 'المسؤل المباشر'.replace(" ",""):
                        self.startworking(users,context)
                        self.page2.lodDataEditSendrs(self)
                        set_itemx(self.getuser['userName'],'تعديل النثريات')
                        #  print('sindrissssss')
                else:
                        messagebox.showwarning(title="Error",message="ليس لديك الصلاحية الكافية للدخول")
            elif context == self.page3 :
                self.startworking(users,context)
                set_itemx(self.getuser['userName'],'محرك البحث')
                self.page3.loadqury()
            elif context == self.page4  and kind == {'ACount'}:
                if usersactyle['Responsibilities'].replace(" ","") == 'المسؤل المباشر'.replace(" ","") or usersactyle['إضافة_وتعديل_اعتماد'] == 'true'or usersactyle['توقيف_اعتماد'] == 'true':
                            self.startworking(users,context)
                            set_itemx(self.getuser['userName'],'صفحة اضافة الاعتمادات')
                else:
                        messagebox.showwarning(title="Error",message="ليس لديك الصلاحية الكافية للدخول")
            elif context == self.page4  and kind == {'Start'} :
                        self.startworking(users,context)
                        itemuser = get_virfe()
                        self.page4.findmovement(itemuser)
            elif context == self.page5  and kind =={'Start'} :
                        self.startworking(users,context)
                        itemuser = get_virfe()
                        self.page5.findmovement(itemuser)
            elif context == self.page5  and kind =={'ALL'} :
                if usersactyle['Responsibilities'].replace(" ","") == 'المسؤل المباشر'.replace(" ","") or usersactyle['التوريد_بكميات_جديدة'] == 'true':
                        self.startworking(users,context)
                        set_itemx(self.getuser['userName'],'صفحة اضافة حمولة')
                        self.page5.load_data(self)
                else:
                        messagebox.showwarning(title="Error",message="ليس لديك الصلاحية الكافية للدخول")
            elif context == self.page6 :
                if usersactyle['Responsibilities'].replace(" ","") == 'المسؤل المباشر'.replace(" ","") or usersactyle['طباعة_تقارير'] == 'true':
                    self.startworking(users,context)
                    set_itemx(self.getuser['userName'],'صفحة الطباعة')
                else:
                    messagebox.showwarning(title="Error",message="ليس لديك الصلاحية الكافية للدخول")
            elif context == self.page7 :
                if usersactyle['Responsibilities'].replace(" ","") == 'المسؤل المباشر'.replace(" ",""):
                    self.startworking(users,context)
                    set_itemx(self.getuser['userName'],'صفحة تسجيل مستخدم جديد') 
                else:
                    messagebox.showwarning(title="Error",message="ليس لديك الصلاحية الكافية للدخول")
            elif context == self.page8:
                if usersactyle['Responsibilities'].replace(" ","") == 'المسؤل المباشر'.replace(" ",""):
                        self.startworking(users,context)
                        set_itemx(self.getuser['userName'],'صفحة تعديل حساب مستخدم') 
                else:
                        messagebox.showwarning(title="Error",message="ليس لديك الصلاحية الكافية للدخول")
            elif context == self.page9:
                if usersactyle['Responsibilities'].replace(" ","") == 'المسؤل المباشر'.replace(" ",""):
                    self.startworking(users,context)
                    set_itemx(self.getuser['userName'],'صفحة حركة المستخدم')      
                    self.page9.loden(self)
                else:
                    messagebox.showwarning(title="Error",message="ليس لديك الصلاحية الكافية للدخول")
            else:
              if usersactyle['Responsibilities'].replace(" ","") == 'المسؤل المباشر'.replace(" ",""):
                # print(kind['pableic'])
                self.page10.lodData(self,kind['pableic']) 
                self.startworking(users,context)
                set_itemx(self.getuser['userName'],'سحب الكمية المتبقية') 
              else:
                messagebox.showwarning(title="صلاحية المسؤل",message='ليس لديك الصلاحية الكافية لتنفيذ العملية')
        else:
            self.startworking(users,context)
        self.distripShow(context)
    def startworking(self,users,context):
        if users == True:
            frame = self.frames[context] 
        else:
            frame = self.frames[self.page7]
        frame.tkraise()   
        
    def distripShow(self,page):
         for Fd in (self.page1,self.page2,self.page3,self.page4,self.page5,self.page6,self.page8,self.page7,self.page9,self.page10):
            if Fd != page: 
                for widget in Fd.winfo_children(self):
                         widget.destroy
    def chack(self,item,kind,dr,o):
        return item['aciton'] == 'previous' and item["DoneF"] == 'false' and item['classifyProcess'] == o and int(item['thermen']) > 0 and kind == dr         
    def postPopUpMenuFarmer(self,kind): 
        try:
            if findUser() == True:    
                station =  StationMonthSqly.inComin_dataAll()
                popUpMenu = tk.Menu(fromer_import, tearoff=0)
                Menudiesel = tk.Menu(popUpMenu, tearoff=0)
                MenuOIl = tk.Menu(popUpMenu, tearoff=0)
                findDatat = next((pic for pic in station  if pic['aciton'] == 'previous' and pic["DoneF"] == 'false'),None)
                if findDatat is not None:
                    if findDatat['aciton'] == 'previous' and findDatat["DoneF"] == 'false' and findDatat['classifyProcess'] == 'diesel' and int(findDatat['thermen']) > 0:
                        popUpMenu.add_cascade(menu=Menudiesel, label="ديزل" )
                    if  findDatat['aciton'] == 'previous' and findDatat["DoneF"] == 'false' and findDatat['classifyProcess'] == 'OIL' and int(findDatat['thermen']) > 0:
                        popUpMenu.add_cascade(menu=MenuOIl, label="بترول" )
                    for item in station:
                            if self.chack(item,kind,'drag',"diesel"):
                                    abdun = item
                                    Menudiesel.add_command(label=switchMonth(datetime.strptime(item['receivedData'],'%Y-%m-%d').strftime('%B')),command=lambda: 
                                    self.Show_frame(self.page10,{"pableic":abdun}), accelerator='')
                                    Menudiesel.add_separator()
                            if self.chack(item,kind,'drag',"OIL"):
                                    # print('ooys Oil',item)
                                abdun = item
                                MenuOIl.add_command(label=switchMonth(datetime.strptime(item['receivedData'],'%Y-%m-%d').strftime('%B')),command=lambda:self.Show_frame(self.page10,{"pableic":abdun}), accelerator='')
                                MenuOIl.add_separator()
                else:
                    messagebox.showwarning(message="لايوجد هناك حمولة سابقة")
                valuesx = fromer_import.winfo_rootx()
                valuesy = fromer_import.winfo_rooty()
                popUpMenu.post(valuesx,valuesy)     
                # else:
                    # messagebox.showwarning(title="خطاء بيانات",message='لايوجد هناك حمولة سابقة')
        except:
            pass   
    def postPopUpMenu(self):
        if findUser() == True: 
            self.Show_frame(self.page9,{'data graph'})         
    def SumAcon(self):
        if findUser() == True: 
            loaddata(self.nuber,self.textnubermonth,"OIL")        
            loadDatastation(self.textnuberAllMonth,self.textnuberAll,self.textnuber,'OIL')    
            gc.collect()     
            loaddata(self.nuberdiesel,self.textnubermonthdiesel,"diesel")        
            loadDatastation(self.textnuberAllMonthdiesel,self.textnuberAlldiesel,self.textnuberdiesel,'diesel')   
    def vewBackup(self):
        BackupView()
        self.Show_frame(self.page1,{"name1" : 'OIL',"name2":'new',"Time":datetime.now().date()})
    def Readucing(self):
        try:
            if findUser() == True:
                usersactyle = responsebletUser()
                if usersactyle['Responsibilities'].replace(" ","") == 'المسؤل المباشر'.replace(" ",""):
                    MaunReaducing = tk.Menu(Reducing, tearoff=0)
                    Readuci = tk.Menu(MaunReaducing,tearoff=0)
                    copyBack = tk.Menu(MaunReaducing,tearoff=0)
                    MaunReaducing.add_cascade(menu=Readuci,label="تقليص اعتمادات",underline=5,accelerator=" ")
                    MaunReaducing.add_command(label="تبديل منفذ الطابعة",underline=5,command=lambda:SelectPrinter(Reducing),accelerator=" ")
                    MaunReaducing.add_command(label="حساب التراكمي",underline=5,command=lambda:cumulative(Reducing),accelerator=" ")
                    MaunReaducing.add_cascade(label="نسخ احتياطي",underline=5,menu=copyBack,accelerator=" ")
                    MaunReaducing.add_command(label="للتواصل بالدعم",underline=5,command=lambda:conectionEngneer(Reducing),accelerator=" ")
                  
                    copyBack.add_command(label="نسخ",underline=5, command=Backup,accelerator=" ")
                    copyBack.add_separator()
                    copyBack.add_command(label="استيراد",underline=5,command=self.vewBackup,accelerator=" ")
                    copyBack.add_separator()
                    Readuci.add_command(label="اعتمادات الديزل", underline=5,command=lambda:self.virefiinsert("diesel"),accelerator=" ")
                    Readuci.add_separator()
                    Readuci.add_command(label="اعتماد البترول",underline=5,command=lambda:self.virefiinsert("OIL"),accelerator=" ")
                    Readuci.add_separator()
                    MaunReaducing.post(Reducing.winfo_rootx(),Reducing.winfo_rooty())
                else:
                    messagebox.showwarning(title="Error",message="ليس لديك الصلاحية الكافية لتنفيذ العملية")     
        except:
               print('error')
    def virefiinsert(self,kind):
         if findUser() == True:
            try:
                    empty = {"userName":""}
                    self.getuser = get_item() if len(get_item()) > 0 else empty
                    if kind == 'OIL':
                        set_itemx(self.getuser['userName'],'تقليص اعتمادات البترول')
                    else:
                        set_itemx(self.getuser['userName'],'تقليص اعتمادات الديزل')
                    quantity_pablic = 0
                    rival = 0
                    sumRival = 0
                    resulterival = 0
                    objectSum = {}
                    station = StationMonthSqly.inComin_dataAll()
                    pablic = StationMonthSqly.inCominSwitch_Pablic()
                    credits = next((item for item in station if item["DoneF"] == 'false' and  datetime.strptime(item['receivedData'],'%Y-%m-%d').month == datetime.now().month and item['classifyProcess'] == kind),None)
                    if credits is not None :
                        if pablic is not None :
                            for i in pablic :
                                if i['nameusefly'].replace(" ","").lower() != "نثريات".replace(" ","").lower() :
                                    quantity = int(i["quantityOIL"])  if kind == 'OIL' else int(i["quantitydiesel"]) 
                                    quantity_pablic += quantity
                            if int(quantity_pablic) > int(credits['incomingquantity']) or float(quantity_pablic) > int(credits['incomingquantity']):
                                rival =  quantity_pablic -  int(credits['incomingquantity']) 
                                sumRival =  rival /  quantity_pablic
                                for item in pablic:
                                    if item['nameusefly'].replace(" ","").lower() != "نثريات".replace(" ","").lower() :
                                                    quantity = int(item["quantityOIL"])  if kind == 'OIL' else int(i["quantitydiesel"]) 
                                                    resulterival =  quantity * sumRival
                                                    sumevll =  quantity  - resulterival 
                                                    objectSum["idusers"] = item['idusers']
                                                    objectSum["quantity"] =  int(float(sumevll))
                                                    StationMonthSqly.Update_pablic(objectSum,"OIL")                 
                                self.page4.load_data(self,'جاري','down')
                                messagebox.showinfo(title="تم", message="تمت العملية بنجاح")         
                            else:
                                    messagebox.showwarning(title="Error",message="لايمكن تقليص الفارق فالحمولة الموجودة اعلى من اجمالي الاعتمادات")
                        else:
                            messagebox.showwarning(title="Error", message="لايوجد اعتمادات مضافة حالياً")
                    else:
                        messagebox.showwarning(title="Error", message="لايوجد حمولة متاحة حالياً")
            except :
                print('هناك خطاء')      
    def founPush(self):
            self.Show_frame(self.page1,{"name1" : 'OIL',"name2":'new',"Time":datetime.now().date()}) 
    def founPushDISBLI(self):
            self.Show_frame(self.page1,{"name1" : 'diesel',"name2":'new',"Time":datetime.now().date()})
    def Exetjop(self,k,controller):
        try:
            empty = {"userName":""}
            self.getuser = get_item() if len(get_item()) > 0 else empty
            if k == 'exitUser':
                if findUser() == True:
                    controller.Show_frame(controller.page2)
                    self.Show_frame(self.page1,{"name1" : 'OIL',"name2":'new',"Time":datetime.now().date()})
                    set_itemx(self.getuser['userName'],'خروج المستخدم')   
                    set_loguot()
            else:
                set_itemx(self.getuser['userName'],'اغلاق') 
                set_loguot()
                self.quit()
        except:
            self.quit()

    def printOprtion(self):
        if findUser() == True:
            user = get_item()
            # print(user)
            # print(user['jsonResponsibilities'])
            jsonRespon = user['jsonResponsibilities']
            if user['Responsibilities'].replace(" ","") == 'المسؤول المباشر'.replace(" ","") or  jsonRespon['طباعة تقارير'].replace(" ","") == "true".replace(" ","") :
                self.Show_frame(self.page6,'print')
            else:
                    popUpMenu = tk.Menu(Print, tearoff=0, font=("Tajawal", 13))
                    popUpMenu.add_command(label="عرض",command=lambda: statament_day(varfetch={"type": "dayUser","user":user['userName'],'kindjop':'view'}), accelerator='')
                    popUpMenu.add_separator()
                    popUpMenu.add_command(label="طباعة",command=lambda:statament_day(varfetch={"type": "dayUser","user":user['userName'],'kindjop':'print','page':self}), accelerator='')
                    popUpMenu.add_separator()
                    valuesx = Print.winfo_rootx()
                    valuesy = Print.winfo_rooty()
                    # print(valuesx,valuesy)
                    popUpMenu.post(valuesx,valuesy) 