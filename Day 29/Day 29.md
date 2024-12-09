### AVL Tree: Overview
An **AVL Tree** (Adelson-Velsky and Landis Tree) is a type of self-balancing binary search tree where the height difference (balance factor) between the left and right subtrees of any node is at most 1. This ensures that the tree remains approximately balanced, optimizing search, insert, and delete operations.

### Why AVL Tree?
- Ensures O(log n) time complexity for search, insertion, and deletion operations by maintaining balance.
- Useful in applications where frequent insertions and deletions occur, and the tree must remain balanced for efficient operations.

### Common Operations on AVL Trees
1. **Insertion**: Insert a node while maintaining balance using rotations.
2. **Deletion**: Delete a node and restore balance using rotations.
3. **Traversal**: In-order, pre-order, and post-order traversal methods can be applied.
4. **Rotations**: Used to maintain balance after insertions and deletions:
   - Left Rotation (LL)
   - Right Rotation (RR)
   - Left-Right Rotation (LR)
   - Right-Left Rotation (RL)

### Insert a Node in AVL
1. **Left Left Condition (LL)**: Single right rotation is used when the imbalance is due to the left subtree of the left child.
2. **Left Right Condition (LR)**: Double rotation (left, then right) is used when the imbalance is due to the right subtree of the left child.
3. **Right Right Condition (RR)**: Single left rotation is used when the imbalance is due to the right subtree of the right child.
4. **Right Left Condition (RL)**: Double rotation (right, then left) is used when the imbalance is due to the left subtree of the right child.

### Delete a Node from AVL
1. Identify the node to delete, adjust the tree structure, and apply rotations to restore balance.
2. Cases include handling LL, LR, RR, and RL imbalances.

### Time and Space Complexity
- **Time Complexity**:
  - Search, Insert, Delete: O(log n)
  - Traversal: O(n)
- **Space Complexity**:
  - O(n) due to the storage of nodes.

---

### Python Code Example for AVL Tree
Below is a basic implementation of an AVL tree with insert and rotate operations:

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalanceFactor(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def rotateRight(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rotateLeft(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalanceFactor(root)

        # LL
        if balance > 1 and key < root.left.key:
            return self.rotateRight(root)

        # RR
        if balance < -1 and key > root.right.key:
            return self.rotateLeft(root)

        # LR
        if balance > 1 and key > root.left.key:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)

        # RL
        if balance < -1 and key < root.right.key:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root

    def preOrder(self, root):
        if not root:
            return
        print(root.key, end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)

# Example Usage
tree = AVLTree()
root = None
keys = [10, 20, 30, 40, 50, 25]
for key in keys:
    root = tree.insert(root, key)

print("Pre-order traversal of AVL Tree:")
tree.preOrder(root)
```

Output:
```
Pre-order traversal of AVL Tree:
30 20 10 25 40 50
