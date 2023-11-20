from tkinter import *
from tkinter import ttk
from convertcod.internal_Loginstorge import *
from convertcod.json_stringify import json_stringify
from convertcod.internal_storage import set_itemx
class Register(ttk.Frame):
    def __init__(self,parent,controller):
            ttk.Frame.__init__(self,parent)
             
       
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
            
          
            newimport = BooleanVar()
            newAddcrides= BooleanVar()
            stopCrides = BooleanVar()
            EditCrides= BooleanVar()
            printstatmeent = BooleanVar()
            
            # imageArry = PhotoImage(file= "AERWICON.png")
            # imageArry.width =200

            widgets_frame = ttk.LabelFrame(self, text="تسجيل مستخدم",padding=(20,15))
            widgets_frame.pack(side='top',anchor='center',padx=20,pady=20)
            # widgets_frame.place(y=250,x=600)
      
            pachNew = ttk.Frame(widgets_frame)
            pachNew.grid(row=0,column=0,pady=15,padx=5)
            text_kind = ttk.Label(pachNew,text="...اسم المستخدم" )
            text_kind.grid(row=0,column=1,padx=15,pady=15)
           
            name_pach = ttk.Entry(pachNew,width=30)
            name_pach.grid(row=0, column=0,padx=5, pady=5, sticky="ew")
            name_pach.insert(0,'ادخل اسم المستخدم')
            name_pach.bind("<FocusIn>", lambda e:name_pach.delete(0,'end'))
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
        
            pachSpent = ttk.Frame(widgets_frame,width=40)
            pachSpent.grid(row=2,column=0,pady=15,padx=5)
            Spnlabltext = ttk.Label(pachSpent,text="كلمة المرور")
            Spnlabltext.grid(row=0,column=0)
            spent_entry= ttk.Entry(pachSpent,width=25)
            spent_entry.grid(row=0, column=1,padx=5, pady=5, sticky="ew")
            spent_entry.insert(0,'ادخل كلمة مرور')
            spent_entry.bind("<FocusIn>",lambda e: spent_entry.delete(0,'end'))
            
            kindspent_entry =ttk.Button(widgets_frame,text="ادخال",command=lambda: self.founInsert(controller),width=40)
            kindspent_entry.grid(row=4, column=0,padx=5, pady=5, sticky="ew")
            
  
    def founInsert(self,controller):
            # print('hello')
            self.datauser = get_loginAll()   
            usernamre =name_pach.get()
            passwor= spent_entry.get()
            newimportres= "true"
            newAddcridesres = "true"
            stopCridesres =  "true"
            printstatmentres = "true"
            respnbilt ="المسؤل المباشر"
            if len(usernamre) > 0 and usernamre != 'ادخل اسم المستخدم' and len(passwor) > 0 and passwor != 'ادخل كلمة مرور' :
                if self.datauser is not None and len(self.datauser) > 0:
                    # print(self.datauser)
                    # print(newimport.get())              
                    # print(userDatat,'hllllllo')
                    newimportres="true" if  newimport.get() == True else 'false'
                    newAddcridesres ="true"  if newAddcrides.get() == True else 'false'
                    stopCridesres = "true" if  stopCrides.get() == True else 'false'
                    printstatmentres = "true" if  printstatmeent.get() == True else 'false'
                    respnbilt ="مناوب"
                jsonRespons = {"التوريد بكميات جديدة":newimportres,"إضافة وتعديل اعتماد":newAddcridesres,"توقيف اعتماد":stopCridesres,"طباعة تقارير":printstatmentres}
                set_item(usernamre,passwor,respnbilt,json_stringify(jsonRespons))
                if  respnbilt.replace(" ","") == 'المسؤل المباشر'.replace(" ","") and  len(self.datauser) <= 1:
                    set_itemActivite({"userName":usernamre,"passwordUSER":passwor,"Responsibilities": respnbilt,"jsonResponsibilities":json_stringify(jsonRespons)})
                    set_itemx(usernamre,'بداية تشغيل')
                    controller.Show_frame(controller.page5,{"Start"})
                messagebox.showinfo(title="تم",message="تم انشاء حساب  بنجاح ")
                # controller.Show_frame(controller.page1,{"name1" : 'OIL',"name2":'new'})
                name_pach.delete(0,'end')
                name_pach.insert(0,'ادخل اسم المستخدم')
                spent_entry.delete(0,'end')
                spent_entry.insert(0,'ادخل كلمة مرور')
                newimport_chackbox.state(["!selected"])
                newAddcrides_chackbox.state(["!selected"])
                stopCrides_chackbox.state(["!selected"])
                Printstatment_chackbox.state(["!selected"])  
            else:
                messagebox.showwarning(title="Error",message="يرجى اكمال البيانات ")
            