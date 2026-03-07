# Intuition
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create an iterable variable
        i = 0               
        # create a variable to hold the node's value
        current = head
        # iterate through the ListNode to get it's length
        while current:
            i += 1
            current = current.next
        # get the middle number, rounded down
        i = i // 2
        # create a varible to hold the answer
        answer = head
        # iterate through the list to get the middle node
        while i > 0:
            i -= 1
            answer = answer.next
        return answer

# Optimized Solution
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # Return head if it is only member of ListNode
        if not head or not head.next:
            return head
        # Set two pointers to track middle and last member
        slow, fast = head, head
        # iterate through ListNode, with slow moving by 1 and fast by two
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
