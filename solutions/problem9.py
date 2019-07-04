class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xs = str(x)
        xs_r = str(x)
        xs = list(xs)
        xs_r = list(xs_r)
        xs_r.reverse()
        if xs == xs_r:
            return True
        else:
            return False


def run():
    num = 121
    s = Solution()
    res = s.isPalindrome(num)
    print(res)


if __name__ == '__main__':
    run()
