class Solution:
    def reverse(self, x: int) -> int:
        #y=str(x)
        if '-' in str(x):
            x= int(str(x)[0]+str(x)[1:][::-1])
        else:
            x= int(str(x)[::-1])
        if -2147483648 < x < 2147483647:
            return x
        else:
            return 0