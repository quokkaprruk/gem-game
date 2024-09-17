# Copy over your a1_partc.py file here
#    Main Author(s): Sayeda Insha Fatima Zaidi
#    Main Reviewer(s): Anthony Sin, Siripa Purinruk

class Stack:
    """
    Purpose: Initializes an instance of 'Stack' class
    Parameters:
    1. 'self': current instance of 'Stack' class
    2. 'cap': integral number of elements we would want our stack to contain, default is 10
    Return Value: None
    Limitations: None
    """
    def __init__(self, cap=10):
        # initializing 'stack' with an empty list
        self.cap = cap
        self.stack = [None] * self.cap
        self.size = 0

    """
    Purpose: Creates a new stack with double the initial capacity and sets it to replace the original stack in case we add more elements than dictated by the initial capacity
    Parameters:
    1. 'self': current instance of 'Stack' class
    Return Value: None
    Limitations: None
    """
    def resize(self):
        # double the capacity
        self.cap *= 2

        # create a new stack with the new capacity
        new_stack = [None] * self.cap
        
        # copy the data from the original stack to the new stack
        for i in range(self.size):
            new_stack[i] = self.stack[i]
            
        self.stack = new_stack

    """
    Purpose: Returns the capacity or 'cap' of the stack
    Parameters:
    1. 'self': Current instance of 'Stack' class 
    Return Value:'self.cap': The capacity of current stack
    Limitations: None
    """
    def capacity(self):
        # returning current capacity of stack
        return self.cap

    """
    Purpose: Adds data to the top of the stack
    Parameters: 
    1. 'self': Current instance of 'Stack' class
    2. 'data': The new element that we wish to add to the top of the stack
    Return Value: None
    Limitations: None
    """
    def push(self, data):
        # if capacity is exceeded
        if self.size >= self.cap:
            # call resize function
            self.resize()
            
        # add new data to the stack
        self.stack[self.size] = data
        self.size += 1

    """
    Purpose: Removes the data or value at the top of the stack
    Parameters:
    1. 'self': Current instance of 'Stack' class
    Return Value: 'rm_item': The data or value removed from the stack
    Limitations: None
    """
    def pop(self):
        # if stack is empty
        if self.is_empty():
            raise IndexError('pop() used on empty stack')
        else:
            rm_item = self.stack[self.size - 1]
            self.stack[self.size - 1] = None
            self.size -= 1
            return rm_item

    """
    Purpose: Returns the topmost element from the stack
    Parameters:
    1. 'self': Current instance of 'Stack' class
    Return Value: 'None' if the stack is empty, the topmost value otherwise
    Limitations: None
    """
    def get_top(self):
        # if stack is empty, return 'None'
        if self.is_empty():
            return None
        else:
            # the topmost item is the one added last
            return self.stack[self.size - 1]

    """
    Purpose: Checks if the stack is empty
    Parameters:
    1. 'self': Current instance of 'Stack' class
    Return Value: True if the stack contains no elements, False otherwise
    Limitations: None
    """
    def is_empty(self):
        # if length of stack is 0 (no items), the stack is empty
        return self.size == 0

    """
    Purpose: Returns the number or values in teh stack
    Parameters:
    1. 'self': Current instance of 'Stack' class
    Return Value: 'self.size': The number of values currently in the stack
    Limitations: None
    """
    def __len__(self):
        # returning number of items in the stack
        return self.size


class Queue:
    """
    Purpose: Initialize a queue with a given capacity.
    Parameters:
    1. cap (optional): The initial capacity of the queue (default is 10).
    Return Value: None
    Limitations: None
    """
    def __init__(self, cap=10):
        self.cap = cap
        self.queue = [None] * self.cap
        self.front = 0
        self.back = 0
        self.size = 0

    """
    Purpose: Retrieve the capacity of the queue.
    Parameters: None
    Return Value: The capacity of the queue.
    Limitations: None
    """
    def capacity(self):
        return self.cap

    """
    Purpose: Add an item to the back of the queue.
    Parameters: 
    1. data: The data to be added to the queue.
    Return Value: None
    Limitations: None
    """
    def enqueue(self, data):
        if self.size >= self.cap:
            new_queue = self.queue
            self.cap *= 2
            self.queue = [None] * self.cap
            for i in range(self.size):
                self.queue[i] = new_queue[(self.front + i) % self.size]
            self.front = 0
            self.back = self.size

        self.queue[self.back] = data
        self.back = (self.back + 1) % self.cap
        self.size += 1

    """
    Purpose: Remove and return the item from the front of the queue.
    Parameters: None
    Return Value: The item from the front of the queue.
    Limitations: Raises IndexError if the queue is empty.
    """
    def dequeue(self):
        if self.is_empty():
            raise IndexError('dequeue() used on empty queue')
        rm_item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.cap
        self.size -= 1
        return rm_item

    """
    Purpose: Retrieve the item at the front of the queue
    Parameters: None
    Return Value: The item at the front of the queue, or None if the queue is empty.
    Limitations: None
    """
    def get_front(self):
        if self.is_empty():
            return None
        else:
            return self.queue[self.front]

    """
    Purpose: Check if the queue is empty.
    Parameters: None
    Return Value: True if the queue is empty, False otherwise.
    Limitations: None
    """
    def is_empty(self):
        return self.size == 0

    """
    Purpose: Get the number of items in the queue.
    Parameters: None
    Return Value: The number of items in the queue.
    Limitations: None
    """
    def __len__(self):
        return self.size


