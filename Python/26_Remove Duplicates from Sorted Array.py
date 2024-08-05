class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        dict_first_ocurrence_nums = {}
        for i, num in enumerate(nums):
            if num not in dict_first_ocurrence_nums:
                dict_first_ocurrence_nums[num] = i
        print(dict_first_ocurrence_nums.items())
        for j, [num, pos] in enumerate(dict_first_ocurrence_nums.items()):
            print(j, num, pos)
            print(nums[pos], nums[j])
            nums[pos] = nums[j]
            nums[j] = num
        return len(dict_first_ocurrence_nums)
