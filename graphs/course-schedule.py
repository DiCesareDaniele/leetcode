'''
https://leetcode.com/problems/course-schedule
'''

class Solution:
    # pylint: disable-next=invalid-name
    def canFinish(self, num_courses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(num_courses)]
        for course, requisite in prerequisites:
            graph[course].append(requisite)
        visited = [False] * num_courses
        rec_stack = [False] * num_courses
        def has_cycle(i: int) -> bool:
            if rec_stack[i]:
                return True
            if visited[i]:
                return False
            visited[i] = True
            rec_stack[i] = True
            for j in graph[i]:
                if has_cycle(j):
                    return True
            rec_stack[i] = False
            return False
        for i in range(num_courses):
            if has_cycle(i):
                return False
        return True
