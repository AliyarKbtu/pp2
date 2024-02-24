#task1
from datetime import date, timedelta
curdate = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',curdate)

#task2
from datetime import date, timedelta
today=date.today()
yesterday=date.today()-timedelta(1)
tomorrow=date.today()+timedelta(1)
print("Yesterday:",yesterday,"\n","Today:",today,"\n","Tomorrow:",tomorrow)

#task3
from datetime import datetime
time=datetime.today().replace(microsecond=0)
print(time)

#task4
from datetime import datetime
time1=datetime.strptime("2024-02-18 09:40:00", "%Y-%m-%d %H:%M:%S")
time2=datetime.now()
dif=time2-time1
print(int(dif.total_seconds()))

