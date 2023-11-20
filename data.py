
from convertcod.internal_storage import get_itemx
from convertcod.internal_Loginstorge import get_loginAll
from datetime import datetime
import re
sales_data = {
    "Product A": 100,
    "Product B": 200,
    "Product C": 600,
    "Product D": 400,
    "Product E": 500,   
}


try:
    arraymovem = get_itemx() 
    userorgin = get_loginAll() 

    i = 0
    userObject ={}
    user = []
    usernam = []
    month =[]
    datas={}
    datasMonth={}
    dataday ={}
    na = 'عبدالرحمن الفيل'
    # na.lower()
    for name in userorgin:
            userObject[name[1]] = [count for count in arraymovem if name[1] == count['userName']]
            user.append(userObject)
            for us in user:
                datas[f"{name[1]}"] = len([item for item in us[name[1]] if int(re.findall('\d+',item["datamovement"])[1]) == datetime.now().month ])
                for item in us[name[1]]:
                    # print(item['datamovement'])
                    try:
                        dataname = datetime.strptime(item["datamovement"],'%Y-%m-%d %H:%M:%S.%f')
                        name_month = dataname.strftime('%B') 
                        name_day = dataname.strftime('%A') 
                        # print(dataname)
                        datasMonth[f"{name_month}"] = len([i for i in us[name[1]] if  int(re.findall('\d+',i['datamovement'])[2]) ==  dataname.month])
                        dataday[f"{name_day}"] = len([i for i in us[name[1]] if  int(re.findall('\d+',i['datamovement'])[2]) ==  dataname.day])
                        # month.append(datasMonth)
                    except ValueError as e:
                        print(e)
                # print(datasMonth)
except:
    pass

inventory_data = datas
product_data = datas
sales_year_data = {
    2018: 5000,
    2019: 17500,
    2020: 10000,
    2021: 7500,
    2022: 15000
}
inventory_day_data = {}
for d in dataday.keys():
    # print(d) 
    for p in dataday.values():
        inventory_day_data = {
            'Saturday': p if d == 'Saturday' else 0,
            "Sunday":  p if d == 'Sunday' else 0,
            "Monday":  p if d == 'Monday' else 0,
            "Tuesday":  p if d == 'Tuesday' else 0,
            "Wednesday":  p if d == 'Wednesday' else 0,
            "Thursday":  p if d == 'Thursday' else 0,
            "Friday":  p if d == 'Friday' else 0,
        }
inventory_month_data = {}
for d in datasMonth.keys():
    # print(d) 
    for p in datasMonth.values():
        inventory_month_data = {
            'Jan': p if d == 'January' else 0,
            "Feb":  p if d == 'February' else 0,
            "March":  p if d == 'March' else 0,
            "April":  p if d == 'April' else 0,
            "May":  p if d == 'May' else 0,
            "June":  p if d == 'June' else 0,
            "July":  p if d == 'July' else 0,
            "Aug":  p if d == 'August' else 0,
            "Sep":  p if d == 'September' else 0,
            "Octo":  p if d == 'October' else 0,
            "Nove":  p if d == 'November' else 0,
            "Dece":  p if d == 'December' else 0,
        }
