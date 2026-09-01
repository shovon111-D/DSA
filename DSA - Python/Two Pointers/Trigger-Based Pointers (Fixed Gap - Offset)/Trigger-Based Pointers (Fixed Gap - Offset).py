def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:
    """Remove the N-th node from the end of a linked list in one pass."""
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy

    # Trigger phase: Advance fast pointer n + 1 steps ahead
    for _ in range(n + 1):
        fast = fast.next

    # Lockstep phase: Move both until fast reaches the end
    while fast:
        fast = fast.next
        slow = slow.next

    # Skip the nth node from the end
    slow.next = slow.next.next

    return dummy.next