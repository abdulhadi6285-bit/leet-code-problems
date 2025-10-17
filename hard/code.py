def isMatch(s: str, p: str) -> bool:
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True 

    for j in range(2, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]
                if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
    return dp[len(s)][len(p)]


print("Problem #1 - Regular Expression Matching")
print(f"isMatch('aa', 'a') → {isMatch('aa', 'a')}")
print(f"isMatch('aa', 'a*') → {isMatch('aa', 'a*')}")
print(f"isMatch('ab', '.*') → {isMatch('ab', '.*')}")
print(f"isMatch('aab', 'c*a*b') → {isMatch('aab', 'c*a*b')}")
print(f"isMatch('mississippi', 'mis*is*p*.') → {isMatch('mississippi', 'mis*is*p*.')}")


import heapq
from typing import List, Optional

# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    
    dummy = ListNode(0)
    curr = dummy
    
    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next


print("Problem #2 - Merge k Sorted Lists")
print("mergeKLists([[1,4,5],[1,3,4],[2,6]]) → [1,1,2,3,4,4,5,6]")
