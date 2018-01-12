class Solution:
    """
    :type n: int
    :rtype: str
    """
    # Solution 1: Recursive method
    # Testcase Runtime: 75ms
    # Space complexity: O(n)
    def countAndSay_1(self, n):
        if n <= 1:
            return "1"
        else:
            seq = self.countAndSay(n-1)
            
            current, result = seq[0], ""
            count = 0
            for num in seq:
                if current == num:
                    count += 1
                else:
                    result = result + str(count) + str(current)
                    current = num
                    count = 1
            result = result + str(count) + str(current)
            return result
    
    # Solution 2: Sequential method
    # Testcase Runtime: 80ms
    def countAndSay_2(self, n):   
        if n <= 1:
            return "1"
            
        i = 2
        temp = "1"
        while(i<=n):
            current, result = temp[0], ""
            count = 0
            for num in temp:
                if num == current:
                    count+=1
                else:
                    result = result+str(count)+str(current)
                    current = num
                    count = 1
            result = result+str(count)+str(current)
            temp = result
            i+=1
        return result