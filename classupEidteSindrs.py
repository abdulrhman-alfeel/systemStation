import sqlite3
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, timedelta
from sqiltyFoun import StationMonthSqly
from convertcod.processor import on_KeyPress
import time
# import options
# options.clear_option_database()
# # Add a new option to the option database.
# options.option_add("my_option", "default_value")
# # Get the value of the option.
# my_option_value = options.get("my_option")
# # Print the value of the option.
# print(my_option_value)

last_updated_at = time.time()
class SindrsEdit(ttk.Frame):
    def __init__(self, parent,controller):
        ttk.Frame.__init__(self,parent)
        self.combo_list = ["Subscribed", "Not Subscribed", "Other"]
        self.pablicprosonl = []
        start_date = datetime.now()
        # start_date = datetime(2023, 9, 1)
        end_date = datetime(2028, 9, 30)
        self.dates = []
        for day in range((end_date - start_date).days + 1):
         datall = start_date + timedelta(days=day)
         self.dates.append(datall.date())
        # self.lodDataEditSendrs(
        global quantity_spinbox
        global quantity_spinboxdiesel
        oneFrame = ttk.LabelFrame(self,text="الكمية المخصصة للنثريات")
        # oneFrame.grid(row=0,column=1, pady=15,padx=15)
        oneFrame.pack(side='right',anchor='ne')
        oneFrame.place(x=200,y=200)
        # text_Leble = ttk.Label(oneFrame,text=,padding=(10,10))
        # text_Leble.grid(row=0,column=0,padx=5, pady=15, sticky="nsew")
        Frameoil = ttk.LabelFrame(oneFrame,text='بترول')
        Frameoil.grid(row=1,column=1,padx=5,pady=15, sticky='nsew')
        quantity_spinbox = ttk.Spinbox(Frameoil, from_=18, to=100,width=40 )
        quantity_spinbox.grid(row=0, column=0,padx=5, pady=15, sticky="nsew")
        quantity_spinbox.insert(0, 0)
        quantity_spinbox.bind("<FocusIn>", lambda e:  quantity_spinbox.delete('0', "end"))
        quantity_spinbox.bind("<KeyRelease>",lambda e :on_KeyPress(quantity_spinbox,e))
        Framediesel = ttk.LabelFrame(oneFrame,text='ديزل')
        Framediesel.grid(row=1,column=2,padx=5,pady=15, sticky='nsew')
        quantity_spinboxdiesel = ttk.Spinbox(Framediesel, from_=18, to=100,width=40 )
        quantity_spinboxdiesel.grid(row=1, column=2,padx=5, pady=15, sticky="nsew")
        quantity_spinboxdiesel.insert(0, 0)
        quantity_spinboxdiesel.bind("<FocusIn>", lambda e:  quantity_spinboxdiesel.delete('0', "end"))
        quantity_spinboxdiesel.bind("<KeyRelease>",lambda e :on_KeyPress(quantity_spinboxdiesel,e))
        
        status_combobox = ttk.Combobox(oneFrame, state="readonly",values=self.dates,width=35)
        status_combobox.grid(row=1, column=0,padx=5, pady=5, sticky="nsew")
        status_combobox.set(self.dates[0])
        button = ttk.Button(oneFrame,text="تعديل", command=self.insert_row)
        button.grid(row=7, column=0,padx=15, pady=5, sticky="nsew")
        
        separator = ttk.Separator(oneFrame,orient="vertical")
        separator.grid(row=9, column=0, padx=10, pady=20, sticky="nsew")
        
        self.lodDataEditSendrs()
    def insert_row(self):      
            # global vierfiyDone
            incomquantity = quantity_spinbox.get()
            incomquantitydiesel = quantity_spinboxdiesel.get()
            if int(incomquantity) > 0 or int(incomquantitydiesel) > 0:
                # print(keys)
                if keys == "نثريات":
                 StationMonthSqly.UpdateSinders(incomquantity,incomquantitydiesel) 
                else:
                    messagebox.showwarning(title='Error',message='لايوجد حساب نثريات حتى الان يرجى انشاء حساب نثريات اوثلاً') 
                    quantity_spinbox.delete(0,'end')
                    quantity_spinbox.insert(0,0)
            else:
                    messagebox.showwarning(title="Erorr", message="يجب اكمال ادخال البيانات")
    def lodDataEditSendrs(self):
            global pablic
            global keys
            keys = 'اعتماد'
            try:
                pablic = StationMonthSqly.inComin_Pablic()
                for i in pablic:
                    if i[1] == "نثريات":
                            keys = "نثريات"
                            quantity_spinbox.delete(0,'end')
                            quantity_spinbox.insert(0,i[2])
                            quantity_spinboxdiesel.delete(0,'end')
                            quantity_spinboxdiesel.insert(0,i[3])
            except sqlite3.IntegrityError:
                print("error sqlite")
                
          
 
    
  
      
    
      