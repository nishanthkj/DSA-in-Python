

#### **1. Sum of Digits Function (`sumofDigits`)**

**Problem:** Given a positive integer `n`, sum the digits of `n`.

```python
def sumofDigits(n):
    assert n >= 0 and int(n) == n, 'The number has to be a positive integer only!'
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumofDigits(int(n / 10))
```

- **Recursion Breakdown:** The function takes the last digit (`n % 10`), and then recursively sums the digits of the remaining number (`int(n / 10)`).
- **Base Case:** `n == 0`, which returns 0 (end of recursion).
- **Assertion:** Ensures `n` is a positive integer.

**Example Output:** `sumofDigits(11111)` will return `5` (1+1+1+1+1).

---

#### **2. Power Function (`power`)**

**Problem:** Compute `base^exp` using recursion.

```python
def power(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * power(base, exp - 1)
```

- **Recursion Breakdown:** The function multiplies `base` with the result of `base^(exp-1)`.
- **Base Cases:** 
  - If `exp == 0`, return 1 (any number raised to the power of 0 is 1).
  - If `exp == 1`, return the base itself.
- **Efficiency:** This can be optimized using the "exponentiation by squaring" method for larger exponents.

**Example Output:** `power(4, 2)` will return `16`.

---

#### **3. GCD Function (`gcd`)**

**Problem:** Find the greatest common divisor (GCD) of two integers `a` and `b`.

```python
def gcd(a, b):
    assert int(a) == a and int(b) == b, 'The numbers must be integers only!'
    a, b = abs(a), abs(b)  # Handle negative numbers
    if b == 0:
        return a
    return gcd(b, a % b)
```

- **Recursion Breakdown:** Uses the Euclidean algorithm, which states that `gcd(a, b) = gcd(b, a % b)`.
- **Base Case:** When `b == 0`, return `a`, which is the GCD.
- **Assertion:** Ensures both inputs are integers.

**Example Output:** `gcd(12, 1)` will return `1`.

---

#### **4. Decimal to Binary Conversion (`decimalToBinary`)**

**Problem:** Convert a decimal number `n` to its binary representation.

```python
def decimalToBinary(n):
    if n == 0:
        return 0
    return n % 2 + 10 * decimalToBinary(int(n / 2))
```

- **Recursion Breakdown:** The remainder of `n % 2` gives the binary digits. The function recursively divides `n` by 2.
- **Base Case:** When `n == 0`, return 0.
- **Conversion Logic:** The function builds the binary number by appending the remainders in reverse order (multiplied by powers of 10).

**Example Output:** `decimalToBinary(1)` will return `1`.

---

### General Notes on Recursion:
1. **Base Case:** All recursive functions need a base case, which prevents infinite recursion and ensures termination.
2. **Efficiency:** Some recursive solutions, like the power function, can be inefficient for large inputs due to repeated calculations. This can be optimized using techniques like memoization or exponentiation by squaring.
3. **Memory Usage:** Recursion can be memory-intensive because each function call creates a new frame on the call stack. For large problems, iterative solutions might be more efficient.

