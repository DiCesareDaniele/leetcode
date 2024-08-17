'''
https://leetcode.com/problems/course-schedule-ii
'''

class Solution:
    # pylint: disable-next=invalid-name
    def findOrder(self, num_courses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(num_courses)]
        for course, requisite in prerequisites:
            graph[course].append(requisite)
        visited = [False] * num_courses
        rec_stack = [False] * num_courses
        stack = []
        def top_order(i: int) -> bool:
            if rec_stack[i]:
                return False
            if visited[i]:
                return True
            visited[i] = True
            rec_stack[i] = True
            for j in graph[i]:
                if not top_order(j):
                    return False
            stack.append(i)
            rec_stack[i] = False
            return True
        for i in range(num_courses):
            if not top_order(i):
                return []
        return stack
