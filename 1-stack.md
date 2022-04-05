# Stack

**Introduction**

A stack is a data structure where information can be stored in sequence. The main characteristic of a stack is that the last element added to the stack is the first to be removed (LIFO). Elements are always added and removed from the top of the stack. Just as a stack of plates, when adding a new plate, the easiest way is to add to the top, because it doesn't require to move the other plates. The same process apply when removing a plate, the easiest way is to remove from the top.

Stacks are widely used in many different ways in programming, function calls is one of them. When a function is called inside another function, the second call is added to the functino call stack, only when the second function is finished, the previous function will continue to run.


**Purpose**

 The purpose of a stack is to organize a sequence of elements in a specific order. Every element added to the sequence is pushed to the end. When an element is removed from the sequence, the last element is popped out.
 
**Performance**
 
 |Command    |Description   | Python Code| Performance|
 |-----------|--------------|------------|------------|
 |append(data) |Adds a new element to the stack   | append()   | O(1)       |
 |pop()      |Removes the last element from the stack an returns its value   | pop()      | O(1)       |
 |size()     |Retrives the actual number (int) of elements inside a list   | len(my_stack)      | O(1)       |
 |empty()    |Returns False if the list has at least one element, and True otherwise   | len(my_stack) == 0      | O(1)       |
 |get(index)      |Retrieves the element at the provided index   | my_stack[index]      | O(1)

**Problems that can be Solved Using this Data Structure**
 1. The backspace button on the keyboard is a common problem that can be solved with a stack. If we think about it, we notice that after typing a few characters, pushing the backspace button will remove the last character added, not the first.

 2. Stacks are also a good option when reverting a sequence. Looping through a sequence from the first character to the last one and appending each item to a stack will revert that sequence. Like the example below:

 ```python
stack = [] # initialize stack
word = 'python'

for ch in word: # loop through the string
    stack.append(ch) # append each item to the stack

print(''.join(stack)) # output: nohtyp 
 ```
**Common Errors**

 A common error when working with stacks is to not understand how the push and pop functions work. The default for many people is to think that the first element added must be the first to be removed, and that is not true when talking about stacks. Another common error is to think that the element will be added in the first position of the sequence, and this is also not true. Most implementations will add the element to the last position of the sequence and remove also from the last position.

**Example**

```python
stack = [1,2,3,4,5,6,7,8,9,10] # initialize the stack with some elements

stack.append(11) # [1,2,3,4,5,6,7,8,9,10,11] new list
element = stack.pop() # 11 is poped out of the list because it was the last to be added

print(element)
```

**Problem to Solve**

```python
class Plate:

    def __str__(self) -> str:
        return '--_______--'

class StackOfPlates:
    stack = []

    def add(self, amount = 1):
        if amount == 1:
            self.stack.append(Plate())
        else:
            '''
            Implement the code that handles two other situations.
            First: if amount is 0
            Second: If amount is greater than 1
            '''
            pass

    def remove(self, amount = 1):
        if amount == 1:
            self.stack.pop()
        else:
            '''
            Implement the code that handles two other situations.
            First: if amount is 0
            Second: If amount is greater than 1
            '''
            pass

    def displayStack(self):
        '''
        Implement some code that prints a message if the stack is empty
        '''
        stackOfPlates = f'{str(Plate())}\n' * len(self.stack)
        print(stackOfPlates)
    
    def displayAmount(self):
        '''
        Implement some code that display the number of plates in the stack
        '''
        pass

```

[Solution](stack_solution.py)