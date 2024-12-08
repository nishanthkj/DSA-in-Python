### What is a Tree?
A **Tree** is a hierarchical data structure consisting of nodes connected by edges. It is a non-linear data structure used to represent relationships and hierarchical data, such as a file system, organizational structure, or XML/HTML document.

**Key Characteristics**:
1. A tree has a root node (the topmost node).
2. Each node contains data and may have child nodes (connected via edges).
3. A tree does not contain cycles (no closed loops).

---

### Why Trees?
Trees are used for:
1. **Hierarchical Representation**: Represent data with parent-child relationships (e.g., file systems).
2. **Searching and Sorting**: Binary Search Trees (BSTs) provide efficient searching, insertion, and deletion.
3. **Traversal**: Allow for structured traversal methods (e.g., pre-order, in-order, post-order).
4. **Specialized Applications**:
   - Parsing expressions (expression trees).
   - Representing decision-making processes (decision trees).
   - Memory management (heap trees).

---

### Tree Terminology
1. **Node**: An element of the tree containing data and references to child nodes.
2. **Root**: The topmost node in a tree.
3. **Parent**: A node that has child nodes.
4. **Child**: A node connected to a parent node.
5. **Leaf**: A node without any children.
6. **Edge**: A connection between two nodes.
7. **Height**: The longest path from the root to a leaf.
8. **Depth**: The distance from the root to a node.
9. **Subtree**: A tree formed by any node and its descendants.
10. **Degree**: The number of children a node has.

---

### Basic Tree Implementation in Python
Here’s an implementation of a simple tree:

```python
class TreeNode:
    """Class representing a node in a tree."""
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        """Add a child to the current node."""
        self.children.append(child_node)

    def __str__(self, level=0):
        """String representation of the tree."""
        result = " " * level * 4 + str(self.data) + "\n"
        for child in self.children:
            result += child.__str__(level + 1)
        return result


# Example Usage
if __name__ == "__main__":
    root = TreeNode("Root")
    child1 = TreeNode("Child 1")
    child2 = TreeNode("Child 2")
    child1.add_child(TreeNode("Child 1.1"))
    child1.add_child(TreeNode("Child 1.2"))
    child2.add_child(TreeNode("Child 2.1"))
    child2.add_child(TreeNode("Child 2.2"))

    root.add_child(child1)
    root.add_child(child2)

    print("Tree Structure:")
    print(root)
```

**Output**:
```
Root
    Child 1
        Child 1.1
        Child 1.2
    Child 2
        Child 2.1
        Child 2.2
```

---

### Binary Tree Representation (Python)
A **Binary Tree** is a tree where each node has at most two children: left and right.

#### Binary Tree Node Class
```python
class BinaryTreeNode:
    """Class representing a node in a binary tree."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

#### Example: Creating a Binary Tree
```python
# Create nodes
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)

print("Root Node:", root.data)
print("Left Child of Root:", root.left.data)
print("Right Child of Root:", root.right.data)
```

**Output**:
```
Root Node: 1
Left Child of Root: 2
Right Child of Root: 3
