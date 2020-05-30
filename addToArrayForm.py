class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        st=''
        for i in A:
            st=st + str(i)
        st=str(int(st) + K)
        return [int(i) for i in st]