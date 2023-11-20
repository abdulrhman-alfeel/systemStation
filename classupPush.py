from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from convertcod.SumAll import *
from convertcod.internal_storage import *
from datetime import datetime, timedelta
from sqlit_ferquntlye import MethodSqlet
from Print.printes import printerNew
from Print.Oprationprint import Oprationprint
# import threading
from convertcod.waitng import AppConvex
from convertcod.userfind import *
from Print.viewpdf import switchMonth
from convertcod.insertSelectprinter import SelectPrinter
# import gc
Cash= ''
chaking = False
class MyClassPush(ttk.Frame):
    # def __init__(self,pags_labl,aciton,nuber,textnuber,textnubermonth):
    def __init__(self, parent,controller):
            ttk.Frame.__init__(self,parent)
            global theRem_entry
            global spent_entry
            global iduser_spinbox
            global curntPash_spinbox
            global kindspent_entry
            global status_combobox
            global name_pach
            global treeview
            global buttonInsert
            global text_qutinty
            global frameAmont
            global text_amont
            global dates
            global recevid
            global user_text
            global userConternr
            global namerecevid
            global widgets_frame
            global buttonTSinders
            global treeFrame
            # global user_Time
            self.dataEdit = {}
            self.id_kind = 0
            self.brcod = False
            dates= []
            start_date = datetime.now()
            end_date = datetime(2028, 9, 30)
            global FerquntlyeDeay
            FerquntlyeDeay = StationMonthSqly.inComin_Data() 
            for day in range((end_date - start_date).days + 1):
                datall = start_date + timedelta(days=day)
                dates.append(datall.date())
            global text_kind
            # self.progress = ttk.Progressbar(self,  mode="indeterminate")
            # self.progress.grid(row=0, column=1, padx=10, pady=(5, 0), sticky="ew")
            # user_Time = ttk.Label(self,font=("Tajawal,13"))
            # user_Time.grid(column=1,row=0, padx=10, pady=(5, 0), sticky="ew") 
            widgets_frame = ttk.LabelFrame(self, padding=(5,5),height=800)
            widgets_frame.grid(row=1, column=1, padx=15, pady=2, sticky="nsew")
            widgets_frame.pack_propagate(0)
            # widgets_frame.pack(side='right',anchor='e')
            frameAmont = ttk.LabelFrame(widgets_frame)
            frameAmont.grid(column=0,row=0,padx=5,pady=2,sticky='ew')
            frameAmont.anchor('center')
            userConternr = ttk.LabelFrame(frameAmont,text='اسم المستخدم')
            user_text = ttk.Label(userConternr)
            user_text.grid(column=0,row=0,padx=5,pady=2) 
            text_amont = ttk.Label(frameAmont,text="" )
            text_qutinty = ttk.Label(frameAmont,text="" )
            text_kind = ttk.Label(frameAmont,text="...حساب حالي" )
            text_kind.grid(column=1,row=0,padx=5,pady=2)
            # text_kind = tk.Label(widgets_frame,text=aciton,fg="white",font=("Tajawal",13))
            text_kind.update_idletasks()
            name_pach = ttk.Entry(widgets_frame)
            name_pach.insert(0,Cash)
            name_pach.bind("<FocusIn>", lambda e: self.clickName('name',name_pach.delete('0', "end")) )
            name_pach.grid(row=2, column=0,padx=5, pady=2, sticky="ew")
          
            pachNew = ttk.LabelFrame(widgets_frame,text="المصروف الان")
            pachNew.grid(row=3,column=0,padx=5)
           
            # labltext.place(y=100,x=75,anchor="center")
            curntPash_spinbox = ttk.Spinbox(pachNew, from_=20, to=5000)
            curntPash_spinbox.grid(row=0, column=0, pady=5, sticky="ew")
            curntPash_spinbox.bind("<FocusIn>",lambda e: self.clickName('spent',
                                                                        curntPash_spinbox.delete(0,"end")))
            curntPash_spinbox.bind("<KeyRelease>",
                                   lambda event: self.Pashcurt(event,controller,kindspent_entry.get()))
            namerecevid = ttk.LabelFrame(widgets_frame,text="الشخص المستلم",width=10)
            namerecevid.grid(row=4,column=0,padx=5)
            recevid= ttk.Entry(namerecevid)
            recevid.grid(row=0, column=0, pady=5, sticky="ew")
            recevid.bind("<KeyRelease>",lambda event: self.Pashcurt(event,controller,kindspent_entry.get()))
            status_combobox = ttk.Combobox(namerecevid, values=dates)
            status_combobox.grid(row=0, column=1,padx=5, pady=2, sticky="ew")
            status_combobox.set(dates[0])
            Farmstatment = ttk.Frame(widgets_frame)
            Farmstatment.grid(row=5,column=0,pady=15,padx=5)
            Spnlabltext = ttk.LabelFrame(Farmstatment,text="الكمية المصروفة")
            Spnlabltext.grid(row=0,column=0,pady=2,padx=5)
            spent_entry= ttk.Entry(Spnlabltext)
            spent_entry.insert(0,0)
            spent_entry.grid(row=0, column=0,padx=5, pady=5, sticky="ew")
            spent_entry.bind("<FocusIn>",lambda e: self.clickName('amount', spent_entry.delete(0,'end')))
            
            thelabltext = ttk.LabelFrame(Farmstatment,text="الكمية المتبقية")
            thelabltext.grid(row=0,column=1,pady=2,padx=5)
            theRem_entry= ttk.Entry(thelabltext)
            theRem_entry.insert(0,0)
            theRem_entry.grid(row=0, column=0,padx=5, pady=5, sticky="ew")
            theRem_entry.bind("<FocusIn>", lambda e: self.clickName("therem",theRem_entry.delete(0,"end")))

            kindspent_entry =ttk.Entry(widgets_frame)
            kindspent_entry.grid(row=6, column=0,padx=5, pady=5, sticky="ew")
            kindspent_entry.insert(0,"نوع الصرف")
            kindspent_entry.bind("<FocusIn>", lambda e: self.clickName('Kindspent', kindspent_entry.delete(0,'end')))
        
            iduser_spinbox = ttk.Entry(widgets_frame)
            iduser_spinbox.grid(row=7,column=0, padx=5, pady=15, sticky="ew")
            iduser_spinbox.insert(0,"انقر هناء لفحص الباركود")
            iduser_spinbox.bind("<FocusIn>", lambda e:self.clickName('insert',   iduser_spinbox.delete(0,'end')))
            # iduser_spinbox.bind("<KeyPress>",on_press)
            iduser_spinbox.bind("<KeyRelease>",self.on_press)

            treeFrameButon = ttk.Frame(widgets_frame)
            treeFrameButon.grid(row=8,column=0, padx=10, pady=(10, 5), sticky="nsew")
            buttonTSinders = ttk.Button(treeFrameButon,text="نثريات",
                                        command=lambda:self.Sinders("نثريات"),width=10)
            buttonTSinders.grid(row=0, column=2,padx=5, pady=5, sticky="ew")
            buttonT = ttk.Button(treeFrameButon,text="تهيئة",
                                 command=lambda:self.databis(controller),width=10)
            buttonT.grid(row=0, column=1,padx=5, pady=5, sticky="ew")
            buttonInsert = ttk.Button(treeFrameButon,text="صرف", 
                                      command=lambda:self.insert_row(controller,kindspent_entry.get()),width=10)
            buttonInsert.grid(row=0, column=0,padx=5, pady=5, sticky="ew")
            separator = ttk.Separator(widgets_frame,orient="vertical")
            separator.grid(row=12, column=0, padx=(10,5), pady=5, sticky="ew")
            treeFrame = ttk.Frame(self,width=1100,height=600)
            treeFrame.grid(row=1,column=0, pady=5,padx=10)
            treeFrame.pack_propagate(0)
            fromButtom = ttk.Frame(treeFrame)
            fromButtom.pack(side='bottom',anchor="n")
            buttonSinders = ttk.Button(fromButtom,text='نثريات',width=30,
                                       cursor="hand2",command=lambda : self.SwitchData(saw="نثريات",Page=buttonSinders))
            buttonSinders.grid(row=0,column=0,padx=5,pady=5)
            buttonCrdits = ttk.Button(fromButtom,text="اعتمادات",width=30,
                                      command=lambda:self.SwitchData(saw="اعتمادات",Page=buttonCrdits))
            buttonCrdits.grid(row=0,column=1,padx=5,pady=5)
            
            treeScroll = ttk.Scrollbar(treeFrame)
            treeScroll.pack(side="right", fill="y")
            cols= ('حمولة شهر',"المستخدم","التاريخ", "المصروف","اسم المستلم",
                   "اسم المستفيد","رمز الباركود",'العملية',"م")
            # cols= ("المستخدم","التاريخ", "المصروف اليوم","اسم المستلم","اسم المستفيد","رمز الباركود",'رقم العملية',"م")
            treeview = ttk.Treeview(treeFrame, show="headings",
                                    yscrollcommand=treeScroll.set, columns=cols, height=600)
            treeview.column("م",width=20,anchor="center",)
            treeview.column("العملية",width=80,anchor="center")
            treeview.column("رمز الباركود",width=180,anchor="center",)
            treeview.column("اسم المستفيد",width=150,anchor="center")
            treeview.column("اسم المستلم",width=150,anchor="center")
            treeview.column("المصروف",width=100,anchor="center")
            treeview.column("التاريخ",width=120,anchor="center")
            treeview.column("المستخدم",width=150,anchor="center")
            treeview.column("حمولة شهر",width=100,anchor="center")
            treeview.tag_bind("row",'<Button-3>', lambda event: self.on_tree_view_select(event,controller))
            # treeview.column("Employment",width=100,anchor="center")
            treeview.pack(side="right",pady=5)
            treeScroll.config(command=treeview.yview)
            self.keyPrssnum = 0 
    def prossecc(self,controller,statment):
        self.insert_row(controller=controller,statment=statment)
        
    def SwitchData(self,saw,Page):
        Man = tk.Menu(Page,tearoff=0)
        Man.add_command(label="اليومي",columnbreak=10,accelerator=" ",command=lambda:self.load_data(statemant=saw,tim='day'))
        Man.add_command(label="الشهري",columnbreak=10,accelerator=" ",command=lambda:self.load_data(statemant=saw,tim='month'))
        Man.post(Page.winfo_rootx(),Page.winfo_rooty())
 
    #  عملية  الصرف
    def insert_row(self,controller=None,statment=None):
                try:
                    # time.sleep(0.03)
                    # print(Cash)
                    # self.progress.start(10)
                    name = name_pach.get()
                    curntPash = curntPash_spinbox.get()
                    iduse_user = iduser_spinbox.get()
                    sendrisOpject={}
                    if len(name) > 0 and  name != "اسم المستفيد" and int(curntPash) > 0 and iduse_user != 'انقر هنا لفحض الباركود' and len(iduse_user) > 0 :
                        widgets_frame.grid_forget()
                        AppConvex(self,oprtion=None)
                        sendrisOpject['nameSub'] = name
                        selectPreter = get_selectprinter()
                        if len(selectPreter) <= 0:
                            SelectPrinter(self)
                        # printer = get_selectprinter()
                        # if len(printer) > 0 :
                        methodSub = MethodSqlet(iduse_user,sendrisOpject,kindaciton['name2'],clssefin,datetime.strptime(str(kindaciton['Time']),'%Y-%m-%d').month)
                        namerecieved = recevid.get() if len(recevid.get()) > 0 else 'نفسه'
                        user = get_virfe()
                        methodSub.insert_ferquntly(curntPash,"صرف",0,namerecieved,user["userName"])
                        opration = {"kindopr":"صرف","Timeopr":str(datetime.now().time()),'nameusefly':str(name)}
                        InsertJson(opration)
                            # time.sleep(0.03)
                            # self.animation()
                        self.Fundisblayted("normal")
                        self.databis(controller)
                            # self.progress.config(value=0)
                        self.brcod = False
                        status_combobox.set(dates[0])
                        self.UpdateTreeviewandAllSum(controller,statment)
                            # self.progress.stop()
                        AppConvex(self,oprtion="forget")
                        gc.collect()
                    else:
                        messagebox.showwarning(title="Error", message="يجب ادخال البيانات اولاً")
                        name_pach.delete(0, "end")
                        name_pach.insert(0,"اسم المستفيد")
                        iduser_spinbox.delete(0,"end")
                        iduser_spinbox.insert(0,'انقر هنا لفحض الباركود')
                except ValueError:
                    messagebox.showwarning(title="Error", message="يجب ادخال البيانات اولاً")
                widgets_frame.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")
    #عمليات التعديل
 
    #  عملية التعديل
    def Edit_send(self,controller,statment,user):
                array= {}
                amuntSpentday =curntPash_spinbox.get()
                dataStat = status_combobox.get()
                sendrisOpject = {}
                sendrisOpject['nameSub'] = self.dataEdit['nameusefly']
                array={'ID': self.dataEdit["ID"], 'idusers': self.dataEdit["idusers"] , 
                       'nameusefly': self.dataEdit["nameusefly"] , 'amountSpentday': amuntSpentday ,
                       "Classefiy":clssefin, 'Timedey': dataStat,'namerecevid':self.dataEdit['namerecved'],
                       "user":user ,'inconmicquntity':self.dataEdit['inconmicquntity'] }
                methodSub = MethodSqlet(self.dataEdit["idusers"],sendrisOpject,kindaciton['name2'],
                                        clssefin,datetime.strptime(self.dataEdit['Times'],'%Y-%m-%d').month)
                methodSub.insert_ferquntly(amuntSpentday,array,numberprevdis,self.dataEdit['namerecved'],user)
                opration = {"kindopr":"تعديل صرف","Timeopr":str(datetime.now().time()),'nameusefly': self.dataEdit["nameusefly"]}
                InsertJson(opration)
                self.databis(controller)
                self.UpdateTreeviewandAllSum(controller,statment)

    def on_tree_view_select(self,event,controller): 
            global numberprevdis
            try:
                id_row = treeview.identify_row(event.y)
                treeview.selection_set(id_row)          
                row_value = treeview.item(id_row)["values"] 
                # print(row_value)
                numberprevdis = row_value[3]
                selectClick = Menu(treeview,tearoff=0)
                    # print( row_value[3])
                dataMath = next((item for item in FerquntlyeDeay if int(item['idusers']) == int(row_value[6])),None)
                if dataMath is not None:
                    # print(dataMath)
                    self.empytePage() 
                    amountSpent=  dataMath['amountٍٍSpentOIL']   if str(frameAmont.config("text")[4]).replace(" ","") == "بترول".replace(" ","") else dataMath['amountٍٍSpentdiesel']
                    thremen = dataMath["thermenOIL"] if frameAmont.config('text')[4] == "بترول" else dataMath['thermendiesel']
                    self.dataEdit={"ID":row_value[7],"idusers":row_value[6],"nameusefly":row_value[5],"namerecved":row_value[4],"curntPash":numberprevdis,"amountٍSpent":amountSpent,"thermen":thremen,'inconmicquntity':row_value[0],"Times":row_value[2]}
                    # print(row_value[1])
                    if  kindspent_entry.get().replace(" ","").lower() != 'نثريات'.replace(" ","").lower():
                        selectClick.add_command(label="طباعة حراري"
                                                ,command=lambda:printerNew(amountSpent,thremen,numberprevdis,str(row_value[1]),row_value[5],row_value[4],frameAmont.config('text')[4],False if kindspent_entry.get().replace(" ","").lower() != 'نثريات'.replace(" ","").lower() else True,row_value[2],row_value[0]))
                        selectClick.add_separator()
                    selectClick.add_command(label='طباعة فاتورة استلام'
                                            ,command=lambda: Oprationprint.startfunction(row_value[7],row_value[5],row_value[4],numberprevdis,frameAmont.config('text')[4],row_value[1],row_value[0]))
                    selectClick.add_separator()
                    user = responsebletUser()
                    if user['Responsibilities'].replace(" ","") == "المسؤل المباشر".replace(" ",""):
                        selectClick.add_command(label="تعديل",command=lambda: self.barcodeFon(self.dataEdit,'تعديل'))
                    userConternr.grid(column=0,row=0,padx=5,pady=5,sticky='ew')
                    user_text.config(text=row_value[1])
                    buttonInsert.config(text="تعديل", command=lambda:self.Edit_send(controller,kindspent_entry.get(),row_value[0]))
                # else:
                #     print('error',row_value[2])
                #     print('error',FerquntlyeDeay)
                    selectClick.post(event.x_root,event.y_root)
            except:
                print('خطاء تحديد')
 
    #  عمليات التحديث
    def empytePage(self):
                spent_entry.configure(state="normal")
                theRem_entry.configure(state="normal")
                iduser_spinbox.configure(state="normal")
                name_pach.configure(state="normal")
                name_pach.delete(0,'end')
                name_pach.delete(0,'end')
                name_pach.insert(0,'اسم المستفيد')
                recevid.delete(0,"end")
                iduser_spinbox.delete(0,"end")
                theRem_entry.delete(0,"end")
                spent_entry.delete(0,"end")
                theRem_entry.insert(0,0)
                spent_entry.insert(0,0)
                curntPash_spinbox.delete(0,"end")
                curntPash_spinbox.insert(0,0)
                kindspent_entry.configure(state="normal")
                kindspent_entry.delete(0,"end")
                kindspent_entry.insert(0,"اعتمادات")
                kindspent_entry.configure(state="disabled")
                iduser_spinbox.insert(0,'انقر هنا لفحض الباركود')
                status_combobox.set(dates[0])
                text_qutinty.config(text="")
                text_qutinty.grid_forget()
                userConternr.grid_forget()
                text_amont.config(text="")
                text_amont.grid_forget()
                namerecevid.grid(row=4,column=0,pady=15,padx=5)
                # gc.collect()

    def databis(self,controller):  
                global chaking
                chaking = False
                self.brcod=False
                buttonInsert.config(text="صرف",
                                    command=lambda:self.prossecc(controller=controller,statment=kindspent_entry.get()))
                self.empytePage()                  

    def UpdateTreeviewandAllSum(self,controller,statment):
            self.load_data(statment)
            loaddata(controller.nuber,controller.textnubermonth,"OIL")        
            loaddata(controller.nuberdiesel,controller.textnubermonthdiesel,"diesel") 

