#移动元素函数
def res(p,s):
    while s>1:
        p.append(p.pop(0))
        s=s-1
    p.pop(0)
    return p
#运行函数
def cl(n,m,s):
    list1=[i for i in range(1,n+1) ]
    while len(list1)>s:
        res(list1,m)
    return list1
#一般执行
n=int(input("总人数："))
m=int(input("淘汰位："))
s=int(input("留下人数："))
print(cl(n,m,s))