from tkinter import *
from tkinter import ttk
from Print.printdivce import Printdivec
from convertcod.internal_Loginstorge import *
from datetime import datetime, timedelta
from sqiltyFoun import *
from convertcod.internal_storage import *
from Print.printSearch import printSearch
from convertcod.userfind import responsebletUser
class QurySerch(ttk.Frame):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)
        self.Date = []
        start_data = datetime(2023,9,1)
        end_data = datetime(2030,9,1)
        for day in range((end_data - start_data).days +1):
                databis = start_data + timedelta(days=day)
                self.Date.append(databis.date())  
        self.DateMonth = []
        yars = [f"20{key}" for key in range(23,33)]
        month = [item for item in range(1,13)]  
        for iyrs in yars :
                for keymon in month:
                    datab =f"{iyrs}-{keymon}"
                    self.DateMonth.append(datab)            
        global spent_entry
        global newimport
        global newAddcrides
        global stopCrides
        global printstatmeent
        global treeview
        global select_entry
        global select_entryD
        global select_kindcont
        global kind_oprtion
        global select_entryMonth
        global kind_oprtionkind
        global DataMonth
        global DatatPablic
        global name_oprtionname
        # DataMonth =  []
        # DatatPablic = []
                # What is the shortcut to return the specified data space in visual studio code?
        newimport = BooleanVar()
        newAddcrides= BooleanVar()
        stopCrides = BooleanVar()
        printstatmeent = BooleanVar()
        pachSpent = ttk.Frame(self)
        pachSpent.pack(expand=True)
        pach = ttk.Frame(pachSpent,width=200)
        pach.grid(row=0,column=0,padx=10,pady=5)
        # Spnlabltext = ttk.Label(pach,text="", font=("Tajawal",13),width=100)
        # Spnlabltext.grid(row=0,column=0,padx=5,pady=5)
        # Spnlabltext.anchor('ne')
        spent_entry= ttk.Entry(pach,width=70)
        spent_entry.grid(row=0,column=0)
        spent_entry.insert(0,'عن ماذا تبحث ')
        spent_entry.bind('<FocusIn>',lambda e:spent_entry.delete(0,'end'))
        spent_entry.bind('<KeyRelease>',self.on_search)                          
        pachOprition = ttk.LabelFrame(pachSpent,text='خيارات البحث ',padding=10)
        pachOprition.grid(row=1,column=1,padx=3,pady=10,sticky='nesw')
        select_Textentry = ttk.LabelFrame(pachOprition,text="حدد القسم الذي تريد البحث فيه ")
        select_Textentry.grid(row=0,column=0,pady=10)
        selct= ['عمليات الصرف','الحسابات']
        select_entry = ttk.Combobox(select_Textentry,values=selct)
        select_entry.grid(row=0,column=0,pady=10,padx=5,sticky='nesw')
        select_entry.set(selct[0])
        self.columnname = ["المستخدم","المستلم",'المستفيد']
        name_oprtionname = ttk.Combobox(select_Textentry,values=self.columnname)
        name_oprtionname.grid(row=0,column=1,pady=10,padx=10)
        name_oprtionname.current(2)
        selectKIND = ttk.LabelFrame(pachOprition,text="حدد نوعية واسلوب البحث ")
        selectKIND.grid(row=1,column=0,pady=10)
        self.column = ['الاسم وتاريخ اليوم والنوع','الاسم وتاريخ الشهر والنوع','الاسم وتاريخ الشهر واليوم','الاسم وتاريخ الشهر',"مجمل البيانات"]
        kind_oprtion = ttk.Combobox(selectKIND,values=self.column)
        kind_oprtion.grid(row=0,column=1,pady=10,padx=10)
        kind_oprtion.current(4)
        
        self.columnkind = ["بترول","ديزل",'كافة']
        kind_oprtionkind = ttk.Combobox(selectKIND,values=self.columnkind)
        kind_oprtionkind.grid(row=0,column=0,pady=10,padx=10)
        kind_oprtionkind.current(2)
                # findData = next((item for item in  self.Date if item.key() == datetime.now()))
        frame_month = ttk.LabelFrame(pachOprition,text="تاريخ الشهر")
        frame_month.grid(row=2,column=0,pady=10,sticky='nesw')  
        select_entryMonthButton = ttk.Button(frame_month,text='مجمل',command=lambda:self.Oprtionfun('month'))
        select_entryMonthButton.grid(row=0,column=1,pady=10,padx=10,sticky='nesw')

        select_entryMonth = ttk.Combobox(frame_month,values=self.DateMonth)
        select_entryMonth.grid(row=0,column=0,pady=10,padx=10,sticky='nesw')
        select_entryMonth.current(0)
        
        frame_day = ttk.LabelFrame(pachOprition,text='اليوم')
        frame_day.grid(row=3,column=0,padx=5,pady=10,sticky='nesw') 
        select_entryDButton = ttk.Button(frame_day,text='مجمل',command=lambda:self.Oprtionfun('day'))
        select_entryDButton.grid(row=0,column=1,pady=10,padx=10)

        select_entryD = ttk.Combobox(frame_day,values=self.Date)
        select_entryD.grid(row=0,column=0 ,pady=10,padx=10)
        select_entryD.current(0)

        select_kindconttryD = ttk.LabelFrame(pachOprition,text="نوع الحساب المطلوب ")
        select_kindconttryD.grid(row=4,column=0,pady=10)
        col  = ['جاري','موقف','محذوف']
        select_kindcont = ttk.Combobox(select_kindconttryD,values=col,width=35)
        select_kindcont.grid(row=0,column=0,pady=10,padx=10,sticky='nesw')
        select_kindcont.current(0)
                
        FarmTree = ttk.Frame(pachSpent,width=1000,height=400)
        FarmTree.grid(row=1,column=0,padx=15,pady=15,sticky='nesw')
        FarmTree.pack_propagate(0)
        buttonCrdits = ttk.Button(FarmTree,text="طباعة",style="Accent.TButton",width=30,command=self.Printsearch)
        buttonCrdits.pack(side='bottom',anchor="n")
        
        treeScroll= ttk.Scrollbar(FarmTree)
        treeScroll.pack(side='right',fill='y')
        cols=("#10","#9","#8","#7",'#6','#5','#4','#3',"#2",'#1')
                
        treeview = ttk.Treeview(FarmTree,show='headings', yscrollcommand=treeScroll.set,columns=cols,height=400)
        treeview.column('#1',width=80,anchor='center')
        treeview.column('#2',width=100,anchor='center')
        treeview.column('#3', width=80,anchor='center')
        treeview.column('#4', width=90,anchor='center')
        treeview.column('#5', width=90,anchor='center')
        treeview.column('#6', width=100,anchor='center')
        treeview.column('#7', width=100,anchor='center')
        treeview.column('#8', width=100,anchor='center')
        treeview.column('#9', width=100,anchor='center')
        treeview.column('#10', width=100,anchor='center')
        # treeview.bind('<<TreeviewSelect>>',self.on_selectuser)
        treeview.pack(side="right")
        treeScroll.config(command=treeview.yview)
    def loadqury():
        global DataMonth
        global DatatPablic
        DataMonth =  StationMonthSqly.inComin_Data()
        DatatPablic = StationMonthSqly.inComin_Pablic() 
        #    وظيفة البحث حسب التاريخ 
    def Oprtionfun(self,k):
        global kind_oprtion
        if k == 'day':
            kind_oprtion.set(self.column[0])
        else:
            kind_oprtion.set(self.column[1])
        self.on_search('',d="timeData")  
    # وظيفة الفلتر
    def on_search(self,event,d='name'):
            maine_search = spent_entry.get()
            seaction_select = select_entry.get()
            kindCont = select_kindcont.get()          
            # headerArray= list({'#11','#10','#9','#8','#7','#6','#5','#4','#3',"#2",'#1'})
            headerArray= list({"#10","#9","#8",'#7','#6','#5','#4','#3',"#2",'#1'})
            headerArray.reverse()
            for col_name in headerArray:
                treeview.heading(col_name,text=col_name)
            # print(event)
            if seaction_select.replace(" ","").lower() == "الحسابات".replace(" ","").lower():
                   for item in  DatatPablic:
                       if item[7] == kindCont or item[6] == kindCont :
                            if len(maine_search) > 0:
                                get_chaldern = treeview.get_children()
                                if len(get_chaldern) > 0 :
                                    for item in get_chaldern:
                                        treeview.delete(item)
                                itemData = next((item for item in DatatPablic if str(item[1]).replace(" ","").lower() == maine_search.replace(" ","").lower() ),None)
                                if itemData is not None:
                                    values = list(itemData)
                                    values.reverse()
                                    listObject = (values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7])
                                    # print(listObject)
                                    treeview.insert('',END, values=listObject )
                                    treeview.configure(selectmode="extended")      
            else:
                get_chaldern = treeview.get_children()
                namesearsh = name_oprtionname.get()
                for items in get_chaldern:
                        treeview.delete(items)
                for item in DataMonth:
                    if item["ACcrditionStateOIL"] == kindCont or item['ACcrditionStatediesel'] == kindCont:
                            # print(item)
                            for ite in item['Arraypash']: 
                                if d.lower().replace(" ","") == "timeData".lower().replace(" ",""):
                                    spent_entry.delete(0,"end")
                                    self.Funextrct(ite,item)
                                else:
                                    if len(maine_search) > 0:
                                        if namesearsh == 'المستلم':
                                            if ite['namerecevid'].replace(" ","").lower() == maine_search.replace(" ","").lower():
                                                self.Funextrct(ite,item)
                                        elif namesearsh == 'المستخدم':
                                            if ite['user'].replace(" ","").lower() == maine_search.replace(" ","").lower():
                                                self.Funextrct(ite,item)
                                        else:  
                                            if ite['nameusefly'].replace(" ","").lower() == maine_search.replace(" ","").lower():
                                                self.Funextrct(ite,item)
    # وظيفة فلترة حسب الفرز التاريخ والنوع والاسم
    def Funextrct(self,ite,item):
        classefiyoprtion = "OIL" if  kind_oprtionkind.get()  == 'بترول' else 'diesel'
        if kind_oprtion.get().lower().replace(" ","") == "الاسم وتاريخ الشهر واليوم".lower().replace(" ",""):
            if datetime.strptime(ite['Timedey'],'%Y-%m-%d').date() ==  datetime.strptime(select_entryD.get(),'%Y-%m-%d').date() :
                # print(kind_oprtion.get()) 
                self.oprtion_all(ite,item)
        elif kind_oprtion.get().replace(" ","").lower() == 'الاسم وتاريخ الشهر'.replace(" ","").lower():
                if datetime.strptime(ite['Timedey'],'%Y-%m-%d').month ==  int(re.findall('\d+',str(select_entryMonth.get()))[1]) and  datetime.strptime(ite['Timedey'],'%Y-%m-%d').year ==  int(re.findall('\d+',str(select_entryMonth.get()))[0]):
                    # print(ite)
                    # print(kind_oprtion.get()) 
                    self.oprtion_all(ite,item)
        elif kind_oprtion.get().lower().replace(" ","") == "الاسم وتاريخ الشهر والنوع".lower().replace(" ",""): 
            if datetime.strptime(ite['Timedey'],'%Y-%m-%d').month ==  datetime.strptime(select_entryMonth.get(),"%Y-%m").month and  ite['Classefiy'] == classefiyoprtion:
                        self.oprtion_all(ite,item)
        elif kind_oprtion.get().lower().replace(" ","") == 'الاسم وتاريخ اليوم والنوع'.lower().replace(" ",""): 
            if datetime.strptime(ite['Timedey'],'%Y-%m-%d') ==  datetime.strptime(select_entryD.get(),"%Y-%m-%d") and  ite['Classefiy'] == classefiyoprtion:
                self.oprtion_all(ite,item)  
        else:
                self.oprtion_all(ite,item)
 # وظيفة ادخال البيانات المفلتره
    def oprtion_all(self,ite,item):
        classefiy = kind_oprtionkind.get()
        namecalssify = 'بترول' if  ite['Classefiy'] == 'OIL' else 'ديزل'
        if classefiy.lower().replace(" ","") == 'كافة'.lower().replace(" ",""):
             listObject = (ite['ID'],ite["idusers"],ite['nameusefly'],item['quantityOIL'],item['quantitydiesel'],ite['amountSpentday'],ite['Timedey'],ite['namerecevid'],namecalssify,ite['user'],ite['inconmicquntity'])
        else:
            allquantity = item['quantityOIL'] if  classefiy.lower().replace(" ","") == 'بترول'.lower().replace(" ","")  else item['quantitydiesel']
            listObject = (ite['ID'],ite["idusers"],ite['nameusefly'],allquantity,ite['amountSpentday'],ite['Timedey'],ite['namerecevid'],namecalssify,ite['user'],ite['inconmicquntity'])
        value =list(listObject)
        value.reverse()
        treeview.insert('', END, values=value)
        treeview.configure(selectmode='extended')  
        # keyname= item['nameusefly']
    def Printsearch(self):
        user = responsebletUser()
        if len(user) > 0 and user is not None  :
            if user['Responsibilities'].replace(" ","") == "المسؤل المباشر".replace(" ",""):
                arrays = []
                dataTreeview = treeview.get_children()
                for key in dataTreeview:
                    data = treeview.item(key)['values']
                    arrays.append(data)
                search = select_entry.get()
                # print(arrays)
                if len(arrays) > 0:
                    url= printSearch(arrays,kind_oprtion.get(),search,user['userName'])   
                    Printdivec(self,url)       
                else:
                     messagebox.showwarning(title='خطأ', message="عملية البحث فارغه لايمكن طباعتها")  
            else: 
                messagebox.showwarning(title='خطأ', message="ليس لديك الصلاحية الكافية لطباعة العملية")         
                
                              
                          
                
        
          