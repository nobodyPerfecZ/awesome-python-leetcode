import collections
from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        There are a total of numCourses courses you have to take, labeled from 0 to
        numCourses - 1. You are given an array prerequisites where prerequisites[i] =
        [ai, bi] indicates that you must take course bi first if you want to take course
        ai.

        - For example, the pair [0, 1], indicates that to take course 0 you have to
        first take course 1.

        Return true if you can finish all courses. Otherwise, return false.
        """
        adj = collections.defaultdict(list)
        for course1, course2 in prerequisites:
            adj[course1].append(course2)
        visited = set()

        def dfs(course: int) -> bool:
            if course in visited:
                return False
            if not adj[course]:
                return True
            visited.add(course)
            for next_course in adj[course]:
                if not dfs(next_course):
                    return False
            visited.remove(course)
            adj[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
