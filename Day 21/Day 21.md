**What is a Stack?**
- **Definition**: A stack is a linear data structure that follows the **LIFO (Last In, First Out)** principle. The last element added to the stack is the first one to be removed.
- **Examples**: Undo functionality in text editors, Backtracking in algorithms, Browser history.

---

**Stack Operations**
- **Primary Operations**:
  - **Push**: Add an element to the top of the stack.
  - **Pop**: Remove and return the top element of the stack.
  - **Peek/Top**: View the top element without removing it.
  - **isEmpty**: Check if the stack is empty.
  - **isFull**: Check if the stack is full (if size is limited).

---

**Create Stack using List without size limit**
```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if not self.isEmpty() else "Stack is empty"

    def peek(self):
        return self.stack[-1] if not self.isEmpty() else "Stack is empty"

    def isEmpty(self):
        return len(self.stack) == 0

    def delete(self):
        self.stack = []

# Example
stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())  # Output: 20
```

---

**NEW `__str__` Method**
- Use the `__str__` method to provide a string representation of the stack:
```python
class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return "Stack: " + str(self.stack)

stack = Stack()
stack.push(10)
stack.push(20)
print(stack)  # Output: Stack: [10, 20]
```

---

**Operations on Stack using List**
- Implementation with operations:
```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if not self.isEmpty() else "Stack is empty"

    def peek(self):
        return self.stack[-1] if not self.isEmpty() else "Stack is empty"

    def isEmpty(self):
        return len(self.stack) == 0

    def delete(self):
        self.stack = []
```

---

**Create Stack with Limit**
```python
class Stack:
    def __init__(self, limit):
        self.stack = []
        self.limit = limit

    def isFull(self):
        return len(self.stack) == self.limit

    def push(self, item):
        if self.isFull():
            return "Stack is full"
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if not self.isEmpty() else "Stack is empty"

    def peek(self):
        return self.stack[-1] if not self.isEmpty() else "Stack is empty"

    def isEmpty(self):
        return len(self.stack) == 0

    def delete(self):
        self.stack = []
```

---

**Create Stack using Linked List**
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.next
        return popped_node.data
```

---

**Linked List for Stack**
- A **linked list** allows dynamic size and efficient memory usage for stack implementation.

---

**Operations on Stack using Linked List**
```python
    def peek(self):
        return self.head.data if not self.isEmpty() else "Stack is empty"

    def delete(self):
        self.head = None
```

---

**Time and Space Complexity of Stack using Linked List**
- **Time Complexity**:
  - Push: \( O(1) \)
  - Pop: \( O(1) \)
  - Peek: \( O(1) \)
- **Space Complexity**:
  - Depends on the number of nodes. Dynamic allocation may use more memory compared to array-based stack.

---

**When to Use/Avoid Stack**
- **Use**:
  - Backtracking algorithms.
  - Function call management.
  - Parsing expressions.
- **Avoid**:
  - Random access of elements.
  - When non-linear traversal is needed.