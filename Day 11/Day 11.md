### 1. **Sum and Product**

```python
def sum_and_product(arr):
    total_sum = 0
    total_product = 1
    for num in arr:
        total_sum += num
        total_product *= num
    return total_sum, total_product
```

- **Time Complexity**: O(n) because we iterate through the array once.
- **Space Complexity**: O(1), since we are using only a constant amount of extra space.

---

### 2. **Elementwise Sum**

```python
def elementwise_sum(arr1, arr2):
    return [a + b for a, b in zip(arr1, arr2)]
```

- **Time Complexity**: O(n), where n is the length of the arrays, since we iterate through both arrays once.
- **Space Complexity**: O(n) because we are creating a new list to store the result.

---

### 3. **Insert at the Beginning**

```python
def insert_at_beginning(arr, value):
    return [value] + arr
```

- **Time Complexity**: O(n), because inserting at the beginning requires shifting all existing elements.
- **Space Complexity**: O(n), as we are creating a new array to store the result.

---

### 4. **Concatenate**

```python
def concatenate(arr1, arr2):
    return arr1 + arr2
```

- **Time Complexity**: O(n + m), where n is the size of `arr1` and m is the size of `arr2`, because both arrays need to be copied.
- **Space Complexity**: O(n + m), as we are creating a new array to store the concatenated result.

---

### 5. **Diagonal**

```python
def diagonal(matrix):
    return [matrix[i][i] for i in range(len(matrix))]
```

- **Time Complexity**: O(n), where n is the size of the matrix (n x n), because we are iterating once through the diagonal.
- **Space Complexity**: O(n), since we are storing the diagonal elements in a new list.

---

### 6. **Common Elements**

```python
def common_elements(arr1, arr2):
    return list(set(arr1) & set(arr2))
```

- **Time Complexity**: O(n + m), where n and m are the lengths of the two arrays. Converting arrays to sets takes O(n) and O(m) time, and the intersection operation takes O(min(n, m)) time.
- **Space Complexity**: O(n + m), because we create two sets to store the unique elements of each array.

---

### Summary of Time and Space Complexity:

1. **Sum and Product**:
   - **Time Complexity**: O(n)
   - **Space Complexity**: O(1)

2. **Elementwise Sum**:
   - **Time Complexity**: O(n)
   - **Space Complexity**: O(n)

3. **Insert at the Beginning**:
   - **Time Complexity**: O(n)
   - **Space Complexity**: O(n)

4. **Concatenate**:
   - **Time Complexity**: O(n + m)
   - **Space Complexity**: O(n + m)

5. **Diagonal**:
   - **Time Complexity**: O(n)
   - **Space Complexity**: O(n)

6. **Common Elements**:
   - **Time Complexity**: O(n + m)
   - **Space Complexity**: O(n + m)

