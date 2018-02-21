/*
Topic:
3 Sum

Description:
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0.
Find all unique triplets in the array which gives the sum of zero.

Note: 
The solution set must not contain duplicate triplets.
*/

class Solution {
public:

    // Solution: First, sort the list by calling a sorting function.
    //           Select the first element by looping the sorted list. 
    //           Once the first element is selected, assume the problem as a two sum problem.
    //           Select the second element from the beginning of the remaining list and the third element from the end of the list.
    //           If the sum of two elements is larger than the target number, move the third element to its previous element, and vise versa.
    //           Once a combination of the answer is found, add it to the result vector.
    // Time Complexity: O(NlogN)[Sorting] + O(N^2) [Looping] = O(N^2)
    // Space Complexity: O(1)
    vector<vector<int>> threeSum(vector<int>& nums) {
        
        if (nums.size() < 3){
            return vector<vector<int>>();
        }
        
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());
        
        for(int i=0; i<nums.size()-2; i++){
            int j = i+1;
            int k = nums.size()-1;
            int target = -nums[i];
            while(j<k){
                if (nums[j]+nums[k] == target){
                    vector<int> ans = {nums[i], nums[j], nums[k]};
                    result.push_back(ans);
                    while(nums[++j]==nums[j-1] && j<k);
                    while(nums[--k]==nums[k+1] && j<k);
                }
                else if (nums[j]+nums[k] > target){
                    k--;
                }
                else{
                    j++;
                }
            }
            while(nums[i+1]==nums[i] && i<nums.size()-2) i++;
        }
        return result;
    }
};