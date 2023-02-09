from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        maxVal = 0
        start = 0
        end = len(height) - 1
        while(start != end):
            if height[start] * (end - start) > maxVal and height[start] <= height[end]:
                maxVal = height[start] * (end - start)
            elif height[end] * (end - start) > maxVal and height[start] >= height[end]:
                maxVal = height[end] * (end - start)
            if height[start] >= height[end]:
                end -= 1
            else:
                start += 1

        return maxVal


sol = Solution()
heightList = [1, 1]
heightList = [1, 2]
heightList = [1,8,6,2,5,4,8,3,7]

print(sol.maxArea(heightList))