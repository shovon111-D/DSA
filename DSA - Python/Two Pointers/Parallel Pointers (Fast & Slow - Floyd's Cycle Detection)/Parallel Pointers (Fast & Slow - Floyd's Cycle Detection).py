class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: ListNode | None) -> bool:
    """Detect if a linked list contains a cycle."""
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


# --- Example 1: No cycle ---
# 1 -> 2 -> 3 -> None
n3 = ListNode(3)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

print(has_cycle(n1))  # False


# --- Example 2: With a cycle ---
# 1 -> 2 -> 3 -> back to 2 (cycle)
n3 = ListNode(3)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
n3.next = n2  # creates the cycle

print(has_cycle(n1))  # True


# --- Example 3: Empty list ---
print(has_cycle(None))  # False


# --- Example 4: Single node, self-loop ---
single = ListNode(1)
single.next = single

print(has_cycle(single))  # True