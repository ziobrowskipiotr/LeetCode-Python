#1
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        nodes = collections.defaultdict(list)
        for x1, y1 in points:
            for x2, y2 in points:
                if (x1, y1) == (x2, y2):
                    continue
                else:
                    nodes[(x1, y1)].append([abs(x1-x2) + abs(y1-y2), (x2, y2)])
        
        n = len(points)
        heap = []
        visit_set = set()
        total_cost = 0
        point0 = tuple(points[0])
        heapq.heappush(heap, (0,point0))
        while len(visit_set) < n:
            weight, point = heapq.heappop(heap)
            if point in visit_set:
                continue
            visit_set.add(point)
            total_cost += weight
            for new_weight, new_point in nodes[point]:
                if new_point in visit_set:
                    continue
                else:
                    heapq.heappush(heap, (new_weight, new_point))
        return total_cost
            



