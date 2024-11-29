

### **Linked List Class**
A class to represent a basic singly linked list.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return str(result)
```

---

### **Coding Exercise: Remove Duplicates**
Remove duplicate elements from an unsorted linked list.

```python
def remove_duplicates(self):
    if not self.head:
        return
    seen = set()
    current = self.head
    prev = None
    while current:
        if current.data in seen:
            prev.next = current.next
        else:
            seen.add(current.data)
            prev = current
        current = current.next
```

---

### **Solution to Remove Duplicates**
Using a `set` to track seen values ensures O(n) time complexity.

```python
def remove_duplicates_optimized(self):
    if not self.head:
        return
    seen = set()
    current = self.head
    seen.add(current.data)
    while current.next:
        if current.next.data in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.data)
            current = current.next
```

---

### **Return Kth to Last**
Find the k-th to last element in the linked list.

```python
def kth_to_last(self, k):
    slow = self.head
    fast = self.head
    for _ in range(k):
        if not fast:
            return None
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow.data if slow else None
```

---

### **Partition**
Partition the linked list around a value `x`, placing nodes less than `x` before nodes greater than or equal to `x`.

```python
def partition(self, x):
    before_head = before = Node(0)
    after_head = after = Node(0)
    current = self.head

    while current:
        if current.data < x:
            before.next = current
            before = before.next
        else:
            after.next = current
            after = after.next
        current = current.next

    after.next = None
    before.next = after_head.next
    self.head = before_head.next
```

---

### **Sum Linked Lists**
Sum two linked lists, where each node represents a digit in reverse order.

```python
def sum_linked_lists(l1, l2):
    dummy_head = Node(0)
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.data if l1 else 0
        val2 = l2.data if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        current.next = Node(total % 10)
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy_head.next
```

---

### **Intersection**
Find the node where two linked lists intersect.

```python
def find_intersection(headA, headB):
    if not headA or not headB:
        return None

    a, b = headA, headB

    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA

    return a
```

