n=int(input())
a=list(map(int,input().split()))
m,c=a[0],a[0]
for i in range(1,n):
    c=max(a[i],c+a[i]) 
    m=max(m,c) 
print(m) 
