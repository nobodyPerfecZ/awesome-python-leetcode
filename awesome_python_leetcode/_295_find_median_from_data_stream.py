from heapq import heappush, heappop


class MedianFinder:
    """
    The median is the middle value in an ordered integer list. If the size of the list
    is even, there is no middle value, and the median is the mean of the two middle
    values.
    - For example, for arr = [2,3,4], the median is 3.
    - For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

    Implement the MedianFinder class:
    - MedianFinder() initializes the MedianFinder object.
    - void addNum(int num) adds the integer num from the data stream to the data
    structure.
    - double findMedian() returns the median of all elements so far. Answers within
    10-5 of the actual answer will be accepted.
    """

    def __init__(self):
        self.smallHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heappush(self.smallHeap, -num)

        if (
            self.smallHeap
            and self.maxHeap
            and (-1 * self.smallHeap[0]) > self.maxHeap[0]
        ):
            val = heappop(self.smallHeap)
            heappush(self.maxHeap, -val)

        if len(self.smallHeap) > len(self.maxHeap) + 1:
            val = heappop(self.smallHeap)
            heappush(self.maxHeap, -val)

        if len(self.maxHeap) > len(self.smallHeap) + 1:
            val = heappop(self.maxHeap)
            heappush(self.smallHeap, -val)

    def findMedian(self) -> float:
        if len(self.smallHeap) == len(self.maxHeap):
            return 0.5 * (-self.smallHeap[0] + self.maxHeap[0])
        elif len(self.smallHeap) > len(self.maxHeap):
            return -self.smallHeap[0]
        else:
            return self.maxHeap[0]
