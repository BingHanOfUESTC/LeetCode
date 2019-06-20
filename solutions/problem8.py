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
                    return 0
        if len(res) == 0:
            return 0
        res = int(res)
        if res < -2147483648:
            res = -2147483648
        if res > 2147483648:
            res = 2147483648
        return res


def run():
    s = Solution()
    b = "4193 with words"
    res = s.myAtoi(b)
    print(res)


if __name__ == '__main__':
    run()
