import tempfile
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, timedelta
import random
import barcode
from barcode.writer import ImageWriter
from sqiltyFoun import StationMonthSqly
# from escpos.printer import Serial
from convertcod.processor import on_KeyPress
from convertcod.userfind import *
from convertcod.internal_storage import *
from Print.printesbarcod import convertcarte
from convertcod.insertSelectprinter import SelectPrinter

# import asyncio
# from convertcod.ImageWriter import ImageWriter
# from wand.image import Image as wImage
# from wand.drawing import Drawing as wDrawing
# from wand.color import Color as wColor
# from PIL import Image,ImageDraw,ImageFont
# from snapshottest import TestCase, snapshot

    

class MyClassAdd(ttk.Frame):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)
        self.combo_list = ["Subscribed", "Not Subscribed", "Other"]
        start_date = datetime.now()
        # start_date = datetime(2023, 9, 1)
        self.ACcrditionStateOIL = "none"
        self.ACcrditionStatediesel = "none"
        end_date = datetime(2028, 9, 30)
        self.dates = []
        for day in range((end_date - start_date).days + 1):
         datall = start_date + timedelta(days=day)
         self.dates.append(datall.date())
        self.data = dict()
        self.Statimnt()
        self.load_data('جاري','موقف')
        # create radom
        
    def UpdateFunction(self,data):
        global ID
        pablicprosonl =StationMonthSqly.inComin_Pablic()
        datarefesh = next((item for item in pablicprosonl if item[0] == data[7]),None)
        if datarefesh is not None and str(data[6]).replace(" ","") != 'نثريات'.replace(" ",""):
                    ID = datarefesh[0]
                    name_entry.delete(0,"end")
                    name_entry.insert(0,datarefesh[1])
                    quantitydiesel_spinbox.delete(0, "end")
                    quantitydiesel_spinbox.insert(0, datarefesh[3])
                    quantityOIL_spinbox.delete(0, "end")
                    quantityOIL_spinbox.insert(0, datarefesh[2])
                    buttonInsert.config(text='تعديل',command=self.Updat_Acont)
                    if datarefesh[4] == "إدارة":
                        aP.set(value=False)
                        a.set(value=True)
                        checkbutton.state(["selected"])
                        checkbuttonPro.state(["!selected"])
                    else:
                        aP.set(value=True)
                        a.set(value=False)
                        checkbutton.state(["!selected"])
                        checkbuttonPro.state(["selected"])
    def Statimnt(self):
        global treeview
        # global treeFrame
        global name_entry
        global a
        global aP
        global quantitydiesel_spinbox
        global quantityOIL_spinbox
        global status_combobox
        global checkbutton
        global checkbuttonPro
        global buttonInsert
        global oneFrame
        global textStat
        global contener
        def select(kind):
            if kind == 'إدارة':
                checkbuttonPro.state(["!selected"])
                aP.set(value=False)
            else:
                checkbutton.state(["!selected"])
                a.set(value=False)
        oneFrame = ttk.LabelFrame(self,padding=(10,10),width=200)
        # oneFrame.grid(row=0,column=1, pady=5)
        oneFrame.pack(side='right',anchor='center',fill='both',padx=5,pady=10)
        contener = ttk.Frame(oneFrame,width=40)
        contener.grid(row=0,column=0,padx=10,pady=10)
        
        textStat = ttk.Label(contener,text='لابد من اضافة المستفيدين  قبل البد باي عملية')
        textStat.grid_forget()
        
        name_entry = ttk.Entry(contener,width=40)
        name_entry.insert(0, "اسم المستفيد")
        name_entry.bind("<FocusIn>", lambda e: name_entry.delete('0', "end"))
        # name_entry.columnconfigure((1,2,2),weight=200)
        name_entry.grid(row=1, column=0,padx=10, pady=15, sticky="ew")
        
        frameclass = ttk.Frame(contener,width=40)
        frameclass.grid(row=2,column=0,padx=10,pady=10)
        
        quantitydiesel_spinbox = ttk.Spinbox(frameclass, from_=18, to=100,width=16)
        quantitydiesel_spinbox.grid(row=0, column=0,padx=5, pady=5)
        quantitydiesel_spinbox.insert(0, "اعتماد الديزل")
        quantitydiesel_spinbox.bind("<FocusIn>", lambda e: quantitydiesel_spinbox.delete('0', "end"))
        quantitydiesel_spinbox.bind("<KeyRelease>",lambda e :self.keypresslisn(quantitydiesel_spinbox,e))
        
        quantityOIL_spinbox = ttk.Spinbox(frameclass, from_=18, to=100,width=16 )
        quantityOIL_spinbox.grid(row=0, column=1,padx=5, pady=5)
        quantityOIL_spinbox.insert(0, "اعتماد البترول")
        quantityOIL_spinbox.bind("<FocusIn>", lambda e:quantityOIL_spinbox.delete('0', "end"))
        quantityOIL_spinbox.bind("<KeyRelease>",lambda e :self.keypresslisn(quantityOIL_spinbox,e))
            
        status_combobox = ttk.Combobox(contener, values=self.dates)
        status_combobox.grid(row=3, column=0,padx=15, pady=15, sticky="ew")
        status_combobox.set(self.dates[0])
        a = tk.BooleanVar(value=False)
        treyF = ttk.Frame(contener)
        treyF.grid(row=4, column=0,padx=15, pady=15, sticky="ew")
        checkbutton = ttk.Checkbutton(treyF, text="إدارة", variable=a)
        checkbutton.grid(row=0, column=0,padx=15, pady=15, sticky="ew")
        checkbutton.bind("<FocusIn>", lambda e: select("إدارة") )
        aP = tk.BooleanVar(value=True)
        checkbuttonPro = ttk.Checkbutton(treyF, text="شخصي", variable=aP )
        checkbuttonPro.grid(row=0, column=1,padx=15, pady=15, sticky="ew")
        checkbuttonPro.bind("<FocusIn>", lambda e: select("شخصي") )
      
        buttonInsert = ttk.Button(contener,text="ادخال", command=lambda:self.awiating(),width=30)
        buttonInsert.grid(row=5, column=0,padx=10, pady=15, sticky="nsew")
        # buttonEdit = ttk.Button(fromBattom,text="تعديل", command=self.Updat_Acont,width=30)
        # buttonEdit.pack_forget()--

        separator = ttk.Separator(contener,orient="vertical")
        separator.grid(row=6, column=0, padx=(5,5), pady=20, sticky="nsew")

        treeFrame = ttk.Frame(self,width=1100,height=500)
        # treeFrame.grid(row=0,column=0, pady=5,padx=5)
        treeFrame.pack(side='left',anchor='n',expand=True)
        formBottom = ttk.Frame(treeFrame)
        formBottom.pack(sid='bottom',anchor='sw')
        button = ttk.Button(formBottom,text="محذوف", command=lambda:self.switchDatat('محذوف',''),width=30)
        button.grid(row=0,column=0, padx=10,pady=10)
        buttoncontin = ttk.Button(formBottom,text="جاري", command=lambda:self.switchDatat('جاري','موقف'),width=30)
        buttoncontin.grid(row=0,column=1, padx=10,pady=10)
        treeFrame.pack_propagate(0)
        treeScroll = ttk.Scrollbar(treeFrame)
        treeScroll.pack(side="right", fill="y")
        cols= ("حالة البترول","حالة الديزل","التاريخ","نوع الاعتماد", "الكمية من الديزل","الكمية من البترول","اسم المستفيد","رمز الباركود")
        treeview = ttk.Treeview(treeFrame, show="headings",yscrollcommand=treeScroll.set, columns=cols,height=500)
        treeview.column("رمز الباركود",width=180,anchor="center")
        treeview.column("اسم المستفيد",width=200,anchor="center")
        treeview.column("الكمية من الديزل",width=150,anchor="center")
        treeview.column("الكمية من البترول",width=150,anchor="center")
        treeview.column("نوع الاعتماد",width=70,anchor="center")
        treeview.column("التاريخ",width=150,anchor="center")
        treeview.column("حالة الديزل",width=90,anchor="center")
        treeview.column("حالة البترول",width=90,anchor="center")
        treeview.tag_bind("row", "<Button-3>", lambda event: self.founction(event))
        treeview.pack()
        treeScroll.config(command=treeview.yview)
     
    def findmovement(itemuser):
            global movment
            movment = itemuser
            if itemuser["kindMovment"].replace(" ","") == 'بداية تشغيل'.replace(" ",""):
                textStat.grid(row=0,column=0,padx=5,pady=5)
                
    def NumberGenerter(self):
            num1= "0123456789"
            num2 = "0123456789"
            number = num1 + num2
            length = 12 
            result = "".join(random.sample(number,length))
            print(result)
            return result
        
    def barcodnther(self,idUser,name,quantityoil,quantitydiesel): 
        try:   
            print(name)
            creat_nather = barcode.get_barcode_class("ean13")
            generated = creat_nather(idUser , writer=ImageWriter())
            fil = tempfile.mkstemp()
            # fil =f'.\\assets\\{name}'
            generated.save(f"{fil[1]}")
            self.data[generated] = [quantityoil,quantitydiesel, f"{fil[1]}.png"]
            print(generated)
            return generated , fil
        except:
            messagebox.showwarning(title='error barcod',message='خطاء في الباركود')
            
        #   function  Edite 
    def keypresslisn(self,num,event):
        on_KeyPress(num,event)
        if event.keysym == 'Return':
               self.awiating()
     
    def awiating(self):
        kindpag = buttonInsert.config('text')[4]
        if kindpag.lower().replace(" ","") == 'ادخال'.lower().replace(" ",""):
              self.insert_row()
        else:
             self.Updat_Acont()
        gc.collect()
        
    def insert_row(self):
        # try:
            pablic = StationMonthSqly.inComin_Pablic()
            keyhush = 0
            keyDelet = 0
            name = name_entry.get()
            # jopderc= jop_name.get()
            if quantityOIL_spinbox.get() == "اعتماد البترول" :
                quantityoil= 0
            else:
                quantityoil= int(quantityOIL_spinbox.get()) if len(quantityOIL_spinbox.get()) > 0 else 0 
            if quantitydiesel_spinbox.get() == "اعتماد الديزل":
                quantitydiesel= 0
            else:
                 quantitydiesel= int(quantitydiesel_spinbox.get()) if len(quantitydiesel_spinbox.get()) > 0 else 0
            ACcrditionStatediesel = "جاري" if quantitydiesel > 0 else "none"
            ACcrditionStateOIL = "جاري"  if quantityoil > 0 else "none"
            Time= status_combobox.get()
            prosonle = "شخصي" if aP.get() else "إدارة"
            selectPreter = get_selectprinter()
            if quantityoil > 0  and len(name) > 0 and name != "اسم المستفيد" or quantitydiesel > 0  and len(name) > 0 and name != "اسم المستفيد":    
                    print(name,quantitydiesel)
                    for i in pablic:
                        if str(i[1]).replace(" ","") == name.replace(' ','')   and str(i[6]).replace(" ","") == "محذوف".replace(' ','') :
                            keyDelet +=1
                        if  str(i[1]).replace(" ","") == name.replace(' ','')   and str(i[6]).replace(" ","") != "محذوف".replace(' ','') :
                            keyhush +=1
                    if keyDelet > 0 :
                        messagebox.showwarning(title="Error",message=" اسم المستفيد موجود بالفعل وهو في قائمة المحذوفات")
                        keyDelet = 0
                    elif keyhush > 0:   
                        messagebox.showwarning(title="Error",message="اسم المستفيد موجود بالفعل")
                        keyhush =0
                    else:        
                        # contener.grid_forget()
                        # AppConvex(oneFrame,'addpack')
                        idUser = self.NumberGenerter()
                        userNumber, fil = self.barcodnther(idUser,name,quantityoil,quantitydiesel)
                        print(userNumber)
                        convertcarte(fil[1],name)
                        # print(userNumber,idUser,"hleo")
                        StationMonthSqly.insert_Pablic(userNumber,name,quantityoil,quantitydiesel,prosonle,Time,ACcrditionStatediesel,ACcrditionStateOIL)
                        opration = {"kindopr":"اضافة اعتماد","Timeopr":str(datetime.now().time()),'nameusefly':name }
                        InsertJson(opration)
                        
                        # AppConvex(oneFrame,'addfor')
                        # contener.grid(row=0,column=0,padx=10,pady=10)
                        # self.update()
                        self.upTreeview()
                        name_entry.delete(0,"end")
                        name_entry.insert(0,"اسم المستفيد")
                        quantitydiesel_spinbox.delete(0, "end")
                        quantitydiesel_spinbox.insert(0, "اعتماد الديزل")
                        quantityOIL_spinbox.delete(0, "end")
                        quantityOIL_spinbox.insert(0, "اعتماد البترول")
                        try:
                            if movment["kindMovment"].replace(" ","") == 'بداية تشغيل'.replace(" ","") and len(selectPreter) <= 0 and len(pablic) <= 1:
                                SelectPrinter(self)
                        except:
                            pass
                        textStat.grid_forget()
                        aP.set(value=False)
                        a.set(value=True)
            else:
                messagebox.showwarning(title="Error", message="من فضلك يجب اكمال البيانات")
        # except:
            # print('error insert')
        # gc.collect()
    
    def upTreeview(self):
          get_it = treeview.get_children()
          for item in get_it:
            treeview.delete(item)
          treeview.update()
          self.load_data('جاري','موقف')           
    def load_data(self,creditsKind1,creditsKind2):
            global pablicprosonl
            if creditsKind2 == 'down':
                get_it = treeview.get_children()
                for item in get_it:
                    treeview.delete(item)
                treeview.update()
            pablicprosonl =StationMonthSqly.inComin_Pablic()
            lisvalues = list({"حالة البترول","حالة الديزل","التاريخ","نوع الاعتماد", "الكمية من الديزل","الكمية من البترول","اسم المستفيد","رمز الباركود"})
            for col_name in lisvalues:
                    treeview.heading(col_name, text=col_name)
            for value_tuple in pablicprosonl:
                    if value_tuple[6] == creditsKind1 or value_tuple[6] == creditsKind2 or value_tuple[7] == creditsKind1 or value_tuple[7] == creditsKind2:
                        # self.ACcrditionStatediesel= value_tuple[6]
                        # self.ACcrditionStateOIL = value_tuple[7]
                        values = list(value_tuple)
                        values.reverse()
                        # print(values)
                        # opretion = (str(value_tuple[0]),str(value_tuple[1]),str(value_tuple[2]),str(value_tuple[3]),str(value_tuple[4]),str(value_tuple[5]),str(value_tuple[6]),str(value_tuple[7]))
                        treeview.insert('', tk.END, values=values,tags=('event', 'row'))
                        treeview.configure(selectmode="extended")    
