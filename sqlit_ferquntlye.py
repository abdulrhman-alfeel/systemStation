from datetime import datetime
import random
from sqiltyFoun import StationMonthSqly
from tkinter import messagebox
from Print.printes import printerNew
from Print.Oprationprint import Oprationprint
# Dispatch actions to update the state
from Print.viewpdf import switchMonth

class MethodSqlet():
        def __init__(self,idusers,sendrisOpject,aciton,classefiy,Time):
            self.quantityAll= 0
            self.DoneF= 'false'
            self.expiryDate= 0
            self.IDAllStation= 0
            self.IDHomM= 0
            self.QuantitySub= 0
            self.Quantitydefrint= 0
            self.thermandefrint= 0
            self.DoneSub= 'false'
            self.SpentSub= 0
            self.RmenSub= 0
            self.nameSub=''
            self.idusers= idusers
            self.idusersM=0
            self.datatim=0
            self.amountSpent = 0
            self.therman = 0
            self.sendrisOpject = sendrisOpject
            self.acitonMon =aciton
            self.acitonStat=aciton
            self.Time  = Time
            # self.idMushuser = 896378072967
            self.idMushuser = "نثريات"
            self.SindrTrue = False
            self.classefiy = classefiy
            self.Arraypash = []
            self.get_comenData()
        def get_comenData(self):
            station =  StationMonthSqly.inComin_dataAll()
            Ferquntlye =  StationMonthSqly.inComin_Data()
            # print(self.Time,self.acitonStat)
            # print(int(self.idusers))and int(re.findall('\d+', item['datatim'])[1]) == datetime.now().month
            stationcrute = next((item for item in station if item["DoneF"] == 'false' and item['aciton'] == self.acitonStat and item['classifyProcess'] == self.classefiy and datetime.strptime(item['receivedData'],'%Y-%m-%d').month == self.Time),None)
            if stationcrute is not None: 
                Ferquntcurent = next((item for item in Ferquntlye if item['idusers'] == int(self.idusers) ),None)
                if  Ferquntcurent is not None and Ferquntcurent['aciton'] == self.acitonMon and Ferquntcurent["DoneSub"] == "false" and Ferquntcurent["ACcrditionStateOIL"] != "موقف" and datetime.strptime(Ferquntcurent['datatim'],'%Y-%m-%d').month == self.Time or Ferquntcurent is not None and Ferquntcurent['aciton'] == self.acitonMon and Ferquntcurent["DoneSub"] == "false" and  Ferquntcurent["ACcrditionStatediesel"] != "موقف" and datetime.strptime(Ferquntcurent['datatim'],'%Y-%m-%d').month == self.Time : 
                        # print(len(stationcrute),len(Ferquntcurent))
                        #Ferqunt  obje[''] =  data[i][11]     
                    if  stationcrute['classifyProcess']  == 'OIL' :
                        self.QuantitySub = int(Ferquntcurent['quantityOIL'])
                        self.SpentSub= int(Ferquntcurent['amountٍٍSpentOIL']) if Ferquntcurent['amountٍٍSpentOIL'] is not None else 0
                        self.RmenSub = int(Ferquntcurent['thermenOIL']) 
                        self.Quantitydefrint= int(Ferquntcurent['quantitydiesel'])   
                        self.thermandefrint=  int(Ferquntcurent['thermendiesel'])  
                    else:
                        self.QuantitySub = int(Ferquntcurent['quantitydiesel']) 
                        self.SpentSub= int(Ferquntcurent['amountٍٍSpentdiesel']) if Ferquntcurent['amountٍٍSpentdiesel'] is not None else 0
                        self.RmenSub = int(Ferquntcurent['thermendiesel']) 
                        self.Quantitydefrint= int(Ferquntcurent['quantityOIL'])  
                        self.thermandefrint=  int(Ferquntcurent['thermenOIL']) 
                    self.Time = stationcrute['receivedData'] 
                    self.DoneSub= Ferquntcurent['DoneSub']
                    self.idusersM= Ferquntcurent['idusers']
                    self.IDHomM= Ferquntcurent['ID']
                    self.datatim= Ferquntcurent['datatim']
                    if Ferquntcurent['Arraypash'] is not None and len(Ferquntcurent['Arraypash']) > 0:
                        self.Arraypash = Ferquntcurent['Arraypash']
                    self.acitonMon= Ferquntcurent['aciton']
                    if Ferquntcurent is not None and  Ferquntcurent['nameusefly'].replace(" ","") == self.idMushuser.replace(" ",""):
                            self.nameSub = self.sendrisOpject['nameSub']
                            self.SindrTrue = True
                    else:
                            self.nameSub= Ferquntcurent['nameusefly']
                else:
                        if  Ferquntcurent is not None  and Ferquntcurent["DoneSub"] == "true" :
                            messagebox.showwarning(title="Error",message="رصيد الحساب منتهي")
                        else:   
                             messagebox.showwarning(title="Error",message="لايمكن اكمال العملية لايوجد مدخل معتمد لهذا الحساب")
                self.acitonStat = stationcrute["aciton"]
                    # station
                self.quantityAll = stationcrute['incomingquantity']
                self.amountSpent = int(stationcrute['amountٍٍSpent']) if stationcrute['amountٍٍSpent'] is not None else 0
                self.therman = int(stationcrute['thermen']) if stationcrute['thermen'] is not None else 0
                self.DoneF = stationcrute['DoneF']  
                self.expiryDate = stationcrute['expiryDate']
                self.IDAllStation = stationcrute['ID']
            else:
                if self.acitonStat == 'previous':
                     messagebox.showinfo(title="الحمولة السابقة خلصت",message="لم يعد هناك حمولة سابقة في المحطة")
                else:
                     messagebox.showwarning(title="Error",message="يجب تحميل حمولة قبل البدء بعمليةالصرف")
            
        def insert_ferquntly(self,spentNumb,kindinsert,sumprive,namerecevid,user):
            objectINsert={}
            #ferquntly
            if  self.SindrTrue  == True:
                namedusfly='نثريات' 
                recevid = self.nameSub
            else:
                namedusfly= self.nameSub
                recevid = namerecevid
            spentM =  int(self.SpentSub) 
            num1= "0123456789"
            num2= "0123456789"
            number= num1 + num2
            length = 6
            resulte = "".join(random.sample(number,length))
            if kindinsert != 'صرف':
                spentM -= sumprive
                self.amountSpent -= sumprive
                self.RmenSub += sumprive
                resulte = kindinsert["ID"]
            falsing = False
            if self.idusersM == int(self.idusers)  :
                    if spentM > 0:
                        spentM +=  int(spentNumb)
                    else:
                        spentM = int(spentNumb)
                    if spentM >  int(self.QuantitySub):
                        falsing = False
                        messagebox.showwarning(title="Error", message="لايمكن اكمال العملية الكمية اكبر من المتبقي لديه ")            
                    elif spentM == int(self.QuantitySub):
                            self.SpentSub = spentM
                            if self.Quantitydefrint > 0 and self.thermandefrint <= 0  or self.Quantitydefrint <= 0: 
                                 self.DoneSub = 'true'
                            self.RmenSub -= int(spentNumb) 
                            falsing = True 
                    else:
                          self.SpentSub = spentM
                          self.DoneSub = 'false'
                          self.RmenSub -= int(spentNumb)
                          falsing = True  
            if  falsing is True:
                # self.amountSpent += int(self.SpentSub)
                self.amountSpent += int(spentNumb)
                # print(self.amountSpent,int(self.SpentSub),int(spentNumb),'hllow')
                if self.amountSpent >  int(self.quantityAll):
                    falsing = False
                    messagebox.showwarning(title="Error", message=" لايمكن اكمال العملية الكمية المصروفة اكبر من الايراد العام  ")
                elif  self.amountSpent == int(self.quantityAll):
                        self.DoneF= 'true'
                        falsing = True
                        self.expiryDate = str(datetime.now())
                else:
                    self.DoneF= 'false'
                    falsing = True
                # print(falsing) 
                if falsing is True :  
                    objectINsert['Idcoder']= self.idusersM
                    arrayall = []
                    for item in  self.Arraypash:
                        if int(item["ID"]) == int(resulte):
                             arrayall.append(kindinsert)
                        else:
                            arrayall.append(item)
                    jsonPash = [ites for ites in arrayall]
                    # print(kindinsert)
                    if kindinsert == 'صرف':
                         jsonPash.append({"ID":str(resulte),"idusers": str(self.idusersM),'nameusefly':str(namedusfly),"amountSpentday":str(spentNumb),"Classefiy": str(self.classefiy),"Timedey": str(datetime.now().date()),'namerecevid':str(recevid),"user":str(user),"inconmicquntity":switchMonth(datetime.strptime(self.Time,'%Y-%m-%d').strftime('%B'))})
                    if jsonPash is not None and len(jsonPash) > 0 :
                        objectINsert['Arraypash'] = jsonPash
                    else:
                           objectINsert['Arraypash'] = []
                    #mounth
                    objectINsert['amountn']= self.SpentSub
                    objectINsert['therm']=  self.RmenSub 
                    objectINsert['DoneSub']= self.DoneSub
                    objectINsert['Idcoder']= self.idusersM
                    objectINsert['idhom']= self.IDAllStation
                    objectINsert['datatim'] = self.datatim
                    # print(self.datatim)
                    #allfrequntly
                    objectINsert['acitonMon'] = self.acitonMon
                    objectINsert["acitonStat"] = self.acitonStat
                    objectINsert['amountnAll']= self.amountSpent
                    objectINsert['thermAA']=  int(self.quantityAll) - self.amountSpent  
                    objectINsert['DoneF']= self.DoneF
                    objectINsert['expiryDate']=  self.expiryDate
                    objectINsert['ID']= self.IDAllStation
                    objectINsert['classifyprocess']= self.classefiy   
                    # def printAsy():    
                    StationMonthSqly.insert_SqlytMot(objectINsert,str(self.classefiy))
                    kindamunt = "بترول" if self.classefiy == "OIL" else "ديزل"
                    percentage_view= 0
                    if self.SindrTrue  == False:
                        try:
                            printerNew(self.SpentSub,self.RmenSub,spentNumb,user,namedusfly,recevid,kindamunt,self.SindrTrue,datetime.now().date(),switchMonth(datetime.strptime(self.Time,'%Y-%m-%d').strftime('%B')))
                        except:
                            print("error printer")
                    try:
                        percentage_view= Oprationprint.startfunction(resulte,namedusfly,recevid,spentNumb,kindamunt,user,switchMonth(datetime.strptime(self.Time,'%Y-%m-%d').strftime('%B')))
                    except:
                            print('error printer Epson')
                    return percentage_view
               