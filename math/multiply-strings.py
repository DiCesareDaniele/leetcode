'''
https://leetcode.com/problems/multiply-strings
'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        def str_to_int(num: str) -> int:
            res = 0
            for c in num:
                n = ord(c) - ord("0")
                res = res * 10 + n
            return res
        def int_to_str(num: int) -> str:
            num_str = ""
            while num > 0:
                n = num % 10
                c = chr(ord("0") + n)
                num_str = c + num_str
                num //= 10
            return num_str
        return int_to_str(str_to_int(num1) * str_to_int(num2))
