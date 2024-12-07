# Tree and Binary Tree Notes
## Tree
### Definition
A hierarchical data structure consisting of nodes:
- **Root**: The topmost node.
- **Child/Parent**: Nodes connected directly by edges.
- **Leaf**: A node with no children.
- **Height**: The number of edges from a node to the deepest leaf.
- **Depth**: The number of edges from the root to a node.

### Why Trees?
- Efficient for hierarchical data representation (e.g., file systems, organizational charts).
- Fast operations like searching, insertion, and deletion in balanced scenarios.

---

## Binary Tree
### Definition
A tree where each node has at most two children (left and right).

### Types of Binary Trees
- **Full Binary Tree**: Every node has 0 or 2 children.
- **Complete Binary Tree**: All levels are fully filled except possibly the last, which is filled from left to right.
- **Perfect Binary Tree**: All internal nodes have two children, and all leaves are at the same level.
- **Skewed Tree**: Nodes have only one child (left-skewed or right-skewed).

---

## Tree Representation
### Linked List Representation
- Each node is an object with attributes for value, left child, and right child.
- Example:
  ```python
  class Node:
      def __init__(self, value):
          self.value = value
          self.left = None
          self.right = None
