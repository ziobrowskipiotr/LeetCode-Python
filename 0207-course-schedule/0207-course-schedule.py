class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses_map = {i:[] for i in range(numCourses)}
        cycle_set, courses_set = set(), set()
        for pre in prerequisites:
            courses_map[pre[0]] += [pre[1]]

        def dfs(course):
            if course in cycle_set:
                return False
            if course in courses_set:
                return True
            cycle_set.add(course)
            for prev in courses_map[course]:
                if not dfs(prev):
                    return False
            cycle_set.remove(course)
            courses_set.add(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
