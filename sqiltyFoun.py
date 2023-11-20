import sqlite3
from datetime import datetime
from tkinter import messagebox
import re
from convertcod.json_stringify import json_stringify
from convertcod.json_parse import *
import os 
from convertcod.processor import resource_path
from convertcod.internal_storage import get_selectData
def nameData():
    Dirbase = get_selectData()
    if len(Dirbase) <= 0 :
        Dirbase= 'assets\\backup\\data.db'
    # print(Dirbase[0][1])
    return resource_path(str(Dirbase[0][1]))
class StationMonthSqly():
        def __init__(self):
            self.Frequntlye = []
            self.inComin_dataAll()
        
        #   عملية توريد الكميات
        def insert_Pablic_station(incomingquantity,receivedData,classifyP):
                numberIdusb= randomnumber()
                        # print(classifyP)
                arrayNew=[]
                numSum = 0
                
                        # connection = sqlite3.connect(resource_path('assets\\backup\\data.db'))
                try:
                    
                    connection = sqlite3.connect(nameData())
                    cursor = connection.cursor()
                    try:
                        stat = station  
                        with connection:
                            vierfiy = next((item for item in stat if item["DoneF"] == "false" and datetime.strptime(item["receivedData"],'%Y-%m-%d').month < datetime.now().month and item["classifyProcess"] == classifyP),None)
                            vierfiyDone = next((item for item in stat if item["DoneF"] == "false" and  datetime.strptime(item["receivedData"],'%Y-%m-%d').month == datetime.now().month and item["classifyProcess"] == classifyP ),None)
                            # print(incomingquantity,vierfiy,vierfiyDone)
                            if vierfiy is not None :
                                teable_stat = '''UPDATE station SET aciton = "previous" WHERE DoneF="false" OR aciton="new"'''
                                cursor.execute(teable_stat)
                                arraye = [{"IDS":numberIdusb , "incomingSub": incomingquantity,"receivedSub":receivedData,"kindpackge":"اضافة حمولة"}]
                                array_data= json_stringify(arraye)
                                teable_insert_qurey= '''INSERT INTO station (incomingquantity,receivedData,amountٍٍSpent,thermen,DoneF,aciton,Arrayjson,classifyProcess) VALUES(?,?,?,?,"false","new",?,?)'''
                                data_insert_tuple = (incomingquantity,receivedData,0,incomingquantity,array_data,classifyP)
                                cursor.execute(teable_insert_qurey,data_insert_tuple)
                                connection.commit()
                            elif vierfiyDone is not None  :
                                array = vierfiyDone['Arrayjson'] if vierfiyDone['Arrayjson'] is not None else []
                                arrayNew = list(array)
                                arrayNew.append({"IDS":numberIdusb , "incomingSub": incomingquantity,"receivedSub":receivedData,"kindpackge":"اضافة حمولة"})
                                iD = vierfiyDone["ID"]
                                numSum += int(vierfiyDone['incomingquantity'])
                                numSum += int(incomingquantity)
                                # print(numSum,array)
                                array_data = json_stringify(arrayNew)
                                # print(array_data)   
                                teable_update = '''UPDATE station SET incomingquantity=?, Arrayjson=? WHERE ID=?'''
                                dataupdate = (numSum,array_data,iD)
                                cursor.execute(teable_update,dataupdate)
                                connection.commit()
                            else:
                                arraye = [{"IDS":numberIdusb , "incomingSub": incomingquantity,"receivedSub":receivedData,"kindpackge":"حمولة جديدة"}]
                                array_data= json_stringify(arraye)
                                teable_insert_qurey= '''INSERT INTO station (incomingquantity,receivedData,amountٍٍSpent,thermen,DoneF,aciton,Arrayjson,classifyProcess) VALUES(?,?,?,?,"false","new",?,?)'''
                                data_insert_tuple = (incomingquantity,receivedData,0,incomingquantity,array_data,classifyP)
                                cursor.execute(teable_insert_qurey,data_insert_tuple)
                                connection.commit()
                                # print("scssefly")               
                    except:
                            # print("there is a problem") 
                                arraye = [{"IDS":numberIdusb , "incomingSub": incomingquantity,"receivedSub":receivedData,"kindpackge":"حمولة جديدة"}]
                                array_data= json_stringify(arraye)
                                teable_insert_qurey= '''INSERT INTO station (incomingquantity,receivedData,amountٍٍSpent,thermen,DoneF,aciton,Arrayjson,classifyProcess) VALUES(?,?,?,?,"false","new",?,?)'''
                                data_insert_tuple = (incomingquantity,receivedData,0,incomingquantity,array_data,classifyP)
                                cursor.execute(teable_insert_qurey,data_insert_tuple)
                                connection.commit()
                except sqlite3.IntegrityError:
                    connection.close() 
        def exportpackge(key):
            ArrayUpdat = key['Arrayjson']
            ArrayjsonNow = json_stringify(key['ArrayjsonNow'])
            # print(ArrayjsonNow)
            conection  =  sqlite3.connect(nameData())
            try:
                # print(ArrayjsonNow)
                cursor = conection.cursor()
                table = 'UPDATE station SET incomingquantity=?, amountٍٍSpent=?,thermen=?,DoneF ="true", Arrayjson=? WHERE  DoneF ="false" AND aciton="previous" AND  classifyProcess=?'
                cursor.execute(table,[key['amountٍٍSpent'],key['amountٍٍSpent'],key['thermen'],ArrayjsonNow,key['classifyProcess']])
                conection.commit()
                vierfiyDone = next((item for item in station if item["DoneF"] == "false" and  datetime.strptime(item["receivedData"],'%Y-%m-%d').month == datetime.now().month and item["classifyProcess"] == key['classifyProcess'] ),None)
                if vierfiyDone is not None :
                                numSum = int(ArrayUpdat['incomingSub'])
                                array = vierfiyDone['Arrayjson'] if vierfiyDone['Arrayjson'] is not None else []
                                arrayNew = list(array)
                                arrayNew.append(ArrayUpdat)
                                iD = vierfiyDone["ID"]
                                numSum += int(vierfiyDone['incomingquantity'])
                                # print(numSum,array)
                                array_data = json_stringify(arrayNew)
                                thermen = numSum - int(vierfiyDone['amountٍٍSpent'])
                                # print(array_data)   
                                teable_update = '''UPDATE station SET incomingquantity=?,thermen=?, Arrayjson=? WHERE ID=?'''
                                dataupdate = (numSum,thermen,array_data,iD)
                                cursor.execute(teable_update,dataupdate)
                                conection.commit()
                else:
                                arraye = [ArrayUpdat]
                                array_data= json_stringify(arraye)
                                incomingquantity= int(ArrayUpdat['incomingSub'])
                                teable_insert_qurey= '''INSERT INTO station (incomingquantity,receivedData,amountٍٍSpent,thermen,DoneF,aciton,Arrayjson,classifyProcess) VALUES(?,?,?,?,"false","new",?,?)'''
                                data_insert_tuple = (incomingquantity,ArrayUpdat['receivedSub'],0,incomingquantity,array_data,key['classifyProcess'])
                                cursor.execute(teable_insert_qurey,data_insert_tuple)
                                conection.commit()
            except sqlite3.IntegrityError:
                print("error in sqlite")
            conection.close()
        def SpentINconmec(key):
            ArrayUpdat = json_stringify(key['Arrayjson'])
            # print(ArrayjsonNow)
            conection  =  sqlite3.connect(nameData())
            try:
                # print(ArrayjsonNow)
                cursor = conection.cursor()
                table = 'UPDATE station SET amountٍٍSpent=?,thermen=?,DoneF ="true", Arrayjson=? WHERE ID=?'
                cursor.execute(table,[key['amountٍٍSpent'],key['thermen'],ArrayUpdat,key['ID']])
                conection.commit()
            except sqlite3.IntegrityError:
                pass
            conection.close()
   # وظائف حسابات الاعتمادات    
        def insert_Pablic(idUser,name,quantityOIL,quantitydiesel,prosonle,Time,ACcrditionStatediesel,ACcrditionStateOIL):
                    connection =  sqlite3.connect(nameData())
                    try:
                        with connection:                     
                            teable_insert_qurey= '''INSERT INTO station_pablic (idusers,nameusefly,quantityOIL,quantitydiesel,DoneSub,oprtionPush,ACcrditionStatediesel,ACcrditionStateOIL,datatim,aciton ) VALUES(?,?,?,?,"false",?,?,?,?,"new")'''
                            data_insert_tuple = (str(idUser),str(name),str(quantityOIL),str(quantitydiesel),str(prosonle),str(ACcrditionStatediesel),str(ACcrditionStateOIL),str(Time))
                            cursor = connection.cursor()
                            cursor.execute(teable_insert_qurey,data_insert_tuple)
                            valuefind = next((item for item in Ferquntlye if item['idusers'] == str(idUser)),None)
                            if valuefind is None :
                                statmentall = '''INSERT INTO station_MonthD (idusers,nameusefly,quantityOIL,quantitydiesel,thermenOIL,thermendiesel,DoneSub,ACcrditionStatediesel,ACcrditionStateOIL,aciton) VALUES (?,?,?,?,?,?,"false",?,?,"new")'''
                                statmentallSUb = (str(idUser),str(name),str(quantityOIL),str(quantitydiesel),str(quantityOIL),str(quantitydiesel),str(ACcrditionStatediesel),str(ACcrditionStateOIL))
                                cursor.execute(statmentall,statmentallSUb)
                            connection.commit()
                    except sqlite3.IntegrityError:
                            print("there is a problem") 
                    
                    connection.close() 
        def Update_pablic(objectSum,VIREBLISWITCH):
            try:
                conn =  sqlite3.connect(nameData())
                with conn:
                        cursor = conn.cursor()
                        if VIREBLISWITCH == 'OIL':
                            updtastat = '''UPDATE station_pablic SET quantityOIL=? WHERE idusers =?
                            '''
                            dataupdate = (objectSum["quantity"] , objectSum["idusers"] )
                            cursor.execute(updtastat,dataupdate)
                        else:
                            updtastatDIESEL = '''UPDATE station_pablic SET quantitydiesel=? WHERE idusers =?
                            '''
                            dataupdateDIESEL = (objectSum["quantity"] , objectSum["idusers"] )
                        
                            cursor.execute(updtastatDIESEL,dataupdateDIESEL)
                        conn.commit()  
            except sqlite3.IntegrityError:
                    messagebox.showerror(title="Erorr", message="تاكد من ملف البيانات الرئيسية قد يكون محذوفاً او مضروباً")
            conn.close()
        
        def Update_pablicAll(objectSum):
            try:
                conn =  sqlite3.connect(nameData())
                with conn:
                        cursor = conn.cursor()
                        updtastat = '''UPDATE station_pablic SET nameusefly=?, quantityOIL=?,quantitydiesel=?,oprtionPush=?,ACcrditionStatediesel=?,ACcrditionStateOIL=? WHERE idusers =? 
                        '''
                        dataupdate = (objectSum['nameusefly'],objectSum["quantityOIL"] ,objectSum['quentitydiesel'],objectSum['oprtionPush'],objectSum['ACcrditionStatediesel'],objectSum["ACrditionStateOIL"], objectSum["idusers"] )
                        cursor.execute(updtastat,dataupdate)
                        updtastatMonth = '''UPDATE station_MonthD SET nameusefly=?, quantityOIL=?,quantitydiesel=?,ACcrditionStatediesel=?,ACcrditionStateOIL=? WHERE idusers =?  AND datatim BETWEEN strftime('%Y-%m-01',CURRENT_DATE )  AND CURRENT_DATE 
                        '''
                        dataupdatemonth = (objectSum['nameusefly'],objectSum["quantityOIL"] ,objectSum['quentitydiesel'],objectSum['ACcrditionStatediesel'],objectSum["ACrditionStateOIL"], objectSum["idusers"] )
                        cursor.execute(updtastatMonth,dataupdatemonth)
                        conn.commit()
                        return True                
            except sqlite3.IntegrityError:
                    messagebox.showerror(title="Erorr", message="تاكد من ملف البيانات الرئيسية قد يكون محذوفاً او مضروباً")
            conn.close()
        
        def UpdateStopdCrdits(Statecrdition,idU,kindoprition):
                # print(Statecrdition,idU)
                connnection =  sqlite3.connect(nameData())
                try:
                    with connnection:
                        cursor = connnection.cursor()
                        if kindoprition == 'All':
                             statCurso = "UPDATE station_pablic SET ACcrditionStatediesel=?,ACcrditionStateOIL=? WHERE idusers = ? "
                        # STATdata = ()
                             cursor.execute(statCurso,[Statecrdition,Statecrdition,idU])
                             statCursoMONth = "UPDATE station_MonthD SET ACcrditionStatediesel=?,ACcrditionStateOIL=? WHERE idusers = ?  AND datatim BETWEEN strftime('%Y-%m-01',CURRENT_DATE )  AND CURRENT_DATE"
                        # STATdata = ()
                             cursor.execute(statCursoMONth,[Statecrdition,Statecrdition,idU])
                        elif kindoprition == 'OIL':
                                statCurso = "UPDATE station_pablic SET ACcrditionStateOIL=? WHERE idusers = ? "
                        # STATdata = ()
                                cursor.execute(statCurso,[Statecrdition,idU])
                                statCursoMONth = "UPDATE station_MonthD SET ACcrditionStateOIL=? WHERE idusers = ?  AND datatim BETWEEN strftime('%Y-%m-01',CURRENT_DATE )  AND CURRENT_DATE"
                                cursor.execute(statCursoMONth,[Statecrdition,idU])
                        else:
                               statCurso = "UPDATE station_pablic SET ACcrditionStatediesel=? WHERE idusers = ? "
                        # STATdata = ()
                               cursor.execute(statCurso,[Statecrdition,idU])
                               statCursoMONth = "UPDATE station_MonthD SET ACcrditionStatediesel=? WHERE idusers = ?  AND datatim BETWEEN strftime('%Y-%m-01',CURRENT_DATE )  AND CURRENT_DATE"
                               cursor.execute(statCursoMONth,[Statecrdition,idU])
                            
                        connnection.commit()
                        messagebox.showinfo(title="ok",message="تم  توقيف الاعتماد بنجاح" if Statecrdition == 'موقف' else 'تم اعادة الاعتماد بنجاح')
                        return True
                except sqlite3.IntegrityError:
                        print('there error ')
                connnection.close()
