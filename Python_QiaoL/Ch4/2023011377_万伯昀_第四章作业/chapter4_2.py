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
    print(f"{'Sun Mon Tue Wed Thu Fri Sat'.center(15)}")  
    print(f"{'-' * 27}")  
  
    # 打空格对齐第一行  
    print(' ' * (4 * first_weekday),end='')
  
    # 打印每一天 
    day = 1  
    for _ in range(days_in_month):  
        weekday_index = (day + first_weekday - 1) % 7  
        #这个式子计算几号是星期几 
        print(f"{day:2d} ", end=' ')  
        if weekday_index == 6: 
                #如果是周六就要换行
                print()  
        day += 1  
  
    # 一个月的最后一天不是周六也要换行  
    if (day + first_weekday - 2) % 7 != 6:  
        print()  
  
# 打印2024年的日历 
monlist=[[],[],[],[],[],[],[],[],[],[],[],[]]
for month in range(1, 13):  
    print(f"\n{2024} {month} Calendar:")  
    print_month_calendar(2024, month)