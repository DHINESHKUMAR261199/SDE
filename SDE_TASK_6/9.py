t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    d,l1=map(str,input().split())
    if l1=="E":
        l2="H"
    else:
        l2="E"
    s=""
    for i in range(n):
        if i%2==0:
            s+=l1
        else:
            s+=l2
    if d=="L":
        print(x,s[x-1])
    else:
        print(n-x+1,s[-1*x])
        
    
    
