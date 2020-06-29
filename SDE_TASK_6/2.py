from collections import Counter as c
n,k=map(int,input().split())
a=list(map(int,input().split()))
c=c(a)
for i in c.most_common(k):
    print(i[0],end=" ")
