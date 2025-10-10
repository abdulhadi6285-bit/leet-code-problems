from typing import Optional
from typing import List

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


def convert(s: str, numRows: int) -> str:
    if numRows == 1 or len(s) <= numRows:
        return s

    result = [''] * numRows
    index = 0
    step = 1

    for char in s:
        result[index] += char
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
        index += step
    return ''.join(result)


print("Problem #4 - ZigZagConversion")
print("convert('PAYPALISHIRING', 3)? ", convert("PAYPALISHIRING", 3))
print("convert('PAYPALISHIRING', 4)? ", convert("PAYPALISHIRING", 4))
print("convert('A', 1)? ", convert("A", 1))
print("convert('HELLO', 2)? ", convert("HELLO", 2))

def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1
    x = abs(x)

    result = 0
    while x != 0:
        digit = x % 10
        x //= 10
        result = result * 10 + digit

    result *= sign

    if result < -2**31 or result > 2**31 - 1:
        return 0
    return result


print("Problem #5 - reverse integer")
print("reverse(123)? ", reverse(123))
print("reverse(-123)? ", reverse(-123))
print("reverse(120)? ", reverse(120))
print("reverse(0)? ", reverse(0))
print("reverse(1534236469)? ", reverse(1534236469))


def myAtoi(s: str) -> int:
    s = s.strip()

    if not s:
        return 0

    sign = 1
    result = 0

    if s[0] == '-' or s[0] == '+':
        if s[0] == '-':
            sign = -1
        s = s[1:]

    for char in s:
        if not char.isdigit():
            break
        result = result * 10 + int(char)

    result *= sign

    if result < -2**31:
        return -2**31
    if result > 2**31 - 1:
        return 2**31 - 1

    return result


print("Problem #6 - String To Integer?")
print("myAtoi('42')? ", myAtoi("42"))
print("myAtoi('   -42')? ", myAtoi("   -42"))
print("myAtoi('4193 with words')? ", myAtoi("4193 with words"))
print("myAtoi('words and 987')? ", myAtoi("words and 987"))
print("myAtoi('-91283472332')? ", myAtoi("-91283472332"))


def maxArea(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


print("Problem #7 - Container With Most Water")
print("maxArea([1,8,6,2,5,4,8,3,7]) →", maxArea([1,8,6,2,5,4,8,3,7]))
print("maxArea([1,1]) →", maxArea([1,1]))
print("maxArea([4,3,2,1,4]) →", maxArea([4,3,2,1,4]))
print("maxArea([1,2,1]) →", maxArea([1,2,1]))