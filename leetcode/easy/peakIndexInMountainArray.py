class Solution:
    def peakIndexInMountainArray(self, arr: []) -> int:
        ans = arr.index(max(arr))
        return ans

arr = [-1, 5, 8, 9, 16]
a = Solution()
print(a.peakIndexInMountainArray(arr))  
        