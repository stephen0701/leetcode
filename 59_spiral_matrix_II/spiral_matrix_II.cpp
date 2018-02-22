/*
Topic:
    Spiral Matrix II

Description:
    Given an integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.

Example: 
    Given n = 3,
    return the following matrix:
    [
     [ 1, 2, 3 ],
     [ 8, 9, 4 ],
     [ 7, 6, 5 ]
    ]
*/

class Solution {
public:

    // Solution: Use four variables to indicate the boundaries, which are r1, r2, c1, c2.
    //           Start inserting the element from the outer layer to the inner layer.
    // Time Complexity: O(N)
    // Space Complexity: O(N), the space of the result matrix.
    vector<vector<int>> generateMatrix(int n) {
        if (n<=0){
            return vector<vector<int>>();    
        }
        
        vector<vector<int>> result;
        for (int i=0; i<n; i++){
            result.push_back(vector<int>(n));
        }
        
        int r1 = 0, r2 = n-1;
        int c1 = 0, c2 = n-1;
        int count = 1;
        while(r1<r2 && c1<c2){
            for(int c=c1; c<c2; c++) result[r1][c]=count++;
            for(int r=r1; r<r2; r++) result[r][c2]=count++;
            for(int c=c2; c>c1; c--) result[r2][c]=count++;
            for(int r=r2; r>r1; r--) result[r][c1]=count++;
            r1++;
            r2--;
            c1++;
            c2--;
        }
        if (r1==r2 && c1==c2){
            result[r1][c1]=count;
        }
        return result;
    }
};