from functools import cache
from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employees = {e.id: e for e in employees}

        def dfs(id: int) -> int:
            e = employees[id]
            return e.importance + sum(dfs(sub) for sub in e.subordinates)

        return dfs(id)
