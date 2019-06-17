import numpy as np


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        len_sum = len1 + len2
        nums = nums1 + nums2
        nums = sorted(nums)
        if len_sum is 0:
            return []
        elif len_sum is 1:
            return nums[0]

        if len_sum % 2 == 0:
            mid_idx1 = int(len_sum/2 + 0.5)
            mid_idx2 = mid_idx1 - 1
            return (nums[mid_idx1] + nums[mid_idx2])/2
        else:
            mid_idx = int(len_sum/2)
            return nums[mid_idx]


if __name__ == '__main__':
    s = Solution()
    nums1 = [1,2]
    nums2 = [3,4]
    res = s.findMedianSortedArrays(nums1, nums2)
    print(res)
