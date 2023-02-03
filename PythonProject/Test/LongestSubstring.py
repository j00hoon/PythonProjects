class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        maxNum = 0
        tmpString = ""

        for letter in s:
            if letter not in tmpString:
                tmpString += letter
            else:
                tmpString = tmpString[tmpString.index(letter) + 1:] + letter

            if maxNum < len(tmpString):
                maxNum = len(tmpString)
        return maxNum


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))