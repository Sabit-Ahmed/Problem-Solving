from typing import List


class CheckDoubleInArray:

    def __init__(self):
        arr = [10,2,5,3]
        res = self.checkIfExist(arr)
        print(res)

    def checkIfExist(self, arr: List[int]) -> bool:
        hashmap = {}
        for i in range(len(arr)):
            product = arr[i] / 2
            print(hashmap.keys())
            if product in hashmap.keys():
                return True
            hashmap[product] = i
        return False