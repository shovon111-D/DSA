# Floyd's Cycle Detection Algorithm

> Also known as the **Tortoise and Hare** algorithm — detects whether a linked list contains a cycle in `O(n)` time and `O(1)` space.

## 📋 Overview

| Property | Value |
|---|---|
| **Time Complexity** | `O(n)` |
| **Space Complexity** | `O(1)` |
| **Technique** | Two-pointer (slow/fast) |

## 🔧 Implementation

```python
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
```

## 💡 How It Works

1. Two pointers start at `head`: `slow` (1 step/iter) and `fast` (2 steps/iter)
2. If a cycle exists, `fast` eventually laps `slow` → they meet → `True`
3. If no cycle, `fast` hits `None` → loop ends → `False`

## ▶️ Example Usage

```python
# No cycle: 1 -> 2 -> 3 -> None
n3 = ListNode(3)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
print(has_cycle(n1))  # False

# With cycle: 1 -> 2 -> 3 -> back to 2
n3.next = n2
print(has_cycle(n1))  # True

# Edge cases
print(has_cycle(None))        # False
single = ListNode(1)
single.next = single
print(has_cycle(single))      # True
```

## ⚖️ Why Not a Hash Set?

| Approach | Time | Space |
|---|---|---|
| Hash Set (visited nodes) | `O(n)` | `O(n)` |
| **Floyd's (this)** | `O(n)` | **`O(1)`** ✅ |