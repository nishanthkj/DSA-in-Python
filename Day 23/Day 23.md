

### **Three in One**
The goal is to implement three stacks using a single list. This approach partitions the list into three segments.

#### **Python Implementation**
```python
class ThreeInOne:
    def __init__(self, stack_size):
        self.num_stacks = 3
        self.stack_size = stack_size
        self.array = [None] * (stack_size * self.num_stacks)
        self.sizes = [0] * self.num_stacks

    def is_full(self, stack_num):
        return self.sizes[stack_num] == self.stack_size

    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0

    def index_of_top(self, stack_num):
        offset = stack_num * self.stack_size
        return offset + self.sizes[stack_num] - 1

    def push(self, stack_num, value):
        if self.is_full(stack_num):
            raise Exception("Stack is full")
        self.sizes[stack_num] += 1
        self.array[self.index_of_top(stack_num)] = value

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception("Stack is empty")
        top_index = self.index_of_top(stack_num)
        value = self.array[top_index]
        self.array[top_index] = None
        self.sizes[stack_num] -= 1
        return value

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception("Stack is empty")
        return self.array[self.index_of_top(stack_num)]

# Example Usage
stacks = ThreeInOne(5)
stacks.push(0, 10)  # Push 10 to stack 0
stacks.push(1, 20)  # Push 20 to stack 1
print(stacks.pop(0))  # Output: 10
```

---

### **Stack Minimum**
Design a stack that, in addition to `push` and `pop`, has a function `min` that returns the minimum element in O(1).

#### **Python Implementation**
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            raise Exception("Stack is empty")
        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value

    def min(self):
        if not self.min_stack:
            raise Exception("Stack is empty")
        return self.min_stack[-1]

# Example Usage
stack = MinStack()
stack.push(5)
stack.push(3)
stack.push(7)
print(stack.min())  # Output: 3
stack.pop()
print(stack.min())  # Output: 3
```

---

### **Stack of Plates**
Implements a stack that creates a new stack once the previous one exceeds a threshold.

#### **Python Implementation**
```python
class SetOfStacks:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity

    def push(self, value):
        if not self.stacks or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(value)

    def pop(self):
        if not self.stacks:
            raise Exception("All stacks are empty")
        value = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return value

# Example Usage
stacks = SetOfStacks(3)
stacks.push(1)
stacks.push(2)
stacks.push(3)
stacks.push(4)  # Creates a new stack
print(stacks.pop())  # Output: 4
```

---

### **Queue via Stacks**
Implements a queue using two stacks.

#### **Python Implementation**
```python
class QueueViaStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        self.stack1.append(value)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise Exception("Queue is empty")
        return self.stack2.pop()

# Example Usage
queue = QueueViaStacks()
queue.enqueue(10)
queue.enqueue(20)
print(queue.dequeue())  # Output: 10
```

---

### **Animal Shelter**
A queue-like structure to manage animals in an animal shelter with operations like `enqueue`, `dequeueAny`, `dequeueDog`, and `dequeueCat`.

#### **Python Implementation**
```python
class AnimalShelter:
    def __init__(self):
        self.dogs = []
        self.cats = []
        self.order = 0

    def enqueue(self, animal, type):
        if type == "dog":
            self.dogs.append((self.order, animal))
        elif type == "cat":
            self.cats.append((self.order, animal))
        self.order += 1

    def dequeueAny(self):
        if not self.dogs and not self.cats:
            raise Exception("No animals available")
        if not self.dogs:
            return self.dequeueCat()
        if not self.cats:
            return self.dequeueDog()
        if self.dogs[0][0] < self.cats[0][0]:
            return self.dequeueDog()
        else:
            return self.dequeueCat()

    def dequeueDog(self):
        if not self.dogs:
            raise Exception("No dogs available")
        return self.dogs.pop(0)[1]

    def dequeueCat(self):
        if not self.cats:
            raise Exception("No cats available")
        return self.cats.pop(0)[1]

# Example Usage
shelter = AnimalShelter()
shelter.enqueue("Dog1", "dog")
shelter.enqueue("Cat1", "cat")
print(shelter.dequeueAny())  # Output: Dog1
