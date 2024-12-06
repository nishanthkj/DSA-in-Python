

### **1. Power**
```python
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)
```

---

### **2. Factorial**
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

---

### **3. Product of Array**
```python
def product_of_array(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * product_of_array(arr[1:])
```

---

### **4. Recursive Range**
```python
def recursive_range(n):
    if n == 0:
        return 0
    return n + recursive_range(n - 1)
```

---

### **5. Fibonacci**
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

---

### **6. Reverse String**
```python
def reverse(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse(s[:-1])
```

---

### **7. Is Palindrome**
```python
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
```

---

### **8. Some Recursive**
```python
def some_recursive(arr, func):
    if len(arr) == 0:
        return False
    if func(arr[0]):
        return True
    return some_recursive(arr[1:], func)
```

---

### **9. Flatten**
```python
def flatten(arr):
    result = []
    for elem in arr:
        if isinstance(elem, list):
            result.extend(flatten(elem))
        else:
            result.append(elem)
    return result
```

---

### **10. Capitalize First**
```python
def capitalize_first(arr):
    if len(arr) == 0:
        return []
    return [arr[0].capitalize()] + capitalize_first(arr[1:])
```

---

### **11. Nested Even Sum**
```python
def nested_even_sum(obj):
    total = 0
    for key in obj:
        if isinstance(obj[key], dict):
            total += nested_even_sum(obj[key])
        elif isinstance(obj[key], int) and obj[key] % 2 == 0:
            total += obj[key]
    return total
```

---

### **12. Capitalize Words**
```python
def capitalize_words(arr):
    if len(arr) == 0:
        return []
    return [arr[0].upper()] + capitalize_words(arr[1:])
```

---

### **13. Stringify Numbers**
```python
def stringify_numbers(obj):
    new_obj = {}
    for key in obj:
        if isinstance(obj[key], dict):
            new_obj[key] = stringify_numbers(obj[key])
        elif isinstance(obj[key], int):
            new_obj[key] = str(obj[key])
        else:
            new_obj[key] = obj[key]
    return new_obj
```

---

### **14. Collect Strings**
```python
def collect_strings(obj):
    strings = []
    for key in obj:
        if isinstance(obj[key], str):
            strings.append(obj[key])
        elif isinstance(obj[key], dict):
            strings.extend(collect_strings(obj[key]))
    return strings
```

---

### Notes on Recursive Functions
1. **Base Case**: Every recursive function must have a stopping condition to prevent infinite loops.
2. **Recursive Case**: Define how the function will call itself with reduced input.
3. **Immutable Data**: For operations on strings or tuples, recursion naturally supports immutability.
4. **Stack Overflow**: Deep recursion may lead to a stack overflow; Python has a recursion limit (default is 1000).

