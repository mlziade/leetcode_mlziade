class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        aux = 0
        for x in nums:
            if x != val:
                nums[aux] = x
                aux += 1
        return aux