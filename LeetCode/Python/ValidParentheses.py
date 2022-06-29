class ValidParentheses:

    def __init__(self):
        res = self.isValid("()[]{}")
        print(res)

    @staticmethod
    def isValid(s: str) -> bool:
        # Write your code here
        c = 0
        while True:
            if s.find('()') != -1:
                s = s.split('()')
                s = ''.join(s)
            elif s.find('{}') != -1:
                s = s.split('{}')
                s = ''.join(s)
            elif s.find('[]') != -1:
                s = s.split('[]')
                s = ''.join(s)
            else:
                c = len(s)
                break

        if c == 0:
            return True

        else:
            return False
