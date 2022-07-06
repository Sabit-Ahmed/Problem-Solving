from typing import List


class ValidMountainArray:

    def __init__(self):
        res = self.validMountainArray([2,0,2])
        print(res)

    def validMountainArray(self, arr: List[int]) -> bool:
        mid = arr.index(max(arr))
        # print(mid)
        i = j = mid
        left = mid - 1
        right = mid + 1
        if len(arr) <= 2:
            return False

        while i > 0 and j < len(arr) - 1:

            if arr[left] >= arr[i] or arr[right] >= arr[j]:
                return False

            left -= 1
            i -= 1
            right += 1
            j += 1

        return True
