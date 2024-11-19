class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        high = len(nums) - 1
        low = 0
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        if mid > low:
            return mid
        else:
            return low 