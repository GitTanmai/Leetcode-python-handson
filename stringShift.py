class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for i,c in enumerate(shift):
            for j in range(c[1]):
                if c[0] ==1:
                    s=s[len(s)-1]+ s[:-1]
                if c[0]==0:
                    s=s[1:]+s[0]
        return s