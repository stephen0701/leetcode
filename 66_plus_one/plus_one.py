class Solution:
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    
    # Solution 1: Plus one from the end of the list of integers, and handle the carry-over situation
    # Testcase Runtime: 63ms
    def plusOne(self, digits):
        i = len(digits)-1
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                i-=1
            else:
                digits[i] += 1
                break
        return digits
    
    # Solution 2: Use iteration to convert list of integers to num, plus one to num, and convert it back to list
    # Testcase Runtime: 64ms
    def plusOne_2(self, digits):
        num = 0
        for i in range(len(digits)):
            num = num*10 + digits[i]
        return [int(n) for n in str(num+1)]
    
    # Solution 3: Fastest solution, use reduce() to convert list of integers to num, plus one to num, and convert back to list
    # Note: reduce() can only be used in Python 2; In Python 3, reduce() is moved into the "functools" package
    # Testcase Runtime: 35ms
    def plusOne_3(self, digits):
        num = functools.reduce(lambda x,y: x*10+y, nums)+1
        return [int(n) for n in str(num)]