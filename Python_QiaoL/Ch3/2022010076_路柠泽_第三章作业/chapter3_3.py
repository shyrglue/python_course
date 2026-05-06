def comb(n,k):
    if k==0 or k==n:    #Special cases
        return 1
    else:
        return comb(n-1,k-1)+comb(n-1,k)
        #Recursive through identity
n=int(input())  #Test
k=int(input())
print(comb(n,k))