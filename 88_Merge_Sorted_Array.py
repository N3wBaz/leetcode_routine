class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        p1 = m - 1  # Последний значимый элемент в nums1
        p2 = n - 1  # Последний элемент в nums2
        p = m + n - 1  # Последний индекс массива nums1

        # Шаг 1: Сравниваем элементы с конца и заполняем nums1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:  # Если текущий элемент nums1 больше
                nums1[p] = nums1[p1]
                p1 -= 1  # Перемещаем указатель p1
            else:  # Если текущий элемент nums2 больше или равен
                nums1[p] = nums2[p2]
                p2 -= 1  # Перемещаем указатель p2
            p -= 1  # Перемещаем общий указатель p

        # Шаг 2: Если остались элементы в nums2, копируем их в nums1
        # Элементы nums1 уже на месте, их не нужно копировать
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1