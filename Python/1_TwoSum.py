class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_vistos = {}

        for indice, num in enumerate(nums):
            restante = target - nums[indice]
            if restante in dict_vistos:
                return [indice, dict_vistos[restante]]
            else:
                dict_vistos[num] = indice