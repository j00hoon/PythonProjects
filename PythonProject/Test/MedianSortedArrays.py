from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()

        median = len(nums3) % 2
        index = int(len(nums3) / 2)

        if median != 0:
            return float(nums3[index])
        else:
            return float((nums3[index - 1] + nums3[index]) / 2)


sol = Solution()
nums1 = [1,2]
nums2 = [3,4]
print(sol.findMedianSortedArrays(nums1, nums2))