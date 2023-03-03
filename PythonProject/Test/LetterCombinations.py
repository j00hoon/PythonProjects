import itertools
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        res_list = []
        tmp_list = []
        # t_list = []

        for index in range(0, len(digits)):
            if digits[index] in number_dict:
                tmp_list.append(number_dict[digits[index]])

        # for words in tmp_list:
        #     t_list += words

        ### Compute all cartesian values from tmp_list
        tmp_list = list(itertools.product(*tmp_list))
        # print(tmp_list)

        for i in tmp_list:
            ### i is tuple, so need to make as string
            ### use "".join() to make a tuple as a string
            res_list.append("".join(i))

        return res_list


sol = Solution()
string = "23"

print(sol.letterCombinations(string))