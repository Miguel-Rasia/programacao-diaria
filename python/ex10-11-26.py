# LeetCode Two Sums Exercise
# Abordagem: fazer um algoritmo de força bruta para analisar todas as possibilidades. Como o j só
# percorre de i + 1 até len(nums), é impossível acontecer o caso de somar um número com ele mesmo e obter
# o resultado correto
# Complexidade de tempo: O(n^2)
# Complexidade de espaço: O(n)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]