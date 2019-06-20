class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if abs(x) > 2147483648:
            return 0
        s = list(str(x))
        s.reverse()
        res = ''
        for num in s:
            res += num
        if x < 0:
            res = -int(res[:-1])
        else:
            res = int(res)
        if abs(res) > 2147483648:
            return 0
        return res


def run():
    s = Solution()
    test_num = 1534236469
    num = s.reverse(test_num)
    print(num)


if __name__ == '__main__':
    run()
