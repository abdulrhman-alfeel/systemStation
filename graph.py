
from datetime import datetime , timedelta
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from data import inventory_day_data,inventory_month_data
from convertcod.json_parse import json_parse
from convertcod.internal_storage import get_itemx
from convertcod.internal_Loginstorge import get_loginAll
import re
# import gc

class graph(ttk.Frame):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)
        global treeview
        global select_kindcont
        global se_entry
        global select_entryD
        number = 0
        colselect = ["نوع وتاريخ","تاريخ الحركة","نوع الحركة","اسم المستخدم"]
        col = ["تاريخ الحركة","نوع الحركة","اسم المستخدم","م"]
        self.search_ent_var = tk.StringVar()
        self.Data=[]
        start = datetime(2023,10,1)
        end_data = datetime(2030,10,1)
        for day in range((end_data - start).days +1):
            datat = start +timedelta(days=day)
            self.Data.append(datat.date())
        frameall = ttk.LabelFrame(self,border=15,borderwidth=2)
        frameall.pack(expand=True)
        # goback = ttk.Button(frameall,text='رجوع',command=lambda:controller.Show_frame(controller.page1,{"name1" : 'OIL',"name2":'new'}))
        # goback.pack(side='right',anchor='ne')
        # goback.place(y=30,x=1300)
        search_frame = ttk.LabelFrame(frameall,text='استعلام')
        search_frame.pack(side='top',fill='none',expand=True)
     
        fram_entry = ttk.LabelFrame(search_frame)
        fram_entry.grid(row=0,column=0,padx=10,pady=10,sticky='nesw')
        buttom_entry = ttk.Button(fram_entry,text="حسب التاريخ",command=lambda:  self.oprtionSearch(select_entryD.get() if select_entryD.get() == "تاريخ الحركة" else '' ,'',number))
        buttom_entry.grid(row=0,column=1,padx=5)
        select_entryD = ttk.Combobox(fram_entry,values=self.Data)
        select_entryD.grid(row=0,column=0,padx=5,pady=5)
        select_entryD.set(self.Data[3])
        select_kindconttryD = ttk.Label(search_frame,text="نوع عملية البحث")
        select_kindconttryD.grid(row=0,column=1,padx=5,pady=5)
        select_kindcont = ttk.Combobox(search_frame,values=colselect,width=25)
        select_kindcont.grid(row=0,column=2,padx=5,pady=15,sticky='nesw')
        select_kindcont.bind("FoucesIN",self.filterFirstname)
        select_kindcont.current(1)
        se_entry = ttk.Entry(search_frame,textvariable=self.search_ent_var)
        se_entry.grid(row=0,column=3,padx=15,pady=15,sticky='nesw')
        se_entry.bind('<KeyRelease>',self.filterFirstname)
        self.search_ent_var.trace("w",self.filterFirstname)
        freetree = ttk.Frame(frameall,width=800,height=500)
        freetree.pack_propagate(0)
        freetree.pack(side='right',anchor='e')
        scroll = ttk.Scrollbar(freetree,orient='vertical')
        scroll.pack(side='right',fill='y',pady=20)
        scrollx = ttk.Scrollbar(freetree,orient='horizontal')
        scrollx.pack(side='bottom',fill='x',padx=20)
        treeview = ttk.Treeview(freetree,columns=col,yscrollcommand=scroll.set,xscrollcommand=scrollx.set,height=400)
        treeview.heading("م",text="م")
        treeview.heading('اسم المستخدم',text='اسم المستخدم')
        treeview.heading('نوع الحركة',text='نوع الحركة')
        treeview.heading("تاريخ الحركة",text="تاريخ الحركة")
        treeview.column('م',width=50,anchor='center')
        treeview.column('اسم المستخدم',width=250,anchor='center')
        treeview.column('نوع الحركة',width=150 ,anchor='center')
        treeview.column("تاريخ الحركة",width=200,anchor='center')
        treeview.pack(side="right",fill='both',padx=(10,0))
        scrollx.config(command=treeview.xview)
        scroll.config(command=treeview.yview)

