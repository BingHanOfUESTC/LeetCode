class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        res = ''
        s_idx = 0
        for idx, x in enumerate(str):
            if x == ' ':
                s_idx = idx
                continue
            else:
                if x == '-':
                    res = '-'
                    if idx + 1 >= len(str):
                        return 0
                    continue
                if (ord(x) <= ord('9')) and (ord(x) >= ord('0')):
                    res += x
                else:
                    continue
        if len(res) == 0:
            return 0
        res = int(res)
        if res < -2147483648:
            res = -2147483648
        if res > 2147483648:
            res = 2147483648
        return res


class Solution1(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        res = ''
        for idx, x in enumerate(str):
            if x == '-' and len(res) == 0:
                res = '-'
                if idx + 1 >= len(str):
                    return 0
                continue
            if (ord(x) <= ord('9')) and (ord(x) >= ord('0')):
                res += x
            elif idx > 0:
                return 0
            else:
                continue

        if (len(res) == 0) or (res == '-'):
            return 0
        res = int(res)
        if res < -2147483648:
            res = -2147483648
        if res > 2147483648:
            res = 2147483648
        return res


def run():
    s = Solution1()
    b = "    54words and 987"
    res = s.myAtoi(b)
    print(res)


if __name__ == '__main__':
    run()
