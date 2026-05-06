sum=0
i=0
while 1:        #infinite loop
    a=float(input())
    if a==0:
        break   #end when 0 input
    else:
        i+=1    #the number of numbers
        sum+=a  #the summary
print(sum/i)    #calculate the average