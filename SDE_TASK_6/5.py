n=int(input())
s=input()
l=[]
for i in range(n):
    for j in range(i+1,n+1):
        t=s[i:j]
        if t==t[::-1]:
            l.append(t)
ans=max(l,key=len)
print(len(ans))
print(ans)
