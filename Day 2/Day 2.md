### **Recursion: An Overview**

#### **What is Recursion?**
- **Definition:** Recursion is a method of solving a problem where the solution involves the function calling itself with a modified input.
- **Key Points:**
  - A problem is solved by breaking it down into smaller subproblems of the same type.
  - Every recursive function has a **base case** (a stopping condition), which prevents the function from calling itself indefinitely, avoiding an infinite loop.
  - The goal is to simplify the problem at each recursive call until it reaches the base case.

#### **Example of Recursion:**
```python
def openRussianDoll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        openRussianDoll(doll - 1)
```
- In this example, the function `openRussianDoll` keeps calling itself with a smaller input (`doll - 1`) until `doll == 1`, at which point the function stops.

#### **Why is Recursion Useful?**
1. **Problem Breakdown:** It helps break down complex problems into smaller, manageable subproblems. This is particularly useful for problems that can be divided into similar smaller subproblems.
2. **Used in Data Structures:** Recursion is common in data structures like trees and graphs, where a structure is recursively defined (e.g., a binary tree).
3. **Algorithms:** Recursion is used in several important algorithms like:
   - Divide and Conquer (e.g., Quick Sort, Merge Sort)
   - Dynamic Programming (e.g., Fibonacci sequence)
   - Greedy algorithms

#### **How Recursion Works?**
1. A function calls itself with modified arguments.
2. A **base case** is essential to avoid infinite recursion.
3. The **stack memory** stores function calls, meaning that each function call waits for the previous one to return before continuing execution.

#### **Example of Stack Memory in Recursion:**
```python
def recursiveMethod(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursiveMethod(n - 1)
        print(n)

recursiveMethod(3)
```
- The function `recursiveMethod(3)` calls `recursiveMethod(2)`, then `recursiveMethod(1)`, and finally prints the numbers in order as the recursive calls return.

#### **Recursive vs Iterative Solutions:**

| **Feature**            | **Recursion**                  | **Iteration**                  |
|------------------------|---------------------------------|--------------------------------|
| **Space Efficiency**    | No (uses stack memory)          | Yes                            |
| **Time Efficiency**     | No (more overhead with calls)   | Yes                            |
| **Ease of Coding**      | Yes (good for problems that can be divided into subproblems) | No                             |

**Example: Power of 2:**

- **Recursive version:**
  ```python
  def powerOfTwo(n):
      if n == 0:
          return 1
      else:
          return powerOfTwo(n-1) * 2
  ```
- **Iterative version:**
  ```python
  def powerOfTwoIt(n):
      power = 1
      for i in range(n):
          power *= 2
      return power
  ```

#### **When to Use or Avoid Recursion?**

- **When to Use Recursion:**
  1. When problems can be broken down into similar subproblems.
  2. When using **memoization** or **dynamic programming**.
  3. When traversing complex structures like trees (e.g., tree traversals).
  4. When you need a quick, simple solution (and can tolerate the extra time and space overhead).

- **When to Avoid Recursion:**
  1. When **space and time complexity** are critical, since recursion often uses more memory (due to stack usage) and may be slower.
  2. When working with limited memory environments (e.g., mobile devices with low memory).
  
#### **Writing Recursion in 3 Steps:**

1. **Define the Base Case:** The condition under which the recursion stops (e.g., `n == 0`).
2. **Define the Recursive Case:** The process that reduces the problem and calls the function again with a modified argument.
3. **Handle Invalid Input:** Ensure that the input is valid and can be handled by the recursive function.

#### **Factorial Example:**

Factorial is the product of all positive integers less than or equal to `n`, denoted as `n!`:

- Formula:  
  \( n! = n \times (n-1) \times (n-2) \times \dots \times 1 \)
- Example: \( 4! = 4 \times 3 \times 2 \times 1 = 24 \)

**Recursive implementation of Factorial:**
```python
def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be a positive integer!'
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
```

- Here, the base case is when `n == 0` or `n == 1`.
- The recursive case reduces the problem by calling `factorial(n - 1)`.

#### **Fibonacci Numbers Example:**

The Fibonacci sequence is defined as:
- \( f(0) = 0 \)
- \( f(1) = 1 \)
- \( f(n) = f(n-1) + f(n-2) \) for \( n > 1 \)

**Recursive Fibonacci Implementation:**
```python
def fibonacci(n):
    assert n >= 0 and int(n) == n, 'Fibonacci number cannot be negative or non-integer.'
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

This function calculates the Fibonacci sequence recursively by calling `fibonacci(n-1)` and `fibonacci(n-2)` until it reaches the base case.

---

### **Summary:**

- **Recursion** is a method of solving problems by breaking them into smaller subproblems, with the function calling itself.
- It is useful for problems that can be divided into smaller, similar problems (e.g., tree traversal, divide-and-conquer algorithms).
- Key components of recursion are:
  1. **Base Case**: The stopping condition for recursion.
  2. **Recursive Case**: The step that reduces the problem size.
- **Advantages**: Recursive solutions are often simpler to write, especially when dealing with problems that naturally break down into subproblems.
- **Disadvantages**: Recursion can use a lot of memory (due to the call stack) and might be slower due to the overhead of function calls. Iteration may be more space-efficient in such cases.

