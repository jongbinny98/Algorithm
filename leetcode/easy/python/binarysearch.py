class Solution:
    def search(self, nums: [], target: int) -> int:
        L = 0
        R = len(nums) - 1
         
        while(L <= R):
            m = (L + R) //2
            if nums[m] > target:
                R = m - 1
            elif nums[m] < target:
                L = m + 1
            else:
                return m
        return -1

nums = [-1, 5, 8, 9, 16]
target = 9
a = Solution()
print(a.search(nums, target))               