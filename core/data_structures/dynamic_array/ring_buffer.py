"""
A Ring Buffer is a buffer with a fixed size.
When it fills up, it overwrites from the beginning.
"""

class RingBuffer(object):
    def __init__(self, max_size):
        self.data = []
        self.max_size = max_size

    def append(self, el):
        self.data.append(el)
        if len(self.data) == self.max_size:
            self.curr = 0
            self.__class__ = RingBufferFull

    def get(self):
        return self.data

class RingBufferFull(object):
    def __init__(self):
        raise 'You should use a RingBuffer'

    def append(self, el):
        self.data[curr] = el
        self.curr = (self.data + 1) % self.max_size

    def get(self):
        return self.data[self.curr:] + self.data[:self.curr] # not quite sure why we can't just return self.data?
