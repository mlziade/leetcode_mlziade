#Brute Force insert in 0 and pop last
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums_size = len(nums)
        for _ in range(k):
            nums.insert(0, nums[-1])
            nums.pop(nums_size)

#Concat array with last item and subarray [0:nums_size - 1]
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums_size = len(nums)
        for _ in range(k):
            nums = [nums[-1]] + nums[0:nums_size - 1]
        print(nums)

#Brute Force but reverts it if (nums_size/2 < k < nums_size)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums_size = len(nums)
        if k < nums_size/2 or k > nums_size:
            for _ in range(k):
                nums.insert(0, nums[-1])
                nums.pop(nums_size)
        else:
            for _ in range(nums_size - k):
                nums.append(nums[0])
                nums.pop(0)