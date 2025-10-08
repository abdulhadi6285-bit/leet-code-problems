# Problem #1

# # 
# def twoSum(nums: List[int], target: int) -> List[int]:
#     seen = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in seen:
#             return [seen[complement], i]
#         seen[num] = i

print("Problem #1 - sum")
def sum(num1, num2):
  return num1 + num2

print("sum(1, 3) is: ",sum(1, 3))
print("--------------------")

def isPalindrome(x: int) -> bool:

    if x < 0:
        return False

    s = str(x)
    return s == s[::-1]

print("Problem #2 - isPalindrom?")
print("isPalindrome(121)? ", isPalindrome(121))
print("isPalindrome(223)? ", isPalindrome(223))

def romanToInt(s: str) -> int:
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    n = len(s)
    
    for i in range(n):
        if i + 1 < n and roman_map[s[i]] < roman_map[s[i + 1]]:
            total -= roman_map[s[i]]
        else:
            total += roman_map[s[i]]
    
    return total


print("Problem #3 - RomanToInteger?")
print("romanToInt('III')? ", romanToInt("III"))
print("romanToInt('LVIII')? ", romanToInt("LVIII"))
print("romanToInt('MCMXCIV')? ", romanToInt("MCMXCIV"))


from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix


print("Problem #4 - longestCommonPrefix?")
print("longestCommonPrefix(['flower', 'flow', 'flight'])? ", longestCommonPrefix(['flower', 'flow', 'flight']))
print("longestCommonPrefix(['dog', 'racecar', 'car'])? ", longestCommonPrefix(['dog', 'racecar', 'car']))


def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    
    return not stack


print("Problem #5 - isValidParenthesis?")
print("isValid('()')? ", isValid("()"))
print("isValid('()[]{}')? ", isValid("()[]{}"))
print("isValid('(]')? ", isValid("(]"))
print("isValid('([)]')? ", isValid("([)]"))
print("isValid('{[]}')? ", isValid("{[]}"))



def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0

    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1


print("Problem #7 - removeDuplicates?")
nums1 = [1, 1, 2]
k1 = removeDuplicates(nums1)
print("removeDuplicates([1,1,2])? -> k =", k1, ", nums =", nums1[:k1])

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = removeDuplicates(nums2)
print("removeDuplicates([0,0,1,1,1,2,2,3,3,4])? -> k =", k2, ", nums =", nums2[:k2])
