from itertools import combinations as com
n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=0
for i in range(1,len(l)+1):
    for j in list(com(l,i)):
        p=1
        for e in j:
            p*=e
        if p<k:
            c+=1
print(c)
