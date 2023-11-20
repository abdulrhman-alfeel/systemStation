import sqlite3
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, timedelta
from sqiltyFoun import StationMonthSqly
from convertcod.processor import on_KeyPress
import time
from convertcod.json_parse import randomnumber
# import options
# options.clear_option_database()
# # Add a new option to the option database.
# options.option_add("my_option", "default_value")

# # Get the value of the option.
# my_option_value = options.get("my_option")

# # Print the value of the option.
# print(my_option_value)

last_updated_at = time.time()
class Spentincomeng(ttk.Frame):
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
        global quantity_name
        global quantity_amount
        oneFrame = ttk.LabelFrame(self,text="الكميةالمراد تصريفها")
        # oneFrame.grid(row=0,column=1, pady=15,padx=15)
        oneFrame.pack(anchor='center',pady=85)
        # oneFrame.place(x=200,y=200)
        # text_Leble = ttk.Label(oneFrame,text=,padding=(10,10))
        # text_Leble.grid(row=0,column=0,padx=5, pady=15, sticky="nsew")
        Frameoil = ttk.LabelFrame(oneFrame,text='مستلم الكمية')
        Frameoil.grid(row=0,column=0,padx=5,pady=15, sticky='nsew')
        quantity_name = ttk.Entry(Frameoil,width=40 )
        quantity_name.grid(row=0, column=0,padx=25, pady=15, sticky="nsew")
        quantity_name.insert(0, "اسم المستلم")
        quantity_name.bind("<FocusIn>", lambda e:  quantity_name.delete('0', "end"))
        Framediesel = ttk.LabelFrame(oneFrame,text='لتر')
        Framediesel.grid(row=1,column=0,padx=25,pady=15, sticky='nsew')
        quantity_amount = ttk.Entry(Framediesel,width=40 )
        quantity_amount.grid(row=0, column=0,padx=5, pady=15, sticky="nsew")
        # quantity_amount.insert(0, "الكمية")
        quantity_amount.bind("<FocusIn>", lambda e:  quantity_amount.delete('0', "end"))
        quantity_amount.bind("<KeyRelease>",lambda e :on_KeyPress(quantity_amount,e))
    
        button = ttk.Button(oneFrame,text="سحب", command=self.insert_row)
        button.grid(row=2, column=0,padx=15, pady=5, sticky="nsew")
        separator = ttk.Separator(oneFrame,orient="vertical")
        separator.grid(row=3, column=0, padx=10, pady=20, sticky="nsew")
        
    def insert_row(self):      
            # global vierfiyDone
            classifyProcess = pablic['classifyProcess']
            Namerecevd = quantity_name.get()
            if len(Namerecevd) > 0 :
                # print(keys)
                try:
                            thermen = int(pablic['thermen'])
                            amountٍٍSpent = int(pablic['amountٍٍSpent'])
                            amountٍٍSpent += thermen 
                            # monthstr = datetime.strptime(pic['receivedData'],'%Y-%m-%d').strftime("%B")
                            numberIdusb= randomnumber()
                            ArrayjsonNow={"IDS":numberIdusb , "incomingSub": thermen,"receivedSub":str(datetime.now().date()),"kindpackge":f"سحب باقي الحمولة باستلام {Namerecevd}"}
                            array =  []
                            for i in pablic['Arrayjson']:
                                array.append({'IDS': i['IDS'], 'incomingSub':i["incomingSub"], 'receivedSub': i['receivedSub'], 'kindpackge': i['kindpackge']})
                            array.append(ArrayjsonNow)
                            # print(pablic['Arrayjson'],array) 
                            updatobject={"ID":pablic['ID'],'amountٍٍSpent':amountٍٍSpent,"thermen":0,"Arrayjson":array,'classifyProcess':classifyProcess}
                            StationMonthSqly.SpentINconmec(updatobject)   
                            messagebox.showinfo(title="ok",message="تم سرف الكمية بنجاح")
                except:
                    print('هناك خطاء')     
            else:
                    messagebox.showwarning(title="Erorr", message="يجب اكمال ادخال البيانات")
      
    def lodData(self,item):
            global pablic
            global keys
            keys = 'اعتماد'
            try:
                pablic = item
                quantity_amount.configure(state='normal')
                quantity_amount.delete(0,"end")
                quantity_amount.insert(0,item['thermen'])
                quantity_amount.configure(state='disabled')
            except sqlite3.IntegrityError:
                print("error sqlite")
                
          
 
    
  
      
    
      