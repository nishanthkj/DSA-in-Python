

### **What is Queue?**
- **Queue** is a linear data structure that follows the **FIFO (First In, First Out)** principle.
- Common operations:
  - **Enqueue**: Add an element to the rear of the queue.
  - **Dequeue**: Remove an element from the front of the queue.
  - **Peek**: Retrieve the front element without removal.
  - **isEmpty**: Check if the queue is empty.
- **Applications**:
  - Task scheduling.
  - Breadth-First Search (BFS).
  - Managing data buffers.

---

### **Queue Using Python List (No Size Limit)**
- Python lists are dynamic and can be used to implement queues.
- Operations:
  - **Enqueue**: `list.append(element)`
  - **Dequeue**: `list.pop(0)` (inefficient due to shifting).
- Example:
```python
queue = []
queue.append(10)  # Enqueue
queue.append(20)
queue.pop(0)      # Dequeue
print(queue)      # Output: [20]
```

---

### **Queue Using Python List - Operations**
1. **Enqueue**: Add an element to the end.
2. **Dequeue**: Remove the element at the front.
3. **Peek**: View the front element without removing.
```python
queue = []
queue.append(10)  # Enqueue
queue.append(20)
print(queue[0])   # Peek: Output 10
queue.pop(0)      # Dequeue
```

---

### **Circular Queue Using Python List**
- **Circular Queue** optimizes memory usage by reusing empty spaces.
- Key idea: Use modulo operator to manage index wrapping.
```python
class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full!")
        elif self.front == -1:  # First element
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty!")
        else:
            temp = self.queue[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.size
            return temp
```

---

### **Circular Queue Operations**
1. **Enqueue**: Add an element.
2. **Dequeue**: Remove an element.
3. **Peek**: View the front element.
4. **Delete**: Clear the entire queue.

---

### **Queue Using Linked List**
- Avoids the size limitation of arrays.
- Stores elements dynamically as nodes in memory.
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if not self.rear:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front:
            print("Queue is empty!")
        else:
            temp = self.front
            self.front = self.front.next
            if not self.front:
                self.rear = None
            return temp.data
```

---

### **Queue Linked List Operations**
1. **Create**: Initialize `front` and `rear` pointers.
2. **Enqueue**: Add a new node at the rear.
3. **Dequeue**: Remove the front node.

---

### **Queue Linked List Other Operations**
1. **isEmpty**: Return `True` if the front pointer is `None`.
2. **Peek**: Access the front node without removal.

---

### **Time and Space Complexity**
| Operation     | List Queue (Dynamic) | Linked List Queue |
|---------------|-----------------------|-------------------|
| Enqueue       | \( O(1) \)           | \( O(1) \)        |
| Dequeue       | \( O(n) \) (shifting)| \( O(1) \)        |
| Space Usage   | \( O(n) \)           | \( O(n) \)        |

---

### **List vs Linked List Implementation**
| Feature           | List                   | Linked List          |
|--------------------|------------------------|----------------------|
| **Size**          | Dynamic                | Unlimited            |
| **Efficiency**    | Dequeue is \( O(n) \)  | Dequeue is \( O(1) \)|
| **Memory Usage**  | Higher (shifting data) | Lower                |

---

### **Collections Module**
- The `deque` class in `collections` provides efficient queue functionality.
- **Advantages**: \( O(1) \) for append and pop operations.
```python
from collections import deque

queue = deque()
queue.append(10)    # Enqueue
queue.popleft()     # Dequeue
```

---

### **Queue Module**
- Provides thread-safe queue implementations.
- Types:
  - `Queue`: FIFO.
  - `LifoQueue`: LIFO (stack-like).
  - `PriorityQueue`: Based on priorities.

---

### **Multiprocessing Module**
- `multiprocessing.Queue` for inter-process communication.
- Used in parallel processing.

---

### **Removing Numbers in Python**
To remove numbers from a list, use these techniques:

1. **Remove First Occurrence**:
   ```python
   numbers = [1, 2, 3, 4, 3]
   numbers.remove(3)  # Removes the first occurrence
   print(numbers)  # Output: [1, 2, 4, 3]
   ```

2. **Remove All Occurrences**:
   ```python
   numbers = [1, 2, 3, 4, 3]
   numbers = [x for x in numbers if x != 3]
   print(numbers)  # Output: [1, 2, 4]
   ```

3. **Remove by Index**:
   ```python
   numbers = [1, 2, 3, 4]
   numbers.pop(2)  # Removes the number at index 2
   print(numbers)  # Output: [1, 2, 4]
   ```

4. **Clear All Numbers**:
   ```python
   numbers = [1, 2, 3, 4]
   numbers.clear()
   print(numbers)  # Output: []
   ```

