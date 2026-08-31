from typing import List, Optional

from awesome_python_leetcode.list import ListNode


class Solution:
    """Base class for all LeetCode Problems."""

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        """
        A critical point in a linked list is defined as either a local maxima
        or a local minima.

        A node is a local maxima if the current node has a value strictly greater
        than the previous node and the next node.

        A node is a local minima if the current node has a value strictly smaller
        than the previous node and the next node.

        Note that a node can only be a local maxima/minima if there exists both
        a previous node and a next node.

        Given a linked list head, return an array of length 2 containing
        [minDistance, maxDistance] where minDistance is the minimum distance
        between any two distinct critical points and maxDistance is the maximum
        distance between any two distinct critical points. If there are fewer
        than two critical points, return [-1, -1].
        """
        if head is None:
            return [-1, -1]
        if head.next is None:
            return [-1, -1]

        prev = head
        cur = head.next
        nxt = head.next.next

        # minDistance = min(minDistance, |i - j|)
        # maxDistance = last_critical_point - first_critical_point
        min_distance = float("inf")
        max_distance = float("inf")

        first = -1  # first critical point position
        last = -1  # another (or last) critical point position
        i = 1  # another (or last) critical point position
        j = -1  # prev critical point position

        while prev and cur and nxt:
            if (prev.val < cur.val and nxt.val < cur.val) or (
                prev.val > cur.val and nxt.val > cur.val
            ):
                # Case: Critical point found
                if first == -1:
                    # Case: First critical point found
                    first = i
                else:
                    # Case: Another (or last) critical point found
                    last = i

                if j == -1:
                    # Case: First critical point found
                    j = i
                else:
                    # Case: Another (or last) critical point found
                    min_distance = min(min_distance, i - j)
                    max_distance = last - first
                    j = i

            i += 1
            prev = cur
            cur = nxt
            nxt = nxt.next
        return (
            [int(min_distance), int(max_distance)]
            if min_distance != float("inf") and max_distance != float("inf")
            else [-1, -1]
        )
