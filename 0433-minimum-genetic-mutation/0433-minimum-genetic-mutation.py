class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def bfs(gene, endGene):
            queue = []
            visited = set()
            if endGene not in bank:
                return -1
            queue.append((gene,0))
            visited.add(gene)
            while queue:
                actual_gene, ix = queue.pop(0)
                if actual_gene == endGene:
                    return ix
                if actual_gene in bank or ix == 0:
                    for c in "ACGT":
                        for i in range(len(actual_gene)):
                            new_gene = actual_gene[0:i]+c+actual_gene[i+1:]
                            if new_gene in bank and new_gene not in visited:
                                queue.append((new_gene, ix+1))
                                visited.add(new_gene)
            return -1
        return bfs(startGene, endGene)
                