#  لجمع بيانات الشهرية للحساب وحذفة 
        def DeletAcontfetchArryJson(idusers,VIREBLISWITCH):
            conn =  sqlite3.connect(nameData())
            try:
                cursor = conn.cursor()
                print(VIREBLISWITCH)

                if VIREBLISWITCH["name1"] == 'DeletAll':
                    cursor.execute('UPDATE station_pablic SET Arraypash = ( SELECT  Arraypash  FROM (station_MonthD)  WHERE idusers=? ) , ACcrditionStateOIL="محذوف",ACcrditionStatediesel="محذوف"  WHERE idusers=? ',[idusers,idusers])
                    cursor.execute("UPDATE station_MonthD SET ACcrditionStateOIL='محذوف', ACcrditionStatediesel='محذوف' WHERE idusers=?",[idusers]) 
                    messagebox.showwarning(title='Error', message='تم حذف الاعتماد بنجاح')
                else:
                    cursor.execute("UPDATE station_pablic SET ACcrditionStateOIL=?, ACcrditionStatediesel=? WHERE idusers=?",[VIREBLISWITCH['name1'],VIREBLISWITCH['name2'],idusers])
                    cursor.execute("UPDATE station_MonthD  SET ACcrditionStateOIL=?, ACcrditionStatediesel=? WHERE idusers=?",[VIREBLISWITCH['name1'],VIREBLISWITCH['name2'],idusers]) 
                    messagebox.showwarning(title='Error', message='تم استرداد الاعتماد بنجاح')
                conn.commit()
                return True
            except sqlite3.IntegrityError:
                print('Error',sqlite3.IntegrityError)
            
                # وظيفة نسخ بيانات الاعتمادات إلى مدخلات الشهر 
        def Fausth_stationPablic():
                # print(Frequntlye)
                    value = next((item for item in  Ferquntlye if item['DoneSub'] == "false" and datetime.strptime(item['datatim'],"%Y-%m-%d").month < datetime.now().month ),None)
                    conn =  sqlite3.connect(nameData())
                    cursor = conn.cursor()
                    try:
                        if value is not None:
                            statmentmonth = 'UPDATE station_MonthD SET aciton="previous" WHERE DoneSub= "false"'
                            cursor.execute(statmentmonth)
                        cursor.execute("INSERT INTO station_MonthD (idusers,nameusefly,quantityOIL,quantitydiesel,thermenOIL,thermendiesel,DoneSub,ACcrditionStateOIL,ACcrditionStatediesel,aciton) SELECT idusers,nameusefly,quantityOIL,quantitydiesel,quantityOIL,quantitydiesel,DoneSub,ACcrditionStatediesel,ACcrditionStatediesel,aciton FROM station_pablic WHERE  ACcrditionStateOIL != 'محذوف' OR ACcrditionStatediesel != 'محذوف'")
                        conn.commit()                   
                    except sqlite3.IntegrityError:
                        print('error accnt')
                    conn.close()
