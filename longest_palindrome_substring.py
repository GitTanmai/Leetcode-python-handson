class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=[]
        if len(s)== 0:
            return ""
        for i in range(len(s)):
            for j in range(len(s),i,-1):
                if s[i:j:] == s[i:j:][::-1]:
                    l.append(s[i:j:])   
        return max(l, key=len)