
### 1. **Create Simple Singly Linked List DS**
First, let's create the basic **Singly Linked List** data structure, which will include a Node class and a LinkedList class to manage the nodes.

```python
class Node:
    def __init__(self, value):
        self.value = value  # Value of the node
        self.next = None  # Pointer to the next node

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initialize an empty list

    # Method to print the list
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Example usage
sll = SinglyLinkedList()
sll.print_list()  # Should print: None (empty list)
```

### 2. **Insertion at the Beginning of a Singly Linked List**
To insert an element at the beginning of the list, you need to update the head of the list to point to the new node.

```python
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert a node at the beginning
    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head  # Point the new node to the current head
        self.head = new_node  # Update head to the new node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Example usage
sll = SinglyLinkedList()
sll.insert_at_beginning(10)
sll.insert_at_beginning(20)
sll.print_list()  # Should print: 20 -> 10 -> None
```

### 3. **Insertion at the End of a Singly Linked List**
To insert a node at the end of the list, you need to traverse the list until the last node and update its `next` to point to the new node.

```python
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert a node at the end
    def insert_at_end(self, value):
        new_node = Node(value)
        if not self.head:  # If the list is empty, make the new node the head
            self.head = new_node
            return
        last = self.head
        while last.next:  # Traverse to the last node
            last = last.next
        last.next = new_node  # Update the last node's next to the new node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Example usage
sll = SinglyLinkedList()
sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.print_list()  # Should print: 10 -> 20 -> 30 -> None
```

### 4. **Deletion from a Singly Linked List**
To delete a node, you need to adjust the `next` pointer of the previous node to skip the node you want to delete.

```python
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Delete a node with a given value
    def delete(self, value):
        current = self.head
        if current and current.value == value:  # If head needs to be removed
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.value != value:  # Traverse the list
            prev = current
            current = current.next

        if current is None:  # If the value wasn't found
            print(f"Value {value} not found.")
            return

        prev.next = current.next  # Remove the node from the list
        current = None

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Example usage
sll = SinglyLinkedList()
sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.delete(20)
sll.print_list()  # Should print: 10 -> 30 -> None
```

### 5. **Reverse a Singly Linked List**
Reversing a linked list involves re-pointing each node’s `next` pointer to its previous node.

```python
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Store next node
            current.next = prev  # Reverse the current node's pointer
            prev = current  # Move prev and current one step forward
            current = next_node
        self.head = prev  # Update the head to the new first node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Example usage
sll = SinglyLinkedList()
sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.reverse()
sll.print_list()  # Should print: 30 -> 20 -> 10 -> None
```

### 6. **Middle of a Singly Linked List**
To find the middle node, you can use the **Tortoise and Hare** algorithm, where one pointer moves two steps at a time and the other moves one step.

```python
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Find the middle of the linked list
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value if slow else None

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Example usage
sll = SinglyLinkedList()
sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.insert_at_end(40)
sll.insert_at_end(50)
print(f"Middle: {sll.find_middle()}")  # Should print: Middle: 30
```

### 7. **Remove Duplicates from a Singly Linked List**
To remove duplicates, you can use a set to keep track of values you've already seen.

```python
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Remove duplicates from the list
    def remove_duplicates(self):
        current = self.head
        seen = set()
        prev = None
        while current:
            if current.value in seen:
                prev.next = current.next  # Skip the current node
            else:
                seen.add(current.value)
                prev = current
            current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Example usage
sll = SinglyLinkedList()
sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.insert_at_end(30)
sll.remove_duplicates()
sll.print_list()  # Should print: 10 -> 20 -> 30 -> None
```

