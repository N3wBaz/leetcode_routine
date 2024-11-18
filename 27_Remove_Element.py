class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = len(nums) - nums.count(val)
        for i in range(len(nums)):
            if nums[i] == val:
                for j in range(i, len(nums)):
                    if nums[j] != val:
                        break
                nums[i] = nums[j]
                nums[j] = val
        return k