def Longest_Common_Subsequence(st1,st2,l1,l2): 
    LCS=[[0 for j in range(l2+1)] for i in range(l1+1)]
    for i in range(l1+1):
        for j in range(l2+1):
            if i==0 or j==0:
                LCS[i][j]=0
            elif st1[i-1]==st2[j-1]:
                LCS[i][j]=LCS[i-1][j-1]+1
            else:
                LCS[i][j]=max(LCS[i-1][j],LCS[i][j-1])
    return LCS[l1][l2]
st1,st2=map(str,input().split())
l1,l2=len(st1),len(st2)
print(Longest_Common_Subsequence(st1,st2,l1,l2))
