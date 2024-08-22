class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        ans=[]
        for number in nums:
            if number!=0:
                ans.append(number)
        for number in nums:
            if number==0:
                ans.append(number)
        
        return ans
        