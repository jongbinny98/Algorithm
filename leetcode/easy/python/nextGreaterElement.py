class Solution:
    def nextGreaterElement(self, nums1, nums2):
        res_index = {num:index for index, num in enumerate(nums1)}
        # print(res_index)
        result = [-1] * len(nums1)

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if (nums1[i] == nums2[j]):
                    if(nums2[j] < nums2[j+1]):
                        index = res_index[nums1[i]]
                        result[index] = nums2[j + 1]
                        break
        return result 

nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
sol = Solution()
print(sol.nextGreaterElement(nums1, nums2))      
        