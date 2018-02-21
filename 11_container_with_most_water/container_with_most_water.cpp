/*
Topic:
Container With Most Water

Description:
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, 
such that the container contains the most water.

Note: 
You may not slant the container and n is at least 2.
*/

class Solution {
    public:
    
        // Solution: Use two indice to indicate the two lines, one from the beginning and the other from the end.
        //           Move the shorter line inwards until it finds a line longer than the one outside.
        //           Repeat the steps above until two lines intersect.
        // Time Complexity: O(N)
        // Space Complexity: O(1)
        int maxArea(vector<int>& height) {
            
            int maxArea = 0;
            int i = 0;
            int j = height.size()-1;
            while(i<j){
                int depth = (height[i]<height[j])?height[i]:height[j];
                int area = depth*(j-i);
                maxArea = (area>maxArea)?area:maxArea;
                while(height[i]<=depth && i<j) i++;
                while(height[j]<=depth && i<j) j--;
            }
            return maxArea;
        }
};