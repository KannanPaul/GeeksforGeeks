'''Given a N x M grid. Find All possible paths from top left to bottom right.From each cell you can either move only to right or down.

Example 1:

Input: 1 2 3
       4 5 6
Output: 1 4 5 6
        1 2 5 6 
        1 2 3 6
Explanation: We can see that there are 3 
paths from the cell (0,0) to (1,2).

Example 2:

Input: 1 2
       3 4
Output: 1 2 4
        1 3 4
'''

Solution:
  Time Complexity: O(2^N*M)
  Auxiliary Space: O(N)
    
    from typing import List
class Solution:
            
    def findAllPossiblePaths(self, n : int, m : int, grid : List[List[int]]) -> List[List[int]]:
        # code here
        res=[]
        def backtrack(mat,path,i,j):
            if not mat or not len(mat):
                return
            m=len(mat)
            n=len(mat[0])
            
            if i==m-1 and j==n-1:
                #path=path+[mat[i][j]]
                #res.append(path.copy())
                res.append(path+[mat[i][j]])
                return 
            
            path.append(mat[i][j])
            if 0<=i+1<m and 0<=j<n:
                backtrack(mat,path,i+1,j)
            if 0<=i<m and 0<=j+1<n:
                backtrack(mat,path,i,j+1)
            
            path.pop()
                      
        x=y=0
        path=[]
        backtrack(grid,path,x,y)
        return res
        
'''link -https://www.techiedelight.com/find-all-paths-from-source-to-destination-in-matrix/'''
