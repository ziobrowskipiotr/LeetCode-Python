class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        map_nodes = collections.defaultdict(list)
        for i in range(len(equations)):
            map_nodes[equations[i][0]].append((equations[i][1], values[i]))
            map_nodes[equations[i][1]].append((equations[i][0], 1/values[i]))
        
        def bfs(source, target):
            if source not in map_nodes or target not in map_nodes:
                return -1
            queue, visited_set = [], set()
            queue.append([source, 1])

            while queue:
                n, w = queue.pop(0)
                if n == target:
                    return w
                for nex, val in map_nodes[n]:
                    if nex not in visited_set:
                        visited_set.add(nex)
                        queue.append([nex, w*val])

            return -1
        
        return [bfs(que[0], que[1]) for que in queries]

