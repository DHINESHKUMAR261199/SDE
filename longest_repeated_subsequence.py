def Longest_Repeated_Subsequence(n,string):
    LR=[[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if string[i-1]==string[j-1] and i!=j:
                LR[i][j]=1+LR[i-1][j-1]
            else:
                LR[i][j]=max(LR[i][j-1],LR[i-1][j])
    i,j,ans=n,n,""
    while i>0 and j>0:
        if LR[i][j]==LR[i-1][j-1]+1:
            ans+=string[i-1]
            i-=1
            j-=1 
        elif LR[i][j]==LR[i-1][j]:
            i-=1
        else:
            j-=1
    return "".join(ans[::-1])
n=int(input())
string=input()
print(Longest_Repeated_Subsequence(n,string)) 
