class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ""
        I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 1000
        while num > 0:
            if (num > I) and (num < V - 1):
                res = "I"*num
            elif (num >= V-1) and (num < X - 1):
                temp_num = num - V
                if temp_num < 0:
                    res = "I"*abs(temp_num) + "V"
                else:
                    res = "V" + 'I'*temp_num
            elif (num >= X-1) and (num < L - 1):
                return 0


def run():
    s = Solution()


if __name__ == '__main__':
    run()
