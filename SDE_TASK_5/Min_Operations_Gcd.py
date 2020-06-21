n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(n):
    if l[i]!=1 and l[i]>k:
        c+=min(l[i]%k,k-l[i]%k)
    else:
        c+=k-l[i]
print(c)
