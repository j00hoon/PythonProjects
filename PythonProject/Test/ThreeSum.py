from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        resList = []

        if len(nums) == 3 and sum(nums) == 0:
            resList.append(nums)
            return resList

        nums.sort()

        for x in range(0, len(nums) - 2):
            y = x + 1
            z = len(nums) - 1

            if x > 0 and nums[x] == nums[x - 1]:
                continue

            while y < z:
                if z < len(nums) - 1 and nums[z] == nums[z + 1]:
                    z -= 1
                    continue
                else:
                    if nums[x] + nums[y] + nums[z] == 0:
                        resList.append(nums[x], nums[y], nums[z])
                        y += 1
                        z -= 1
                    elif nums[x] + nums[y] + nums[z] > 0:
                        z -= 1
                    elif nums[x] + nums[y] + nums[z] < 0:
                        y += 1
                if nums[x] > 0 or nums[z] < 0:
                    break

        return resList


sol = Solution()

numsList = [0, 1, 1]

numsList = [1, 2, -2, -1]
numsList = [0, 0, 0]
numsList = [-1,0,1,2,-1,-4,-2,-3,3,0,4]

numsList = [34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]
numsList = [-1, 0, 1, 2, -1, -4]
numsList = []
#[[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]

print(sol.threeSum(numsList))

