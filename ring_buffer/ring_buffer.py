class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.current_pos = 0
        self.max = 0

    def append(self, item):

        if self.current_pos < self.capacity:
            self.buffer.append(item)
            self.current_pos += 1
        else:
            if self.max > self.capacity - 1:
                self.max = self.max % (self.capacity)
            self.buffer[self.max] = item
            self.max += 1

    def get(self):
        return self.buffer


# buffer = RingBuffer(3)

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')
# buffer.append('d')
# buffer.append('e')

# buffer.get()
