from math import sqrt as s
n,k=map(int,input().split())
l=[]
while n%2 == 0:
    l.append(2)
    n//=2
for i in range(3,int(s(n))+1,2):
    while n%i == 0:
        l.append(i)
        n//=i
if n>2:
    l.append(n)
if k<=len(l):
    print(l[k-1])
else:
    print(-1)