#  لعملية الصرف   
        def insert_SqlytMot(objectINsert,VIREBLISWITCH):
            connection =  sqlite3.connect(nameData())
            try:
                with connection: 
                    cursor = connection.cursor()
                    # print(objectINsert)       
                    statmentall = 'UPDATE station SET amountٍٍSpent=?, thermen=?,DoneF=?,expiryDate=?  WHERE ID=? AND aciton=? AND classifyProcess =? '
                    statmentallSUb = (objectINsert['amountnAll'],objectINsert['thermAA'],objectINsert['DoneF'],objectINsert['expiryDate'],objectINsert['ID'],objectINsert["acitonStat"],objectINsert['classifyprocess'])
                    cursor.execute(statmentall,statmentallSUb)
                    # print(objectINsert['ID'])
                    arrayJson = json_stringify(objectINsert['Arraypash'])
                    # print(arrayJson)
                    if VIREBLISWITCH == 'OIL':
                        statmentmonth = 'UPDATE station_MonthD SET idHom=?, amountٍٍSpentOIL=?, thermenOIL=?,DoneSub=?,Arraypash =? WHERE idusers=? AND datatim =? AND aciton=?'
                        statmentmonthSUb = (objectINsert['idhom'],objectINsert['amountn'],objectINsert['therm'],objectINsert['DoneSub'],arrayJson,objectINsert['Idcoder'],objectINsert['datatim'],objectINsert["acitonMon"])
                        cursor.execute(statmentmonth,statmentmonthSUb)
                    else:
                        statmentmonth = 'UPDATE station_MonthD SET idHom=?, amountٍٍSpentdiesel=?, thermendiesel=?,DoneSub=?,Arraypash =? WHERE idusers=? AND datatim =? AND aciton=?'
                        statmentmonthSUb = (objectINsert['idhom'],objectINsert['amountn'],objectINsert['therm'],objectINsert['DoneSub'],arrayJson,objectINsert['Idcoder'],objectINsert['datatim'],objectINsert["acitonMon"])
                        cursor.execute(statmentmonth,statmentmonthSUb)
                    connection.commit()
            except sqlite3.IntegrityError:
                print("couldn't add Python twice")
            connection.close()

        def UpdateSinders(quantity,VIREBLISWITCH):
                connnection =  sqlite3.connect(nameData())
                try:
                    with connnection:
                        cursor = connnection.cursor()
                        Oil = "جاري" if int(quantity) > 0 else 'none'
                        diesel = 'جاري' if  int(VIREBLISWITCH) > 0 else 'none' 
                        # print(Oil,diesel)
                        statCursor = "UPDATE station_MonthD SET quantityOIL =? ,quantitydiesel=?, ACcrditionStatediesel=?, ACcrditionStateOIL=? WHERE nameusefly = 'نثريات'  AND datatim  BETWEEN strftime('%Y-%m-01', CURRENT_DATE ) AND CURRENT_DATE "
                        cursor.execute(statCursor,[quantity,VIREBLISWITCH,diesel,Oil])
                        statCurso = f"UPDATE station_pablic SET quantityOIL =? ,quantitydiesel=?, ACcrditionStatediesel=?, ACcrditionStateOIL=?  WHERE nameusefly = 'نثريات' "
                        cursor.execute(statCurso,[quantity,VIREBLISWITCH,diesel,Oil])
                        connnection.commit()
                        messagebox.showinfo(title="ok",message="تم تعديل نثريات الشهر بنجاح")
                except sqlite3.IntegrityError:
                        print('there error ')
                connnection.close()                       

