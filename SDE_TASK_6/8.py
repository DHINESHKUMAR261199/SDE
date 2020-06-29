t=int(input())
for _ in range(t):
    a=input().upper()
    b=input().upper()
s=""
for i in a:
    if i not in b:
        s+=i
print(s)
