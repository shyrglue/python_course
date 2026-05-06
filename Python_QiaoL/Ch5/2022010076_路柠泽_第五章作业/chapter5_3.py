import random
def p24(nums):
    if len(nums)==1:
        return abs(nums[0]-24)<1e-6
        #(consider float accuracy)
    for i in range(len(nums)):
        a=nums[i]
        for j in range(1+i,len(nums)):
            b=nums[j]
            other=nums[:]
            other.remove(a)
            other.remove(b)
            #pick a random pair for the first step
        for c in [a+b,a-b,b-a,a*b]:
            if p24([c]+other):
                return True
            if b!=0 and p24([a/b]+other):
                return True
            if a!=0 and p24([b/a]+other):  
                return True
            #recursion with remaining numbers
    return False
nums=[random.randint(1,10)for n in range(4)]
#generate random numbers
print(nums)
if p24(nums):
    print("Can get 24")
else:
    print("Cannot get 24")