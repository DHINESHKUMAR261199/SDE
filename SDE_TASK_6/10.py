n,a=map(int,input().split())
while(a>0):
    if str(n)[-1]=="0":
        n=int(str(n)[:-1])
        a-=1
    else:
        n=n-1
        a-=1
    if n==0:
        break
print(n)
        
