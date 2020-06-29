n,p1,p2,d,m=int(input()),[],[],[],0
for i in range(n):
    x,y=map(int,input().split())
    p1.append(x)
    p2.append(y)
for i in range(n):
    a,b=sum(p1[:i+1]),sum(p2[:i+1])
    if a-b>0:
        if a-b>m:
            m=a-b
            w=1
    else:
        if a-b>m:
            m=a-b
            w=2        
print(w,m)

