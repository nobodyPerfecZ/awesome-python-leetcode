from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def hammingweight(self, gene1: str, gene2: str) -> int:
        weight = 0
        for s1, s2 in zip(gene1, gene2, strict=True):
            if s1 != s2:
                weight += 1
        return weight

    def neighbors(self, gene: str, bank: List[str]) -> List[str]:
        return [gene2 for gene2 in bank if self.hammingweight(gene, gene2) == 1]

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        """
        A gene string can be represented by an 8-character long string, with choices
        from 'A', 'C', 'G', and 'T'.

        Suppose we need to investigate a mutation from a gene string startGene to a gene
        string endGene where one mutation is defined as one single character changed in
        the gene string.

        For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
        There is also a gene bank bank that records all the valid gene mutations. A
        gene must be in bank to make it a valid gene string.

        Given the two gene strings startGene and endGene and the gene bank bank, return
        the minimum number of mutations needed to mutate from startGene to endGene. If
        there is no such a mutation, return -1.

        Note that the starting point is assumed to be valid, so it might not be included
        in the bank.
        """

        def bfs(src, target):
            queue = [(src, 0)]
            visited = {src}
            while queue:
                gene, mutations = queue.pop(0)
                if gene == target:
                    return mutations
                for next_gene in self.neighbors(gene, bank):
                    if next_gene not in visited:
                        queue.append((next_gene, mutations + 1))
                        visited.add(next_gene)
            return -1

        return bfs(startGene, endGene)
