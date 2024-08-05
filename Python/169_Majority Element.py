class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_nums_count = {}
        for num in nums:
            if num not in dict_nums_count:
                dict_nums_count[num] = 1
            else:
                dict_nums_count[num] += 1
        return max(dict_nums_count, key=dict_nums_count.get)
