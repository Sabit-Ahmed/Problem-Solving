from typing import List

class MergeSortedArray:

    def __init__(self):
        nums1 = [4,5,6,0,0,0]
        m = 3
        nums2 = [1,2,3]
        n = 3
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
        if n > 0:
            if m == 0 or nums3[m - 1] <= nums2[0]:
                for i in range(n):
                    nums1[m + i] = nums2[i]
            elif nums3[0] > nums2[n - 1]:
                for i in range(m+n):
                    if i < m:
                        nums1[i] = nums2[i]
                    else:
                        nums1[i] = nums3[m - i]
            else:
                i = 0
                j = 0
                while j < n and i < m+n:
                    if i > m:
                        nums1[i] = nums2[j]
                        i += 1
                        j += 1
                    else:
                        if nums3[i] > nums2[j]:
                            nums1[i] = nums2[j]
                            nums1[i + 1] = nums3[i]
                            j += 1
                        else:
                            i += 1

                if j >= n:
                    for k in range(i + 2, m+n):
                        nums1[k] = nums3[k - 1]
        print(nums1)


        # arr3 = [None] * (m + n)
        # i = 0
        # j = 0
        # k = 0
        #
        # # Traverse both array
        # while i < m and j < n:
        #     if nums1[i] < nums2[j]:
        #         arr3[k] = nums1[i]
        #         k = k + 1
        #         i = i + 1
        #     else:
        #         arr3[k] = nums2[j]
        #         k = k + 1
        #         j = j + 1
        # print(arr3)