class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = []
        visit_set = set()
        graph_map = collections.defaultdict(list)
        for time in times:
            graph_map[time[0]].append((time[2], time[1]))

        result = 0
        heapq.heappush(heap, (0, k))
        while heap:
            weight, node = heapq.heappop(heap)
            if node in visit_set:
                continue
            visit_set.add(node)
            result = max(result, weight)
            for actual_weight, actual_node in graph_map[node]:
                if actual_node not in visit_set:
                    heapq.heappush(heap, (weight+actual_weight, actual_node))

        return result if len(visit_set) == n else -1 
