A **Doubly Linked List (DLL)** is a type of linked data structure where each node contains three components:  
1. **Data**: The actual data value of the node.  
2. **Next Pointer**: A reference to the next node in the list.  
3. **Previous Pointer**: A reference to the previous node in the list.  

This allows traversal in both forward and backward directions, unlike a singly linked list, which can only be traversed forward. DLLs are particularly useful in applications where both forward and backward navigation is required or when operations like insertion and deletion need to be performed more efficiently compared to singly linked lists.

### Node Class Constructor
Here is an example implementation of the Node class for a DLL in Python:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node
```

### Operations in a Doubly Linked List

1. **Append Method**  
   Adds a new node to the end of the list.

2. **Prepend Method**  
   Adds a new node at the beginning of the list.

3. **Traverse Method**  
   Iterates through the list from the head node to the last node.

4. **Reverse Traverse Method**  
   Iterates through the list from the last node to the head node.

5. **Search Method**  
   Searches for a node with a specific value in the list.

6. **Get Method**  
   Retrieves the value at a specific index in the list.

7. **Set Method**  
   Updates the value of a node at a specific index.

8. **Insert Method**  
   Inserts a new node at a specified index.

9. **Pop First Method**  
   Removes the first node of the list and returns its value.

10. **Pop Method**  
    Removes the last node of the list and returns its value.

11. **Remove Method**  
    Removes a node with a specific value from the list.

### Time and Space Complexity of a Doubly Linked List
- **Access**: \(O(n)\) — Traversing to a specific node requires iterating through the list.
- **Search**: \(O(n)\) — Requires traversal to find the desired node.
- **Insert/Delete at Head or Tail**: \(O(1)\) — Direct access via the head or tail pointer.
- **Insert/Delete at Arbitrary Position**: \(O(n)\) — Requires traversal to find the position.
- **Space Complexity**: \(O(n)\) — Each node requires extra space for the `prev` pointer.

