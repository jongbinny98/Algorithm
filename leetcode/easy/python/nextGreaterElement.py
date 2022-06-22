class Solution:
    def nextGreaterElement(self, nums1, nums2):

        num_idx = {n:i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in num_idx:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = num_idx[nums2[i]]
                    res[idx] = nums2[j]
                    break
        return res

nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
sol = Solution()
print(sol.nextGreaterElement(nums1, nums2))      
        