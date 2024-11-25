class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda x: x[0])
        i = 0
        while i<len(intervals):
            result.append(intervals[i])
            i += 1
            while i<len(intervals):
                if intervals[i][0] <= result[-1][1]:
                    if intervals[i][1] <= result[-1][1]:
                        i += 1
                        continue
                    else:
                        result[-1][1] = intervals[i][1]
                        i += 1
                else:
                    break            
        return result
