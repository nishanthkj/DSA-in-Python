### **Binary Heap Overview**

A **binary heap** is a complete binary tree that satisfies the **heap property**:
1. **Max-Heap Property**: The value of each parent node is greater than or equal to its children.
2. **Min-Heap Property**: The value of each parent node is less than or equal to its children.

### **Why Do We Need Binary Heap?**
1. **Efficient Priority Queue**: Binary heaps are used to implement priority queues, where you need efficient access to the largest (max-heap) or smallest (min-heap) element.
2. **Heap Sort**: Binary heaps are a core component of the heap sort algorithm, which provides O(n log n) sorting.
3. **Graph Algorithms**: Used in algorithms like Dijkstra's shortest path and Prim's minimum spanning tree for efficient priority queue operations.
4. **Dynamic Median**: Helps in efficiently finding the median in a dynamic data set using two heaps.

---

### **Common Operations on Binary Heap**
1. **Creation**: Building a binary heap from an array.
2. **Peek**: Access the maximum (or minimum) element, depending on the heap type.
3. **Size of Heap**: Retrieve the number of elements in the heap.

---

### **Insertion in Binary Heap**
When inserting a new node into a binary heap:
1. Add the node at the next available position to maintain the complete tree property.
2. **Heapify-Up**: Compare the new node with its parent and swap if necessary to maintain the heap property. Repeat until the heap property is restored.

---

### **Extract Node from Binary Heap**
To extract the maximum (or minimum) element:
1. Remove the root node (max or min element).
2. Replace it with the last element in the heap.
3. **Heapify-Down**: Compare the new root with its children and swap if necessary to maintain the heap property. Repeat until the heap property is restored.

---

### **Delete Entire Binary Heap**
To delete a binary heap:
1. Simply clear all elements in the array (used to represent the heap) or set the heap size to 0.

---

### **Time and Space Complexity**

1. **Creation**:  
   - **Time**: O(n) using heapify (building a heap from an array).
   - **Space**: O(1) additional space (in-place heap construction).

2. **Peek (Get Maximum/Minimum)**:  
   - **Time**: O(1).

3. **Insert**:  
   - **Time**: O(log n) for heapify-up.
   - **Space**: O(1).

4. **Extract (Delete Max/Min)**:  
   - **Time**: O(log n) for heapify-down.
   - **Space**: O(1).

5. **Delete Entire Heap**:  
   - **Time**: O(1) to clear the array or reset the size.
   - **Space**: O(1).

6. **Space Complexity of Binary Heap**:  
   - **Overall Space**: O(n), where n is the number of elements.

---

### **Python Implementation Notes**

Here’s a quick example of basic binary heap operations in Python:

```python
import heapq

# Min-Heap by default
heap = []

# Insert elements
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
heapq.heappush(heap, 5)

# Peek at the smallest element
print("Smallest element:", heap[0])

# Extract the smallest element
print("Extracted element:", heapq.heappop(heap))

# Convert list to heap (heapify)
data = [3, 1, 4, 1, 5, 9]
heapq.heapify(data)
print("Heapified data:", data)
```