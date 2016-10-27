class UnionFind(object):

    '''Implementation of Union Find (a.k.a. Disjoint Set) data structure,
    with 'union by rank' optimization.'''

    def __init__(self, n):
        self.leader = list(range(n))
        self.rank = [0 for i in range(n)]

    def find(self, elem):
        if elem != self.leader[elem]:
            self.leader[elem] = self.find(self.leader[elem])
        return self.leader[elem]

    def union(self, elem1, elem2):
        root1 = self.find(elem1)
        root2 = self.find(elem2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.leader[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.leader[root1] = root2
            else:
                self.leader[root2] = root1
                self.rank[root1] += 1
