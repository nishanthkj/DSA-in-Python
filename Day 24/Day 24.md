### Recursion: An Overview
**Recursion** is a programming technique where a function calls itself to solve smaller instances of the same problem until it reaches a base case (the stopping condition). It's often used for problems that can be broken down into similar subproblems.

---

### Why Do We Need Recursion?
- Simplifies code for problems involving repetitive substructures (e.g., tree traversals, factorial calculation, Fibonacci sequence).
- Enables divide-and-conquer strategies (e.g., quicksort, mergesort).
- Useful for solving problems with branching structures (e.g., graph traversal, dynamic programming).

---

### How Recursion Works?
- **Base Case**: The condition under which recursion stops to prevent infinite loops.
- **Recursive Case**: The part of the function where the function calls itself with modified parameters.
- Stack Memory: Each recursive call is stored in the call stack, waiting for the base case to return results back up the stack.

Example: Factorial Calculation
```python
def factorial(n):
    if n == 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case
```

---

### Recursive vs Iterative Solutions
- **Recursive**
  - Elegant for problems with natural recursive definitions.
  - May cause stack overflow for deep recursion.
  - Uses more memory due to stack calls.
- **Iterative**
  - More efficient in terms of memory.
  - Often harder to write for problems naturally suited to recursion.

---

### When to Use/Avoid Recursion?
- **Use**
  - Divide-and-conquer problems (e.g., sorting, searching).
  - Problems with branching or hierarchical structures.
  - Problems naturally defined recursively.
- **Avoid**
  - When recursion depth exceeds the system's stack size.
  - When an iterative solution is more efficient.

---

### How to Write Recursion in 3 Steps?
1. **Define the Base Case**: Identify when the recursion should stop.
2. **Define the Recursive Case**: Determine how the problem can be divided.
3. **Combine the Results**: Merge the outputs of smaller subproblems.

Example: Sum of Array
```python
def sum_array(arr):
    if len(arr) == 0:  # Base case
        return 0
    return arr[0] + sum_array(arr[1:])  # Recursive case
```

---

### Fibonacci Numbers Using Recursion
**Fibonacci Series**: Each number is the sum of the two preceding ones.
```python
def fibonacci(n):
    if n <= 1:  # Base cases
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case
```

---

### Time Complexity for Recursive Calls
- Calculate the number of recursive calls.
- Evaluate the work done per call.
- Combine the two to find total time complexity.

Example: Fibonacci Recursive Complexity
- Recurrence relation: \( T(n) = T(n-1) + T(n-2) + O(1) \)
- Time Complexity: \( O(2^n) \)

---

### Measuring Recursive Algorithms with Multiple Calls
- Use a recurrence tree to visualize recursive calls.
- Calculate the depth of the tree and the number of nodes.
- Example: Merge Sort
  - Recurrence Relation: \( T(n) = 2T(n/2) + O(n) \)
  - Time Complexity: \( O(n \log n) \)

--- 

### Python Notes for Recursion
1. **Recursion Depth Limit**: Use `sys.setrecursionlimit()` to change the default recursion limit.
2. **Memoization**: Use `functools.lru_cache` to optimize recursive calls.
   ```python
   from functools import lru_cache

   @lru_cache(maxsize=None)
   def fibonacci(n):
       if n <= 1:
           return n
       return fibonacci(n - 1) + fibonacci(n - 2)
   ```
3. **Tail Recursion**: Python doesn’t optimize tail recursion, so deep recursion can still cause stack overflow.