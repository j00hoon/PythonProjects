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
        t_list = []

        for index in range(0, len(digits)):
            if digits[index] in number_dict:
                tmp_list.append(number_dict[digits[index]])
                print(number_dict[digits[index]])




        # t_list = [ for word in tmp_list]

        # tmp_list = list(itertools.product(*tmp_list))

        for i in tmp_list:
            res_list.append("".join(map(str, i)))

        return res_list

sol = Solution()
string = "23"

print(sol.letterCombinations(string))