"""
Topic: 
    Merge Sorted Array
Description:
    Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
    You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
    The number of elements initialized in nums1 and nums2 are m and n respectively.
"""
class Solution:
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    # Solution 1: Merge the arrays from the end. Easy to implement but ineffcient.
    # Testcase Runtime: 100ms
    def merge(self, nums1, m, nums2, n):
        i, j, end = m-1, n-1, m+n-1
        while i>=0 and j>=0:
            if nums1[i] >= nums2[j]:
                nums1[end]=nums1[i]
                i -= 1
            else:
                nums1[end]=nums2[j]
                j -= 1
            end -= 1
        if j>=0:
            nums1[0:j+1]=nums2[0:j+1]
            
    # Solution 2: More elegant than #1. [Referenced]
    # Testcase Runtime: 90ms
    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
            
    # Solution 3: Merge the arrays from the beginning. Faster but indexing needs to be handled carefully
    # Testcase Runtime: 72ms
    def merge(self, nums1, m, nums2, n):
        nums1[:] = nums1[:m]
        nums2[:] = nums2[:n]
        i, j, current= 0, 0, 0
        while i-j < m and j < n:
            if nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                j += 1
            i += 1
        while j < n:
            nums1.append(nums2[j])
            j+=1