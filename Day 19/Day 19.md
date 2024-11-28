

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # 1. Append Method
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = self.tail = new_node
            new_node.next = new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node

    # 2. __str__ Method (String representation)
    def __str__(self):
        if not self.head:
            return "List is empty."
        nodes = []
        current = self.head
        while True:
            nodes.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        return " <-> ".join(nodes)

    # 3. Prepend Method
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = self.tail = new_node
            new_node.next = new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node

    # 4. Traverse Method
    def traverse(self):
        if not self.head:
            return
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()

    # 5. Reverse Traverse Method
    def reverse_traverse(self):
        if not self.head:
            return
        current = self.tail
        while current:
            print(current.data, end=" ")
            current = current.prev
            if current == self.tail:
                break
        print()

    # 6. Search Method
    def search(self, data):
        if not self.head:
            return None
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
            if current == self.head:
                break
        return None

    # 7. Get Method (by index)
    def get(self, index):
        if not self.head:
            return None
        current = self.head
        count = 0
        while current:
            if count == index:
                return current
            current = current.next
            count += 1
            if current == self.head:
                break
        return None

    # 8. Set Method (by index)
    def set(self, index, data):
        node = self.get(index)
        if node:
            node.data = data
        else:
            print("Index out of range")

    # 9. Insert Method (at index)
    def insert(self, index, data):
        if index == 0:
            self.prepend(data)
            return
        new_node = Node(data)
        current = self.head
        count = 0
        while current:
            if count == index - 1:
                new_node.next = current.next
                new_node.prev = current
                current.next.prev = new_node
                current.next = new_node
                if new_node.next == self.head:  # Adjust the tail if inserted at the end
                    self.tail = new_node
                return
            current = current.next
            count += 1
            if current == self.head:
                break
        print("Index out of range")

    # 10. Pop First Method
    def pop_first(self):
        if not self.head:
            return None
        if self.head == self.tail:  # Single node
            data = self.head.data
            self.head = self.tail = None
            return data
        data = self.head.data
        self.head = self.head.next
        self.tail.next = self.head
        self.head.prev = self.tail
        return data

    # 11. Pop Method (last node)
    def pop(self):
        if not self.head:
            return None
        if self.head == self.tail:  # Single node
            data = self.head.data
            self.head = self.tail = None
            return data
        data = self.tail.data
        self.tail = self.tail.prev
        self.tail.next = self.head
        self.head.prev = self.tail
        return data

    # 12. Remove Method (by value)
    def remove(self, data):
        if not self.head:
            return
        current = self.head
        while current:
            if current.data == data:
                if current == self.head:  # Remove the head
                    self.pop_first()
                elif current == self.tail:  # Remove the tail
                    self.pop()
                else:  # Remove from the middle
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next
            if current == self.head:
                break
        print("Node not found")

    # 13. Delete All Method
    def delete_all(self):
        self.head = self.tail = None

    # 14. Time and Space Complexity
    # Operations like append, prepend, insert, remove, and pop all take O(1) time and O(1) space,
    # except for methods like search and get, which require O(n) time complexity.
    # Space complexity is O(n) where n is the number of nodes in the list.
```

### Explanation of the Methods:

1. **Append**: Adds a new node at the end of the list.
2. **`__str__`**: Provides a string representation of the list for easy printing.
3. **Prepend**: Adds a new node at the beginning of the list.
4. **Traverse**: Traverses the list from head to tail and prints all node data.
5. **Reverse Traverse**: Traverses the list from tail to head and prints all node data.
6. **Search**: Searches for a node with a specific value and returns it.
7. **Get**: Retrieves a node at a given index.
8. **Set**: Sets the value of a node at a given index.
9. **Insert**: Inserts a node at a specific index.
10. **Pop First**: Removes the first node (head) of the list.
11. **Pop**: Removes the last node (tail) of the list.
12. **Remove**: Removes a node by value from the list.
13. **Delete All**: Deletes all nodes, clearing the list.
14. **Time and Space Complexity**: 
   - Time complexity for methods like `append`, `prepend`, `pop`, and `pop_first` is **O(1)**.
   - Time complexity for methods like `search`, `get`, and `remove` is **O(n)** since they may require traversing the entire list.
   - Space complexity is **O(n)**, where `n` is the number of nodes.

### Example Usage:

```python
# Create the circular doubly linked list
cdll = CircularDoublyLinkedList()

# Append data
cdll.append(10)
cdll.append(20)
cdll.append(30)

# Prepend data
cdll.prepend(5)

# Print list
print(cdll)  # Output: 5 <-> 10 <-> 20 <-> 30

# Traverse list
cdll.traverse()  # Output: 5 10 20 30

# Reverse traverse
cdll.reverse_traverse()  # Output: 30 20 10 5

# Search for a value
node = cdll.search(20)
if node:
    print(f"Found: {node.data}")  # Output: Found: 20

# Remove a value
cdll.remove(20)
print(cdll)  # Output: 5 <-> 10 <-> 30

# Pop the last node
cdll.pop()
print(cdll)  # Output: 5 <-> 10

# Delete all nodes
cdll.delete_all()
print(cdll)  # Output: List is empty.
