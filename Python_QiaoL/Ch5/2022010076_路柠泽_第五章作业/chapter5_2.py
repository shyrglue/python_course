def calculate(s):
    stack=[]
    num=0
    op='+'
    flag=0  #distinguish between integer and decimal parts
    for i in range(len(s)):
        c=s[i]
        if c=='.':
            flag+=1
        if c.isdigit():
            if not flag:
                num=int(c)+10*num
            else:
                num=(10**(flag-1)*num*10+int(c))/10**flag
                flag+=1
        #read a number
        if(not c.isdigit() and c!=' ' and c!='.') or i==len(s)-1:
            if op=='+':
                stack.append(num)
            elif op=='-':
                stack.append(-num)
            elif op=='*':
                stack.append(stack.pop()*num)
            elif op=='/':
                stack.append(stack.pop()/num)
        #read an operater and use the stack to calculate and storage
            op=c
            num=0
            flag=0
    return sum(stack)
s=input("Please enter an expression: ")
print("The result is: ",calculate(s))