# textReshaped = arabic_reshaper.reshape(textUtf8)
# textDisplay = get_display(textReshaped)
        farcm = ttk.Frame(frameall)
        farcm.pack(side='right',fill='both',expand=True)
        scrollbar = ttk.Scrollbar(farcm, orient='vertical')
        scrollbar.pack(side='right', fill='y')
        
        scrollbarhst = ttk.Scrollbar(farcm,orient='horizontal')
   
        scrollbarhst.pack(side='bottom', fill='x')
        # scrollbarhst.place(y=255,x=255)
        canva = tk.Canvas(farcm ,bg="#313131",width=800,height=400,xscrollcommand=scrollbarhst.set,yscrollcommand=scrollbar.set)
        canva.pack(fill='both',side='right',expand=True)
                 
        canva.bind("<FocusIn>",lambda e: canva.configure(scrollregion=canva.bbox("all")))
        scrollbarhst.config(command=canva.xview)
        scrollbar.config(command=canva.yview)
        upper_frame = ttk.Frame(canva)
        canva.create_window((0,0),window=upper_frame)
        plt.rcParams['axes.prop_cycle']= plt.cycler(
            color=['#4C2AB5', "#BE96FF", "#957DAD", "#5E366E","#A98CCC"]   
        )
        # inventory = list(inventory_data.keys())
        # inventory.reverse()
        # fig2, ax2 = plt.subplots()
        # ax2.bar(inventory,inventory_data.values())
        # ax2.set_title("الحركة الشهرية للمستخدم")
        # ax2.set_xlabel("المستخدم")
        # ax2.set_ylabel("الحركة")
        # one_frame = ttk.Frame(upper_frame)
        # one_frame.pack(fill='both', expand=True)
        # canvas2 = FigureCanvasTkAgg(fig2,one_frame)
        # canvas2.draw()
        # canvas2.get_tk_widget().config(height=400,width=850) 
        # canvas2.get_tk_widget().pack(side='right')
        fig4, ax4 = plt.subplots()
        ax4.plot(list(inventory_month_data.keys()), list(inventory_month_data.values()))
        ax4.set_title('الحركة خلال السنة')
        # canvas2.switch_backends(one_frame)
        lower_frame = ttk.Frame(upper_frame)
        lower_frame.pack(fill='both', expand=True)
        canvas4 = FigureCanvasTkAgg(fig4,lower_frame)
        canvas4.draw()
        canvas4.get_tk_widget().config(height=350,width=850)
        canvas4.get_tk_widget().pack()
        # self.loden()
        fig5, ax5 = plt.subplots()
        ax5.fill_between(inventory_day_data.keys(), inventory_day_data.values())
        ax5.set_title('الحركة الاسبوعية')
        canvas5 = FigureCanvasTkAgg(fig5,lower_frame)
        canvas5.draw()
        canvas5.get_tk_widget().pack(side='left',fill='both',expand=True)
    def loden(self):
        index =0
        global arrays
        global arrayrepb
        global arraymovemd
        global userorgin
        arraymovemd = get_itemx() 
        userorgin = get_loginAll() 
        arrays = []
        arrayrepb= []
        # print(len(arraymovemd))
        dataview = treeview.get_children()
        for keyu in dataview:
            treeview.delete(keyu)
        # treeview.update()
        for nams in userorgin:
            dat = treeview.insert(parent="",index=tk.END,text=nams[1].capitalize())
            for v in arraymovemd:
                    if v['userName'].lower().replace(" ",'') == nams[1].lower().replace(" ",''):   
                        index += 1
                        # print(k) 
                        op = json_parse(v["arrayMovement"]) if v['arrayMovement'] is not None else []
                                            # print(op)
                        saction = list(v.values())
                        saction.reverse()
                        # if str(saction[4]).lower() == nams[1].lower():
                        all = (saction[3],saction[2],saction[4],saction[5])
                                                # print(saction[5])
                        arr = treeview.insert(parent=dat,index=tk.END,values=all)
                        # treeview.update()
                        if len(op) > 0 :
                            for mov in op:
                                    rev = list(mov.values())
                                    # rev.reverse()
                                    arrayrepb.append(rev)
                                    treeview.insert(parent=arr,index=tk.END,values=rev)
                    # else:
                #     index = 0
    def filterFirstname(self,event,*args):
            global index 
            index = 0
            itemIon=  treeview.get_children()
            search = se_entry.get().capitalize()
            kind = select_kindcont.get()
            try:
                for each in itemIon:
                    # print(each)
                    # trree = treeview.item(each)
                    # print(trree['values'])
                    # if search == trree['text']:
                    if event.keycode == 8 and len(search) <= 0:
                    # if event.keysym == "BackSpace" and len(search) <= 0:
                                treeview.delete(each)
                    else:
                        treeview.delete(each)
                if event.keycode == 8  and len(search) <= 0:
                    # if event.keysym == "BackSpace"  and len(search) <= 0:
                    self.loden()
                # print(event)
                if kind.lower().replace(" ","") == 'اسم المستخدم'.lower().replace(" ",""):
                    for pic in userorgin: 
                        # if str(pic[1]).lower().capitalize() == search.lower().capitalize(): 
                        if re.search(pic[1].lower().replace(" ",''),search.lower().replace(" ",'')): 
                            # print(pic[1])
                            dat = treeview.insert(parent="",index=tk.END,text=pic[1].lower())
                            for ite in arraymovemd:
                                if ite['userName'] == pic[1]:
                                    index +=1
                                    self.oprtionSearch(kind,dat,index,picc=ite)
                                else:
                                    index=0
                else:
                    self.oprtionSearch(kind,'',index)
            except KeyError:
                print('keysym')
     
    def oprtionSearch(self,kin,dat,index,picc=None):
        timd = select_entryD.get()
        if kin == '':
            itemIon=  treeview.get_children()
            for pic in itemIon:
                treeview.delete(pic)
            se_entry.delete(0,"end")
        # print(timd)
        if kin.lower().replace(" ","") != 'اسم المستخدم'.lower().replace(" ",""):
            for item in arraymovemd:
                extrctdemon = datetime.strptime(str(timd), '%Y-%m-%d').date()
                extractorgion = datetime.strptime(item['datamovement'],'%Y-%m-%d %H:%M:%S.%f').date()
                # print(re.search(item['datamovement'],timd))
                if kin == 'تاريخ الحركة':
                    if  extrctdemon == extractorgion:
                        index +=1
                        self.selsctcrditon(item,dat,index) 
                elif kin == 'نوع الحركة':
                    if re.search(se_entry.get().lower().replace(" ",'') , item['kindMovment'].lower().replace(" ",'')):
                        index +=1
                        self.selsctcrditon(item,dat,index) 
                else:
                    if  re.search(se_entry.get().lower().replace(" ",''), item['kindMovment'].lower().replace(" ",'')) and  extrctdemon == extractorgion:
                        index += 1
                        self.selsctcrditon(item,dat,index) 
                # gc.collect()
        else:
            self.selsctcrditon(picc,dat,index)
    def selsctcrditon(self,item,dat,index):
          op=json_parse(item["arrayMovement"]) if item['arrayMovement'] is not None else []
          seac = list(item.values())
          seac.reverse()
          index +=1
          al = (seac[3],seac[2],seac[4],index)
          arr =treeview.insert(parent=dat,index=tk.END,values=al)
          for j in op:
            subJson = list(j.values())
            subJson.reverse() 
            treeview.insert(parent=arr,index=tk.END,values=subJson)
                    # else:
                    #        
        #   gc.collect()