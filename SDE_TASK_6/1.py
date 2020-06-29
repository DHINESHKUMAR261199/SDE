n,l=int(input()),[]
for i in range(n):
    x,y=map(int,input().split())
    t=[]
    t.extend([x,y,i+1])
    l.append(t)
d=sorted(l,key=lambda x:(x[1],-x[0],-x[2]))
for i in d:
    print(i[2],end=" ")
