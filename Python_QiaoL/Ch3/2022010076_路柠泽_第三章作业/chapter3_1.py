def sum(n):
    s=0
    while n>0:      #End when n is 0
        s+=n%10     #Extract the units digit
        n//=10      #Move forward
    return s
def rsum(n):
    while n>9:      #Repeat, end when n is single digit
        n=sum(n)
    return n
n=int(input("Input a natural number: "))    #Test
print(sum(n))
print(rsum(n))