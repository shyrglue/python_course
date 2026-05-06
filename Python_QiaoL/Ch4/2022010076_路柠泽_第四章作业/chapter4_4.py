def is_leapyear(y):     #tell if is leapyear
    return (y%4==0 and y%100!=0)or(y%100==0)

def num_of_days(y,m):   #determine number of days in each month
    if m in [1,3,5,7,8,10,12]:
        return 31
    elif m==2:
        return 29 if is_leapyear(y) else 28
    else:
        return 30
    
def day1_in_year(y):    #determine what the 1st day of a yaer is using Zeller's formula
    return ((y%100-1)+((y%100-1)//4)+((y-1)//100//4)-(2*((y-1)//100))+(26*14//10))%7

def printcalendar(y=2024):
    print('{:^71}'.format(y)+'\n')              #the year title
    month=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    for s in range(1,5):                        #in each season...
        for m in month[3*(s-1):3*s]:            #the month title*3
            print('{:^21}'.format(m),end='    ')
        print()
        for w in ['S','M','T','W','T','F','S','    ']*3:
            print('{:^3}'.format(w),end='')     #the week*3
        print()
        day1=[0,0,0]
        for m in range(3*(s-1)+1,3*s+1):
            day1[(m-1)%3]=sum(num_of_days(y,m) for m in range(1,m))+day1_in_year(y)
                #determine what the 1st day of a month is
        start=[1,1,1]                                                       #the starting day of each line
        flag=1
        while flag:                                                     #WEEK
            for m in range(3*(s-1)+1,3*s+1):                                #MONTH
                if start[(m-1)%3]==1:
                    print("   "*(day1[(m-1)%3]%7),end="")                   #blank space at the first line
                for d in range(start[(m-1)%3],num_of_days(y,m)+1):              #DATE
                    if start[(m-1)%3]==0:                                           #blank line
                        print("   "*7,end='    ')
                        break
                    print('{:^3}'.format(d),end='')                                 #output days
                    if (d+day1[(m-1)%3])%7==0:                                          #end of a line
                        print('    ',end='')
                        if d<num_of_days(y,m):
                            start[(m-1)%3]=d+1
                        else:
                            start[(m-1)%3]=0
                        break
                    if d==num_of_days(y,m):
                        print("   "*(7-(day1[(m-1)%3]+num_of_days(y,m))%7),end="    ")  #end of a month
                        start[(m-1)%3]=0
                        break
            if start==[0,0,0]:
                flag=0                                                                  #end of a season
            print()
        print()
printcalendar()