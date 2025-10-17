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

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:

    def get_length(node):
        length = 0
        while node:
            node = node.next
            length += 1
        return length

    def reverse(start, k):
        prev = None
        curr = start
        while k > 0:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            k -= 1
        return prev

    total_len = get_length(head)
    dummy = ListNode(0)
    dummy.next = head
    prev_group = dummy
    curr = head

    while total_len >= k:
        group_start = curr

        for _ in range(k):
            curr = curr.next

        new_head = reverse(group_start, k)
        prev_group.next = new_head
        group_start.next = curr
        prev_group = group_start
        total_len -= k

    return dummy.next


print("Problem #3 - Reverse Nodes in k-Group")
print("reverseKGroup([1,2,3,4,5], 2) → [2,1,4,3,5]")


from collections import Counter
from typing import List

def findSubstring(s: str, words: List[str]) -> List[int]:
    if not s or not words:
        return []
    
    word_len = len(words[0])
    total_len = word_len * len(words)
    word_count = Counter(words)
    n = len(s)
    result = []

    for i in range(word_len):
        left = i
        seen = Counter()
        count = 0

        for right in range(i, n - word_len + 1, word_len):
            word = s[right:right + word_len]
            if word in word_count:
                seen[word] += 1
                count += 1

                while seen[word] > word_count[word]:
                    left_word = s[left:left + word_len]
                    seen[left_word] -= 1
                    left += word_len
                    count -= 1

                if count == len(words):
                    result.append(left)
            else:
                seen.clear()
                count = 0
                left = right + word_len

    return result


print("Problem #4 - Substring with Concatenation of All Words")
print("findSubstring('barfoothefoobarman', ['foo','bar']) → [0,9]")


def longestValidParentheses(s: str) -> int:
    stack = [-1] 
    longest = 0

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                longest = max(longest, i - stack[-1])
    return longest


print("Problem #5 - Longest Valid Parentheses")
print("longestValidParentheses('(()') → 2")
print("longestValidParentheses(')()())') → 4")
print("longestValidParentheses('') → 0")



def solveSudoku(board: List[List[str]]) -> None:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empty = []

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.':
                empty.append((r, c))
            else:
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r // 3) * 3 + (c // 3)].add(val)

    def backtrack(i=0):
        if i == len(empty):
            return True

        r, c = empty[i]
        box_idx = (r // 3) * 3 + (c // 3)

        for num in map(str, range(1, 10)):
            if num not in rows[r] and num not in cols[c] and num not in boxes[box_idx]:
                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_idx].add(num)

                if backtrack(i + 1):
                    return True

                board[r][c] = '.'
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[box_idx].remove(num)

        return False

    backtrack()


print("Problem #6 - Sudoku Solver")
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
solveSudoku(board)
for row in board:
    print(row)
