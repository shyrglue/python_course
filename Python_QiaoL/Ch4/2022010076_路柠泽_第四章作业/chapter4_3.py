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

def printcalendar(file,y=2024):
    with open(file,'w') as f:                               #open the file to write in
        f.write('{:^21}'.format(y)+'\n\n')                  #the year title
        month=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
        for m in range(1,13):
            f.write('{:^21}'.format(month[m-1])+'\n')       #the month titles
            for w in ['S','M','T','W','T','F','S']:
                f.write('{:^3}'.format(w))                  #the week
            day1=sum(num_of_days(y,m) for m in range(1,m))+day1_in_year(y)
                #determine what the 1st day of a month is
            f.write('\n'+"   "*(day1%7))            #blank space at the beginning
            for d in range(1,num_of_days(y,m)+1):   #output days and change line every week
                f.write('{:^3}'.format(d))
                if (d+day1)%7==0 and d<num_of_days(y,m):
                    f.write('\n')
            f.write('\n\n')
printcalendar('output.txt')