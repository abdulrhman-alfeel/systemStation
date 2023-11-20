import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, timedelta
from convertcod.processor import on_KeyPress
from sqiltyFoun import StationMonthSqly
from convertcod.internal_storage import *
from convertcod.SumAll import loadDatastation
from Print.viewpdf import switchMonth
from convertcod.json_parse import randomnumber
from convertcod.userfind import findUser 

class StationAdd(ttk.Frame):
    # def __init__(self,pags_labl,textnuberAllMonth,textnuberAll):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)
        self.combo_list = ["Subscribed", "Not Subscribed", "Other"]
        self.pablicprosonl = []
        global Oil
        global diesel 
        global fromClassify
        global statDiesal
        global statOil
        global status_combobox
        global treeview 
        global quantity_spinbox
        global dates 
        global textStat
        start_date = datetime.now()
        # start_date = datetime(2023, 9, 1)
        end_date = datetime(2028, 9, 30)
        dates = []
        Oil = tk.BooleanVar(value=True)
        diesel = tk.BooleanVar(value=False)

        for day in range((end_date - start_date).days + 1):
         datall = start_date + timedelta(days=day)
         dates.append(datall.date())
        #   load_data()
        treeFrame = ttk.Frame(self,width=1200,height=500)
        treeFrame.grid(row=0,column=0, pady=15,padx=5)
        treeFrame.pack_propagate(0)
        treeScroll = ttk.Scrollbar(treeFrame)
        treeScroll.pack(side="right", fill="y")
        cols= ("نوع التوريد","حالة الحمولة","المتبقي منها","المنصرف منها","تاريخ الاستلام", "الكمية الواردة","م")
        treeview = ttk.Treeview(treeFrame,show='tree headings',yscrollcommand=treeScroll.set, columns=cols,height=500,padding=(10,10))
        treeview.column("م",width=20,anchor='center')
        treeview.column("الكمية الواردة",width=150,anchor='center')
        treeview.column("تاريخ الاستلام",width=130,anchor='center')
        treeview.column("المنصرف منها",width=200,anchor='center')
        treeview.column("المتبقي منها",width=150,anchor='center')
        treeview.column("حالة الحمولة",width=150,anchor='center')
        treeview.column("نوع التوريد",width=150,anchor='center')
        treeview.pack()
        treeScroll.config(command=treeview.yview)
        oneFrame = ttk.Frame(self)
        oneFrame.grid(row=0,column=1, pady=15,padx=15)
        # oneFrame.pack(anchor="center",fill='both')
        textStat = ttk.Label(oneFrame,text='لابد من تسجيل الحمولة قبل البد باي عملية')
        textStat.grid_forget()
        # self.findmovement()
        fromClassify = ttk.LabelFrame(oneFrame)
        fromClassify.grid(row=1,column=0)

        statOil = ttk.Checkbutton(fromClassify,text='بترول',variable=Oil)
        statOil.grid(row=1,column=0,padx=5,pady=5)
        statOil.bind("<FocusIn>",lambda e: self.statFunction("oil"))
        statDiesal = ttk.Checkbutton(fromClassify,text='ديزل',variable=diesel)
        statDiesal.bind("<FocusIn>",lambda e: self.statFunction("diesel") )
        statDiesal.grid(row=1,column=1,padx=5,pady=5)
        quantity_spinbox = ttk.Spinbox(oneFrame, from_=18, to=100 )
        quantity_spinbox.grid(row=2, column=0,padx=5, pady=15, sticky="ew")
        quantity_spinbox.insert(0, "الكمية الواردة")
        quantity_spinbox.bind("<FocusIn>", lambda e:  quantity_spinbox.delete('0', "end"))
        quantity_spinbox.bind("<KeyRelease>",lambda e :on_KeyPress(quantity_spinbox,e))
        status_combobox = ttk.Combobox(oneFrame, state="readonly",values=dates,width=35)
        status_combobox.grid(row=3, column=0,padx=15, pady=5, sticky="ew")
        status_combobox.set(dates[0])
        button = ttk.Button(oneFrame,text="اضافة", command=lambda:self.insert_row(controller))
        button.grid(row=4, column=0,padx=15, pady=5, sticky="ew")
        separator = ttk.Separator(oneFrame,orient="vertical")
        separator.grid(row=5, column=0, padx=10, pady=20, sticky="ew")
        self.load_data()
    def findmovement(itemuser):
            # print(itemuser)
            if itemuser["kindMovment"].replace(" ","") == 'بداية تشغيل'.replace(" ",""):
                # print('بدء running')
                textStat.grid(row=0,column=0,padx=5,pady=5)
    def insert_row(self, controller):      
            # global vierfiyDone
        # try:
            incomquantity = quantity_spinbox.get()
            receivedData = status_combobox.get()
            classifyP = "OIL"  if Oil.get() == True else "diesel"
            if int(incomquantity) > 0  and len(classifyP) > 0 :
                StationMonthSqly.insert_Pablic_station(incomquantity,receivedData,classifyP)
                Items = treeview.get_children()
