It looks like you're working through a series of coding exercises, and you've provided a summary of the exercises along with solutions to each of them. Below are some notes that could help clarify these exercises and their time/space complexity:

### 1. **Count Word Frequency**

**Problem**: You are likely tasked with counting the frequency of each word in a list or string.
**Solution**:

- Use a dictionary (or hash map) to store the word count.
- Traverse the list or string and update the dictionary.

**Time Complexity**: O(n), where _n_ is the number of words in the input (since each word is processed once).  
 **Space Complexity**: O(k), where _k_ is the number of unique words (since a dictionary stores a key-value pair for each word).

---

### 2. **Common Keys**

**Problem**: Find the common keys between two dictionaries.
**Solution**:

- You can use set operations on the keys of the dictionaries (`dict1.keys() & dict2.keys()`).

**Time Complexity**: O(min(m, n)), where _m_ and _n_ are the number of keys in the two dictionaries. Set operations (intersection) are typically O(min(m, n)) where m and n are the lengths of the sets being compared.  
 **Space Complexity**: O(k), where _k_ is the number of common keys (since you're storing the common keys).

---

### 3. **Key with the Highest Value**

**Problem**: Identify the key in a dictionary that has the highest value.
**Solution**:

- Traverse the dictionary and compare values to find the maximum.

**Time Complexity**: O(n), where _n_ is the number of keys in the dictionary (since you check each key once).  
 **Space Complexity**: O(1), because only the maximum key and value are stored.

---

### 4. **Reverse Key-Value Pairs**

**Problem**: Swap the keys and values in a dictionary.
**Solution**:

- Iterate through the dictionary and create a new one where the keys are the original values and the values are the original keys.

**Time Complexity**: O(n), where _n_ is the number of keys in the dictionary (since you're iterating over each key-value pair).  
 **Space Complexity**: O(n), because you are storing a new dictionary with the reversed key-value pairs.

---

### 5. **Conditional Filter**

**Problem**: Filter a dictionary based on a condition (e.g., values greater than a threshold).
**Solution**:

- Iterate through the dictionary and apply the condition to filter out unwanted items.

**Time Complexity**: O(n), where _n_ is the number of keys in the dictionary (since you check each key-value pair once).  
 **Space Complexity**: O(m), where _m_ is the number of items that satisfy the condition (as you're creating a new dictionary with those items).

---

### 6. **Same Frequency**

**Problem**: Check whether two dictionaries have the same frequency of values.
**Solution**:

- Use a `Counter` (from the `collections` module) to count the frequency of values in both dictionaries and compare the counters.

**Time Complexity**: O(n), where _n_ is the number of items in the dictionary (since you're counting the values).  
 **Space Complexity**: O(n), where _n_ is the number of unique values, because you are storing the frequency counts.

---

### Summary of Time and Space Complexity:

| Exercise                    | Time Complexity | Space Complexity |
| --------------------------- | --------------- | ---------------- |
| **Count Word Frequency**    | O(n)            | O(k)             |
| **Common Keys**             | O(min(m, n))    | O(k)             |
| **Key with Highest Value**  | O(n)            | O(1)             |
| **Reverse Key-Value Pairs** | O(n)            | O(n)             |
| **Conditional Filter**      | O(n)            | O(m)             |
| **Same Frequency**          | O(n)            | O(n)             |

Let me know if you need further clarification or if you'd like help with specific exercises!
