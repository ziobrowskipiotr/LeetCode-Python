class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses_map = {i:[] for i in range(numCourses)}
        cycle_set, courses_set = set(), set()
        result_list = []
        for el in prerequisites:
            courses_map[el[0]].append(el[1])
        
        def topological_sort(course):
            if course in cycle_set:
                return False
            if course in courses_set:
                return True
            cycle_set.add(course)
            for prev in courses_map[course]:
                if not topological_sort(prev):
                    return False
            courses_set.add(course)
            result_list.append(course)
            cycle_set.remove(course)
            return True
        
        for i in range(numCourses):
            if not topological_sort(i):
                return []
        return result_list
