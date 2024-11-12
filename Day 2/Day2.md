

### **Big O Notations - Theta, Omega, and Big O**  
- **Big O (O)**: Describes the **upper bound** of an algorithm's runtime, representing the worst-case scenario.
- **Theta (Θ)**: Describes a **tight bound**, where the running time is guaranteed to fall within a specific range (both upper and lower).
- **Omega (Ω)**: Represents the **lower bound**, describing the best-case scenario.

---

### **Big O - O(1)**  
- **O(1)**: **Constant time complexity**.  
  - The algorithm executes in the same time regardless of input size.
  - Example: Accessing an element in an array by index.

---

### **Big O - O(N)**  
- **O(N)**: **Linear time complexity**.  
  - The algorithm’s execution time grows directly with the size of the input.
  - Example: Iterating over each element in an array.

---

### **Drop Constants**  
- When analyzing **Big O**, constants are ignored.  
  - **Reason**: Constants don't significantly affect the growth rate of an algorithm's runtime for large input sizes.  
  - For example: **O(2n)** is simplified to **O(n)**.

---

### **Big O - O(n²)**  
- **O(n²)**: **Quadratic time complexity**.  
  - Occurs when an algorithm involves **nested loops** or operations that scale quadratically.
  - Example: A simple algorithm that compares each element of an array to every other element (e.g., bubble sort).

---

### **Drop Non-Dominant Terms**  
- **Non-dominant terms** are discarded in **Big O analysis**.  
  - **Reason**: As the input size increases, the term with the fastest-growing rate dominates.  
  - For example: **O(n² + n)** simplifies to **O(n²)**.

---

### **Big O - O(log N)**  
- **O(log N)**: **Logarithmic time complexity**.  
  - Occurs in algorithms where the input size is **divided in half** at each step.
  - Example: **Binary search** in a sorted array.

---

### **Space Complexity**  
- **Space complexity** refers to the amount of memory an algorithm requires as the input size grows.
  - Analyzing space complexity is similar to time complexity, but we focus on **memory usage** rather than execution time.

---

### **Different Terms for Input - Add vs Multiply**  
- Distinguishes between operations that grow **linearly** (addition) versus those that grow **exponentially** (multiplication).  
  - Linear growth (addition) increases in direct proportion to input size.  
  - Exponential growth (multiplication) scales much faster.

---

### **How to Measure the Codes Using Big O?**  
- This section explains **how to analyze code** and determine its **Big O time complexity**.  
  - Steps: Examine loops, recursive calls, and operations to understand how the algorithm's time grows with input size.

---

### **Time Complexities Quiz**  
- A **quiz** with questions to assess understanding of the time complexities learned in the course.  
  - Focuses on practical examples and how to identify Big O notations in real algorithms.

---

### **Download the Resources**  
- Download materials for further study and reference.

---

### **Key Takeaways:**
- **Big O Notation** helps analyze the **efficiency** of algorithms.
- Focus on **dominant terms** and **drop constants** when analyzing complexity.
- Different complexities include **O(1)**, **O(N)**, **O(n²)**, and **O(log N)**.
- Understand **space complexity** and how to measure it.

