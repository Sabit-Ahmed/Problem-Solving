from typing import List


class LongestCommonPrefix14:

    def __init__(self):
        res = self.longestCommonPrefix(["ab","a"])
        print(res)

    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLength = 999999999999
        indexOfMinElement = -1
        for (i, v) in enumerate(strs):
            if len(v) < minLength:
                minLength = len(v)
                indexOfMinElement = i
        outputStr = ""
        for k in range(len(strs[indexOfMinElement])):
            for i in range(len(strs)):
                if str.lower(strs[indexOfMinElement][k]) == str.lower(strs[i][k]):
                    if i == len(strs) - 1:
                        outputStr = outputStr + strs[indexOfMinElement][k]
                else:
                    return outputStr

        return outputStr
