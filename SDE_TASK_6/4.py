r,c=map(int,input().split())
l=[]
for i in range(r):
    st=""
    s=str(list(map(int,input().split())))
    for i in s:
        if i=="0" or i=="1":
            st+=i
    l.append(st)
v=set(l)
for i in l:
    if i in v:
        print(" ".join(i))
        v.remove(i)


