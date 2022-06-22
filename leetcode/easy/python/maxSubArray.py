class Solution:
    def maxSubArray(self, nums) -> int:
        maxSum = nums[0]
        prev = maxSum
        
        for i in range(1, len(nums)):
            res = max(nums[i] + prev, nums[i])
            maxSum = max(res, maxSum)
            prev = res
            
        return maxSum



nums = [1, -1, 3, 4, -5, 2]
sol = Solution()
print(sol.maxSubArray(nums))
        