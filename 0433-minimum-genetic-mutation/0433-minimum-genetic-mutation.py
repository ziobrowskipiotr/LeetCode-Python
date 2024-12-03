class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = []
        visited = set()
        if endGene not in bank:
            return -1
        queue.append((startGene,0))
        visited.add(startGene)
        while queue:
            actual_gene, ix = queue.pop(0)
            if actual_gene == endGene:
                return ix
            for c in "ACGT":
                for i in range(len(actual_gene)):
                    new_gene = actual_gene[0:i]+c+actual_gene[i+1:]
                    if new_gene in bank and new_gene not in visited:
                        queue.append((new_gene, ix+1))
                        visited.add(new_gene)
        return -1
                