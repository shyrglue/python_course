def judge(s):
    right={'(':')','[':']','{':'}'}
    zhan=[]
    for i in s:
        if i in '([{':
            zhan.append(i)
        else:
            if len(zhan)==0 or right[zhan[-1]]!=i:
                return 0
            zhan.pop()
    return int(not zhan)

n=int(input())
for i in range(n):
    s=input().strip()
    print(judge(s))
