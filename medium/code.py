from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    res = dummy

    total = carry = 0

    while l1 or l2 or carry:
        total = carry

        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next

        num = total % 10
        carry = total // 10
        dummy.next = ListNode(num)
        dummy = dummy.next

    return res.next


print("Problem 1 - addTwoNumbers?")
print("addTwoNumbers([2,4,3], [5,6,4])? → [7,0,8]")
print("addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9])? → [8,9,9,9,0,0,0,1]")

def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


print("Problem #2 - LengthOfLongestSubstring")
print("lengthOfLongestSubstring('abcabcbb')? ", lengthOfLongestSubstring("abcabcbb"))
print("lengthOfLongestSubstring('bbbbb')? ", lengthOfLongestSubstring("bbbbb"))
print("lengthOfLongestSubstring('pwwkew')? ", lengthOfLongestSubstring("pwwkew"))
print("lengthOfLongestSubstring('dvdf')? ", lengthOfLongestSubstring("dvdf"))


def longestPalindrome(s: str) -> str:
    if len(s) <= 1:
        return s

    start, end = 0, 0

    def expand_from_center(left: int, right: int) -> tuple:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    for i in range(len(s)):
        l1, r1 = expand_from_center(i, i)
        l2, r2 = expand_from_center(i, i + 1)

        if r1 - l1 > end - start:
            start, end = l1, r1
        if r2 - l2 > end - start:
            start, end = l2, r2

    return s[start:end+1]


print("Problem #3 - longestPalindrome")
print("longestPalindrome('babad')? ", longestPalindrome("babad"))
print("longestPalindrome('cbbd')? ", longestPalindrome("cbbd"))
print("longestPalindrome('a')? ", longestPalindrome("a"))
print("longestPalindrome('ac')? ", longestPalindrome("ac"))
print("longestPalindrome('racecar')? ", longestPalindrome("racecar"))
