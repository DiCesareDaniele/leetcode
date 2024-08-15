'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number
'''

class Solution:
    # pylint: disable-next=invalid-name
    def letterCombinations(self, digits: str) -> list[str]:
        if digits == "":
            return []
        digit_to_letters = [
            "",
            "",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz",
        ]
        sol = []
        def letter_combinations_helper(i: int, acc: str):
            if i == len(digits):
                sol.append(acc[:])
                return
            for c in digit_to_letters[int(digits[i])]:
                letter_combinations_helper(i + 1, acc + c)
        letter_combinations_helper(0, "")
        return sol
