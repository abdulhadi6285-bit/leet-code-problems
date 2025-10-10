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


print("Problem #16 - addTwoNumbers?")
print("addTwoNumbers([2,4,3], [5,6,4])? → [7,0,8]")
print("addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9])? → [8,9,9,9,0,0,0,1]")