#     حذفة وتوقيف الاعتماد
    def stopAndDeletCrditesFun(self,kindOp,id,funKind,funkindsub):
            updateelmant = next((values for values in pablicprosonl if values[0] == id[7] ),None)
            # print(updateelmant)  
            if updateelmant is not None and  id[6] != 'نثريات':
                if funKind == 'توقيف' :
                    state = StationMonthSqly.UpdateStopdCrdits(str(kindOp),str(id[7]),funkindsub)                
                    if state == True:  
                      self.upTreeview()
                    opration = {"kindopr":"توقيف اعتماد","Timeopr":str(datetime.now().time()),'nameusefly':id[6] }
                    InsertJson(opration)
                else:
                    if funkindsub == 'DeletAll' and   id[0]  != 'محذوف' or funkindsub == 'DeletAll' and id[1]  != 'محذوف':
                      state = StationMonthSqly.DeletAcontfetchArryJson(str(id[7]),{"name1":"DeletAll"}) 
                    else:
                            OIL =  int(id[5]) > 0
                            diesel = int(id[4]) > 0
                            if OIL and diesel :
                               dieselboouln= 'جاري' 
                               OILboouln= 'جاري'
                            elif OIL:
                               dieselboouln= 'none' 
                               OILboouln= 'جاري'
                            else:
                                dieselboouln='جاري' 
                                OILboouln= 'none'
                            state =  StationMonthSqly.DeletAcontfetchArryJson(str(id[7]),{"name1":OILboouln,"name2":dieselboouln}) 
                    if state == True :
                        treeview.delete(kindOp)   
                    opration = {"kindopr":"حذف اعتماد","Timeopr":str(datetime.now().time()),'nameusefly':id[6] }
                    InsertJson(opration)
    def switchDatat(self,name1,name2):
            get_childern = treeview.get_children()
            for item in  get_childern:
                treeview.delete(item)
            treeview.update()
            self.load_data(name1,name2)
    def Updat_Acont(self):
        try:
            name = name_entry.get()
            # jopderc= jop_name.get()
            # quantity= quantitydiesel_spinbox.get()
            # Time= status_combobox.get()
            quantityoil= quantityOIL_spinbox.get() if len(quantityOIL_spinbox.get()) > 0  and quantityOIL_spinbox.get() != "الكمية المعتمدة من البترول" else 0
            quantitydiesel= quantitydiesel_spinbox.get() if len(quantitydiesel_spinbox.get()) > 0  and quantitydiesel_spinbox.get() != "الكمية المعتمدة من الديزل" else 0
            # print(quantitydiesel,quantityoil)        
            if int(quantitydiesel) > 0:
                self.ACcrditionStatediesel =  "جاري"
            if int(quantityoil) > 0: 
                self.ACcrditionStateOIL =  "جاري"  
            prosonle = "شخصي" if aP.get() == True else "إدارة"
            objectSum ={"nameusefly":str(name),"quantityOIL":str(quantityoil),"quentitydiesel":str(quantitydiesel),"oprtionPush":str(prosonle),
                        "ACcrditionStatediesel":str(self.ACcrditionStatediesel),"ACrditionStateOIL":str(self.ACcrditionStateOIL),"idusers":str(ID)}
            backsend =StationMonthSqly.Update_pablicAll(objectSum)
            opration = {"kindopr":"تعديل اعتماد","Timeopr":str(datetime.now().time()),'nameusefly':name }
            InsertJson(opration)
            if backsend == True:
                self.upTreeview()
                name_entry.delete(0,"end")
                name_entry.insert(0,"اسم المستفيد")
                quantitydiesel_spinbox.delete(0, "end")
                quantitydiesel_spinbox.insert(0, "اعتماد الديزل")
                quantityOIL_spinbox.delete(0, "end")
                quantityOIL_spinbox.insert(0, "اعتماد البترول")
                aP.set(value=False)
                a.set(value=True)
                checkbutton.state(["selected"])
                checkbuttonPro.state(["!selected"])
                buttonInsert.config(text='إدخال',command=self.insert_row)
        except ValueError:
             print("Error")
            
    def founction(self,event):
            global row_values
            try: 
                id_row = treeview.identify_row(event.y)
                treeview.selection_set(id_row)
                row_values= treeview.item(id_row)['values']
                print(row_values)
                user = responsebletUser()
                popUpMenu = tk.Menu(treeview,tearoff=0,font=('Tajawal',13))
                popUpMenu.add_separator()
                if row_values[0] == "جاري" and row_values[6] != 'نثريات' or row_values[0] == "موقف" and row_values[6] != 'نثريات' or row_values[1] == "جاري" and row_values[6] != 'نثريات' or row_values[1] == "موقف" and row_values[6] != 'نثريات':  
                        # print(row_values[1],id_row)
                        self.ACcrditionStatediesel= row_values[1]
                        self.ACcrditionStateOIL= row_values[0]
                        def Chackinform():
                            if  row_values[0] == "جاري" and row_values[1] == "جاري"  or row_values[0] == "جاري" and row_values[1] != "جاري"  or row_values[0] != "جاري" and row_values[1] == "جاري"  :
                                return(True)
                            else:
                                return(False)
                        if row_values[0] != "محذوف" and row_values[1] != "محذوف":
                            popUpMenu.add_command(label='توقيف  الاعتماد كامل' if Chackinform() == True else " الغا توقيف كامل", command=lambda: self.stopAndDeletCrditesFun('موقف'if Chackinform() == True else "جاري" ,row_values,'توقيف',"All"))
                            popUpMenu.add_separator()
                            if row_values[0] != "محذوف" and row_values[0] != "none":
                                popUpMenu.add_command(label="توقيف البترول" if row_values[0] == 'جاري'  else  "إلغاء توقيف البترول" ,command=lambda:self.stopAndDeletCrditesFun("موقف" if row_values[0] == 'جاري'  else "جاري" ,row_values,'توقيف',"OIL"))
                                popUpMenu.add_separator()
                            popUpMenu.add_command(label="توقيف الديزل" if row_values[1] == 'جاري' else "إلغاء توقيف  الديزل",command=lambda:self.stopAndDeletCrditesFun("موقف" if row_values[1] == 'جاري' else "جاري",row_values,'توقيف',"diesel" ))
                            popUpMenu.add_separator()
                        popUpMenu.add_command(label='تعديل', command=lambda: self.UpdateFunction(row_values))
                        popUpMenu.add_separator()
                if user['Responsibilities'].replace(" ","") == "المسؤل المباشر".replace(" ",""):    
                    if row_values[0] != 'محذوف' and row_values[1] != 'محذوف':
                            popUpMenu.add_command(label='حذف الحساب',command=lambda: self.stopAndDeletCrditesFun(id_row, row_values,'محذوف',"DeletAll"))
                            popUpMenu.add_separator()
                    else:
                            # print(row_values[6])
                            popUpMenu.add_command(label='استرداد الحساب ',command=lambda: self.stopAndDeletCrditesFun(id_row, row_values,'محذوف',"importAll") )
                            popUpMenu.add_separator()
                popUpMenu.post(event.x_root,event.y_root)
            except ValueError:
                print("error")
            # gc.collect()
    
  
       
    
  
      
    
      