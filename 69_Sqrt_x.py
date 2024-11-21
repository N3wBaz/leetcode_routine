class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        high = x // 2
        low = 0
        if x == 1:
            return 1
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid + 1
            else:
                high = mid - 1
        if mid * mid > x:
            return mid - 1
        else:
            return mid