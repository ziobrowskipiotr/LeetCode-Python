class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        courses_map = {i:[] for i in range(numCourses)}
        courses_set = set()
        for pre in prerequisites:
            courses_map[pre[0]] += [pre[1]]

        def dfs(course):
            if course in courses_set:
                return False
            if courses_map[course] == []:
                return True
            
            courses_set.add(course)
            for nei in courses_map[course]:
                if not dfs(nei):
                    return False
            courses_set.remove(course)
            courses_map[course] = []
            return True
    
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
