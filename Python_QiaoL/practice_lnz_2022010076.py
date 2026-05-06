#概率论与数理统计编程作业
#路柠泽 生31 2022010076
#由于本人python编程水平限制，仅能实现所要求的功能
#错误处理功能的设计及对代码和输出的美化有限，敬请谅解

def sample(n,r,ordered,replacement):
    def A(elements,r):
        if r==0:
            return [[]]
        if len(elements)==1:
            return [[elements[0]]]
        output=[]
        for i in range(len(elements)):
            used=elements[i]
            left=elements[:i]+elements[i+1:]
            for a in A(left,r-1):
                output.append([used]+a)
        return output
    #排列
    if ordered and (not replacement):
         e=[]
         for i in range(1,n+1):
             e+=[i]
         return A(e,r)
    space=[]
    def f(start,path):
        if len(path) == r:
            space.append(path)
            return
        #“可重复排列”
        if (ordered and replacement):
            for i in range(start,n+1):
                f(start,path+[i])
        #可重复组合
        elif replacement and (not ordered):
            for i in range(start,n+1):
                f(i,path+[i])
        #组合
        else:
            for i in range(start,n+1):
                f(i+1,path+[i])
    f(1,[])
    return space


a=int(input("请输入第一个正整数: "))
b=int(input("请输入第二个数（不大于前者）: "))
c=bool(int(input("是否有序(输入1或0): ")))
d=bool(int(input("是否可重复(输入1或0): ")))

space=sample(a,b,c,d)
print('所生成的样本空间为: ')
print('    ',end='')
print('    '.join(f'X{i+1}'for i in range(b)))
for i,combination in enumerate(space,start=1):
    print(f"{i}:  {' '.join(str(num).ljust(5)for num in combination)}")