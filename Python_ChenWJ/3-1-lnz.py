# 递归计算斐波那契数列的某一项
f={}
def fib(n):
    # TODO: 完成递归定义
    if n in f:
        return f[n]
    if n<3:
        return 1
    else:
        f[n]=fib(n-1)+fib(n-2)
        return f[n]
    pass

# 递归计算两个数的最大公因数
def gcd(a, b):
    # TODO: 完成递归定义
    if b==0:
        return a
    return gcd(b,a%b)
    pass

if __name__ == "__main__":
    a, b = map(int, input().split())
    # TODO: 计算结果并输出
    print(fib(gcd(a,b)))
