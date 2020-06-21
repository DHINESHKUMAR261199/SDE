from math import sqrt as s
from collections import Counter as c
n=int(input())
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
for i,j in dict(c(l)).items():
    print(i,j)
