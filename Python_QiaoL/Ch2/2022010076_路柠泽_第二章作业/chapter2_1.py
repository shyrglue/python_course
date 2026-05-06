for a in range(100,1000):   #from number 100 to 999
    x=int(a/100)
    y=int(a%100/10)
    z=a%10
    #extract the hundreds, the tens and the units
    if(x**3+y**3+z**3==a):
        print(a)
    #detect narcissistic numbers and output