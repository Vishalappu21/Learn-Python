from datetime import datetime,timedelta
Time_1 = datetime.now()
print(Time_1)

Time_Yesterday = Time_1 - timedelta(days =1)
Time_Tomorrow = Time_1+timedelta(days =1)
print(Time_Yesterday)
#print(Time_1)
print(Time_Tomorrow)