class Solution:

    # Solution 1: Simplest Solution
    # Testcase Runtime: 70ms
    # Time Complexity: O(n)
    # Note: Uses two pointer to finish.
    #       One is to compare whether current value is equal to assigned value,
    #       The other is to track the last valid index of the list.
    #       This solution can be improved by a better algorithm.
    # Question: Is it necessary to copy the value even if two pointer are point at the same index?
    #           Is it the best way to move the following unmatching value forward to fill up where matching value occur?
    def removeElement_1(self, nums, val):
        i = 0
        for element in nums:
            if element == val:
                continue
            else:
                nums[i] = element
                i += 1
        return i

    # HINT: Instead of replacing the matching value with the following, is there any more efficient way to change the value?
    # Solution 2: Change the matching value with the last unmatching value.
    # Testcase Runtime: 58ms
    # Time Complexity: O(n)
    def removeElement_2(self, nums, val):
        end = len(nums) - 1
        for i, element in enumerate(nums):
            if i > end:
                break
            elif i == end:
                if element == val:
                    end -= 1
                    break
            else:
                if element == val:
                    while nums[end] == val and end >= i:
                        end -= 1
                    if end > i:
                        nums[i] = nums[end]
                        end -= 1
        length = end+1 if end >= 0 else 0
        return length
        
    # Solution 3: Most elegant code, but most time-consuming
    # Testcase Runtime: 98ms
    # Time Complexity: O(n)
    # Note: If start and end are both equal to val, 
    #       start and end swap the value, which costs a copy operation,
    #       then start remain at the same index, end moves forward.
    #       The unnecessary copy operation doesn't change the result but costs time.
    def removeElement_3(self, nums, val):
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start +=1
        return start
    
    # Solution 4: Improve version of the solution 3
    # Testcase Runtime: 69ms
    # Time Complexity: O(n)
    def removeElement_4(self, nums, val):
        start, end = 0, len(nums)-1
        while start <= end:
            if nums[start] == val:
                while nums[end] == val:
                    end = end-1
                    if end <= start:
                        break
                if end <= start:
                    break
                nums[start], nums[end], end = nums[end], nums[start], end-1
            else:
                start += 1
        length = end+1
        return length