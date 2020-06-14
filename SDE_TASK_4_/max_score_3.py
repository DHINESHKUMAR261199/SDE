from math import gcd as g
n=int(input())
A=sorted(list(map(int,input().split())))
B=sorted(list(map(int,input().split())))
edges=0
for i in A:
    for j in B:
        if i<j and g(i,j)>1:
            edges+=1
print(edges)
            
