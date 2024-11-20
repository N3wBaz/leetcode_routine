class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = sum([v *10**i for i, v in enumerate(digits[::-1])])+1
        digits = []
        while num > 0:
            digit = num % 10
            digits.append(digit)
            num //= 10
        return digits[::-1]