#    عمليات معالجة المعلومات
    def barcodeFon(self,data,oprtion):
                if data is not None :
                            # print(data)
                            kindspent_entry.configure(state="normal")
                            kindspent_entry.delete(0,"end")
                            if data['nameusefly'].replace(" ","") != "نثريات".replace(" ","") :
                                 name_pach.delete(0,'end')
                                 name_pach.insert(0,data['nameusefly'])
                                 kindspent_entry.insert(0,'اعتمادات')
                            else:
                                  name_pach.delete(0,'end')
                                  kindspent_entry.insert(0,'نثريات')
                            # kindspent_entry.configure(state="disabled")
                            theRem_entry.delete(0,'end')
                            spent_entry.delete(0,'end')
                            if oprtion.lower() != 'تعديل'.lower():  
                                if Cash == "OIL" or frameAmont.config('text')[4] == "بترول" :
                                    spent_entry.insert(0,data['amountٍٍSpentOIL'] if data['amountٍٍSpentOIL'] is not None else "0")
                                    theRem_entry.insert(0,data['thermenOIL'] if data['thermenOIL'] is not None else "0" )        
                                    text_qutinty.config(text=data['quantityOIL'])
                                    text_amont.config(text=":اجمالي المخصص")
                                else:
                                    spent_entry.insert(0,data['amountٍٍSpentdiesel'] if data['amountٍٍSpentdiesel'] is not None else "0")
                                    theRem_entry.insert(0,data['thermendiesel'] if data['thermendiesel'] is not None else "0" ) 
                                    text_qutinty.config(text=data['quantitydiesel'])
                                text_qutinty.grid(column=0,row=1,padx=5,pady=5)
                                text_amont.config(text=":اجمالي المخصص")
                                text_amont.grid(column=1,row=1,padx=5,pady=5)  
                            else:
                                iduser_spinbox.delete(0,'end')
                                iduser_spinbox.insert(0,data['idusers'])  
                                self.brcod = False  
                                spent_entry.insert(0,data['amountٍSpent'] if data['amountٍSpent'] is not None else "0")
                                theRem_entry.insert(0,data['thermen'] if data['thermen'] is not None else "0" )      
                                curntPash_spinbox.delete(0,"end")
                                # frameAmont.config(text=":تعديل")
                                curntPash_spinbox.insert(0,data['curntPash'] if data['curntPash'] is not None else '0')   
                                # frameAmont.config(text=":معلومات ")
                            # gc.collect()
                            # 
                else:
                        name_pach.delete(0,'end')
                        iduser_spinbox.delete(0,'end') 
             
   
    def barcodeFonShur(self,value):
            global chaking         
            try:
                    data = next((item for item in Ferquntlye if  re.search(str(value).lower() ,str(item['idusers']).lower()) ), None)
                    # print(data)
                    if data is not None and data["DoneSub"] == "false" and frameAmont.config('text')[4] == "بترول" and data["ACcrditionStateOIL"] != "محذوف" and data["ACcrditionStateOIL"] != "موقف" and data['aciton'] == kindaciton['name2'] or data is not None and frameAmont.config("text")[4] == "ديزل"  and data["DoneSub"] == "false" and data['ACcrditionStatediesel'] != "محذوف" and data['ACcrditionStatediesel'] != "موقف" and data['aciton'] == kindaciton['name2']:
                        if frameAmont.config('text')[4] == "بترول" and int(data['quantityOIL']) > 0 or frameAmont.config("text")[4] == "ديزل" and int(data['quantitydiesel']) > 0:
                            theRem_entry.delete(0,'end')
                            spent_entry.delete(0,'end')
                            iduser_spinbox.delete(0,'end')
                            
                            iduser_spinbox.insert(0,data['idusers'])
                            kindspent_entry.configure(state="normal")
                            kindspent_entry.delete(0,"end")
                            if Cash == "OIL" :
                                spent_entry.insert(0,data['amountٍٍSpentOIL'] if data['amountٍٍSpentOIL'] is not None else "0")
                                theRem_entry.insert(0,data['thermenOIL'] if data['thermenOIL'] is not None else "0" )        
                                text_qutinty.config(text=data['quantityOIL'])
                                text_amont.config(text=":اجمالي المخصص")
                            else:
                                spent_entry.insert(0,data['amountٍٍSpentdiesel'] if data['amountٍٍSpentdiesel'] is not None else "0")
                                theRem_entry.insert(0,data['thermendiesel'] if data['thermendiesel'] is not None else "0" ) 
                                text_qutinty.config(text=data['quantitydiesel'])   
                                text_amont.config(text=":اجمالي المخصص") 
                            if  str(data['nameusefly']).replace(" ","") != "نثريات".replace(" ","") :
                                    # print(data)
                                    name_pach.delete(0,'end')
                                    name_pach.insert(0,data['nameusefly'])
                                    kindspent_entry.insert(0,'اعتمادات')
                                    name_pach.configure(state="disabled")
                            else:
                                    kindspent_entry.insert(0,'نثريات')
                                    namerecevid.grid_forget()
                            text_amont.grid(column=1,row=1,padx=5,pady=2) 
                            text_qutinty.grid(column=0,row=1,padx=5,pady=2) 
                            self.Fundisblayted("disabled")
                            # print(data)
                            self.brcod = False  
                        else:
                            chaking = True
                            messagebox.showwarning(title="Error",message=f"هذا الحساب لايمتلك حساب {frameAmont.config('text')[4]}")
                        # gc.collect()
                    else:       
                                chaking = True
                                stoping =  data["ACcrditionStateOIL"].replace(" ","") if frameAmont.config('text')[4] == "بترول" else  data["ACcrditionStatediesel"].replace(" ","")
                                if data is not None and stoping == "محذوف".replace(" ","") :
                                        messagebox.showwarning(title="Error", message="الحساب محذوف بالفعل")
                                elif str(data['DoneSub']).replace(" ","") == "true".replace(" ",""):
                                        messagebox.showwarning(title='Erorr', message='هذا الحساب قد انتها من استلام كامل الكمية المخصصة له ')
                                elif data is not None and stoping == "موقف".replace(" ", "") :
                                        messagebox.showwarning(title="Error", message='الحساب موقف')
                                else:
                                        messagebox.showwarning(title='Erorr', message='غير موجود')    
                                self.brcod = False 
                                # print(data,'غير موجود')
                                self.empytePage()
                                # print(self.brcod)      
            except:
                pass
                # print('error sqlit')
   
    # اغلاق المدخلات
    def Fundisblayted(self,value):
                spent_entry.configure(state=value)
                theRem_entry.configure(state=value)
                iduser_spinbox.configure(state=value)
                kindspent_entry.configure(state=value)
   
    def lodKindPage(self,kind):
        global Cash
        global kindaciton
        kindaciton = kind
        print(kind['Time'])
        widgets_frame.config(text=switchMonth(datetime.strptime(str(kind['Time']),"%Y-%m-%d").strftime("%B")))
        frameAmont.config(text="بترول"if kind["name1"] == "OIL" else "ديزل")
        text_kind.config(text="...حساب حالي" if kind["name2"] == 'new' else "...حساب سابق")
        Cash = kind['name1']
        # print(frameAmont.config("text")[4])
   
    def Pashcurt(self,event,controller,statment):
                try:
                    vaule = int(curntPash_spinbox.get())
                except ValueError:
                    vaules = curntPash_spinbox.get()
                    curntPash_spinbox.delete(0,'end')
                    curntPash_spinbox.insert(0,vaules[:-1])
                if event.keysym == "Return"  :
                    # self.prossecc(controller,statment)
                    if  buttonInsert.config("text")[4] == 'تعديل':
                        userAll = user_text.config('text')[4]
                        self.Edit_send(controller=controller,statment=statment,user=userAll)
                    else:
                        self.insert_row(controller=controller,statment=statment)
                
    def load_data(self,statemant='اعتمادات',tim=None):
                # global new
                global arrayPash
                global Ferquntlye
                global clssefin
                global station
                clssefin = "OIL" if frameAmont.config("text")[4] == "بترول" else "diesel"
                # Ferquntlye = StationMonthSqly.inComin_Data()
                station =  StationMonthSqly.inComin_dataAll()
                Ferquntlye = StationMonthSqly.inComin_Data() 
                if len(Ferquntlye) <= 0 :
                         StationMonthSqly.Fausth_stationPablic()
                if len(station) > 0 and len(Ferquntlye) > 0 :
                    test= Ferquntlye[len(Ferquntlye) -1] if len(Ferquntlye) > 0 else 0
                    times = test['datatim']
                    # condit = int(re.findall('\d+',times)[1])  
                    conditional = datetime.strptime(times,'%Y-%m-%d').month if len(times) > 0 else 0
                    if conditional < datetime.now().month:
                        StationMonthSqly.Fausth_stationPablic()
                             # lisvalues = list({"المستخدم","التاريخ", "المصروف اليوم","اسم المستلم","اسم المستفيد","رمز الباركود",'رقم العملية',"م"})
                # print(list_values)
                new_object = []
                arrayPash= []
                a =[]
                o = {}
                index=0
                def TimesFanction(pic):
                    Data = datetime.strptime(pic['Timedey'],"%Y-%m-%d")
                    if tim == 'month':
                        return Data.month == datetime.now().month
                    else:    
                        return Data.day == datetime.now().day
          
                items= treeview.get_children()
                for item in items:
                     treeview.delete(item)
                treeview.update()
                
                lisvalues = list({'حمولة شهر',"المستخدم","التاريخ", "المصروف","اسم المستلم","اسم المستفيد","رمز الباركود",'العملية',"م"})
                for col_name in lisvalues:
                        treeview.heading(col_name, text=col_name)
                
                for i in Ferquntlye:   
                    if str(i['aciton']).replace(" ","") == str(kindaciton["name2"]).replace(" ",""):
                        if statemant  == "اعتمادات" :   
                            if  i['Arraypash'] is not None and  str(i["nameusefly"]).replace(" ","") != "نثريات".replace(" ",""): 
                                for value_tuple in i['Arraypash'] :
                                    if value_tuple["Classefiy"] == clssefin:
                                        if TimesFanction(value_tuple):
                                            index+= 1 
                                            # objectsall = (str(values[0]),str(values[1]),str(values[2]),str(values[3]),str(values[4]),str(values[5]),str(values[6]),str(values[7]),str(values[8]))
                                            objectsall = (str(value_tuple['inconmicquntity']),str(value_tuple["user"]),str(value_tuple["Timedey"]),str(value_tuple["amountSpentday"]),str(value_tuple["namerecevid"]),
                                                        str(value_tuple["nameusefly"]),str(value_tuple["idusers"]),str(value_tuple["ID"]),str(index))
                                            # treeview.insert('', END, values=sorted(objectsall),tags=("event",'row'))
                                            # treeview.configure(selectmode="extended") 
                                            arrayPash.append(objectsall) 
                       
                        else:
                            if i['Arraypash'] is not None and  str(i["nameusefly"]).replace(" ","") == "نثريات".replace(" ",""): 
                                for value_tuple in i['Arraypash'] :
                                    new_object.append(value_tuple)
                                    if value_tuple["Classefiy"] == clssefin:
                                        # print(value_tuple)
                                        if TimesFanction(value_tuple):
                                            index+= 1 
                                            values = list(value_tuple.values())
                                            values.reverse()
                                            objectsall = (str(value_tuple['inconmicquntity']),str(value_tuple["user"]),str(value_tuple["Timedey"]),str(value_tuple["amountSpentday"]),
                                                        str(value_tuple["namerecevid"]),str(value_tuple["nameusefly"]),str(value_tuple["idusers"]),str(value_tuple["ID"]),str(index))
                                            # treeview.insert('', END, values=sorted(objectsall),tags=("event",'row'))
                                            # treeview.configure(selectmode="extended") 
                                            arrayPash.append(objectsall)
               
                index = 0
                # new = sorted(arrayPash)
                for pic in arrayPash:
                    treeview.insert('', END, values=pic,tags=("event",'row'))
                    treeview.configure(selectmode='extended') 
                gc.collect()
             
    # def insertbarcod(self):
    #                 # self.brcod=False
    #                 iduser_spinbox.delete(0,'end')
    def clickName(self,vaul,vauleSwich):
        global chaking 
        value= iduser_spinbox.get()
        new_var = False
        if chaking == new_var:
            if value.replace(" ","") != 'انقر هنا لفحض الباركود'.replace(" ","") and len(value) > 5 or vaul == 'insert' and str(buttonInsert.config('text')[4]).replace(" ","").lower() == 'تعديل'.replace(" ","").lower() :
                print(buttonInsert.config('text')[4],value,'hlllllo')
                self.barcodeFonShur(value)
            else:
                if str(buttonInsert.config('text')[4]).replace(" ","").lower() != 'تعديل'.replace(" ","").lower() :
                    iduser_spinbox.delete(0,'end')
                else:
                     vauleSwich               
        chaking=  False
      
    #   للاستماع لمدخلات الباركود
    def on_press(self,event):
        try:
            # DATAMONTH = StationMonthSqly.inComin_Data() 
            value = int(iduser_spinbox.get())         
            # print(event)
            filterF = []
            if len(iduser_spinbox.get()) > 6 : 
                Items = next((item for item in Ferquntlye if re.search(str(value).lower() ,str(item['idusers']).lower()) and str(item["aciton"]).replace(" ","") == str(kindaciton["name2"]).replace(" ","")),None) 
          
                if Items is not None and Cash == "OIL" and Items['ACcrditionStateOIL']  != "none" or Items is not None and Cash == "diesel" and Items['ACcrditionStatediesel']  != "none" : 
                    self.barcodeFon(Items,'صرف')
                    filterF.append(Items)
                # print(event)
                # if event.keysym == 'Return' and len(filterF) > 0 or value >= 12:
                if event.keycode == 13  or len(str(value)) >= 12:
                    if self.brcod == False :
                        self.brcod=True
                        self.barcodeFonShur(value)
                    else:
                        iduser_spinbox.delete(0,'end') 
                        iduser_spinbox.insert(0,value) 
                        # self.empytePage() 
        except ValueError:
                        values = iduser_spinbox.get()
                        iduser_spinbox.delete(0,'end')
                        iduser_spinbox.insert(0,values[:-1])
        # gc.collect()
                    # الاستماع لمدخلات الحرفية في مدخلات الارقام 
    def Sinders(self,kind):
        self.empytePage()
        Items = next((item for item in Ferquntlye if re.search(str(kind).lower() ,str(item['nameusefly']).lower()) and str(item["aciton"]).replace(" ","") == str(kindaciton["name2"]).replace(" ","")),None) 
        # print(kind)
        if Items is not None:
           self.barcodeFonShur(int(Items['idusers']))
        else:
            messagebox.showwarning(title='لايوجد',message='لايوجد حساب نثريات بعد')
     
            
   

   
