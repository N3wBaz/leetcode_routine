class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numbers =[
            ("XL", 40), ("XC", 90),
            ("IV", 4), ("IX", 9),
            ("CD", 400), ("CM", 900),
            ("X", 10), ("V", 5),
            ("L", 50), ("I", 1),
            ("C", 100), ("D", 500),
            ("M", 1000)  
        ]
        rtype = 0
        for key in numbers:
            if key[0] in s:
                rtype += key[1] * s.count(key[0])
                s = s.replace(key[0], "")
        return rtype