
### **Goals - What You Will Make by the End of This Section**

By the end of this section, you'll be able to:
- Calculate the average temperature from a list of temperature readings.
- Identify which days had temperatures above the calculated average.

---

### **Calculate Average Temperature**

To calculate the **average temperature**, use the following formula:

\[
\text{Average Temperature} = \frac{\text{Sum of all temperatures}}{\text{Number of temperatures}}
\]

#### **Steps**:
1. **Collect the temperature data**: You will typically be given a list of temperatures for several days.
2. **Sum the temperatures**.
3. **Count the number of temperature readings**.
4. **Divide the sum by the count** to get the average.

#### **Example**:
Let's say the temperatures for the week are:  
\[ \text{[72, 75, 68, 70, 74]} \]

1. **Sum** the temperatures:  
   \( 72 + 75 + 68 + 70 + 74 = 359 \)
   
2. **Count** the number of readings:  
   There are 5 days, so the count is 5.

3. **Calculate the average**:  
   \[
   \text{Average Temperature} = \frac{359}{5} = 71.8^\circ F
   \]

The average temperature for the week is **71.8°F**.

#### **Python Example Code**:
```python
temperatures = [72, 75, 68, 70, 74]
average_temp = sum(temperatures) / len(temperatures)
print(f"Average Temperature: {average_temp}°F")
```

---

### **Find the Days Above Average Temperature**

After calculating the **average temperature**, the next step is to identify the days with temperatures **above the average**.

#### **Steps**:
1. **Loop through each day's temperature**.
2. **Compare** each temperature with the average.
3. **Select the days** where the temperature is higher than the average.

#### **Example**:
Given the temperatures list:  
\[ \text{[72, 75, 68, 70, 74]} \]  
And an **average temperature** of \( 71.8^\circ F \), the days above average are:
- 72°F is above average
- 75°F is above average
- 74°F is above average

#### **Python Example Code**:
```python
above_average_days = [temp for temp in temperatures if temp > average_temp]
print(f"Days with temperatures above average: {above_average_days}°F")
```

**Output**:
```
Days with temperatures above average: [72, 75, 74]
```

This code filters through the list of temperatures and returns those that are higher than the calculated average.

---

### **Summary**

1. **Calculate the Average**: Add up all temperatures and divide by the total number of readings.
2. **Find Days Above Average**: Compare each temperature to the average and select those that are greater.