# جلب البيانات الشهرية لصرف الاعتمادات
        def inComin_Data():
                   global Ferquntlye
                   connection =  sqlite3.connect(nameData())
                   try:
                       cursor = connection.cursor()
                       with connection:
                            # cursor.execute("SELECT * FROM station_MonthD WHERE datatim BETWEEN strftime('%Y-%m-01',CURRENT_DATE )  AND CURRENT_DATE ")
                            cursor.execute("SELECT * FROM station_MonthD ")
                            # Get the data
                            data = cursor.fetchall()
                            Ferquntlye= []
                            # template = '\n'.join('{0:20} {1}'.format(column_name, value) for column_name, value in zip(column_names, data))
                            # with open('template.txt', 'w') as f:
                            #      f.write(template)
                            # print(data)
                            for i in range(len(data)):
                                        obje = {}
                                        obje['ID']= data[i][0] 
                                        obje['idusers']= data[i][2]
                                        obje['nameusefly']= data[i][3]
                                        obje['quantityOIL']=  data[i][4]
                                        obje['quantitydiesel']=  data[i][5]
                                        obje['amountٍٍSpentOIL']= data[i][6]
                                        obje['thermenOIL']= data[i][7]
                                        obje['amountٍٍSpentdiesel']= data[i][8]
                                        obje['thermendiesel']= data[i][9]
                                        obje['DoneSub']= data[i][10]
                                        obje['ACcrditionStatediesel'] =  data[i][11]
                                        obje['ACcrditionStateOIL']=  data[i][12]
                                        obje['datatim']= data[i][13]
                                        obje['aciton']= data[i][14]
                                        dataArray = data[i][15]
                                        if dataArray is not None and  len(dataArray) > 0:
                                            obje['Arraypash']= json_parse(dataArray) 
                                        else:
                                            obje['Arraypash']= []
                                        Ferquntlye.append(obje) 
                            # return list(Ferquntlye)
                            return Ferquntlye
                   except sqlite3.IntegrityError:
                        print("couldn't add Python twice")
                   connection.close()  
