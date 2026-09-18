class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses

        for src, dst in prerequisites:
            courses[dst].append(src)
            indegrees[src] += 1

        result = []
        queue = deque()
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                result.append(i)
                queue.append(i)

        while queue:
            curr_course = queue.popleft()
            for next_course in courses[curr_course]:
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0:
                    result.append(next_course)
                    queue.append(next_course)
        if len(result) != numCourses:
            return []
        return result