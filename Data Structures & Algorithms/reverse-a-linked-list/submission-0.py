# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Iterative solution
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


        # Recursive solution
        # Base Case（终止条件）：如果队伍是空的，或者只剩一个人，就不用倒转了，直接交上去。
        #if not head or not head.next:
        #    return head

        # Recursive Step（递归交棒）：假设后面的队伍已经完美倒转好了
        #new_head = self.reverseList(head.next)

        # Post-processing（神奇的收尾）：把我自己接在新队伍的最后面
        #head.next.next = head
        #head.next = None

        #return new_head

