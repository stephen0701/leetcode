"""
Topic: 
    Course Schedule II
Description:
    There are a total of n courses you have to take, labeled from 0 to n-1.
    Some courses may have prerequisites, which is expressed as a pair of int in a list, 
    For example, [0, 1] means 1 is the prerequisite of 0.
    Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
    There may be multiple correct orders, you just need to return one of them.
    If it is impossible to finish all courses, return an empty array.
    
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
    :rtype: List[int]
    """

    # Solution: BFS, search all the courses that can be finished.
    # Compare the final finished courses with the total number of courses.
    # Time Complexity: O(E) [Initialize the graph] + O(V+E) [Iterate all the courses and edges]
    # Space Complexity: O(V)
    # Testcase runtime: 52ms
    def findOrder(self, numCourses, prerequisites):

        ordering = []
        queue = [] # or collection.deque (double linked list)
        visited = [False] * numCourses
        edges = [[] for i in range(numCourses)]
        indegree = [0] * numCourses

        for pair in prerequisites:
            edges[pair[1]].append(pair[0])
            indegree[pair[0]] += 1

        for i in range(numCourses):
            if not visited[i] and indegree[i] == 0:
                queue.append(i)

            while len(queue) > 0:
                course = queue.pop(0)
                for nextCourse in edges[course]:
                    indegree[nextCourse] -= 1
                    if indegree[nextCourse] == 0:
                        queue.append(nextCourse)
                visited[course] = True
                ordering.append(course)

        if len(ordering) == numCourses:
            return ordering
        else:
            return []