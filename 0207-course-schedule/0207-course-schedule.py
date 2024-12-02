class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        courses_map = collections.defaultdict(list)
        courses_set = set()
        self.islands = 0
        for pre in prerequisites:
            courses_map[pre[0]] += [pre[1]]
            courses_set.add(pre[1])

        for i in range(numCourses):
            if i not in courses_map:
                courses_map[i] = []
            if i not in courses_set:
                self.islands += 1
        
        courses_set = set()

        def dfs(course):
            courses_set.add(course)

            for nei in courses_map[course]:
                if nei in courses_set:
                    return False
                else:
                    return dfs(nei)

            if len(courses_set)+self.islands == numCourses:
                return True
            else:
                courses_set.remove(course)
                return False
    
        for i in courses_map.keys():
            if dfs(i):
                return True
            courses_set = set()
        else:
            return False
