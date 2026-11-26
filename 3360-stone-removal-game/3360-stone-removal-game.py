class Solution:
    def canAliceWin(self, n: int) -> bool:
        result=0
        k=10
        while n>=k:
            n=n-k
            k-=1
            result+=1
        return result%2==1