# جلب البيانات  الرئيسية لمستفيدين من الصرف  للعرض     
        def inComin_Pablic():
                    connection =  sqlite3.connect(nameData())
                    try:
                        cursor = connection.cursor()
                        # cursor.execute("SELECT * FROM ferquntlye ")
                        with connection:
                            cursor.execute(" SELECT idusers,nameusefly,quantityOIL,quantitydiesel,oprtionPush,datatim,ACcrditionStatediesel,ACcrditionStateOIL FROM station_pablic ")
                           
                            # Get the data
                            data = cursor.fetchall()
                            Ferquntlye= []
                            if data is not None:
                                return list(data)
                    except sqlite3.IntegrityError:
                        print("couldn't add Python twice")
                        # conn.commit() 
                    connection.close()
#جلب البيانات الرئيسية للمستفيدين من الصرف بيانات الاعتمادات  
        def inCominSwitch_Pablic():
                    connection =  sqlite3.connect(nameData())
                    try:
                        cursor = connection.cursor()
                        # cursor.execute("SELECT * FROM ferquntlye ")
                        with connection:
                            cursor.execute(" SELECT * FROM station_pablic WHERE ACcrditionStatediesel != 'محذوف' OR ACcrditionStateOIL != 'محذوف'")
                            # Get the data
                            data = cursor.fetchall()
                            Ferquntlye= []
                            for i in range(len(data)):
                                obje = {"idusers":data[i][0],"nameusefly":data[i][1], "quantityOIL":data[i][2],"quantitydiesel": data[i][3],"DoneSub":data[i][4],"oprtionPush":data[i][5]}
                                Ferquntlye.append(obje)
                            return list(Ferquntlye)
                    except sqlite3.IntegrityError:
                        print("couldn't add Python twice")
                        # conn.commit() 
                    connection.close()
