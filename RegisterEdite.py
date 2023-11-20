from tkinter import *
from tkinter import ttk
from convertcod.internal_Loginstorge import *
from convertcod.json_stringify import json_stringify
from convertcod.json_parse import json_parse


class RegisterEdite(ttk.Frame):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)
        def founInsert():
            print('hello')
            datauser =get_loginAll()     
            usernamre =name_pach.get()
            passwor= spent_entry.get()
            if len(usernamre) > 0 and usernamre != 'ادخل اسم المستخدم' and len(passwor) > 0 and passwor != 'ادخل كلمة مرور' :
                if datauser is None  :
                    newimportres= "true"
                    newAddcridesres = "true"
                    stopCridesres =  "true"
                    printstatmentres = "true"
                else:
                    # print(newimport.get())
                    newimportres="true" if  newimport.get() == True else 'false'
                    newAddcridesres ="true"  if newAddcrides.get() == True else 'false'
                    stopCridesres = "true" if  stopCrides.get() == True else 'false'
                    printstatmentres = "true" if  printstatmeent.get() == True else 'false'
                jsonRespons = {"التوريد بكميات جديدة":newimportres,"إضافة وتعديل اعتماد":newAddcridesres,"توقيف اعتماد":stopCridesres,"طباعة تقارير":printstatmentres}                    
                Updat_item(ID,usernamre,passwor,json_stringify(jsonRespons))
                name_pach.delete(0,'end')
                name_pach.insert(0,'ادخل اسم المستخدم')
                spent_entry.delete(0,'end')
                spent_entry.insert(0,'ادخل كلمة مرور')
                newimport_chackbox.state(["!selected"])
                newAddcrides_chackbox.state(["!selected"])
                stopCrides_chackbox.state(["!selected"])
                Printstatment_chackbox.state(["!selected"])
                gettree = treeview.get_children()
                for item in gettree:
                    treeview.delete(item)
                treeview.update()
                loading()              
            else:
                messagebox.showwarning(title="Error",message="يرجى اكمال البيانات ")
            
        def loading():
            global datauser
            datauser= get_loginAll()
            lisHeading = list({'تاريخ انشاء الحساب',"نوع الحساب",'اسم المستخدم'})
            if len(datauser) > 0 :
                for colsname in  lisHeading:
                    treeview.heading(colsname,text=colsname)
                for values in datauser:
                    valu = list(values)
                    # valu.reverse()
                    item = (valu[5],valu[3],valu[1])
                    treeview.insert('',END,values=item)
                    treeview.configure(selectmode='extended')
             
        def on_selectuser(event):
            global ID
            selcted = treeview.selection()[0]
            table = treeview.item(selcted)["values"]
            # print(table[0])
            if datauser is not None and len(datauser) > 0 :
                for item in datauser:
                    if table[2] == item[1]:
                        ID = item[0]
                        name_pach.delete(0,'end')
                        name_pach.insert(0,item[1])
                        spent_entry.delete(0,'end')
                        spent_entry.insert(0,item[2])
                        if item[4] is not None and len(item[4]) > 0 :
                            dataRespons = json_parse(item[4])
                            # print(dataRespons)
                            if dataRespons["التوريد بكميات جديدة"] == 'true':
                                newimport.set(value=True)
                                newimport_chackbox.state(["selected"])
                            else:
                                newimport.set(value=False)
                                newimport_chackbox.state(["!selected"])
                            if dataRespons["إضافة وتعديل اعتماد"] == 'true':
                                    newAddcrides.set(value=True)
                                    newAddcrides_chackbox.state(["selected"])
                            else:
                                newAddcrides.set(value=False)
                                newAddcrides_chackbox.state(["!selected"])
                            if dataRespons["توقيف اعتماد"] == 'true':
                                    stopCrides.set(value=True)
                                    stopCrides_chackbox.state(["selected"])
                            else:
                                stopCrides.set(value=False)
                                stopCrides_chackbox.state(["!selected"])
                            if dataRespons["طباعة تقارير"] == 'true':
                                printstatmeent.set(value=True)
                                Printstatment_chackbox.state(["selected"])
                            else:
                                printstatmeent.set(value=False)
                                Printstatment_chackbox.state(["!selected"])                                           
        def newPage():
            global name_pach
            global spent_entry
            global newimport
            global newAddcrides
            global stopCrides
            global printstatmeent
            global newimport_chackbox
            global newAddcrides_chackbox
            global stopCrides_chackbox
            global Printstatment_chackbox
            global treeview
            
          
            newimport = BooleanVar()
            newAddcrides= BooleanVar()
            stopCrides = BooleanVar()
            EditCrides= BooleanVar()
            printstatmeent = BooleanVar()

            frame = ttk.Frame(self,padding=15)
            frame.pack(anchor='center',padx=20,pady=60,fill='both')
            widgets_frame = ttk.LabelFrame(frame, text="تسجيل مستخدم",padding=15)
            widgets_frame.grid(row=0,column=1,padx=15,pady=5,sticky='en')
            # widgets_frame.place(y=250,x=690)
      
            pachNew = ttk.Frame(widgets_frame)
            pachNew.grid(row=0,column=0,pady=15,padx=5,sticky='nesw')
            text_kind = ttk.Label(pachNew,text="...اسم المستخدم" )
            text_kind.grid(row=0,column=1,padx=15,pady=15)
            def on_focus_in(event):
                 name_pach.focus_force()
                 name_pach.icursor('end')

            name_pach = ttk.Entry(pachNew,width=30)
            # name_pach.config(cursor="arrow")
            name_pach.bind("<FocusIn>",on_focus_in)
            name_pach.grid(row=0, column=0,padx=5, pady=5, sticky="ew")
            # name_pach.insert(0,'ادخل اسم المستخدم')
    
            viewChack= ttk.LabelFrame(widgets_frame,text='صلاحية المستخدم',padding=10)
            viewChack.grid(row=1,column=0,padx=20,pady=20)
            textimport = ttk.Label(viewChack,text="التوريد بكميات جديدة")
            textimport.grid(row=2,column=1)
            newimport_chackbox = ttk.Checkbutton(viewChack,variable=newimport)
            newimport_chackbox.grid(row=2,column=0,padx=10,pady=10,sticky="nsew")
            textAddcrides = ttk.Label(viewChack,text="إضافة اعتماد جديد او تعديله")
            textAddcrides.grid(row=2,column=3, padx=10,pady=10,sticky='nsew')
            newAddcrides_chackbox= ttk.Checkbutton(viewChack,variable=newAddcrides)
            newAddcrides_chackbox.grid(row=2,column=2,padx=10,pady=10,sticky='nsew')
            textStpo_chakbox = ttk.Label(viewChack, text='توقيف اعتماد موجود')
            textStpo_chakbox.grid(row=3,column=1,padx=10,pady=10,sticky='nsew')
            stopCrides_chackbox=ttk.Checkbutton(viewChack,variable=stopCrides)
            stopCrides_chackbox.grid(row=3,column=0,padx=10,pady=10,sticky='nsew')
            textPrint= ttk.Label(viewChack,text="طباعة تقارير")
            textPrint.grid(row=3,column=3,pady=10,padx=10,sticky='nsew')
            Printstatment_chackbox= ttk.Checkbutton(viewChack,variable=printstatmeent)
            Printstatment_chackbox.grid(row=3,column=2,padx=10,pady=10,sticky='nsew')
            # التوريد بكميات جديدة 
            # إضافة اعتماد جيديد او تعديل
            # توقيف اعتماد موجود
            # خصم من اعتماد موجود 
            # طباعة التقارير (اليومية-الشهرية-السنوي)
            # طباعة الباركود
            # //المستخدم العادي
            # الاستعلام 
            # الصرف 
            # طباعة تقرير إستلام نهاية الكمية 
            # إدخال الاسم في النثريات
            pachSpent = ttk.Frame(widgets_frame,width=40)
            pachSpent.grid(row=2,column=0,pady=15,padx=5)
            Spnlabltext = ttk.Label(pachSpent,text="كلمة المرور", font=("arial",10,"bold"))
            Spnlabltext.grid(row=0,column=0)
            spent_entry= ttk.Entry(pachSpent,width=25)
            spent_entry.grid(row=0, column=1,padx=5, pady=5, sticky="ew")
            spent_entry.insert(0,'ادخل كلمة مرور')
            
            kindspent_entry =ttk.Button(widgets_frame,text="ادخال",command=founInsert,width=40)
            kindspent_entry.grid(row=4, column=0,padx=5, pady=5, sticky="ew")
            
            FarmTree = ttk.Frame(frame,width=900,height=500)
            FarmTree.grid(row=0,column=0,padx=20,pady=5,sticky='nesw')
            FarmTree.pack_propagate(0)
            treeScroll= ttk.Scrollbar(FarmTree)
            treeScroll.pack(side='right',fill='y')
            cols=('تاريخ انشاء الحساب',"نوع الحساب",'اسم المستخدم')
            
            treeview = ttk.Treeview(FarmTree,show='headings', yscrollcommand=treeScroll.set,columns=cols,height=500)
            treeview.pack(side='right',anchor='center')
            treeview.column('اسم المستخدم',width=350,anchor='center')
            treeview.column('نوع الحساب',width=300,anchor='center')
            treeview.column('تاريخ انشاء الحساب', width=300,anchor='center')
            treeScroll.config(command=treeview.yview)
            treeview.bind('<<TreeviewSelect>>',on_selectuser)
        newPage()
        loading()