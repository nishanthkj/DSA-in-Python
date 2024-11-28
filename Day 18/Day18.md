
---

### Circular Doubly Linked List (CDLL) Notes

#### 1. **Constructor**
A constructor to initialize a CDLL.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
```

---

#### 2. **Append Method**
Adds a new node at the end of the list.

```python
def append(self, value):
    new_node = Node(value)
    if not self.head:
        self.head = self.tail = new_node
        self.head.next = self.head.prev = new_node
    else:
        new_node.prev = self.tail
        new_node.next = self.head
        self.tail.next = new_node
        self.head.prev = new_node
        self.tail = new_node
```

---

#### 3. **`__str__` Method**
For printing the list in a readable format.

```python
def __str__(self):
    if not self.head:
        return "List is empty"
    nodes = []
    current = self.head
    while True:
        nodes.append(str(current.value))
        current = current.next
        if current == self.head:
            break
    return " <-> ".join(nodes)
```

---

#### 4. **Prepend Method**
Adds a new node at the beginning of the list.

```python
def prepend(self, value):
    new_node = Node(value)
    if not self.head:
        self.head = self.tail = new_node
        self.head.next = self.head.prev = new_node
    else:
        new_node.next = self.head
        new_node.prev = self.tail
        self.head.prev = new_node
        self.tail.next = new_node
        self.head = new_node
```

---

#### 5. **Traverse Method**
Traverses the list in the forward direction.

```python
def traverse(self):
    if not self.head:
        return
    current = self.head
    while True:
        print(current.value, end=" ")
        current = current.next
        if current == self.head:
            break
```

---

#### 6. **Reverse Traverse Method**
Traverses the list in the reverse direction.

```python
def reverse_traverse(self):
    if not self.tail:
        return
    current = self.tail
    while True:
        print(current.value, end=" ")
        current = current.prev
        if current == self.tail:
            break
```

---

#### 7. **Search Method**
Finds a node by its value.

```python
def search(self, value):
    if not self.head:
        return False
    current = self.head
    while True:
        if current.value == value:
            return True
        current = current.next
        if current == self.head:
            break
    return False
```

---

#### 8. **Get Method**
Retrieves a node at a specific index.

```python
def get(self, index):
    if not self.head:
        return None
    current = self.head
    count = 0
    while True:
        if count == index:
            return current
        current = current.next
        count += 1
        if current == self.head:
            break
    return None
```

---

#### 9. **Set Method**
Updates the value of a node at a specific index.

```python
def set(self, index, value):
    node = self.get(index)
    if node:
        node.value = value
        return True
    return False
```

---

#### 10. **Insert Method**
Inserts a node at a specific index.

```python
def insert(self, index, value):
    if index == 0:
        self.prepend(value)
        return
    new_node = Node(value)
    prev_node = self.get(index - 1)
    if prev_node:
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next.prev = new_node
        prev_node.next = new_node
```

---

#### 11. **Pop First Method**
Removes the first node of the list.

```python
def pop_first(self):
    if not self.head:
        return None
    if self.head == self.tail:
        value = self.head.value
        self.head = self.tail = None
        return value
    value = self.head.value
    self.head = self.head.next
    self.head.prev = self.tail
    self.tail.next = self.head
    return value
```

---

#### 12. **Pop Method**
Removes the last node of the list.

```python
def pop(self):
    if not self.tail:
        return None
    if self.head == self.tail:
        value = self.tail.value
        self.head = self.tail = None
        return value
    value = self.tail.value
    self.tail = self.tail.prev
    self.tail.next = self.head
    self.head.prev = self.tail
    return value
```

---

#### 13. **Remove Method**
Removes a node by value.

```python
def remove(self, value):
    if not self.head:
        return
    current = self.head
    while True:
        if current.value == value:
            if current == self.head:
                self.pop_first()
            elif current == self.tail:
                self.pop()
            else:
                current.prev.next = current.next
                current.next.prev = current.prev
            return
        current = current.next
        if current == self.head:
            break
```

---

#### 14. **Delete All Method**
Deletes all nodes from the list.

```python
def delete_all(self):
    self.head = self.tail = None
```

---

#### 15. **Time and Space Complexity**
- **Time Complexity**:
  - Access/Search: O(n)
  - Insertion/Deletion: O(1) (at head or tail), O(n) (at specific index)
- **Space Complexity**: O(n) for storing nodes.

--- 

