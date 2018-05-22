"""
Topic: 
    Course Schedule
Description:
    There are a total of n courses you have to take, labeled from 0 to n-1.
    Some courses may have prerequisites, which is expressed as a pair of int in a list, 
    For example, [0, 1] means 1 is the prerequisite of 0.
    Given the total number of courses and a list of prerequisite pairs, find out whether it is possible to finish all courses.
    
Note:
    The input prerequisites is a graph represented by a list of edges.
    You may assume that there are no duplicate edges in the input prerequisites.

 Hints:
    This problem is equivalent to finding if a cycle exists in a directed graph. 
    If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
    Topological Sort can be done via DFS or BFS.    
"""

class Solution:
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    
    # Solution 1: BFS
    # Time Complexity: O(V+E)
    # Space Complexity: O(V)
    # Testcase Runtime: 52ms
    def canFinish_bfs(self, numCourses, prerequisites):

        queue = []
        visited = [False]*numCourses
        indegree = [0]*numCourses
        course_mapping = [[] for i in range(numCourses)]
        
        # Initialize the course correlation and indegree of each course
        for pair in prerequisites:
            course_mapping[pair[1]].append(pair[0])
            indegree[pair[0]]+=1
        
        # BFS: visit the course which indegree = 0
        course_count = 0
        for i in range(numCourses):
            if not visited[i] and indegree[i]==0:
                queue.append(i)
            
            while len(queue) > 0:
                course = queue.pop(0)
                course_count+=1
                for c in course_mapping[course]:
                    if not visited[c]:
                        indegree[c]-=1
                        if indegree[c]==0:
                            queue.append(c)
                visited[course] = True
        return course_count == numCourses
        
    # Solution 2: DFS
    # Time Complexity: O(E)[create course relation] + O(V+E)[DFS]
    # Space Complexity: max(O(E), O(V)), where O(E) is caused by recursion and course_mapping
    # Testcase Runtime: 164ms
    def canFinish(self, numCourses, prerequisites):
    
        course_mapping = {}
        for pair in prerequisites:
            if pair[0] not in course_mapping.keys():
                course_mapping[pair[0]] = []
            course_mapping[pair[0]].append(pair[1])
        
        processed = set()
        for course in range(numCourses):
            
            # nested function
            def dfs(course, path):
                if course not in course_mapping.keys() or not course_mapping[course]:
                    processed.add(course)
                    return True
                elif course in processed:
                    return True
                elif course in path:
                    return False

                path.add(course)
                for c in course_mapping[course]:
                    if not dfs(c, path.copy()):
                        return False
                processed.add(course)
                return True

            if not dfs(course, set()):
                return False
        return True