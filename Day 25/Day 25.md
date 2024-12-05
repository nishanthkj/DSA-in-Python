

### **Question 1: Sum of Digits**
Calculate the sum of digits of a given number.

```python
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

# Example usage
number = 12345
print(f"Sum of digits of {number}: {sum_of_digits(number)}")
```

---

### **Question 2: Power**
Calculate the result of \(a^b\) (a raised to the power of b).

```python
def power(a, b):
    return a ** b

# Example usage
a = 2
b = 10
print(f"{a} raised to the power of {b}: {power(a, b)}")
```

---

### **Question 3: Greatest Common Divisor (GCD)**
Find the GCD of two numbers using Euclid's algorithm.

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
num1 = 48
num2 = 18
print(f"GCD of {num1} and {num2}: {gcd(num1, num2)}")
```

---

### **Question 4: Decimal to Binary**
Convert a decimal number to binary.

```python
def decimal_to_binary(number):
    return bin(number).replace('0b', '')

# Example usage
number = 45
print(f"Binary representation of {number}: {decimal_to_binary(number)}")
```

