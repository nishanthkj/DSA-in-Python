A **Circular Doubly Linked List** is a data structure where:
- Each node points to the next and previous node.
- The last node points back to the first node, making it circular.

---

### **Constructor**
The constructor initializes the linked list:
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
```

---

### **Append Method**
Appends an element at the end of the CDLL:
```python
def append(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = new_node
        self.head.next = self.head
        self.head.prev = self.head
    else:
        tail = self.head.prev
        tail.next = new_node
        new_node.prev = tail
        new_node.next = self.head
        self.head.prev = new_node
```

---

### **`__str__` Method**
Defines the string representation of the CDLL:
```python
def __str__(self):
    if not self.head:
        return "[]"
    result = []
    current = self.head
    while True:
        result.append(current.data)
        current = current.next
        if current == self.head:
            break
    return " -> ".join(map(str, result))
```

---

### **Prepend Method**
Adds an element at the beginning:
```python
def prepend(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = new_node
        self.head.next = self.head
        self.head.prev = self.head
    else:
        tail = self.head.prev
        new_node.next = self.head
        new_node.prev = tail
        tail.next = new_node
        self.head.prev = new_node
        self.head = new_node
```

---

### **Traverse Method**
Traverses the list:
```python
def traverse(self):
    if not self.head:
        return
    current = self.head
    while True:
        print(current.data, end=" ")
        current = current.next
        if current == self.head:
            break
    print()
```

---

### **Reverse Traverse Method**
Traverses the list in reverse:
```python
def reverse_traverse(self):
    if not self.head:
        return
    current = self.head.prev
    while True:
        print(current.data, end=" ")
        current = current.prev
        if current.next == self.head:
            break
    print()
```

---

### **Search Method**
Searches for an element:
```python
def search(self, key):
    if not self.head:
        return False
    current = self.head
    while True:
        if current.data == key:
            return True
        current = current.next
        if current == self.head:
            break
    return False
```

---

### **Get Method**
Gets an element by index:
```python
def get(self, index):
    if not self.head:
        return None
    current = self.head
    count = 0
    while True:
        if count == index:
            return current.data
        current = current.next
        count += 1
        if current == self.head:
            break
    return None
```

---

### **Set Method**
Sets a value at a specific index:
```python
def set(self, index, data):
    if not self.head:
        return
    current = self.head
    count = 0
    while True:
        if count == index:
            current.data = data
            return
        current = current.next
        count += 1
        if current == self.head:
            break
```

---

### **Insert Method**
Inserts an element at a specific index:
```python
def insert(self, index, data):
    new_node = Node(data)
    if index == 0:
        self.prepend(data)
        return
    current = self.head
    count = 0
    while True:
        if count == index - 1:
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
            return
        current = current.next
        count += 1
        if current == self.head:
            break
```

---

### **Pop First Method**
Removes the first element:
```python
def pop_first(self):
    if not self.head:
        return
    if self.head.next == self.head:
        self.head = None
    else:
        tail = self.head.prev
        self.head = self.head.next
        self.head.prev = tail
        tail.next = self.head
```

---

### **Pop Method**
Removes the last element:
```python
def pop(self):
    if not self.head:
        return
    if self.head.next == self.head:
        self.head = None
    else:
        tail = self.head.prev
        new_tail = tail.prev
        new_tail.next = self.head
        self.head.prev = new_tail
```

---

### **Remove Method**
Removes an element by value:
```python
def remove(self, key):
    if not self.head:
        return
    current = self.head
    while True:
        if current.data == key:
            if current == self.head:
                self.pop_first()
            else:
                current.prev.next = current.next
                current.next.prev = current.prev
            return
        current = current.next
        if current == self.head:
            break
```

---

### **Delete All Method**
Deletes all nodes:
```python
def delete_all(self):
    self.head = None
```

---

### **Time and Space Complexity**
1. **Time Complexity**:
   - Append/Prepend: \(O(1)\)
   - Search/Remove: \(O(n)\)
   - Traverse: \(O(n)\)

2. **Space Complexity**:
   - Space for nodes: \(O(n)\)

