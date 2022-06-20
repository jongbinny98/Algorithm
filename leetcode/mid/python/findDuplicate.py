# not efficient
# class Solution:
#     def findDuplicate(self, nums: []) -> int:    
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if (nums[i] == nums[j]):
#                     return nums[i]
                
import numpy as np
class Solution:
    def findDuplicate(self, nums: []) -> int:    
        count = np.zeros(len(nums)+ 1)
        
        for num in nums:
            count[num] += 1
            print(count[num])
            if count[num] > 1:
                return num
                

arr = [-1, 5, 8, 5, 16]
a = Solution()
print(a.findDuplicate(arr))  