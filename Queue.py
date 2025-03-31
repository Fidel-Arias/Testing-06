import array

class Queue:
    def __init__(self, size_max):
        assert size_max > 0 # Queue size must be greater than 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max)) # Initialize the queue

    def is_empty(self):
        """Check if the queue is empty."""
        return self.size == 0
    
    def is_full(self):
        """Check if the queue is full."""
        return self.size == self.max
    
    def enqueue(self, item):
        """Add an item to the queue."""
        if self.is_full():
            raise False
        self.data[self.tail] = item
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0
        return True
    
    def dequeue(self):
        """Remove an item from the queue."""
        if self.is_empty():
            raise None
        item = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return item
