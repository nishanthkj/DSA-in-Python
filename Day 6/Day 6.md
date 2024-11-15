### 1. **Missing Number**
   - **Problem**: Given an array with `n` integers, each between `1` and `n+1`, find the missing number.
   - **Solution in Python**:
     ```python
     def missing_number(nums):
         n = len(nums)
         total_sum = (n + 1) * (n + 2) // 2  # Sum of numbers from 1 to n+1
         array_sum = sum(nums)  # Sum of elements in the given array
         return total_sum - array_sum
     ```
   - **Time Complexity**: O(n)
   - **Space Complexity**: O(1)

---

### 2. **Pairs / Two Sum (LeetCode 1)**
   - **Problem**: Find two indices such that their values add up to the target sum.
   - **Solution in Python**:
     ```python
     def two_sum(nums, target):
         hash_map = {}
         for i, num in enumerate(nums):
             complement = target - num
             if complement in hash_map:
                 return [hash_map[complement], i]
             hash_map[num] = i
         return []
     ```
   - **Time Complexity**: O(n)
   - **Space Complexity**: O(n)

---

### 3. **Finding a Number in an Array**
   - **Problem**: Check if a number exists in an array.
   - **Solution in Python**:
     ```python
     def find_number(nums, target):
         return target in nums
     # OR with linear search
     def linear_search(nums, target):
         for i, num in enumerate(nums):
             if num == target:
                 return i
         return -1  # Not found
     ```
   - **Time Complexity**: O(n)
   - **Space Complexity**: O(1) for `in` operator, O(n) for `linear_search`

---

### 4. **Max Product of Two Integers**
   - **Problem**: Given an array of integers, find the maximum product of any two distinct integers.
   - **Solution in Python**:
     ```python
     def max_product(nums):
         nums.sort()
         return max(nums[0] * nums[1], nums[-1] * nums[-2])
     ```
   - **Time Complexity**: O(n log n) due to sorting
   - **Space Complexity**: O(1) if modifying the array in place

---

### 5. **Middle Function (Linked List)**
   - **Problem**: Given a linked list, return the middle element.
   - **Solution in Python** (Two-pointer approach):
     ```python
     class ListNode:
         def __init__(self, val=0, next=None):
             self.val = val
             self.next = next

     def middle_of_linked_list(head):
         slow, fast = head, head
         while fast and fast.next:
             slow = slow.next
             fast = fast.next.next
         return slow
     ```
   - **Time Complexity**: O(n)
   - **Space Complexity**: O(1)

---

### 6. **2D Lists (Matrix)**
   - **Problem**: Operations on a 2D list, such as sum of rows, columns, etc.
   - **Solution in Python** (Basic 2D operations):
     ```python
     # Sum of all elements in the matrix
     def sum_matrix(matrix):
         return sum(sum(row) for row in matrix)

     # Sum of each row
     def sum_rows(matrix):
         return [sum(row) for row in matrix]

     # Sum of each column
     def sum_columns(matrix):
         return [sum(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0]))]
     ```
   - **Time Complexity**: O(n * m) where `n` is the number of rows and `m` is the number of columns.
   - **Space Complexity**: O(1) if not returning additional data structures.

---

### 7. **Best Score**
   - **Problem**: Given an array of scores, find the best (maximum) score.
   - **Solution in Python**:
     ```python
     def best_score(scores):
         return max(scores)
     ```

   - **Time Complexity**: O(n)
   - **Space Complexity**: O(1)

---

### 8. **Duplicate Number**
   - **Problem**: Given an array, find if there are any duplicates.
   - **Solution in Python**:
     ```python
     def contains_duplicate(nums):
         return len(nums) != len(set(nums))
     ```

   - **Time Complexity**: O(n)
   - **Space Complexity**: O(n)

---

### 9. **Pairs (Duplicate Values)**
   - **Problem**: Find all pairs in the array that sum up to a given target.
   - **Solution in Python**:
     ```python
     def two_sum_pairs(nums, target):
         seen = set()
         pairs = []
         for num in nums:
             complement = target - num
             if complement in seen:
                 pairs.append((complement, num))
             seen.add(num)
         return pairs
     ```

   - **Time Complexity**: O(n)
   - **Space Complexity**: O(n)

---

### 10. **Contains Duplicate**
   - **Problem**: Check if the array contains any duplicates.
   - **Solution in Python**:
     ```python
     def contains_duplicate(nums):
         return len(nums) != len(set(nums))
     ```

   - **Time Complexity**: O(n)
   - **Space Complexity**: O(n)

---

### 11. **Permutation**
   - **Problem**: Check if one string is a permutation of another (i.e., they contain the same characters in a different order).
   - **Solution in Python**:
     ```python
     def is_permutation(s1, s2):
         return sorted(s1) == sorted(s2)
     # OR using Counter from collections
     from collections import Counter
     def is_permutation(s1, s2):
         return Counter(s1) == Counter(s2)
     ```

   - **Time Complexity**: O(n log n) due to sorting or O(n) with Counter
   - **Space Complexity**: O(n)

---

### 12. **Rotate Matrix / Image (LeetCode 48)**
   - **Problem**: Rotate an `n x n` matrix 90 degrees clockwise.
   - **Solution in Python**:
     ```python
     def rotate_matrix(matrix):
         n = len(matrix)
         for i in range(n // 2):
             for j in range(i, n - i - 1):
                 temp = matrix[i][j]
                 matrix[i][j] = matrix[n - j - 1][i]
                 matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                 matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                 matrix[j][n - i - 1] = temp
     ```

   - **Time Complexity**: O(n^2) where `n` is the number of rows or columns.
   - **Space Complexity**: O(1) if the rotation is done in-place.

---

