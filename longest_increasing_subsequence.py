def longest_increasing_subsequence(n,l):
    LS=[1]*n
    for i in range(1,n):
        for j in range(i):
            if l[i]>l[j] and LS[i]<LS[j]+1:
                LS[i]=LS[j]+1
    return max(LS)
n=int(input())
l=list(map(int,input().split()))
print(longest_increasing_subsequence(n,l))
