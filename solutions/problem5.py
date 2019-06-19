class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) is 0:
            return ""
        res_list = []
        for idx, alp in enumerate(s):
            if idx == 0:
                res_list.append(alp)
            else:
                if alp == s[idx - 1]:
                    eve_res = alp + s[idx - 1]
                    odd_res = alp
                    res_list.append(eve_res)
                    iternum = min(idx, len(s)-idx-1)
                    if iternum > 0:
                        for iter_idx in range(iternum):
                            odd_up_idx = idx - iter_idx - 1
                            odd_low_idx = idx + iter_idx + 1
                            if odd_low_idx >= len(s):
                                break
                            if s[odd_up_idx] == s[odd_low_idx]:
                                odd_res = s[idx - iter_idx - 1] + odd_res + s[idx + iter_idx + 1]
                            else:
                                res_list.append(odd_res)
                            eve_up_idx = idx - iter_idx - 2
                            if eve_up_idx < 0:
                                break
                            eve_low_idx = idx + iter_idx + 1
                            if s[eve_up_idx] == s[eve_low_idx]:
                                eve_res = s[eve_up_idx] + eve_res + s[eve_low_idx]
                                res_list.append(eve_res)
                            else:
                                break
                if (idx + 1) >= len(s):
                    break
                elif s[idx - 1] == s[idx + 1]:
                    odd_res = alp
                    res_list.append(odd_res)
                    iternum = min(idx, len(s) - idx - 1)
                    if iternum > 0:
                        for odd_idx in range(iternum):
                            odd_up_idx = idx - odd_idx - 1
                            odd_low_idx = idx + odd_idx + 1
                            if odd_low_idx >= len(s):
                                break
                            if s[odd_up_idx] == s[odd_low_idx]:
                                odd_res = s[odd_up_idx] + odd_res + s[odd_low_idx]
                                res_list.append(odd_res)
                            else:
                                break
        max_num = 0
        max_idx = 0
        for idx, res in enumerate(res_list):
            if len(res) > max_num:
                max_num = len(res)
                max_idx = idx
            else:
                continue
        return res_list[max_idx]


if __name__ == '__main__':
    s = Solution()
    test = 'babadada'
    res = s.longestPalindrome(test)
    print(res)
