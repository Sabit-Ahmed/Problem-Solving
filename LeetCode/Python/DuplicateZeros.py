from typing import List


class DuplicateZeros:

    def __init__(self):
        self.duplicateZeros([1,5,2,0,6,8,0,6,0])

    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        i = 0
        while i < len(arr):
            if arr[i] == 0:
                if i + 1 < len(arr) - 1:
                    for k in range(i + 2, len(arr)).__reversed__():
                        arr[k] = arr[k - 1]
                    arr[i + 1] = 0
                    print(arr)
                i += 2
            else:
                i += 1
        print(arr)

    def duplicateZerosOptimized(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
