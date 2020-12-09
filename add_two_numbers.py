# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ''
        while (l1 != None):
            num1 += str(l1.val)
            l1 = l1.next
        num1 = int(''.join(reversed(num1)))
        num2 = ''
        while (l2 != None):
            num2 += str(l2.val)
            l2 = l2.next
        num2 = int(''.join(reversed(num2)))
        num_sum = str(num1 + num2)
        num_sum = ''.join(reversed(num_sum))
        num_sum = list(num_sum)
        for x in range(len(num_sum)):
            num_sum[x] = int(num_sum[x])
        print(list(num_sum))
