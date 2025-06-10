# Problem Statement: Given a singly linked list, find and return its middle node.
# If there are 2 middle nodes, return the second one

from linked_list_loop import ListNode

def find_midpoint(head: ListNode) -> ListNode:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow