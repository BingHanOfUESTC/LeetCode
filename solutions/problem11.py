class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        vol = []
        for temp_h in height:
            temp_hs = []
            for idx, num in enumerate(height):
                if num >= temp_h:
                    temp_hs.append(idx)
            if len(temp_hs) > 1:
                area = (temp_hs[-1] - temp_hs[0])*temp_h
                vol.append(area)

        res = max(vol)
        return res


class Solution1(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        vol = []
        for idx, num in enumerate(height):
            idx2 = len(height) - 1
            while idx2 > idx:
                h = min(num, height[idx2])
                area = (idx2 - idx)*h
                vol.append(area)
                idx2 -= 1
        res = max(vol)
        return res


def run():
    s = Solution1()
    test_list = [1,8,6,2,5,4,8,3,7]
    res = s.maxArea(test_list)
    print(res)


if __name__ == '__main__':
    run()
