# Problem Statement: Given a singly linked list, determine if it contains a cycle.
# A cycle occurs if a node's next pointer references an earlier node in the list, causing a loop.

class ListNode:
    def __init__(self, val:int, next: ListNode): # type: ignore
        self.val = val
        self.next = next


def detect_cycle(head: ListNode) -> bool:
    slow_ptr = fast_ptr = head
    # check both "fast_ptr" and "fast_ptr.next" to avoid null pointer exception
    while fast_ptr and fast_ptr.next:
        # move the pointer first and then compare
        # if compared first then output will always be True as slow_ptr = fast_ptr = head initially
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        if fast_ptr == slow_ptr:
            return True
    return False
