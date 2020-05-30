class Solution:
    def arrangeCoins(self, n: int) -> int:
        cc=n
        for i in range(1,n//2+2):
            if cc > i:
                cc=cc-i
            elif cc==i:
                return i
            else:
                return (i-1)