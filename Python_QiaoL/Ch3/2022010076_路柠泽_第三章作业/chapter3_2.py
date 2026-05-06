def sum(n):
    s=0
    while n>0:
        s+=n%10
        n//=10
    return s
def rsum(n):
    while n>9:
        n=sum(n)
    return n
def check():
    list=[0,0,0,0,0,0,0,0,0]
    for i in range(1,100000):
        list[rsum(i)-1]+=1
    #Statistical analysis of results
    for i in range(9):
        list[i]/=99999
        print(list[i])
    #Calculate proportion and output
check()