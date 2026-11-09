# font: leetcode
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numbers = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        conversion = 0
        skip = False

        for i in range(len(s)):

            if skip:
                skip = False
                continue

            if i + 1 < len(s) and roman_numbers[s[i]] < roman_numbers[s[i+1]]:
                conversion += roman_numbers[s[i+1]] - roman_numbers[s[i]]
                skip = True
            else:
                conversion += roman_numbers[s[i]]
        
        return conversion