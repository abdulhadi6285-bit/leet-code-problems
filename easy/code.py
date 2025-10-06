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