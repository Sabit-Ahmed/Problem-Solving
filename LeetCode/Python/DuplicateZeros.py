from typing import List


class DuplicateZeros:

    def __init__(self):
        self.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0])

    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        i = 0
        while i < len(arr):
            # print(f"i:: {i}")
            if arr[i] == 0:
                for k in range(i + 2, len(arr)).__reversed__():
                    # print(f"k:: {k}")
                    arr[k] = arr[k - 1]
                if i + 1 < len(arr):
                    arr[i + 1] = 0
                print(arr)
                i += 2
            else:
                i += 1
        print(arr)