import random
def pi(n,t):
    for i in range(t):
        c=0                   #The number of points in circle
        for j in range(n):
            x=random.random()
            y=random.random() #Create a point
            if x*x+y*y<=1:    #Check if in circle
                c+=1
        print(4*c/n)          #Calculate pi and output
n=int(input("Input the number of random points: ")) #Test
t=int(input("Input the times of calculation: "))
pi(n,t)