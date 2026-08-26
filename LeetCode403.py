class Solution:
    def canCross(self, stones: List[int]) -> bool:
        s={}
        memo={}
        for i in range(len(stones)):
            s[stones[i]]=i
        def f(i,k):
            if i<0:
                return False
            if i==len(stones)-1:
                return True
            if (i,k) in memo:
                return memo[(i,k)]
            for j in (k-1,k,k+1):
                if j>0:
                    next=stones[i]+j
                    if next in s:
                        if f(s[next],j):
                            memo[(i,k)]=True
                            return True
            memo[(i,k)]=False
            return False
        return f(0,0)