class Deque:
    """
    Purpose: Initializes an instance of the 'Deque' class
    Parameters:
    1. 'self': current instance of the 'Deque' class
    2. 'cap': integral number of elements we would want our deque to contain, default is 10
    Return Value: None 
    Limitations: None
    """
    def __init__(self, cap=10):
        # initializing 'deque' with an empty list
        self.cap = cap
        self.deque = [None] * cap
        self.front = 0
        self.back = 0
        self.size = 0

    """
    Purpose: Returns the capacity or 'cap' of the deque
    Parameters:
    1. 'self': current instance of the 'Deque' class
    Return Value: 'self.cap': The capacity of current deque
    Limitations: None
    """
    def capacity(self):
        # returning current capacity of deque
        return self.cap

    """
    Purpose: Creates a new deque with double the initial capacity and sets it to replace the original stack in case we add more elements than dictated by the initial capacity
    Parameters:
    1. 'self': current instance of the 'Deque' class
    Return Value: None
    Limitations: None
    """
    def resize(self):
        # capacity is doubled
        new_cap = self.cap * 2
        new_deque = [None] * new_cap

        # copying elements from old deque to new
        for i in range(self.size):
            new_deque[i] = self.deque[(self.front + i) % self.cap]

        self.deque = new_deque
        self.front = 0
        self.back = self.size
        self.cap = new_cap

    """
    Purpose: Adds data to the front of the deque
    Parameters: 
    1. 'self': current instance of the 'Deque' class
    2. 'data': The new element that we wish to add to the front of the deque
    Return Value: None
    Limitations: None
    """
    def push_front(self, data):
        # if capacity is exceeded
        if self.size >= self.cap:
            self.resize()

        # move front pointer back
        self.front = (self.front - 1) % self.cap
        self.deque[self.front] = data
        self.size += 1

    """
    Purpose: Adds data to the back of the deque
    Parameters:
    1. 'self': current instance of the 'Deque' class
    2. 'data': The new element that we wish to add to the back of the deque
    Return Value: None
    Limitations: None
    """
    def push_back(self, data):
        # if capacity is exceeded
        if self.size >= self.cap:
            self.resize()

        # add new data to the rear
        self.deque[self.back] = data
        self.back = (self.back + 1) % self.cap
        self.size += 1

    """
    Purpose: Removes a value or data from the front of the deque
    Parameters:
    1. 'self': current instance of the 'Deque' class
    Return Value: 'rm_item": item removed from the front of the deque
    Limitations: Raises Index error if the deque is empty
    """
    def pop_front(self):
        # if deque is empty
        if self.is_empty():
            raise IndexError('pop_front() used on empty deque')

        rm_item = self.deque[self.front]
        self.deque[self.front] = None
        self.front = (self.front + 1) % self.cap
        self.size -= 1
        return rm_item

    """
    Purpose: Removes a value or data from the back of the deque
    Parameters:
    1. 'self': current instance of the 'Deque' class
    Return Value: 'rm_item": item removed from the back of the deque
    Limitations: Raises Index error if the deque is empty
    """
    def pop_back(self):
        if self.is_empty():
            raise IndexError('pop_back() used on empty deque')

        self.back = (self.back - 1) % self.cap
        rm_item = self.deque[self.back]
        self.deque[self.back] = None
        self.size -= 1
        return rm_item

    """
    Purpose: Returns data at the front of the deque, does not remove it
    Parameters:
    1. 'self': current instance of the 'Deque' class
    Return Value: the value which is the front-most element of the deque
    Limitations: None
    """
    def get_front(self):
        if self.is_empty():
            return None
        return self.deque[self.front]

    """
    Purpose: Returns data at the back of the deque, does not remove it
    Parameters:
    1. 'self': current instance of the 'Deque' class
    Return Value: the value which is the back-most element of the deque
    Limitations: None
    """
    def get_back(self):
        if self.is_empty():
            return None
        return self.deque[(self.back - 1) % self.cap]

    """
    Purpose: Returns True of the deque is empty, False otherwise
    Parameters:
    1. 'self': current instance of the 'Deque' class
    Return Value: True if the deque is empty, False otherwise
    Limitations: None
    """
    def is_empty(self):
        return self.size == 0

    """
    Purpose: Returns the number or values in the deque
    Parameters:
    1. 'self': Current instance of 'Deque' class
    Return Value: 'self.size': The number of values currently in the deque
    Limitations: None
    """
    def __len__(self):
        return self.size

    """
    Purpose: Returns the 'k'th value from the front of the deque, does not remove it
    Parameters:
    1. 'self': Current instance of 'Deque' class
    2. 'k': an integral value representing an index in the deque, the value at which we wish to retrieve
    Return Value: The value at the 'k'th position from the front
    Limitations: Raises Index error if the value of 'k' exceeds the number of values currently in the deque
    """
    def __getitem__(self, k):
        if k >= self.size or k < 0:
            raise IndexError('Index out of range')
        return self.deque[(self.front + k) % self.cap]