class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses

        if len(prerequisites) == 0:
            return True

        for prerequisite in prerequisites:
            preCourse = prerequisite[0]
            suffixCourse = prerequisite[1]
            courses[preCourse].append(suffixCourse)
            indegrees[suffixCourse] += 1

        num_zero_prerequisite = 0
        queue = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
                num_zero_prerequisite += 1

        while queue:
            curr_course = queue.popleft()
            for next_course in courses[curr_course]:
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0:
                    num_zero_prerequisite += 1
                    queue.append(next_course)
        return num_zero_prerequisite == numCourses

        

