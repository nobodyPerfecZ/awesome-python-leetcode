import collections
import heapq
from dataclasses import dataclass
from typing import List


@dataclass(order=True, frozen=True)
class Task:
    priority: int
    taskId: int
    userId: int


class TaskManager:
    """
    There is a task management system that allows users to manage their tasks, each
    associated with a priority. The system should efficiently handle adding, modifying,
    executing, and removing tasks.

    Implement the TaskManager class:
    - TaskManager(vector<vector<int>>& tasks) initializes the task manager with a list
    of user-task-priority triples. Each element in the input list is of the form
    [userId, taskId, priority], which adds a task to the specified user with the given
    priority.
    - void add(int userId, int taskId, int priority) adds a task with the specified
    taskId and priority to the user with userId. It is guaranteed that taskId does not
    exist in the system.
    - void edit(int taskId, int newPriority) updates the priority of the existing
    taskId to newPriority. It is guaranteed that taskId exists in the system.
    - void rmv(int taskId) removes the task identified by taskId from the system. It is
    guaranteed that taskId exists in the system.
    - int execTop() executes the task with the highest priority across all users. If
    there are multiple tasks with the same highest priority, execute the one with the
    highest taskId. After executing, the taskId is removed from the system. Return the
    userId associated with the executed task. If no tasks are available, return -1.

    Note that a user may be assigned multiple tasks.
    """

    def __init__(self, tasks: List[List[int]]):
        # (taskId -> userId)
        self.task_id_to_user_id = collections.defaultdict(int)
        self.task_id_to_priority = collections.defaultdict(int)
        self.heap = []
        for task in tasks:
            userId, taskId, priority = task
            task = Task(-priority, -taskId, -userId)
            self.task_id_to_user_id[taskId] = userId
            self.task_id_to_priority[taskId] = priority
            heapq.heappush(self.heap, task)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        # O(1)
        task = Task(-priority, -taskId, -userId)
        self.task_id_to_user_id[taskId] = userId
        self.task_id_to_priority[taskId] = priority
        heapq.heappush(self.heap, task)

    def edit(self, taskId: int, newPriority: int) -> None:
        # O(1)
        userId = self.task_id_to_user_id[taskId]
        task = Task(-newPriority, -taskId, -userId)
        self.task_id_to_priority[taskId] = newPriority
        heapq.heappush(self.heap, task)

    def rmv(self, taskId: int) -> None:
        # O(1)
        del self.task_id_to_user_id[taskId]
        del self.task_id_to_priority[taskId]

    def execTop(self) -> int:
        # O(log(n))
        # O(1)
        while self.heap:
            task = self.heap[0]
            if -task.taskId not in self.task_id_to_priority:
                heapq.heappop(self.heap)
                continue
            if -task.priority != self.task_id_to_priority[-task.taskId]:
                heapq.heappop(self.heap)
                continue
            break
        if self.heap:
            task = heapq.heappop(self.heap)
            self.rmv(-task.taskId)
            return -task.userId
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
