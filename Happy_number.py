class Solution:
    def isHappy(self, n: int) -> bool:
        seen=[]
        su=[]
        while n not in seen:
            seen.append(n)
            l=[int(i) for i in str(n)]
            su=[pow(i,2) for i in l]
            
            n=sum(su)
            
            if 1 in seen:
                return True
                break

        return False
        