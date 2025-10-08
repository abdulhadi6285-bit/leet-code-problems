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


print("Problem #6 - removeDuplicates?")
nums1 = [1, 1, 2]
k1 = removeDuplicates(nums1)
print("removeDuplicates([1,1,2])? -> k =", k1, ", nums =", nums1[:k1])

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = removeDuplicates(nums2)
print("removeDuplicates([0,0,1,1,1,2,2,3,3,4])? -> k =", k2, ", nums =", nums2[:k2])




def removeElement(nums: List[int], val: int) -> int:
    k = 0  
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


print("Problem #7 - removeElement?")
nums1 = [3, 2, 2, 3]
val1 = 3
k1 = removeElement(nums1, val1)
print(f"removeElement([3,2,2,3], 3)? -> k = {k1}, nums = {nums1[:k1]}")

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
k2 = removeElement(nums2, val2)
print(f"removeElement([0,1,2,2,3,0,4,2], 2)? -> k = {k2}, nums = {nums2[:k2]}")


def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1


print("Problem #8 - Find the Index of the First Occurrence in a String")
print("strStr('sadbutsad', 'sad')? ", strStr("sadbutsad", "sad"))
print("strStr('leetcode', 'leeto')? ", strStr("leetcode", "leeto"))
print("strStr('hello', 'll')? ", strStr("hello", "ll"))
print("strStr('aaaaa', 'bba')? ", strStr("aaaaa", "bba"))


from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


print("Problem #9 - Search Insert Position")
print("searchInsert([1,3,5,6], 5)? ", searchInsert([1,3,5,6], 5))
print("searchInsert([1,3,5,6], 2)? ", searchInsert([1,3,5,6], 2))
print("searchInsert([1,3,5,6], 7)? ", searchInsert([1,3,5,6], 7))
print("searchInsert([1,3,5,6], 0)? ", searchInsert([1,3,5,6], 0))


def lengthOfLastWord(s: str) -> int:
    s = s.rstrip()
    words = s.split(" ")
    return len(words[-1])


print("Problem #10 - lengthOfLastWord?")
print("lengthOfLastWord('Hello World')? ", lengthOfLastWord("Hello World"))
print("lengthOfLastWord('   fly me   to   the moon  ')? ", lengthOfLastWord("   fly me   to   the moon  "))
print("lengthOfLastWord('luffy is still joyboy')? ", lengthOfLastWord("luffy is still joyboy"))


def plusOne(digits: list[int]) -> list[int]:
    n = len(digits)
    
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0 
    
    return [1] + digits


print("Problem #11 - plusOne?")
print("plusOne([1, 2, 3])? ", plusOne([1, 2, 3]))
print("plusOne([4, 3, 2, 1])? ", plusOne([4, 3, 2, 1]))
print("plusOne([9])? ", plusOne([9]))
print("plusOne([9, 9, 9])? ", plusOne([9, 9, 9]))

def addBinary(a: str, b: str) -> str:
    binary_str1 = a
    binary_str2 = b

    int1 = int(binary_str1, 2)
    int2 = int(binary_str2, 2)

    sum_result = int1 + int2
    binary_sum = bin(sum_result)
    binary_sum_clean = binary_sum[2:]
    return binary_sum_clean


print("Problem #12 - addBinary?")
print("addBinary('11', '1')? ", addBinary('11', '1'))
print("addBinary('1010', '1011')? ", addBinary('1010', '1011'))
print("addBinary('0', '0')? ", addBinary('0', '0'))
print("addBinary('111', '1')? ", addBinary('111', '1'))


def mySqrt(x: int) -> int:
    if x < 2:
        return x
    
    left, right = 1, x // 2
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right


print("Problem #13 - mySqrtx")
print("mySqrt(4)? ", mySqrt(4))
print("mySqrt(8)? ", mySqrt(8))
print("mySqrt(0)? ", mySqrt(0))
print("mySqrt(1)? ", mySqrt(1))
print("mySqrt(25)? ", mySqrt(25))
