### **Question 1: Sum and Product of Array**
```python
def foo(array):
    sum = 0
    product = 1
    for i in array:
        sum += i
    for i in array:
        product *= i
    print("Sum = "+str(sum)+", Product = "+str(product))
```
- **Time Complexity**:  
  - There are two separate loops that each iterate over the `array` once. The first loop calculates the sum (`O(n)`), and the second loop calculates the product (`O(n)`).
  - So, the total time complexity is `O(n) + O(n)` = **O(n)**, where `n` is the length of the array.
  
- **Space Complexity**:  
  - The space complexity is **O(1)** because you're only using a fixed number of extra variables (`sum`, `product`), regardless of the size of the input array.

### **Question 2: Print All Pairs**
```python
def printPairs(array):
    for i in array:
        for j in array:
            print(str(i)+","+str(j))
```
- **Time Complexity**:  
  - This code uses a nested loop, both of which iterate over the entire array. If the length of the array is `n`, the first loop runs `n` times, and for each iteration of the first loop, the second loop also runs `n` times.
  - So, the total time complexity is `O(n) * O(n)` = **O(n²)**.

- **Space Complexity**:  
  - The space complexity is **O(1)** because the function only uses a fixed number of variables (`i` and `j`), and the output is printed directly without needing extra space for storage.

### **Question 3: Print Unordered Pairs (No Duplicates)**
```python
def printUnorderedPairs(array):
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            print(array[i] + "," + array[j])
```
- **Time Complexity**:  
  - The outer loop runs `n` times (where `n` is the length of the array). The inner loop runs from `i + 1` to `n`, so it runs `n - i - 1` times.
  - The total number of iterations of the inner loop is the sum of the first `n-1` integers, which is approximately `n(n-1)/2`.
  - Hence, the total time complexity is **O(n²)**.

- **Space Complexity**:  
  - The space complexity is **O(1)**, because the function only uses a fixed number of variables (`i` and `j`).

### **Question 4: Print Unordered Pairs with Condition**
```python
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(str(arrayA[i]) + "," + str(arrayB[j]))

arrayA = [1, 2, 3, 4, 5]
arrayB = [2, 6, 7, 8]
```
- **Time Complexity**:  
  - The outer loop runs `n` times (where `n` is the length of `arrayA`), and the inner loop runs `m` times (where `m` is the length of `arrayB`).
  - The `if` condition inside the inner loop takes constant time, so the total time complexity is **O(n * m)**, where `n` is the length of `arrayA` and `m` is the length of `arrayB`.

- **Space Complexity**:  
  - The space complexity is **O(1)**, because only a constant amount of extra space is used (just a few variables for iteration and comparison).

### **Question 5: Print Unordered Pairs with Inner Loop (Inefficient)**
```python
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0, 100000):
                print(str(arrayA[i]) + "," + str(arrayB[j]))

# printUnorderedPairss(arrayA, arrayB)
```
- **Time Complexity**:  
  - The outer loop runs `n` times (where `n` is the length of `arrayA`), and the inner loop runs `m` times (where `m` is the length of `arrayB`).
  - The innermost loop runs `100000` times for each pair of `i` and `j`.
  - Therefore, the total time complexity is **O(n * m * 100000)**, which simplifies to **O(n * m)**, with a large constant factor (100000).
  
- **Space Complexity**:  
  - The space complexity is **O(1)** because the function uses only a fixed number of extra variables (`i`, `j`, `k`).

### **Question 6: Reverse an Array**
```python
def reverse(array):
    for i in range(0, int(len(array) / 2)):
        other = len(array) - i - 1
        temp = array[i]
        array[i] = array[other]
        array[other] = temp
    print(array)

reverse(arrayA)
```
- **Time Complexity**:  
  - The loop runs for half of the array length (`n/2`), so the time complexity is **O(n)**, where `n` is the length of the array.
  
- **Space Complexity**:  
  - The space complexity is **O(1)**, because only a fixed amount of extra space (for variables `i`, `other`, and `temp`) is used.

---

### Summary of Time and Space Complexities:

| Function | Time Complexity | Space Complexity |
|----------|-----------------|------------------|
| Question 1: `foo` | O(n) | O(1) |
| Question 2: `printPairs` | O(n²) | O(1) |
| Question 3: `printUnorderedPairs` | O(n²) | O(1) |
| Question 4: `printUnorderedPairs` (with condition) | O(n * m) | O(1) |
| Question 5: `printUnorderedPairs` (inefficient) | O(n * m * 100000) ≈ O(n * m) | O(1) |
| Question 6: `reverse` | O(n) | O(1) |
