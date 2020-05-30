class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        calc=1
        lel=[1] * len(nums)
        for i in range(1, len(nums)):
            #print(nums[i])
            lel[i]= lel[i-1]*nums[i-1]

        for i in range(len(nums)-2,-1,-1):
            calc=calc*nums[i+1]
            lel[i]=lel[i]*calc
        return lel