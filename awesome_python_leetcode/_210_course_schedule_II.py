import collections
from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        There are a total of numCourses courses you have to take, labeled from 0 to
        numCourses - 1. You are given an array prerequisites where prerequisites[i] =
        [ai, bi] indicates that you must take course bi first if you want to take
        course ai.

        - For example, the pair [0, 1], indicates that to take course 0 you have to
        first take course 1.

        Return the ordering of courses you should take to finish all courses. If there
        are many valid answers, return any of them. If it is impossible to finish all
        courses, return an empty array.
        """
        adj = collections.defaultdict(list)
        for course1, course2 in prerequisites:
            adj[course1].append(course2)

        visited, cycle, order = set(), set(), []

        def dfs(course: int) -> bool:
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)
            for next_course in adj[course]:
                if not dfs(next_course):
                    return False
            cycle.remove(course)
            visited.add(course)
            order.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return order
