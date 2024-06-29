'''
https://leetcode.com/problems/median-of-two-sorted-arrays
'''

class Solution:
    # pylint: disable-next=invalid-name
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float | None:
        m = len(nums1)
        n = len(nums2)
        if m < n:
            nums1, nums2 = nums2, nums1
            n, m = m, n

        i = 0
        j = 2 * n
        while i <= j:
            mid2 = (i + j) // 2
            mid1 = n + m - mid2

            l1 = -1e10 if mid1 == 0 else nums1[(mid1 - 1) // 2]
            l2 = -1e10 if mid2 == 0 else nums2[(mid2 - 1) // 2]
            r1 = 1e10 if mid1 == 2 * m else nums1[mid1 // 2]
            r2 = 1e10 if mid2 == 2 * n else nums2[mid2 // 2]

            if l1 > r2:
                i = mid2 + 1
            elif l2 > r1:
                j = mid2 - 1
            else:
                return (max(l1, l2) + min(r1, r2)) / 2
        return None
