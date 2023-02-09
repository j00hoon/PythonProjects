class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0 or len(s) == 1 or (s == s[::-1]):
            return s

        # reverseString = s[::-1]
        tmpString = palindromeString = ""

        for start_index in range(0, len(s)):
            for end_index in range(start_index + 1, len(s) + 1):
                tmpString = s[start_index:end_index]
                if tmpString == tmpString[::-1]:
                    if len(palindromeString) < len(tmpString):
                        palindromeString = tmpString

        return palindromeString





# aacabdkacaa
# aacdefcaa
# babad
# cffe
# abbcccbbbcaaccbababcbcabca
# abb

sol = Solution()
print(sol.longestPalindrome("abbc"))


# https://ckd2806.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%ED%8C%B0%EB%A6%B0%EB%93%9C%EB%A1%AC


# sstr = "cffe"
# print(sstr[len(sstr):len(sstr)])
