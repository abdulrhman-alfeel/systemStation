
from tkinter import *
from tkinter import ttk
from convertcod.internal_Loginstorge import *
from Print.PrintDay import *
from Print.PrintMonth import *
from Print.PrintYrs import *
# from tkPDFViewer import tkPDFViewer as pdf
from sqiltyFoun import *
from datetime import datetime ,timedelta 

class PrintStatment(ttk.Frame):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)
        self.frames = {}
        self.Date = []
        global select_toDataday
        global print_toview
        global select_entryD
        start_data = datetime(2023,9,1)
        end_data = datetime(2030,9,1)
        for day in range((end_data - start_data).days +1):
                databis = start_data + timedelta(days=day)
                self.Date.append(databis.date())  
        viewimage = ttk.Frame(self)
        viewimage.pack()
        print_day =ttk.Button(viewimage,text="طباعة تقارير يومية",command=lambda:self.switchFUNCTION(print_day,'day') ,width=30,padding=(5,5))
        print_day.pack(side="right",anchor="n",padx=20,pady=20)
        print_month =ttk.Button(viewimage,text="طباعة تقارير شهرية" ,command=lambda:self.switchFUNCTION(print_month,'month') ,width=35,padding=(7,7))
        print_month.pack(side="right",anchor="n",padx=20,pady=20)   
        print_yurs =ttk.Button(viewimage,text="طباعة تقارير سنوية" ,command=lambda: self.switchFUNCTION(print_yurs,'yrs'),width=35,padding=(7,7) )
        print_yurs.pack(side="right",anchor="ne",padx=20,pady=20) 
        select_TextentryD = ttk.Label(self,text="من إلى ")
        select_TextentryD.pack()
        view = ttk.Frame(self)
        view.pack()
        select_TextentryD = ttk.Label(view,text="من تاريخ")
        select_TextentryD.grid(row=1,column=1,padx=10,pady=10)
        select_entryD = ttk.Combobox(view,values=self.Date,width=35)
        select_entryD.grid(row=2,column=1 ,padx=10,pady=10,sticky='nesw')
        select_entryD.set(self.Date[0])
        select_toData = ttk.Label(view,text="حتى تاريخ")
        select_toData.grid(row=1,column=0,padx=10,pady=10)
        select_toDataday = ttk.Combobox(view,values=self.Date,width=35)
        select_toDataday.grid(row=2,column=0 ,padx=10,pady=10,sticky='nesw')
        select_toDataday.set(self.Date[0])
        print_to =ttk.Button(view,text="طباعة",command=lambda:self.switchFUNCTION(print_to,'BETWEENPRINT') )
        print_to.grid(row=3,column=1 ,padx=15,pady=10,sticky='nesw')
        print_toview =ttk.Button(view,text="عرض", command=lambda:self.switchFUNCTION(print_toview,'BETWEENVIEO') )
        print_toview.grid(row=3,column=0 ,padx=15,pady=10,sticky='nesw')
    def switchFUNCTION(self,print,text): 
        user =get_item()
        popUpMenu = Menu(print, tearoff=0, border=0,borderwidth=5)
        if text == 'month':
            popUpMenu.add_separator()
            popUpMenu.add_command(label="طباعة", accelerator=" ", command=lambda:register_user(varfetc={"type": 'month',"younger-then":datetime.now().date() ,"bigger":datetime.now().date(),'kindjop':'print',"page":print,"user":user['userName']}))
            popUpMenu.add_separator()
            popUpMenu.add_command(label="عرض", accelerator=" ",command=lambda:register_user(varfetc={"type": 'month',"younger-then":datetime.now().date() ,"bigger":datetime.now().date(),'kindjop':'view',"page":print,"user":user['userName']}))
            popUpMenu.add_separator()
        elif text == 'yrs':  
            popUpMenu.add_separator()
            popUpMenu.add_command(label="طباعة", accelerator=" ",command=lambda :register_yrs(item={'kindjop':'print',"page":print,"user":user['userName']}))
            popUpMenu.add_separator()
            popUpMenu.add_command(label="عرض", accelerator=" ",command=lambda :register_yrs(item={'kindjop':'view',"page":print,"user":user['userName']}))  
            popUpMenu.add_separator()
        elif text == 'BETWEENVIEO':
            popUpMenu.add_separator()
            popUpMenu.add_command(label="عرض بالسرد اليومي", accelerator=" ",command=lambda : statament_day(varfetch={"type": "BETWEEN","younger-then":select_toDataday.get() ,"bigger":select_entryD.get(),'kindjop':"view",'page':print,"user":user['userName']}))
            popUpMenu.add_separator()
            popUpMenu.add_command(label="عرض بالسرد الشهري", accelerator=" ",command=lambda :register_user(varfetc={"type": "BETWEEN","younger-then":select_toDataday.get() ,"bigger":select_entryD.get(),'kindjop':"view",'page':print,"user":user['userName']}))  
            popUpMenu.add_separator()
        elif text == 'BETWEENPRINT':
            popUpMenu.add_separator()
            popUpMenu.add_command(label="طباعة بالسرد اليومي", accelerator=" ",command=lambda : statament_day(varfetch={"type": "BETWEEN","younger-then":select_toDataday.get() ,"bigger":select_entryD.get(),'kindjop':"print",'page':print,"user":user['userName']}))
            popUpMenu.add_separator()
            popUpMenu.add_command(label="طباعة بالسرد الشهري", accelerator=" ",command=lambda :register_user(varfetc={"type": "BETWEEN","younger-then":select_toDataday.get() ,"bigger":select_entryD.get(),'kindjop':"print",'page':print,"user":user['userName']}))  
            popUpMenu.add_separator()
        else:
            popUpMenu.add_separator()
            popUpMenu.add_command(label="طباعة", accelerator=" ",command=lambda: statament_day(varfetch={"type": "day","younger-then":datetime.now().date() ,"bigger":datetime.now().date(),'kindjop':'print',"page":print,"user":user['userName']}))
            popUpMenu.add_separator()
            popUpMenu.add_command(label="عرض", accelerator=" ",command=lambda: statament_day(varfetch={"type": "day","younger-then":datetime.now().date() ,"bigger":datetime.now().date(),'kindjop':'view',"page":print,"user":user['userName']}))
            popUpMenu.add_separator()  
        infox = print.winfo_rootx()
        infoy = print.winfo_rooty()
        popUpMenu.post(infox,infoy)      