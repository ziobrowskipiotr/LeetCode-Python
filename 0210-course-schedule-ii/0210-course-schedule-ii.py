class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]
        courses_map = {i:[] for i in range(numCourses)}
        courses_set = set()
        result_list = []
        result_list_set = set()
        for el in prerequisites:
            courses_map[el[0]].append(el[1])
        
        def topological_sort(course):
            if course in courses_set:
                return False
            if courses_map[course] == []:
                if course not in result_list_set:
                    result_list.append(course)
                    result_list_set.add(course)
                return True
            courses_set.add(course)
            for nex in courses_map[course]:
                if not topological_sort(nex):
                    return False
            result_list_set.add(course)
            result_list.append(course)
            courses_set.remove(course)
            courses_map[course] = []
            return True
        
        for i in range(numCourses):
            if not topological_sort(i):
                return []
        return result_list
