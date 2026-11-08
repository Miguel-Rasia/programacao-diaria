#font: leetcode

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        greatest = 0
        for candy in candies:
            if candy >= greatest:
                greatest = candy
        
        result = []
        for candy in candies:
            if candy + extraCandies >= greatest:
                result.append(True)
            else:
                result.append(False)

        return result