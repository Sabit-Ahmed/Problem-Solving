from typing import List


class MergeSortedArray:

    def __init__(self):
        # nums1 = [4,0,0,0,0,0]
        # m = 1
        # nums2 = [1,2,3,5,6]
        # n = 5

        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3

        # nums1 = [0]
        # m = 0
        # nums2 = [1]
        # n = 1
        self.mergeOpimized(nums1, m, nums2, n)

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()
        print(nums1)

    def mergeOpimized(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        nums3 = nums1.copy()
        i = 0
        j = 0
        k = 0

        # Traverse both array
        while i < m and j < n:
            if nums3[i] < nums2[j]:
                nums1[k] = nums3[i]
                k = k + 1
                i = i + 1
            else:
                nums1[k] = nums2[j]
                k = k + 1
                j = j + 1

        if j < n and k < m+n:
            while k < m + n and j < n:
                nums1[k] = nums2[j]
                k += 1
                j += 1

        elif i < m and k < m+n:
            while k < m + n and i < m:
                nums1[k] = nums3[i]
                k += 1
                i += 1

        print(nums1)
