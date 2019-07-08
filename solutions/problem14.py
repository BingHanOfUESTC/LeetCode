class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for idx, s in enumerate(strs):
            if idx == 0:
                res = s
                continue
            else:
                sub_len = min(len(res), len(s))
                res = res[:sub_len]
                for sub_idx in range(sub_len):
                    if res[sub_idx] == s[sub_idx]:
                        continue
                    else:
                        res = res[:sub_idx]
                        break

        return res


def run():
    test = ["flower", "flight", "flow"]
    s = Solution()
    res = s.longestCommonPrefix(test)
    print(res)


if __name__ == '__main__':
    run()