# جلب البيانات الرئيسية للحمولات
        def inComin_dataAll():
                    global station
                    connection =  sqlite3.connect(nameData())
                    try: 
                        cursor = connection.cursor()
                        with connection:
                            cursor.execute("SELECT * FROM station")
                            # Get the data
                            data = cursor.fetchall()
                            # print(data)
                            station= []
                            for i in range(len(data)):
                                        obje = {}
                                        obje['ID']= data[i][0] 
                                        obje['incomingquantity']=  data[i][1]
                                        obje['receivedData']=  data[i][2]
                                        obje['amountٍٍSpent']=  data[i][3]
                                        obje['thermen']=  data[i][4]
                                        obje['DoneF']= data[i][5]
                                        obje['expiryDate']=  data[i][6]
                                        obje['aciton']=  data[i][7]
                                        obje['classifyProcess']=  data[i][8]
                                        dataarrays = data[i][9]
                                        if dataarrays is not None and len(dataarrays) > 0:
                                            obje['Arrayjson']=  json_parse(dataarrays)
                                        else:
                                            obje['Arrayjson']= []
                                        station.append(obje)  
                        return list(station)
                    except sqlite3.IntegrityError:
                        print("couldn't add Python twice")
                        # conn.commit() 
                    connection.close()
        def inComin_dataAllwitch():
                conn =  sqlite3.connect(nameData())
                try:
                    cursor = conn.cursor()
                    with conn:
                            cursor.execute( "SELECT ID,incomingquantity,receivedData,amountٍٍSpent,thermen,DoneF,classifyProcess,Arrayjson FROM station ")
                            data = cursor.fetchall()
                            return list(data)
                except sqlite3.IntegrityError:
                        print("dont's have data ")
                conn.close()
                            
                
                    
        