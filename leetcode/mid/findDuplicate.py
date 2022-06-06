class Solution:
    def findDuplicate(self, nums: []) -> int:    
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] == nums[j]):
                    return nums[i]
                
                

arr = [-1, 5, 8, 5, 16]
a = Solution()
print(a.findDuplicate(arr))  