class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i : [] for i in range(numCourses)}
        for c, pre in prerequisites:
            premap[c].append(pre)

        visitSet = set()
        def dfs(c):
            if c in visitSet:
                return False
            if premap[c] == []:
                return True
            visitSet.add(c)
            for pre in premap[c]:
                if not dfs(pre): return False
            visitSet.remove(c)
            premap[c] = []
            return True
        for c in range(numCourses):
            if not dfs(c): return False
        return True