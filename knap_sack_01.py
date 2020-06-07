def Knap_Sack_01(n,weight,value,capasity):
    KS=[[0 for i in range(capasity+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(capasity+1):
            if i==0 or j==0:
                KS[i][j]=0
            elif weight[i-1]<=j: 
                KS[i][j]=max(value[i-1]+KS[i-1][j-weight[i-1]],KS[i-1][j])
            else:
                KS[i][j] = KS[i-1][j]
    return KS[n][capasity] 
n=int(input("Enter No of Items : "))
weight,value=[],[]
print("Weight :   Value : ")
for i in range(n):
    w,v=map(int,input().split())
    weight.append(w)
    value.append(v)
capasity=int(input("Enter Capasity : "))
print(Knap_Sack_01(n,weight,value,capasity)) 
