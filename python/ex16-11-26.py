#LeetCode: Remove Element
#Dificuldade: Fácil
#Objetivo: Remover o elemento da lista que tiver um certo valor
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for index in range(len(nums) - 1, -1, -1):
            if nums[index] == val:
                nums.pop(index)