# Delete the item
            stat = StationMonthSqly.inComin_dataAll()
            if len(stat) > 0:       
                # datatest = stat[len(stat) -1]
                datatest = next((ite for ite in stat if ite['classifyProcess'] == classifyP and datetime.strptime(ite['receivedData'],'%Y-%m-%d').month < datetime.now().month),None)
                if datatest is not None:
                    self.exportdata(classifyP)
                    print(stat)
                for item in Items:
                    treeview.delete(item)
                treeview.update()
                self.load_data()
                loadDatastation(controller.textnuberAllMonth,controller.textnuberAll,controller.textnuber,'OIL')  
                loadDatastation(controller.textnuberAllMonthdiesel,controller.textnuberAlldiesel,controller.textnuberdiesel,'diesel')
                chaking= get_virfe()
                # print(chaking['kindMovment'])
                if chaking['kindMovment'] == 'بداية تشغيل' :
                        # print('start')
                        controller.Show_frame(controller.page4,{'Start'})
                textStat.grid_forget()
                opration = {"kindopr":"اضافة حمولة","Timeopr":str(datetime.now().time()),'nameusefly':'بترول' if classifyP == 'OIL' else "ديزل" }
                InsertJson(opration)  
                objectSum = {}     
                # set_conv_imge(quantity)
                quantity_spinbox.delete(0,'end')
                quantity_spinbox.insert(0,"الكمية الواردة")
                status_combobox.delete(0,'end')
                status_combobox.set(dates[0])
            else:
                messagebox.showwarning(title="Erorr", message="يجب اكمال ادخال البيانات")
        # except:
        #     pass
   
    def load_data(self):
            global objectsall
            self.pablicprosonl = StationMonthSqly.inComin_dataAllwitch()
            lisvalues = list({"نوع التوريد","حالة الحمولة","المتبقي منها","المنصرف منها","تاريخ الاستلام", "الكمية الواردة",'م'})
        # #     print(list_values)
            index = 0
            items = treeview.get_children()
            for pic in items :
                treeview.delete(pic)
            for col_name in lisvalues:
                    treeview.heading(col_name, text=col_name)
            for value_tuple in self.pablicprosonl:
                    values = list(value_tuple)
                    values.reverse()
                    amountSp = values[3] if values[3] is not None else 0
                    threm = values[4] if values[4] is not None else 0
                    statIncom = "جاري" if values[2] == "false" else "منتهي "
                    kindINcom = "بترول"  if values[1] == 'OIL' else 'ديزل' 
                    index+= 1 
                    objectsall = (kindINcom,statIncom,amountSp,threm,values[5],values[6],index )
                    valu = treeview.insert(parent='',index=values[7],values=objectsall)
                    if len(value_tuple[7])> 0 and value_tuple[7] != "null":    
                        for k in json_parse(value_tuple[7]):
                            # print(k)
                            v = list(k.values())
                            treeview.insert(parent=valu,index=tk.END,values=v)
    def statFunction(self,type):
            if type  == "diesel":
                fromClassify.config(text='ديزل')
                statOil.state(["!selected"])
                Oil.set(value=False)   
            else:
                fromClassify.config(text='بترول')
                statDiesal.state(["!selected"])
                diesel.set(value=False)

    def exportdata(self,kind):
        if findUser() == True:
                try:
                    previous = []
                    importdata = StationMonthSqly.inComin_dataAll()
                    for item in importdata:
                        if item['aciton'] == 'previous' and item['classifyProcess'] == kind and item['DoneF'] == 'false':
                            previous.append(item) 
                    if len(previous) > 0:
                        for pic in previous :
                            incoming =  int(pic['incomingquantity'])
                            thermen = int(pic['thermen']) if pic['thermen'] is not None else 0
                            totle = incoming - thermen
                            monthstr = datetime.strptime(pic['receivedData'],'%Y-%m-%d').strftime("%B")
                            month = switchMonth(monthstr)
                            monthstrnow = datetime.now().strftime("%B")
                            monthnow = switchMonth(monthstrnow)
                            numberIdusb= randomnumber()
                            Arrayjson={"IDS":numberIdusb , "incomingSub": thermen,"receivedSub":str(datetime.now().date()),"kindpackge":f"تحويل من شهر {month}"}
                            ArrayjsonNow={"IDS":numberIdusb , "incomingSub": thermen,"receivedSub":str(datetime.now().date()),"kindpackge":f"تحويل إلى شهر {monthnow}"}
                            array =  []
                            for i in pic['Arrayjson']:
                                array.append({'IDS': i['IDS'], 'incomingSub':i["incomingSub"], 'receivedSub': i['receivedSub'], 'kindpackge': i['kindpackge']})
                            array.append(ArrayjsonNow)
                            # print(pic['Arrayjson'],array) 
                            updatobject={'amountٍٍSpent':totle,"thermen":0,"Arrayjson":Arrayjson,'ArrayjsonNow':array,'classifyProcess':pic['classifyProcess']}
                            StationMonthSqly.exportpackge(updatobject)   
                            messagebox.showinfo(title="ok",message="تم التحويل بنجاح")
                except:
                    print('هناك خطاء')     
          
      