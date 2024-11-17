

### What is a Dictionary?
- A **dictionary** in Python is an unordered collection of items.
- It stores data in key-value pairs. Each key is unique, and each key maps to a value.
- Syntax: 
  ```python
  my_dict = {key1: value1, key2: value2, key3: value3}
  ```
- **Example**:
  ```python
  student = {'name': 'John', 'age': 21, 'major': 'Computer Science'}
  ```

---

### Create a Dictionary
- You can create a dictionary using curly braces `{}` or the `dict()` constructor.
- **Example using curly braces**:
  ```python
  my_dict = {'name': 'Alice', 'age': 25}
  ```
- **Example using `dict()`**:
  ```python
  my_dict = dict(name='Alice', age=25)
  ```

---

### Dictionaries in Memory
- Dictionaries are implemented using a **hash table** in Python.
- This means that they allow fast access to values by their keys, usually in constant time \(O(1)\).
- The keys are **hashed** into an index for quick lookups.

---

### Insert/Update an Element in a Dictionary
- You can insert or update elements in a dictionary by assigning a value to a key.
- **Inserting**:
  ```python
  my_dict['new_key'] = 'new_value'
  ```
- **Updating**:
  ```python
  my_dict['existing_key'] = 'updated_value'
  ```

---

### Traverse through a Dictionary
- You can iterate over the keys, values, or both in a dictionary.
  - **Iterating over keys**:
    ```python
    for key in my_dict:
        print(key)
    ```
  - **Iterating over values**:
    ```python
    for value in my_dict.values():
        print(value)
    ```
  - **Iterating over key-value pairs**:
    ```python
    for key, value in my_dict.items():
        print(key, value)
    ```

---

### Search for an Element in a Dictionary
- You can check if a **key** exists in a dictionary using the `in` keyword.
  ```python
  if 'name' in my_dict:
      print("Key found")
  ```
- To search for a **value**, you can use `values()`:
  ```python
  if 'Alice' in my_dict.values():
      print("Value found")
  ```

---

### Delete/Remove an Element from a Dictionary
- **Using `del`**:
  ```python
  del my_dict['name']
  ```
- **Using `pop()`** (removes the key-value pair and returns the value):
  ```python
  value = my_dict.pop('name')
  print(value)
  ```
- **Using `popitem()`** (removes and returns the last inserted key-value pair):
  ```python
  key, value = my_dict.popitem()
  ```

---

### Dictionary Methods
- Common methods for dictionaries:
  - **`clear()`**: Removes all items.
  - **`get()`**: Returns the value for a given key (returns `None` if the key doesn't exist).
  - **`keys()`**: Returns a view object containing all the keys.
  - **`values()`**: Returns a view object containing all the values.
  - **`items()`**: Returns a view object containing all key-value pairs.
  - **`update()`**: Updates the dictionary with elements from another dictionary or iterable of key-value pairs.

---

### Dictionary Operations / Built-in Functions
- **Common operations**:
  - **Checking the length**: `len(my_dict)`
  - **Checking if a key exists**: `'key' in my_dict`
  - **Getting value by key**: `my_dict.get('key')`
- **Functions**:
  - **`dict()`**: Creates a new dictionary.
  - **`sorted()`**: Sorts a dictionary by key or value.

---

### Dictionary vs List
- **Dictionaries** store data in key-value pairs, while **Lists** store data in ordered sequences.
- **Dictionaries** provide fast lookups, while **Lists** are better for ordered data and sequences.
- **Example**:
  ```python
  my_dict = {'a': 1, 'b': 2}
  my_list = [1, 2, 3]
  ```

---

### Time and Space Complexity of a Dictionary
- **Time Complexity**:
  - **Lookup (getting a value by key)**: O(1) on average (constant time).
  - **Insert (adding or updating an element)**: O(1) on average.
  - **Delete**: O(1) on average.
- **Space Complexity**: The space complexity of a dictionary depends on the number of keys and values, and it’s typically O(n), where **n** is the number of items.

---

### Dictionary Comprehension
- **Dictionary comprehension** allows you to create a new dictionary from an iterable in a concise way.
- **Syntax**:
  ```python
  new_dict = {key: value for key, value in iterable}
  ```
- **Example**:
  ```python
  squares = {x: x**2 for x in range(5)}
  print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
  ```
