class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = []
        graph_map = collections.defaultdict(list)
        for time in times:
            graph_map[time[0]].append((time[2], time[1]))

        heapq.heappush(heap, (0, k))
        while heap:
            weight, node = heapq.heappop(heap)
            for actual_weight, actual_node in graph_map[node]:
                if actual_node == n:
                    if actual_node == k:
                        return weight
                    return weight+actual_weight
                heapq.heappush(heap, (weight+actual_weight, actual_node))
        return -1
