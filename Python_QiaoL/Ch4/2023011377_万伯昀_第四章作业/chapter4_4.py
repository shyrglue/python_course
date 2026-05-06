from datetime import datetime, timedelta  
  
def print_month_calendar(year, month):  
    """  
    Print the calendar for a given year and month.  
    """  
    # 每月第一天  
    first_day = datetime(year, month, 1)  
    # 第一天是周几 (0=Monday, 6=Sunday)  
    first_weekday = first_day.weekday()  
    # 调整一下，使得周日在前  
    first_weekday = (first_weekday + 1) % 7  
  
    #算出每个月的天数 
    if month in [4, 6, 9, 11]:  
        days_in_month = 30  
    elif month == 2:  
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  
            days_in_month = 29  
        else:  
            days_in_month = 28  
    else:  
        days_in_month = 31  
  
    # 打印表头  
    monlist[month-1].append(f"{'Sun Mon Tue Wed Thu Fri Sat '.center(15)}")
    monlist[month-1].append(f"{'-' * 27} ")  
  
    # 打空格对齐第一行  
    monlist[month-1].append(f"{' ' * (4 * first_weekday)}")
  
    # 打印每一天 
    day = 1  
    for _ in range(days_in_month):  
        weekday_index = (day + first_weekday - 1) % 7  
        #这个式子计算几号是星期几 
        monlist[month-1][-1]=monlist[month-1][-1]+f"{day:2d}  "
        if weekday_index == 6: 
                #如果是周六就要换行
                monlist[month-1].append("") 
        day += 1  
    monlist[month-1][-1]=monlist[month-1][-1]+" "*((6-weekday_index)*4)
    # 一个月的最后一天不是周六也要换行  
    if (len(monlist[month-1])!=8):  
        monlist[month-1].append(" "*28)  
  
# 打印2024年的日历 
monlist=[[],[],[],[],[],[],[],[],[],[],[],[]]
for month in range(1, 13):  
    #print(f"\n{2024} {month} Calendar:")  
    print_month_calendar(2024, month)
#for _ in monlist:
   # for j in _:
       # print(j)

#用zip来转置一下
list1 = list(zip(monlist[0],monlist[1],monlist[2]))
for _ in list1:
    for j in _:
        print(j,end="  ")
    print()
 
list2 = list(zip(monlist[3],monlist[4],monlist[5]))
for _ in list2:
    for j in _:
        print(j,end="  ")
    print()
    
list3 = list(zip(monlist[6],monlist[7],monlist[8]))
for _ in list3:
    for j in _:
        print(j,end="  ")
    print()
    
list4 = list(zip(monlist[9],monlist[10],monlist[11]))
for _ in list4:
    for j in _:
        print(j,end="  ")
    print()