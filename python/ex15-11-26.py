#LeetCode: Merge Sorted Array
#Dificuldade: Média
#Objetivo: Mesclar dois arrays de números em uma ordem não decrescente
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        solution = []
        for i in range(n):
            nums1[m+i] = nums2[i]

        nums1.sort()